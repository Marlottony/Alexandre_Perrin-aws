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

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    


    

    
    
    
    
