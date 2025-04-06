<<<<<<< HEAD
from flask import Flask, jsonify

app = Flask(__name__)

# Added 'id' field to the students dictionary for individual lookup
students = [
    {
        'id': 1,
        'name': 'Hrishikesh',
        'age': '20',
        'email': 'hrish2004@gmail.com'
    },
    {
        'id': 2,
        'name': 'Hemanth',
        'age': '20',
        'email': 'hemanthbubby007@gmail.com'
    }
]

# Endpoint to get the full students list
@app.route('/students-list', methods=['GET'])
def get_students_list():
    return jsonify(students)

# Endpoint to get a student by ID
@app.route('/students/get/<int:id>', methods=['GET'])
def get_students_by_id(id):  # Added `id` parameter
    for student in students:
        if student['id'] == id:  # Fixed the condition and corrected dictionary access
            return jsonify(student)  # Return as JSON
    return jsonify({'error': 'Student not found'}), 404  # Handle invalid IDs

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
=======
from flask import Flask, jsonify, request

todo = Flask(__name__)

students = [
    {
        'id': 1,
        'name': 'Mike',
        'age': 10
    },
    {
        'id': 2,
        'name': 'Jonathan',
        'age': 20
    },
    {
        'id': 3,
        'name': 'Dio',
        'age': 30
    },
    {
        'id': 4,
        'name': 'John',
        'age': 40
    }
]


@todo.route('/students-list')
def get_students_list():
    return jsonify(students)


@todo.route('/students/get/<int:id>')
def get_students_by_id(id):
    for std in students:
        if std['id'] == id:
            return jsonify(std)
    return jsonify({'message': 'Student not found'}), 404


# Add POST method to add new student
@todo.route('/students/add', methods=['POST'])
def add_student():
    data = request.get_json()

    # Check if all required fields are present

    if not data or 'name' not in data or 'age' not in data:
        return jsonify({'message': 'Invalid data'}), 400

    # Create new student with the next available ID
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': data['name'],
        'age': data['age']
    }

    # Add new student to the list
    students.append(new_student)

    return jsonify({'message': 'Student added', 'student': new_student}), 201


if __name__ == '__main__':
    todo.run(
        debug=True
    )
>>>>>>> ebd7eea3bc0eaab176c7cd09dc2a2f4505c2ab2f
