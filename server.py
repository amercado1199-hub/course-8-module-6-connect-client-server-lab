from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

#Temporary list of events acting like our database
events = [
    {"id": 1, "title": "Yoga in the park"},
    {"id": 2, "title": "Lake 5k run"},
]

#Home route
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200

#Get route to send all events to the frontend
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

#Post route to recieve a new event from the frontend 
@app.route("/events", methods=["POST"])
def add_event():
    global events
    
    #Get JSON data sent from JavaScript
    data = request.get_json()
    
    #Create a new id by finding the highest current id and adding 1
    new_id = max([event["id"] for event in events], defaukt=0) + 1
    
    #Create a new event object
    new_event = {
        "id": new_id,
        "title": data["title"]
    }
    
    #Add the new event to the eventss list 
    events.append(new_event)
    
    #Send the new event back with 201 Created status
    return jsonify(new_event), 201

#Run the server only when this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)