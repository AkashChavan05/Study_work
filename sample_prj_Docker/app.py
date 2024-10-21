from flask import Flask, jsonify, request, render_template

# Initialize the Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask API"), 200

# Route to render HTML form
@app.route('/add_Employee', methods=['GET'])
def add_item_form():
    return render_template('index.html')


# Route to handle form data and add item
@app.route("/employee_details", methods=["POST"])
def add_item():
    EmployeeID = request.form.get('id')
    Employee_name = request.form.get('name')
    Phone_no = request.form.get("phone_no")

    if EmployeeID and Employee_name:
        new_item = {"id": EmployeeID, "name": Employee_name,
        "phone_no": Phone_no}
        return jsonify(message="Item added successfully", item=new_item), 201
    else:
        return jsonify(message="Missing item ID or name"), 400

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080, debug=True)

