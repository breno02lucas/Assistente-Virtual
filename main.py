from datetime import datetime, date
import python_weather
import asyncio
import pyautogui as gui
import os
import translate as trad
import pywhatkit as yb
import speech as rec
import texttospeech as falar
import sympy
import re 

def data_hoje():
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    falar.Fale(f"Hoje é dia {date.today().day} de {meses[date.today().month - 1]} de {date.today().year}")
    
def hora_agora():
    falar.Fale(f"Agora são {datetime.now().hour} horas e {datetime.now().minute} minutos")

def dia_da_semana():
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    falar.Fale(f"Hoje é {dias[date.today().weekday()]}")

async def clima_hoje():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        clima = await client.get("Brusque")

        if clima.temperature < 15:
            falar.Fale(f"Hoje está um dia frio, a temperatura é de {clima.temperature}°")
        elif clima.temperature >= 15 and clima.temperature < 20:
            falar.Fale(f"Hoje está um dia ameno, a temperatura é de {clima.temperature}°")
        else:
            falar.Fale(f"Hoje está um dia quente, a temperatura é de {clima.temperature}°")

        tempo = clima.kind
        traduzir = trad.Translator(to_lang="pt-br")
        traducao = traduzir.translate(str(tempo))
        falar.Fale(f"O tempo está {traducao}")

#asyncio.run(clima_hoje())

def volume_aumentar():
    for n in range(5):
        gui.press("volumeup")

def volume_diminuir():
    for n in range(5):
        gui.press("volumedown")

def volume_mutar():
    gui.press("volumemute")

def midia_prox():
    gui.press("nexttrack")

def midia_ante():
    gui.press("prevtrack")

def midia_playpause():
    gui.press("playpause")

def prog_word():
    os.system("start WINWORD")
    falar.Fale("Abrindo o Word...")

def prog_excel():
    os.system("start excel")
    falar.Fale("Abrindo o Excel...")

def prog_powerpoint():
    os.system("start powerpnt.exe")
    falar.Fale("Abrindo o PowerPoint...")

def prog_ps():
    os.system("start photoshop.exe")
    falar.Fale("Abrindo o Photoshop...")

def prog_ai():
    os.system("start illustrator.exe")
    falar.Fale("Abrindo o Illustrator...")

def prog_chrome():
    os.system("start chrome")
    falar.Fale("Abrindo o Chrome...")

def prog_google():
    os.system("start chrome google.com")
    falar.Fale("Abrindo o Google Pesquisa...")

def atalho_explorer():
    gui.hotkey("win", "e")
    falar.Fale("Abrindo o Explorador de Arquivos...")

def atalho_gerenciador():
    gui.hotkey("ctrl", "shift", "esc")
    falar.Fale("Abrindo o PowerPoint...")

def atalho_printscreen():
    gui.hotkey("win", "prtsc")
    falar.Fale("Fazendo captura de tela...")

def atalho_bloquear():
    gui.hotkey("win", "l")
    falar.Fale("Bloqueando...")

def traduzir_ingles():
    tradutor = trad.Translator(to_lang="pt-br")
    
    falar.Fale("Fale a frase que deseja traduzir...")
    traduzir = rec.ReconhecerComandos()

    traducao = tradutor.translate(traduzir)
    falar.Fale(f"A tradução é: {traducao}")

def buscar_video_yt():
    falar.Fale("Fale o vídeo que deseja assistir...")

    video = rec.ReconhecerComandos()
    yb.playonyt(video)

def formatar_problema():
    problema = rec.ReconhecerComandos()

    if " elevado a " in problema:
        problema = problema.replace(" elevado a ", "**")

    if " sobre " in problema:
        problema = problema.replace(" sobre ", "/")

    if " dividido por " in problema:
        problema = problema.replace(" dividido por ", "/")

    if " multiplicado por " in problema:
        problema = problema.replace(" multiplicado por ", "*")

    if " x " in problema:
        problema = problema.replace(" x ", "*")
    
    if " vezes " in problema:
        problema = problema.replace(" vezes ", "*")

    if " raiz de " in problema:
        problema = re.sub(r"raiz de (\d+)", r"(\1)**(1/2)", problema)

    if " raiz quadrada de " in problema:
        problema = re.sub(r"raiz quadrada de (\d+)", r"(\1)**(1/2)", problema)

    return problema

def resolver_problema():
    falar.Fale("Diga o cálculo: ")

    problema_str = formatar_problema()
    problema = sympy.sympify(problema_str)

    falar.Fale(f"O resultado é: {problema}")

def resolver_equacoes():
    problema_str = formatar_problema()
    problema_sympy = sympy.sympify(problema_str)
    problema = sympy.solveset(sympy.Eq(problema_sympy, 0), "x")

    print(problema)

def iniciar():

    cronometro = 0
    