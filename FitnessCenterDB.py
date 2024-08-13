# 1. Managing a Fitness Center Database
# Objective: The aim of this assignment is to develop a Flask application to manage a fitness center's database, focusing on interacting 
# with the Members and WorkoutSessionstables. This will enhance your skills in building RESTful APIs using Flask, handling database 
# operations, and implementing CRUD functionalities.

# Task 1: Setting Up the Flask Environment and Database Connection - Create a new Flask project and set up a virtual environment. - 
# Install necessary packages like Flask, Flask-Marshmallow, and MySQL connector. - Establish a connection to your MySQL database. - Use 
# the Members and WorkoutSessions tables used on previous Lessons

# Expected Outcome: A Flask project with a connected database and the required tables created.

# from flask import Flask, jsonify, request
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'user': 'root',
#     'password': '$E@kster1',
#     'host': 'localhost',
#     'database': 'fitness_center_db'
# }

# # Establish database connection
# def get_db_connection():
#     try:
#         connection = mysql.connector.connect(**db_config)
#         if connection.is_connected():
#             print("Database connected successfully!")
#             return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# # Define routes
# @app.route('/')
# def home():
#     return "Welcome to the Fitness Center Management System!"

# @app.route('/members', methods=['GET'])
# def get_members():
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM members")
#         members = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return jsonify(members)
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# @app.route('/workoutsessions', methods=['GET'])
# def get_workout_sessions():
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM workoutsessions")
#         workout_sessions = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return jsonify(workout_sessions)
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)







# Task 2: Implementing CRUD Operations for Members - Create Flask routes to add, retrieve, update, and delete members from the 
# Memberstable. - Use appropriate HTTP methods: POST for adding, GET for retrieving, PUT for updating, and DELETE for deleting members. 
# - Ensure to handle any errors and return appropriate responses.

#Expected Outcome: Functional endpoints for managing members in the database with proper error handling.

#Code Example:
#@app.route('/members', methods=['POST'])
#def add_member():
    # Logic to add a member
#    pass

#@app.route('/members/<int:id>', methods=['GET'])
#def get_member(id):
    # Logic to retrieve a member
#    pass

# other routes to update and delete



# from flask import Flask, jsonify, request
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'user': 'root',
#     'password': '$E@kster1',
#     'host': 'localhost',
#     'database': 'fitness_center_db'
# }

# # Establish database connection
# def get_db_connection():
#     try:
#         connection = mysql.connector.connect(**db_config)
#         if connection.is_connected():
#             print("Database connected successfully!")
#             return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# @app.route('/')
# def home():
#     return "Welcome to the Fitness Center Management System!"

# # READ - Get all members
# @app.route('/members', methods=['GET'])
# def get_members():
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM members")
#         members = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return jsonify(members)
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# # READ - Get a specific member by ID
# @app.route('/members/<int:id>', methods=['GET'])
# def get_member(id):
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM members WHERE id = %s", (id,))
#         member = cursor.fetchone()
#         cursor.close()
#         connection.close()
#         if member:
#             return jsonify(member)
#         else:
#             return jsonify({"error": "Member not found"}), 404
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# # CREATE - Add a new member
# @app.route('/members', methods=['POST'])
# def add_member():
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor()
#         new_member = request.json
#         sql = """INSERT INTO members (name, email, phone, membership_date) 
#                  VALUES (%s, %s, %s, %s)"""
#         cursor.execute(sql, (new_member['name'], new_member['email'], new_member['phone'], new_member['membership_date']))
#         connection.commit()
#         cursor.close()
#         connection.close()
#         return jsonify({"message": "Member added successfully!"}), 201
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# # UPDATE - Update a member's details
# @app.route('/members/<int:id>', methods=['PUT'])
# def update_member(id):
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor()
#         update_data = request.json
#         sql = """UPDATE members SET name = %s, email = %s, phone = %s, membership_date = %s 
#                  WHERE id = %s"""
#         cursor.execute(sql, (update_data['name'], update_data['email'], update_data['phone'], update_data['membership_date'], id))
#         connection.commit()
#         cursor.close()
#         connection.close()
#         if cursor.rowcount == 0:
#             return jsonify({"error": "Member not found"}), 404
#         return jsonify({"message": "Member updated successfully!"})
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# # DELETE - Delete a member by ID
# @app.route('/members/<int:id>', methods=['DELETE'])
# def delete_member(id):
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor()
#         sql = "DELETE FROM members WHERE id = %s"
#         cursor.execute(sql, (id,))
#         connection.commit()
#         cursor.close()
#         connection.close()
#         if cursor.rowcount == 0:
#             return jsonify({"error": "Member not found"}), 404
#         return jsonify({"message": "Member deleted successfully!"})
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# # READ - Get all workout sessions
# @app.route('/workoutsessions', methods=['GET'])
# def get_workout_sessions():
#     connection = get_db_connection()
#     if connection:
#         cursor = connection.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM workoutsessions")
#         workout_sessions = cursor.fetchall()
#         cursor.close()
#         connection.close()
#         return jsonify(workout_sessions)
#     else:
#         return jsonify({"error": "Unable to connect to the database"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)




# Task 3: Managing Workout Sessions - Develop routes to schedule, update, and view workout sessions. - Implement a route to retrieve all 
# workout sessions for a specific member.

# Expected Outcome: A comprehensive set of endpoints for scheduling and viewing workout sessions, with the ability to retrieve detailed 
# information about each session. 


from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '$E@kster1',
    'host': 'localhost',
    'database': 'fitness_center_db'
}

# Establish database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Database connected successfully!")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


@app.route('/')
def home():
    return "Welcome to the Fitness Center Management System!"

# READ - Get all members
@app.route('/members', methods=['GET'])
def get_members():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(members)
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# READ - Get a specific member by ID
@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM members WHERE id = %s", (id,))
        member = cursor.fetchone()
        cursor.close()
        connection.close()
        if member:
            return jsonify(member)
        else:
            return jsonify({"error": "Member not found"}), 404
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# CREATE - Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        new_member = request.json
        sql = """INSERT INTO members (name, email, phone, membership_date) 
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (new_member['name'], new_member['email'], new_member['phone'], new_member['membership_date']))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Member added successfully!"}), 201
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# UPDATE - Update a member's details
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        update_data = request.json
        sql = """UPDATE members SET name = %s, email = %s, phone = %s, membership_date = %s 
                 WHERE id = %s"""
        cursor.execute(sql, (update_data['name'], update_data['email'], update_data['phone'], update_data['membership_date'], id))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Member not found"}), 404
        return jsonify({"message": "Member updated successfully!"})
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# DELETE - Delete a member by ID
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM members WHERE id = %s"
        cursor.execute(sql, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Member not found"}), 404
        return jsonify({"message": "Member deleted successfully!"})
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# CREATE - Schedule a new workout session
@app.route('/workoutsessions', methods=['POST'])
def schedule_workout_session():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        new_session = request.json
        sql = """INSERT INTO workoutsessions (member_id, session_date, session_time, activity_type) 
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (new_session['member_id'], new_session['session_date'], new_session['session_time'], new_session['activity_type']))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Workout session scheduled successfully!"}), 201
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# READ - Get all workout sessions
@app.route('/workoutsessions', methods=['GET'])
def get_workout_sessions():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM workoutsessions")
        workout_sessions = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(workout_sessions)
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# READ - Get all workout sessions for a specific member
@app.route('/workoutsessions/member/<int:member_id>', methods=['GET'])
def get_workout_sessions_by_member(member_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM workoutsessions WHERE member_id = %s", (member_id,))
        workout_sessions = cursor.fetchall()
        cursor.close()
        connection.close()
        if workout_sessions:
            return jsonify(workout_sessions)
        else:
            return jsonify({"error": "No workout sessions found for this member"}), 404
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# UPDATE - Update a workout session
@app.route('/workoutsessions/<int:id>', methods=['PUT'])
def update_workout_session(id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        update_data = request.json
        sql = """UPDATE workoutsessions SET session_date = %s, session_time = %s, activity_type = %s 
                 WHERE id = %s"""
        cursor.execute(sql, (update_data['session_date'], update_data['session_time'], update_data['activity_type'], id))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Workout session not found"}), 404
        return jsonify({"message": "Workout session updated successfully!"})
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

# DELETE - Delete a workout session by ID
@app.route('/workoutsessions/<int:id>', methods=['DELETE'])
def delete_workout_session(id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM workoutsessions WHERE id = %s"
        cursor.execute(sql, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Workout session not found"}), 404
        return jsonify({"message": "Workout session deleted successfully!"})
    else:
        return jsonify({"error": "Unable to connect to the database"}), 500

if __name__ == '__main__':
    app.run(debug=True)



