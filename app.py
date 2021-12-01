from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=["POST"])
def stndard():
    text = request.json.get("request", {}).get("command")
    end = False
    if text == "выход":
        response_text = "Пока!"
        end = True
    elif text:
        response_text = f"Вы сказали {text}"
    else:
        response_text = "ВЫ таки ничего не сказали"
    response = {
        "response":{
            "text":response_text,
            "end_session": end,
            "buttons":[
                {
                    "title": "Нажми меня",
                    "hide": True
                },
                {
                    "title": "Выход",
                    "hide": True
                },
                {
                    "title": "Нажми на ссылку!",
                    "url": "https://www.youtube.com/",
                    "hide": True
                }
            ]
        },

        "version": "2.0"
    }
    return response