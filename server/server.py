# # from flask import Flask

# # app = Flask(__name__)

# # @app.route('/members')
# # def members():
# #     return {"members": ["member1", "member2", "member3"]}

# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # This will enable CORS for all routes

# @app.route('/submit', methods=['POST'])
# def submit():
#     data = request.get_json()
#     print(data)
#     # Process data as needed
#     return jsonify({"message": "Data received"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# import os

# app = Flask(__name__)
# CORS(app)

# # Configuration for PostgreSQL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/testcases_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Model for the test case
# class TestCase(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     input = db.Column(db.String, nullable=False)
#     status = db.Column(db.String, nullable=False)
#     time = db.Column(db.String, nullable=False)
#     type = db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return f"<TestCase {self.input}>"

# # Endpoint to handle the submission of test cases
# @app.route('/submit', methods=['POST'])
# def submit():
#     data = request.get_json()
#     test_cases = data['test_cases']
    
#     for case in test_cases:
#         new_case = TestCase(
#             input=case['input'],
#             status=case['status'],
#             time=case['time'],
#             type=case['type']
#         )
#         db.session.add(new_case)
#     db.session.commit()
#     return jsonify({"message": "Test cases added successfully!"}), 201

# if __name__ == "__main__":
#     if not os.path.exists('testcases.db'):
#         db.create_all()
#     app.run(debug=True)

