import pyttsx3

class Voice:
    def __init__(self):
        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        self.set_voice("male")  # Default to male voice

    def set_voice(self, gender: str):
        voices = self.engine.getProperty('voices')
        # Set voice based on gender
        if gender == "female":
            self.engine.setProperty('voice', voices[1].id)  # Adjust index for female
        else:
            self.engine.setProperty('voice', voices[0].id)  # Default to male

    def speak(self, text: str):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            raise RuntimeError(f"Voice Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    voice = Voice()
    voice.speak("Hello, I am Allie!")
