#pip install SpeechRecognition
#pip install pyttsx3
#pip install pywhatkit
#pip install wikipedia
#pip install language_tool_python
#pip install openai
#pip install pyaudio
#pip install requests
#pip install json

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import language_tool_python
import openai
import threading
import requests
import json
from openai import OpenAI

listener = sr.Recognizer()
tool = language_tool_python.LanguageTool('pt-BR')

openai.api_key = ''
client = OpenAI(
        base_url="http://localhost:11434/1",
        api_key="your api here",
)

def talk(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            return command
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o áudio. Por favor, repita.")
        return take_command()
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados de reconhecimento de fala; {e}.")
        return take_command()

def correct_spelling(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return ' '.join(corrected_text)

def spell_word(word):
    spelled_word = ' '.join(word)
    return spelled_word

def chatGPT(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message["content"]

def deepseek_response(query):
    conversation = [{"role": "user", "content": query}]
    data = {
        "model": "deepseek-r1",
        "messages": conversation,
        "stream": False
    }
    url = "http://localhost:11434/api/chat"
    response = requests.post(url, json=data)
    response_json = json.loads(response.text)
    answer = response_json["message"]["content"]
    return answer

def run_alexa():
    command = take_command()
    print(command)
    if 'desligar' in command:
        talk('Encerrando o programa.')
        print('Encerrando o programa')
        exit()
    elif 'tocar' in command:
        song = command.replace('tocar', '')
        talk('Tocando ' + song)
        print('Tocando ' + song)
        pywhatkit.playonyt(song)
    elif 'horas' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Agora são ' + time)
        print('Agora são ' + time)
    elif 'pesquisar' in command:
        search_query = command.replace('pesquisar', '')
        wikipedia.set_lang("pt")
        info = wikipedia.summary(search_query, 1)
        print(info)
        talk(info)
    elif 'como escrever' in command or 'corrigir' in command:
        word_to_correct = command.replace('como escrever', '').replace('corrigir', '')
        corrected_word = correct_spelling(word_to_correct)
        spelled_word = spell_word(corrected_word)
        talk(f"A ortografia correta de {word_to_correct} é {spelled_word}")
        print(f"A ortografia correta de {word_to_correct} é {spelled_word}")
    elif 'gpt' in command:
        response = "Desculpe, não consegui encontrar uma resposta para essa pergunta."
        try:
            response = chatGPT(command.replace('gpt', ''))
        except Exception as e:
            print(f"Erro ao interagir com o ChatGPT: {e}")
        talk(response)
        print(response)
    elif 'china' in command:
        response = "Desculpe, não consegui encontrar uma resposta para essa pergunta."
        try:
            response = deepseek_response(command.replace('china', ''))
        except Exception as e:
            print(f"Erro ao interagir com o Deepsek: {e}")
        talk(response)
        print(response)
    else:
        talk('Por favor, repita o comando.')
        print('Por favor, repita o comando.')

def main():
    while True:
        command_thread = threading.Thread(target=run_alexa)
        command_thread.start()
        command_thread.join()

if __name__ == "__main__":
    main()
