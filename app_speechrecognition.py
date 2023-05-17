from flask import Flask, render_template, request
import requests
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/switchOn', methods=['POST'])
def switchOn():
    url = "http://192.168.178.188/cm?cmnd=Power%20On"
    response = requests.get(url)
    return response.text

@app.route('/switchOff', methods=['POST'])
def switchOff():
    url = "http://192.168.178.188/cm?cmnd=Power%20Off"
    response = requests.get(url)
    return response.text

@app.route('/voiceCommand', methods=['POST'])
def voiceCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="de-DE")
        if command == 'ein':
            switchOn()
            print("HTTP-Request zum Einschalten an localhost gesendet")
            return "Einschalten"
        elif command == 'aus':
            switchOff()
            print("HTTP-Request zum Ausschalten an localhost gesendet")
            return "Ausschalten"
        else:
            return "Ungültiger Befehl"
    except sr.UnknownValueError:
        return "Sprache konnte nicht erkannt werden"
    except sr.RequestError:
        return "Fehler bei der Spracherkennung"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
