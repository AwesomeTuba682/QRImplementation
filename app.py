from flask import Flask, render_template, request, jsonify
import pyrebase


app = Flask(__name__)

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyBY5nw2l6OV7vj9bY6o9cm-XViE-x8AN6w",
    "authDomain": "luminarymvp.firebaseapp.com",
    "databaseURL": "https://luminarymvp-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "luminarymvp",
    "storageBucket": "luminarymvp.appspot.com",
    "messagingSenderId": "842890581479",
    "appId": "1:842890581479:web:25547f389aec3aa7abd942",
    "measurementId": "G-EMKS8FP9ZJ"
}



firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

@app.route("/<uuid>")
def verify(uuid):
    data = db.child("QR").get().val()
    
    if data and uuid in data.values():
        # Remove the UUID from the database
        db.child("QR").child(get_key_by_value(data, uuid)).remove()
        return render_template("verified.html")
    else:
        return render_template("error.html")

# Helper function to get the key from a dictionary based on a given value
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

if __name__ == "__main__":
    app.run()