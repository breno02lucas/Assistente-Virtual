import speech_recognition as sr

def ReconhecerComandos():

    # Variável para guardar as informações do módulo e seus métodos
    rec = sr.Recognizer()

    # Utilizaremos os métodos do módulo para trabalhar com o que está sendo escutado através do microfone
    # Usaremos o with "com" para entrar no código do Microfone (ele é usado para iniciar/entrar e finalizar/sair de algo)
    with sr.Microphone() as mic: 
        print("Estou te ouvindo")

        # Configuraremos a pausa limite (threshold = limite)
        # Ou seja, reconhecer quando finalizamos uma fala paramos de falar
        rec.pause_threshold = 0.7

        # Variável que guardará o que está sendo dito através do microfone
        audio = rec.listen(mic)

        # Agora, usaremos o try e except (o try é um método para tentar fazer algo, caso não consiga, ele retorne um erro)
        try:
            print("...")

            # Variável para analisar a frase que foi falada
            sintetizarFala = rec.recognize_google(audio, language="pt-br")
            print(sintetizarFala)

        # Caso ele não consiga sintetizar, ele retorna o erro que deu
        except Exception as e:
            print(e)
            print("Não consegui entender, pode repetir?")
            return "..."

        # Retorne o que foi falado
        return sintetizarFala
    
