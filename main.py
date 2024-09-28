import vonage
from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

VONAGE_API_KEY = os.getenv("VONAGE_API_SECRET")
VONAGE_API_SECRET =  os.getenv("VONAGE_API_SECRET")
VONAGE_PHONENO = os.getenv("VONAGE_PHONENO")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = vonage.Sms(client)

def get_weather(location):
    params = {'q': location, 'appid': WEATHER_API_KEY, 'units': 'metric'}
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Weather: {main}, {description}. Temperature: {temp}°C."
    else:
        return "Sorry, couldn't fetch the weather for that location."

@app.route('/sms', methods=['GET'])
def receive_sms():
    incoming_msg = request.form.get('text')
    from_number = request.form.get('msisdn')

    if incoming_msg:
        weather_info = get_weather(incoming_msg.strip())
        sms.send_message({
            'from': VONAGE_PHONENO,
            'to': from_number,
            'text': weather_info
        })
    return "Message sent", 200

if __name__ == '__main__':
    app.run(debug=True)