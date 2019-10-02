
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_helper import push_on_huge_change

cred = credentials.Certificate(
    "iot-plant-cbc8a-firebase-adminsdk-okfmw-f23b682a66.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-plant-cbc8a.firebaseio.com/'
})

def add_listener(path, listener):
    db_ref = db.reference().child(path).listen(listener)

@push_on_huge_change(['humidity', 'temperatue'])
def push_val(path, value):
    value["timestamp"] = {'.sv': 'timestamp'}
    ref = db.reference(path)
    return ref.push(value)