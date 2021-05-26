import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

in_voiceid = "com.apple.speech.synthesis.voice.rishi"

engine.setProperty('voice',in_voiceid)

engine.say("Hi, How are you?")
engine.say("Please wait")

engine.runAndWait()

engine.stop()