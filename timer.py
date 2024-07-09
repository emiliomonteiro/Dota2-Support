import tkinter as tk
from datetime import datetime

# Função para iniciar o timer após 20 segundos
def start_timer(lane_choice):
    global running, lane
    if not running:
        running = True
        lane = lane_choice
        safelane_button.pack_forget()  # Remove o botão safelane
        offlane_button.pack_forget()   # Remove o botão offlane
        close_button.pack()            # Mostra o botão fechar
        reset_button.pack()            # Mostra o botão GG
        
        # Configura um timer de 20 segundos para iniciar o timer principal
        root.after(20000, start_main_timer)

# Função para iniciar o timer principal
def start_main_timer():
    update_timer()
    check_bounty_timer()

# Função para atualizar o timer
def update_timer():
    global timer_seconds, minutes, seconds
    global last_second_checked, last_stack_time
    
    if running:
        timer_seconds += 1
        minutes, seconds = divmod(timer_seconds, 60)
        
        time_str = f"{minutes:02}:{seconds:02}"
        timer_label.config(text=time_str)
        
        if lane == "safelane":
            timer_label.config(fg="blue")
        else:
            timer_label.config(fg="red")

        # Verificar se o tempo está no formato xx:50 para exibir "Stack"
        if seconds == 50 and minutes < 15:
            message = f"Stack - {time_str}"
            add_to_history(message)
            stack_label.config(text="Stack")
            last_stack_time = timer_seconds  # Registra o tempo atual
        elif timer_seconds - last_stack_time >= 10:
            stack_label.config(text="")  # Limpa a mensagem "Stack" após 10 segundos

        last_second_checked = seconds

        root.after(1000, update_timer)  # Chama a função a cada 1 segundo

# Função para verificar e exibir mensagem "Bounty" a cada 3 minutos
def check_bounty_timer():
    global bounty_message_shown
    
    if running:
        if seconds == 0 and minutes % 3 == 0 and not bounty_message_shown:
            message = f"Bounty - {minutes:02}:{seconds:02}"
            add_to_history(message)
            stack_label.config(text="Bounty")
            bounty_message_shown = True
        elif seconds != 0 or minutes % 3 != 0:
            bounty_message_shown = False
        
        root.after(1000, check_bounty_timer)  # Chama a função a cada 1 segundo

# Função para adicionar mensagem ao histórico
def add_to_history(message):
    history.append((message, datetime.now().strftime('%H:%M:%S')))
    if len(history) > 5:
        history.pop(0)  # Remove o primeiro elemento se exceder 5 mensagens
    update_history_label()

# Função para atualizar o histórico na interface
def update_history_label():
    history_text = "\n".join([f"{msg} ({timestamp})" for msg, timestamp in history])
    history_label.config(text=history_text)

# Função para fechar a aplicação
def close_app():
    root.destroy()

# Função para reiniciar a aplicação
def reset_app():
    global running, timer_seconds, minutes, seconds
    global last_second_checked, last_stack_time, lane, bounty_message_shown
    
    running = False
    timer_seconds = 0
    minutes = 0
    seconds = 0
    last_second_checked = -1
    last_stack_time = -30
    lane = "safelane"
    bounty_message_shown = False
    timer_label.config(text="00:00", fg="black")
    stack_label.config(text="")
    safelane_button.pack()
    offlane_button.pack()
    close_button.pack_forget()
    reset_button.pack_forget()
    history.clear()
    update_history_label()

# Variáveis globais
running = False
timer_seconds = 0
minutes = 0
seconds = 0
lane = "safelane"
last_second_checked = -1
last_stack_time = -30  # Inicializa com um valor que garante que a mensagem "Stack" não apareça ao iniciar
bounty_message_shown = False  # Controla se a mensagem "Bounty" foi exibida
history = []  # Lista para armazenar histórico de mensagens

# Configuração da interface gráfica
root = tk.Tk()
root.title("Dota 2 Support Timer")

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack()

stack_label = tk.Label(root, text="", font=("Helvetica", 24))
stack_label.pack()

history_label = tk.Label(root, text="", font=("Helvetica", 12), justify=tk.LEFT, anchor="w", wraplength=400)
history_label.pack()

safelane_button = tk.Button(root, text="Safelane", command=lambda: start_timer("safelane"))
offlane_button = tk.Button(root, text="Offlane", command=lambda: start_timer("offlane"))

safelane_button.pack()
offlane_button.pack()

close_button = tk.Button(root, text="Fechar", command=close_app)
reset_button = tk.Button(root, text="GG", command=reset_app)

root.mainloop()
