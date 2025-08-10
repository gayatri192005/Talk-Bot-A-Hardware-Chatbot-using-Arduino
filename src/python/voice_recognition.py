# File: voice_recognition.py
# Purpose: Capture voice input and convert to text.

import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
        return ""
    except sr.RequestError:
        print("⚠️ API unavailable")
        return ""

if __name__ == "__main__":
    print(get_voice_input())
