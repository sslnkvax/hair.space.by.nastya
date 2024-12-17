from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app, origins=["https://hair-space.info"])

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_to_telegram():
    data = request.json
    name = data.get("name")
    phone = data.get("phone")

    if not name or not phone:
        return jsonify({"error": "Имя и телефон обязательны"}), 400

    # Telegram API
    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")  # Используйте переменные окружения для безопасности
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")  # Используйте переменные окружения для безопасности
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
    port = int(os.environ.get("PORT", 5000))  # Получаем порт из переменной окружения
    app.run(host="0.0.0.0", port=port)  # Запускаем Flask на всех интерфейсах и нужном порту
