import model
import socketio
import json
import Dialogue


sio = socketio.Client()
model_bot = model.model()
communication = Dialogue.Communication()

@sio.event
def connect():
    print('connect')

@sio.event
def disconnect():
    print('disconnect ')

@sio.event()
def updateChat(data):
    print(data)
    jdata = json.loads(data)
    if not communication.reset(sio, jdata["messageContent"]):
        communication.Set_value(sio, jdata["messageContent"])
        communication.verif_value_ok(sio, model_bot)

@sio.event
def newUserToChatRoom(data):
    communication.get_dialogue(sio)

sio.connect('http://localhost:3000')
sio.emit("subscribe", '{"roomName":"covid","userName":"Covid-Bot"}')
