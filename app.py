from Modules.chatgpt_bot import chatgpt
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
# file = open("token.txt", "r")
# token = file.read()
load_dotenv()
token = os.environ['token']
print(token)
# file.close()
bot = chatgpt(token)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["POST"])
def hello():
  data = request.get_json()
  return bot.get_response(data["message"])

@app.route('/test')
def test():
  return "yes working"
