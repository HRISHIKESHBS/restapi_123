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
