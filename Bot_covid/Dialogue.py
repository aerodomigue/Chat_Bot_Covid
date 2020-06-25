import pandas as pd
import numpy as np


class Communication:
    def __init__(self):
        self.diag_line = 0
        self.dfValue = pd.DataFrame({"type": ['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing',
                                         'Sore-Throat', 'None_Sympton', 'Pains', 'Nasal-Congestion',
                                         'Runny-Nose', 'Diarrhea', 'None_Experiencing', 'Age_0-9', 'Age_10-19',
                                         'Age_20-24', 'Age_25-59', 'Age_60+', 'Severity_Mild',
                                         'Severity_Moderate', 'Severity_None', 'Severity_Severe', 'Contact_Yes']})
        self.dfValue["value"] = np.nan

    def get_dialogue(self, sio):
        sio.emit("newMessage", '{"userName":"Covid-Bot","messageContent":"Bonjour","roomName":"covid"}')
        sio.emit("newMessage", '{"userName":"Covid-Bot","messageContent":"Je suis un bot qui est la pour vous aider","roomName":"covid"}')
        sio.emit("newMessage",
                 '{"userName":"Covid-Bot","messageContent":"Pour commencer, a t\'il de la fièvre?","roomName":"covid"}')

    def Set_value(self, data):
        print("message")


