# Script-YouTube-Plays

Um script em Python que permite que espectadores controlem um jogo enviando comandos pelo chat de uma live no YouTube, tipo ao Twitch Plays Pokémon.

Os usuários enviam mensagens como 'cima', 'ataque', 'super', etc., e o script converte automaticamente esses comandos em teclas no computador.

---

##  Funcionalidades

-  Lê mensagens em tempo real do chat da live
-  Converte comandos de texto → teclas reais
-  Cooldown por usuário (evita spam)
-  Ativar/Desativar o sistema com F8
-  Pressiona teclas por tempo configurável
-  Uso de threads para leitura contínua do chat
-  Logs detalhados no terminal (usuário, comando, tecla executada)
-  Configuração simples por variáveis no topo do script

---

##  Como funciona?

1. O script se conecta ao chat da live usando a biblioteca pytchat.  
2. Cada mensagem enviada pelos espectadores é verificada.  
3. Se for um comando válido, ele é convertido em uma tecla.  
4. A tecla é enviada ao jogo usando a biblioteca keyboard.  
5. O terminal exibe qual comando foi executado, por quem e qual tecla foi pressionada.  

---

##  Instalação

### 1. Instale o Python  
Baixe em: https://www.python.org/downloads/  
> Marque Add Python to PATH durante a instalação.

### 2. Instale as dependências  
Abra o CMD e rode:

pip install pytchat keyboard

---

##  Configuração

Edite a variável abaixo no início do arquivo:

python
VIDEO_ID = "ID_DA_LIVE_AQUI"
EX: https://www.youtube.com/live/ABC123XYZ > ABC123XYZ


Edite os comando se quiser
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
