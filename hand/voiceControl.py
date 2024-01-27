import speech_recognition as sr
import autopy

def listen_and_type():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Πες κάτι (Say something in Greek):")
        try:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)  # Listen to audio for 10 seconds
        except sr.WaitTimeoutError:
            print("Δεν ανιχνεύθηκε ήχος (No sound detected).")
            return None

    try:
        print("Αναγνώριση (Recognizing)...")
        text = recognizer.recognize_google(audio, language="el-GR")  # Greek language model
        print(f"Είπες: {text}")
        return text.lower()  # Convert to lowercase for case-insensitive comparison
    except sr.UnknownValueError:
        print("Συγγνώμη, δεν καταλαβαίνω τον ήχο (Sorry, could not understand audio).")
        return None
    except sr.RequestError as e:
        print(f"Σφάλμα κατά τη σύνδεση στο API της Google (Error connecting to Google API): {e}")
        return None

def type_text(text):
    autopy.key.type_string(text)


while True:
    command = listen_and_type()

    if command and "γράψε" in command:
        text_to_type = command.replace("γράψε", "").strip()  # Extract text after "γράψε"
        if text_to_type:
            type_text(text_to_type)
