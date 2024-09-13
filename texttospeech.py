import pyttsx3 as tts

def Fale(diga):

    # Iniciializando o módulo Text to Speech
    sintetizador = tts.init()

    # Escolha da voz
    voz = sintetizador.getProperty("voices")

    # Voz masculina [0] ou feminina [1]
    sintetizador.setProperty("voice", voz[0].id)

    # Texto para Voz
    sintetizador.say(diga)

    # Executar a voz e esperar finalizar a fala
    sintetizador.runAndWait()