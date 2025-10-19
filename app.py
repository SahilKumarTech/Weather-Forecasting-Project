from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# OpenWeatherMap API Key
API_KEY = "afca7094e1a0bd6435e307504985a6f0"
BASE_URL = "https://api.openweathermap.org/data/2.5/"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.json
    city = data.get('city', '').strip()

    if not city:
        return jsonify({'error': 'City name is required'}), 400

    try:
        # Try India first
        current_url = f"{BASE_URL}weather?q={city},IN&appid={API_KEY}&units=metric"
        current_response = requests.get(current_url)
        current_data = current_response.json()

        # If not found in India, try worldwide
        if str(current_data.get('cod')) != '200':
            current_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
            current_response = requests.get(current_url)
            current_data = current_response.json()

        if str(current_data.get('cod')) != '200':
            return jsonify({'error': current_data.get('message', 'City not found')}), 404

        # Process current weather
        current_weather = {
            'temp': round(current_data['main']['temp']),
            'description': current_data['weather'][0]['description'].title(),
            'humidity': current_data['main']['humidity'],
            'wind': current_data['wind']['speed'],
            'feels_like': round(current_data['main']['feels_like']),
            'pressure': current_data['main']['pressure'],
            'icon': current_data['weather'][0]['icon']
        }

        # Get 5-day forecast
        forecast_url = f"{BASE_URL}forecast?q={current_data['name']}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        forecast_list = []
        processed_dates = set()

        for item in forecast_data.get('list', []):
            date_str = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            if date_str not in processed_dates and len(forecast_list) < 5:
                processed_dates.add(date_str)
                forecast_list.append({
                    'dt': item['dt'],
                    'temp': round(item['main']['temp']),
                    'description': item['weather'][0]['description'].title(),
                    'icon': item['weather'][0]['icon']
                })

        return jsonify({
            'current': current_weather,
            'forecast': forecast_list,
            'city': current_data['name']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
