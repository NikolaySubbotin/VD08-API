from flask import Flask, render_template
import requests

app = Flask(__name__)

# Запрос случайной цитаты с API
def get_random_quote():
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Маршрут для главной страницы
@app.route('/')
def home():
    quote = get_random_quote()  # Получаем случайную цитату
    if quote:
        return render_template('index.html', quote=quote)
    else:
        return "Ошибка при загрузке цитаты", 500

if __name__ == '__main__':
    app.run(debug=True)