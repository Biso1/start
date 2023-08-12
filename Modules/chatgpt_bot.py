from revChatGPT.V1 import Chatbot
class chatgpt:
    def __init__(self, key):
        self.main = Chatbot(config={ "access_token": key })
        self.key = key
    def get_response(self, prompt):
        message = ""
        for data in self.main.ask(prompt):
            message = data["message"]
        return message