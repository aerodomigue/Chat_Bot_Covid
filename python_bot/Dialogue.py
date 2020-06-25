import pandas as pd
import numpy as np


class Communication:
    def __init__(self):
        self.diag_line = 0
        self.dfValue = pd.DataFrame({"type": ['Pour commencer, a t\'il de la fièvre [Oui/Non]?',
                                              'est il fatigué [Oui/Non]?',
                                              'a t\'il une toux sèche [Oui/Non]?',
                                              'a t\'il du mal a respirè [Oui/Non]?',
                                              'a t\'il la gorge irrité [Oui/Non]?',
                                              'a t\'il des douleurs [Oui/Non]?',
                                              'a t\'il des Congestion nasale [Oui/Non]?',
                                              'a t\'il le nez qui coule [Oui/Non]?',
                                              'a t\'il la diarrhée [Oui/Non]?',
                                              'est il asymptomatique [Oui/Non]?',
                                              'a t\'il entre 0-9 ans [Oui/Non]?',
                                              'a t\'il entre 10-19 ans [Oui/Non]?',
                                              'a t\'il entre 20-24 ans [Oui/Non]?',
                                              'a t\'il entre 25-59 ans [Oui/Non]?',
                                              'a t\'il entre plus de 59 ans [Oui/Non]?',
                                              'son niveau de gravité est elle légère [Oui/Non]?',
                                              'son niveau de gravité est elle Moyenne [Oui/Non]?',
                                              'son niveau de gravité est elle Importante [Oui/Non]?',
                                              'a t\'il été en contact avec un porteur du covid-19 [Oui/Non]']})
        self.dfValue["value"] = np.nan

    def get_dialogue(self, sio):
        sio.emit("newMessage", '{"userName":"Covid-Bot","messageContent":"Bonjour","roomName":"covid"}')
        sio.emit("newMessage", '{"userName":"Covid-Bot","messageContent":"Je suis un bot qui est la pour vous aider","roomName":"covid"}')
        sio.emit("newMessage",
                 '{"userName":"Covid-Bot","messageContent":"' + self.dfValue.iloc[self.diag_line][
                     "type"] + '","roomName":"covid"}')

    def Set_value(self, sio, data):
        try:
            if data.upper() == "OUI" or data.upper() == "O" or data.upper() == "Y":
                self.dfValue._set_value(self.diag_line, "value", 1)
                self.diag_line += 1
            elif data.upper() == "NON" or data.upper() == "N":
                self.dfValue._set_value(self.diag_line, "value", 0)
                self.diag_line += 1
            else:
                sio.emit("newMessage", '{"userName":"Covid-Bot","messageContent":"Je n\'ai pas compris","roomName":"covid"}')
            sio.emit("newMessage",
                     '{"userName":"Covid-Bot","messageContent":"' + self.dfValue.iloc[self.diag_line][
                         "type"] + '","roomName":"covid"}')
        except IndexError:
            print("error index")

    def verif_value_ok(self, sio, model):
        if self.diag_line >= len(self.dfValue.index):
            if model.fit(self.dfValue):
                message = "Il y a de trés peu chance qu'il soit porteur du covid"
            else:
                message = "Il y a de trés forte change qu'il soit porteur du covid"
            sio.emit("newMessage",
                     '{"userName":"Covid-Bot","messageContent":"' + message + '","roomName":"covid"}')
            self.diag_line = 0

    def reset(self, sio, data):
        if data.upper() == "RESET":
            self.diag_line = 0
            self.dfValue["value"] = np.nan
            sio.emit("newMessage",
                     '{"userName":"Covid-Bot","messageContent":"' + self.dfValue.iloc[self.diag_line][
                         "type"] + '","roomName":"covid"}')
            return True
        else:
            return False





