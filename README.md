#IRCTC Project - Assignment

#How to Setup The Assignment.

1.Clone the repo 

2.Add a config.py file 


It should contain 

import os
 SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/irctc_db"  # Update with your MySQL credentials
SQLALCHEMY_TRACK_MODIFICATIONS = False
 JWT Configuration
JWT_SECRET_KEY = 'your-secret-key'  # Set your own secret key for JWT


3.run the migrate db command 
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

run these 3 caommand so this will create the neccessary tables in your db


4. run the project 
open the command terminal and split it 
----in one terminal run the flask project using "Flask run" command 
----and in other terminal test it using Curl using commands 

///FOR REGISTER 
curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d "{\"username\": \"testuser\", \"password\": \"password123\"}"        


///FOR LOGIN
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d "{\"username\": \"testuser\", \"password\": \"password123\"}"



///GET_SEAT_AVAILABILTY
curl -X GET "http://127.0.0.1:5000/get_seat_availability?source=Mumbai&destination=Delhi" -H "Authorization: Bearer's access token"



///BOOK_SEAT
curl -X POST "http://127.0.0.1:5000/book_seat" -H "Authorization: Bearer's access token" -H "Content-Type: application/json" -d "{\"train_id\": 1, \"seat_number\": 10}"



///GET_BOOKING_DETAILS
curl -X GET "http://127.0.0.1:5000/get_booking_details" -H "Authorization: Bearer'S access token" -H "Content-Type: application/json"



*before login into admin add admin user in the db and make the admin_user = 1*

///FOR ADMIN LOGIN
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d "{\"username\": \"adminuser\", \"password\": \"adminpass12345\"}"



///TO ADD TRAIN IN DB
curl -X POST http://127.0.0.1:5000/add_train -H "Content-Type: application/json" -H "Authorization:Bearer's access token " -d "{\"name\": \"yash Express\", \"source\": \"Mumbai\", \"destination\": \"Kankavli\", \"total_seats\": 80}"
