import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the rate at which the text should be spoken
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# Set the volume of the spoken text
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)

# Set the voice to use
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set the text to be spoken
text = "Hello, this is a test of the text-to-speech system using pyttsx3."

# Save the spoken text to an audio file
engine.save_to_file(text, 'output.mp3')

# Disconnect the TTS engine
engine.stop()