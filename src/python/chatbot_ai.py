# File: chatbot_ai.py
# Purpose: AI chatbot that processes voice commands and controls Arduino.

from voice_recognition import get_voice_input
from serial_comm import ArduinoComm
import random

# Example command mapping
COMMANDS = {
    "turn on light": "LED_ON",
    "light on": "LED_ON",
    "turn off light": "LED_OFF",
    "light off": "LED_OFF",
    "beep": "BUZZER_ON",
    "move servo to": "SERVO_",  # Needs angle after this
}

def process_command(text):
    for phrase, cmd in COMMANDS.items():
        if phrase in text:
            if "servo" in phrase:
                words = text.split()
                for word in words:
                    if word.isdigit():
                        return f"{cmd}{word}"
            return cmd
    return None

def ai_response(text):
    responses = [
        "Got it!",
        "Okay, executing your command.",
        "Done!",
        "On it!"
    ]
    return random.choice(responses)

if __name__ == "__main__":
    arduino = ArduinoComm("COM3", 9600)
    while True:
        voice_text = get_voice_input()
        if not voice_text:
            continue
        command = process_command(voice_text)
        if command:
            arduino.send_command(command)
            print(f"🤖 {ai_response(voice_text)}")
        else:
            print("🤖 Sorry, I didn't understand the command.")
