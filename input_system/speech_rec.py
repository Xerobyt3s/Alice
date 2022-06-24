import speech_recognition as sr
import pyaudio

r = sr.Recognizer()


while True:
    

    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic)

            text = r.recognize_google(audio)

            text.lower()

            test = f"{text}"


            if (text.startwith("alice")):
                print(text)
            

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue
