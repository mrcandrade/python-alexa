# Alexa-like Voice Assistant

Este projeto é um assistente de voz semelhante ao Alexa, que pode executar várias tarefas, como tocar músicas, informar a hora, pesquisar na Wikipedia, corrigir ortografia e interagir com modelos de linguagem como GPT-3.5 e DeepSeek.

## Requisitos

Certifique-se de ter os seguintes pacotes instalados:

```sh
pip install SpeechRecognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia
pip install language_tool_python
pip install openai
pip install pyaudio
pip install requests
pip install json


Configuração
Clone este repositório para o seu ambiente local.
Instale os pacotes necessários listados acima.

openai.api_key = 'sua_chave_api_aqui'

Uso
Execute o script alexa.py para iniciar o assistente de voz:

Funcionalidades
Desligar: Diga "desligar" para encerrar o programa.
Tocar Música: Diga "tocar [nome da música]" para tocar uma música no YouTube.
Informar a Hora: Diga "horas" para ouvir a hora atual.
Pesquisar na Wikipedia: Diga "pesquisar [termo]" para obter um resumo da Wikipedia.
Corrigir Ortografia: Diga "como escrever [palavra]" ou "corrigir [palavra]" para corrigir a ortografia.
Interagir com GPT-3.5: Diga "gpt [pergunta]" para obter uma resposta do modelo GPT-3.5.
Interagir com DeepSeek: Diga "china [pergunta]" para obter uma resposta do modelo DeepSeek.
Exemplo de Uso
Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Envie um pull request com suas alterações.

Licença
