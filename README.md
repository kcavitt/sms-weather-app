# Weather SMS Bot using Vonage and OpenWeatherMap API

This Python script allows users to send an SMS with a location (city or ZIP code) and receive the weather information via SMS using the Vonage API and OpenWeatherMap API. It uses Flask to receive incoming SMS and ngrok to expose your local server for external connections.

## Prerequisites

Before you can use this project, make sure you have the following installed:

- **Python 3.12.**
- **Pip** (Python package manager)
- **Vonage API credentials** (API Key, Secret, and a phone number)
- **OpenWeatherMap API Key**
- **Ngrok Account** (not nessessary)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/weather-sms-bot.git
cd weather-sms-bot
```

### 2. Run the application
```bash
pip install -r requirements.py
python main.py
```

### 3. Expose the webhook
```bash
ngrok http 5000
```

### 4. Configuring Vonage
Docs: https://developer.vonage.com/en/api/sms?source=messaging

View SMS messages at Logs -> SMS Logs
** You need to set the webhook to your ngrok url. **
API Settings -> Inbound SMS hooks
Set it to: https://<your_ngrok_url>/sms# sms-weather-app
