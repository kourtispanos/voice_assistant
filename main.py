import customtkinter as ctk
import threading
import pyttsx3
import speech_recognition as sr
import subprocess
import os

APP_PATHS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
    "paint": "C:\\Windows\\System32\\mspaint.exe",
    "wordpad": "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe",
    "explorer": "C:\\Windows\\explorer.exe",
    "task manager": "C:\\Windows\\System32\\Taskmgr.exe",
    "control panel": "C:\\Windows\\System32\\control.exe",
    "cmd": "C:\\Windows\\System32\\cmd.exe",
    "powershell": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
}

class KOU_AI:
    def __init__(self, root):
        self.root = root
        self.root.title("KOU AI")
        self.root.geometry("800x400")
        self.root.resizable(False, False)

        self.toggle_button = ctk.CTkButton(self.root, text="Activate", command=self.toggle_listening)
        self.toggle_button.pack(pady=160)

        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.listening = False

    def toggle_listening(self):
        self.listening = not self.listening
        if self.listening:
            self.toggle_button.configure(text="Listening...")
            threading.Thread(target=self.listen_and_respond, daemon=True).start()
        else:
            self.toggle_button.configure(text="Activate")

    def listen_and_respond(self):
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)

            query = self.recognizer.recognize_google(audio, language="en-US").lower()
            print(f"You said: {query}")

            if "open" in query:
                self.open_app(query)
                response = "Opened the application."
            elif "close" in query:
                self.close_app(query)
                response = "Closed the application."
            else:
                response = "Sorry, I can only open or close applications."

            print(f"KOU AI: {response}")
            self.engine.say(response)
            self.engine.runAndWait()

        except Exception as e:
            print(f"Error: {e}")
            self.engine.say("Sorry, I didn't catch that.")
            self.engine.runAndWait()

        self.toggle_button.configure(text="Activate")
        self.listening = False

    def open_app(self, command):
        for name, path in APP_PATHS.items():
            if name in command:
                try:
                    subprocess.Popen(path)
                except Exception as e:
                    print(f"Failed to open {name}: {e}")
                break

    def close_app(self, command):
        for name in APP_PATHS:
            if name in command:
                try:
                    exe_name = os.path.basename(APP_PATHS[name])
                    os.system(f"taskkill /f /im {exe_name}")
                except Exception as e:
                    print(f"Failed to close {name}: {e}")
                break

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = KOU_AI(root)
    root.mainloop()
