from flask import Flask, jsonify, request;

app = Flask(__name__)

tasks= [
    {
        "Contact": "9987644456",
        "Name": "Raju",
        "done": False,
        "id": 1,
    },
    {
        "Contact": "9876543222",
        "Name": "Rahul",
        "done": False,
        "id": 2,
    }
]

@app.route("/")
def home_page():
    return(
        "Home page of 124Hw\n"
        "add add-data in the url to add a contact"
    )

@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)

    contact={
        "id": tasks[-1]["id"] + 1,
        "Name": request.json["Name"],
        "Contact":  request.json.get("Contact", ""),
        "done": False
    }
    tasks.append(contact)
    return jsonify({
        "status": "Success",
        "message": "Contact added successfully"
    })

if(__name__== "__main__"):
    app.run(debug=True)