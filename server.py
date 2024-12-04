from flask import Flask, request
import requests

app = Flask(__name__)

# Временные значения токена Telegram-бота и chat_id
TELEGRAM_BOT_TOKEN = "7870334293:AAELUDHPF44pyt7OXLW9OVK5TG-6QHvAeuA"
CHAT_ID = "317963727"  # Ваш временный chat_id

@app.route('/submit', methods=['POST'])
def submit_form():
    # Получаем данные из формы
    data = request.json
    name = data.get('name')
    phone = data.get('phone')

    # Формируем сообщение для Telegram
    message = f"Новая заявка:\nИмя: {name}\nТелефон: {phone}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    # Отправляем сообщение
    response = requests.post(url, json={"chat_id": CHAT_ID, "text": message})

    if response.status_code == 200:
        return {"status": "success"}, 200
    else:
        return {"status": "error", "message": response.text}, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

