from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Это разрешает CORS для всех маршрутов

@app.route("/", methods=["GET"])
def index():
    return "Сервер работает!"

@app.route("/send", methods=["POST"])
def send_to_telegram():
    data = request.json
    name = data.get("name")
    phone = data.get("phone")

    if not name or not phone:
        return jsonify({"error": "Имя и телефон обязательны"}), 400

    # Telegram API
    telegram_bot_token = "Ваш токен"
    chat_id = "Ваш chat_id"
    message = f"Новая заявка:\nИмя: {name}\nТелефон: {phone}"

    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        response = requests.post(url, json=payload)
        if response.ok:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "Ошибка при отправке в Telegram"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

