# Digite no CMD antes de rodar:
# pip install pytchat keyboard  

import pytchat
import keyboard
import time
import threading
from datetime import datetime


# ==============================
# CONFIGURAÇÕES
# ==============================

VIDEO_ID = "COLOQUE_AQUI_O_ID_DA_LIVE"    # ex: https://youtube.com/live/ABCDE → ABCDE
PRESS_TIME = 0.150      # 150 ms segurando a tecla
COOLDOWN = 2.0      # delay de segundos por usuário

script_enabled = False
cooldowns = {}


# Mapeamento de comandos do chat → teclas reais
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


# FUNÇÕES DO SCRIPT
def toggle_script(e):
    #Alterna entre LIGAR/DESLIGAR quando F8 é pressionado.
    global script_enabled
    script_enabled = not script_enabled
    estado = "LIGADO" if script_enabled else "DESLIGADO"
    print(f"\n[TOGGLE] Script agora está: {estado}\n")

def press_key(key):
    keyboard.press(key)
    time.sleep(PRESS_TIME)
    keyboard.release(key)

def process_chat_message(user, msg):
    global cooldowns

    msg = msg.lower().strip()

    if msg not in command_map:
        return

    key = command_map[msg]
    now = time.time()

    if user in cooldowns and now - cooldowns[user] < COOLDOWN:
        return

    cooldowns[user] = now

    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {user}: '{msg}' → tecla '{key}'")

    press_key(key)

def chat_listener(chat):
    print("[INFO] Lendo chat...\n")

    while chat.is_alive():
        for c in chat.get().sync_items():
            if script_enabled:
                process_chat_message(c.author.name, c.message)

print("========= YouTube Plays iniciado =========")
print("Pressione F8 para LIGAR/DESLIGAR o sistema.")
print("==========================================\n")

keyboard.on_press_key("f8", toggle_script)

chat = pytchat.create(video_id=VIDEO_ID)

threading.Thread(target=chat_listener, args=(chat,), daemon=True).start()

while True:
    time.sleep(1)
