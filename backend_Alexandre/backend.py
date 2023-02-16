from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    employees = [
        {'id': 1, 'firstName': 'Paul', 'lastName': 'Jack', 'emailId': 'pauljacke@example.com'},
        {'id': 2, 'firstName': 'Janette', 'lastName': 'Ongle', 'emailId': 'janetteongle@example.com'},
        {'id': 3, 'firstName': 'Phylippe', 'lastName': 'Munche', 'emailId': 'phylippemunche@example.com'}
    ]
    
    return jsonify(employees)
@app.route('/api/v1/employees', methods=['POST'])
def create_employee():
    new_employee = {
        'id': request.json['id'],
        'firstName': request.json['firstName'],
        'lastName': request.json['lastName'],
        'emailId': request.json['emailId']
    }
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/api/v1/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employees.remove(employee)
            return jsonify({'message': f'Employee with ID {employee_id} has been deleted'})
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/v1/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    global employees
    employee_to_update = None
    for employee in employees:
        if employee['id'] == employee_id:
            employee_to_update = employee
            break
    if employee_to_update:
        employee_data = request.get_json()
        employee_to_update.update(employee_data)
        return jsonify(employee_to_update)
    else:
        return jsonify({'erreur': f"L'employé avec l'ID {employee_id} n'a pas été trouvé"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    


    

    
    
    
    
