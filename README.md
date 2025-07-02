# 🧠 KOU AI – Voice-Controlled Desktop Assistant

A simple Python application that allows you to **open and close applications using your voice**.  
It uses speech recognition, text-to-speech, and a minimal GUI built with `customtkinter`.

## 🚀 Features

- 🎙️ Listens for voice commands in English
- 🗣️ Responds using text-to-speech (TTS)
- 🖥️ Opens and closes popular Windows applications:
  - Chrome, Notepad, Calculator, Paint, Explorer, CMD, Task Manager, etc.
- 🎛️ Clean and minimal GUI interface
- 🧵 Runs recognition in a separate thread to avoid freezing the UI

## 🛠️ Technologies Used

- `Python`
- `customtkinter`
- `pyttsx3`
- `speech_recognition`
- `subprocess`, `os`, `threading`


## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
