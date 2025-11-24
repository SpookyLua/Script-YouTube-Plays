# Digite no CMD antes de rodar:
# pip install pytchat keyboard  

import pytchat
import keyboard
import time
import threading
from datetime import datetime
from collections import Counter


# ==============================
# CONFIGURAÇÕES
# ==============================

VIDEO_ID = "COLOQUE_AQUI_O_ID_DA_LIVE"    # ex: https://youtube.com/live/ABCDE → ABCDE
PRESS_TIME = 0.250          # tempo segurando a tecla
COOLDOWN = 1.0              # cooldown por usuário
INTERVALO_VOTACAO = 1.0     # intervalo da democracia (1 segundo)

script_enabled = False
cooldowns = {}

# buffer de votos: lista com comandos
voto_buffer = []


# Mapeamento de comandos → teclas
command_map = {
    "cima": "w",
    "esquerda": "a",
    "baixo": "s",
    "direita": "d",
    "ataque": "space",
    "super": "shift",
    "hipercarga": "q",
    "gadget": "f",
}


# ==============================
# FUNÇÕES DO SCRIPT
# ==============================

def toggle_script(e):
    global script_enabled
    script_enabled = not script_enabled
    estado = "LIGADO" if script_enabled else "DESLIGADO"
    print(f"\n[TOGGLE] Script agora está: {estado}\n")


def press_key(key):
    keyboard.press(key)
    time.sleep(PRESS_TIME)
    keyboard.release(key)


def process_chat_message(user, msg):
    global cooldowns, voto_buffer

    msg = msg.lower().strip()

    if msg not in command_map:
        return

    now = time.time()

    # cooldown por usuário
    if user in cooldowns and now - cooldowns[user] < COOLDOWN:
        return

    cooldowns[user] = now

    # adiciona voto ao buffer
    voto_buffer.append(msg)


def chat_listener(chat):
    print("[INFO] Lendo chat...\n")

    while chat.is_alive():
        for c in chat.get().sync_items():
            if script_enabled:
                process_chat_message(c.author.name, c.message)


def sistema_democracia():
    global voto_buffer

    while True:
        time.sleep(INTERVALO_VOTACAO)

        if not script_enabled:
            continue

        if len(voto_buffer) == 0:
            # sem votos no intervalo
            continue

        # calcula comando mais votado
        contagem = Counter(voto_buffer)
        comando_vencedor, votos = contagem.most_common(1)[0]
        tecla = command_map[comando_vencedor]

        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] DEMOCRACIA → '{comando_vencedor}' venceu com {votos} votos → tecla '{tecla}'")

        press_key(tecla)

        # limpa buffer para próxima rodada
        voto_buffer = []


# ==============================
# INICIAR O SCRIPT
# ==============================

print("========= YouTube Plays — DEMOCRACIA =========")
print("Pressione F8 para LIGAR/DESLIGAR o sistema.")
print("Votação a cada 1 segundo!")
print("===============================================\n")

keyboard.on_press_key("f8", toggle_script)


chat = pytchat.create(video_id=VIDEO_ID)

# Thread de leitura do chat
threading.Thread(target=chat_listener, args=(chat,), daemon=True).start()

# Thread da democracia
threading.Thread(target=sistema_democracia, daemon=True).start()


while True:
    time.sleep(1)
