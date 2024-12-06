from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import db, User, Train
from werkzeug.security import check_password_hash
import json
from app.models import db, User, Train, Booking


routes_bp = Blueprint('routes', __name__)

# User Registration Route
@routes_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User Login Route
@routes_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    identity = json.dumps({"id": user.id, "is_admin": user.is_admin})
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token}), 200

# Admin-only route to add a new train
@routes_bp.route('/add_train', methods=['POST'])
@jwt_required()  
def add_train():
    current_user = json.loads(get_jwt_identity())

    if not current_user.get("is_admin"):
        return jsonify({"message": "Unauthorized, admin access required"}), 403

    data = request.get_json()
    name = data.get('name')
    source = data.get('source')
    destination = data.get('destination')
    total_seats = data.get('total_seats')

    if not name or not source or not destination or not total_seats:
        return jsonify({"message": "Missing required fields"}), 400

    # Creating a new Train object
    train = Train(
        name=name,
        source=source,
        destination=destination,
        total_seats=total_seats,
        available_seats=total_seats  
    )
    db.session.add(train)
    db.session.commit()

    return jsonify({"message": "Train added successfully"}), 201


@routes_bp.route('/get_seat_availability', methods=['GET'])
@jwt_required()  
def get_seat_availability():
    source = request.args.get('source')
    destination = request.args.get('destination')

    if not source or not destination:
        return jsonify({"message": "Source and destination are required"}), 400

    trains = Train.query.filter_by(source=source, destination=destination).all()

    return jsonify([train.serialize() for train in trains]), 200


@routes_bp.route('/book_seat', methods=['POST'])
@jwt_required()  
def book_seat():
    current_user = get_jwt_identity()  

    if isinstance(current_user, str):
        current_user = json.loads(current_user)

    data = request.get_json()
    train_id = data.get('train_id')
    seat_number = data.get('seat_number')

    train = Train.query.filter_by(id=train_id).first()

    if not train:
        return jsonify({"message": "Train not found"}), 404

    if train.available_seats <= 0:
        return jsonify({"message": "No available seats on this train"}), 400

    booking = Booking(user_id=current_user['id'], train_id=train.id, seat_number=seat_number)
    db.session.add(booking)

    train.available_seats -= 1
    db.session.commit()

    return jsonify({"message": "Seat booked successfully"}), 201


@routes_bp.route('/get_booking_details', methods=['GET'])
@jwt_required()  
def get_booking_details():
    current_user = get_jwt_identity()  

    if isinstance(current_user, str):
        current_user = json.loads(current_user)

    bookings = Booking.query.filter_by(user_id=current_user['id']).all()

    if not bookings:
        return jsonify({"message": "No bookings found"}), 404

    return jsonify([{
        "booking_id": b.id,
        "train_name": b.train.name,
        "source": b.train.source,
        "destination": b.train.destination,
        "seat_number": b.seat_number,
        "booking_time": b.booking_time
    } for b in bookings]), 200