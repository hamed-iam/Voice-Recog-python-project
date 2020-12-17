import speech_recognition as sr


r = sr.Recognizer()
def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        print('Sorry, I did not get that! Try again please.')
    except sr.RequestError:
        print('Sorry, my server seems to be down. Please try again later.')
    return voice_data

print('How can I help you?')
voice_data = record_audio()
print(voice_data)
