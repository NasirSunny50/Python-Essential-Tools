import speech_recognition as sr
 
recorder = sr.Recognizer()
file = sr.AudioFile('Horses to Ride till Thrown.wav') 

with file as source_file:
    audio = recorder.record(source_file)
    
print(type(audio))
print(recorder.recognize_google(audio))