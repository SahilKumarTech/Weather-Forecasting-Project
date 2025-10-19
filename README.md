# Weather-Forecasting-Project
A modern and responsive weather forecasting web application built with Flask that provides current weather conditions and 5-day forecasts for any city worldwide.

## Live Demo
Live App Link <>

## Features
- Current Weather - Real-time temperature, humidity, wind speed, and more

- 5-Day Forecast - Weather predictions for the next 5 days

- Global Coverage - Search any city worldwide with India-first priority

- Responsive Design - Works perfectly on desktop, tablet, and mobile

- Beautiful UI - Modern and user-friendly interface

- Accurate Data - Powered by OpenWeatherMap API

## Technology Stack
- Backend: Flask (Python)

- Frontend: HTML, CSS, JavaScript

- API: OpenWeatherMap API

- Deployment: Render

- Version Control: Git & GitHub

## Prerequisites
- Python 3.7+

- OpenWeatherMap API Key

  
## Project Structure
text
weather-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in repo)
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Stylesheets
    ├── js/
    │   └── script.js     # JavaScript functionality
    └── images/           # Static images

## Deployment on Render

1. Fork/Upload to GitHub
Ensure your code is on GitHub repository.

2. Deploy on Render
Go to Render.com

Click "New +" → "Web Service"

Connect your GitHub repository

Use these settings:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Add environment variable:

Key: WEATHER_API_KEY

Value: your_api_key_here

3. Access Your Live App
Once deployed, your app will be available at:
https://your-app-name.onrender.com

🔑 Getting OpenWeatherMap API Key
Sign up at OpenWeatherMap

Go to API Keys section

Generate a new API key (free tier available)

Use this key in your environment variables

🎯 Usage Instructions
Enter a city name in the search box

Click "Get Weather" or press Enter

View current weather and 5-day forecast

The app automatically tries Indian cities first, then searches globally

🐛 Troubleshooting
Common Issues:
City Not Found

Check spelling of city name

Try different city names

API Key Error

Verify your OpenWeatherMap API key

Check environment variables

Deployment Issues

Ensure requirements.txt is correct

Verify start command in Render

🤝 Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
OpenWeatherMap for weather data API

Flask web framework

Render for hosting

📞 Support
If you have any questions or issues, please open an issue on GitHub.

Made with ❤️ using Flask & OpenWeatherMap API

⭐ Don't forget to star this repository if you found it helpful!


