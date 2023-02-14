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


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    


    

    
    
    
    
