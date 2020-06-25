import eventlet
import socketio
import json
import Dialogue


sio = socketio.Client()
communication = Dialogue.Communication()

@sio.event
def connect():
    print('connect')

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect():
    print('disconnect ')

@sio.event()
def updateChat(data):
    print('I received a message!')
    jdata = json.loads(data)
    print(jdata["messageContent"])

@sio.on('my message')
def on_message(data):
    print('I received a message!')
    communication.

@sio.event
def newUserToChatRoom(data):
    print('I received a guy!')
    communication.get_dialogue(sio)

sio.connect('http://localhost:3000')
sio.emit("subscribe", '{"roomName":"covid","userName":"Covid-Bot"}')
