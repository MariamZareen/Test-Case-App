from flask import jsonify, render_template, request, redirect, url_for, flash
from server import app, db
from server.models import TestCase

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    test_cases = data['test_cases']
    
    for case in test_cases:
        new_case = TestCase(
            input=case['input'],
            status=case['status'],
            time=case['time'],
            type=case['type']
        )
        db.session.add(new_case)
    db.session.commit()
    return jsonify({"message": "Test cases added successfully!"}), 201