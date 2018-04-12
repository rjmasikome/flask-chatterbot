from flask import Flask, render_template, request, jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

host = "0.0.0.0"
port = 3115
key = "admin"
botName = "Alfred Pennyworth"

english_bot = ChatBot(botName, storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")


@app.route("/chat",  methods=['GET', 'POST'])

def get_bot_response():

    if request.method != 'POST':
        return jsonify(
            message = "Bad Request"
        ), 400
    else:
        authorization = request.headers.get("Authorization")

        if authorization != key:
            return jsonify(
                message = "Forbidden"
            ), 403

        content = request.json

        if content is None or "message" not in content:
            return jsonify(
                message = "Bad Request"
            ), 400

        return jsonify(
            reply = str(english_bot.get_response(content["message"]))
        )

if __name__ == "__main__":
    app.run(host = host, port = port)
