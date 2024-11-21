import time
import random
from pywinauto import Application
import win32api
import win32con

# Conecta ao aplicativo GeForce Now. Altere o título conforme necessário.
app = Application(backend="uia").connect(title_re="ARK: Survival Ascended no GeForce NOW")

# Obtém a janela principal do GeForce Now
window = app.top_window()

# Obtém as coordenadas da janela do GeForce Now
window_rect = window.rectangle()

# Função para enviar eventos de mouse diretamente para a janela do GeForce Now
def send_mouse_event_to_window(hwnd, x, y):
    lParam = win32api.MAKELONG(x, y)
    win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)

# Função para mover o mouse dentro da janela do GeForce Now
def move_mouse_in_window():
    hwnd = window.handle
    while True:
        # Gera novas coordenadas aleatórias dentro da janela
        new_x = random.randint(0, window_rect.width())
        new_y = random.randint(0, window_rect.height())
        # Envia o evento de movimento do mouse para a janela
        send_mouse_event_to_window(hwnd, new_x, new_y)
        # Espera um tempo aleatório entre 5 e 10 segundos
        time.sleep(1)
        print('movimentado no geforce')

# Inicia a movimentação do mouse
move_mouse_in_window()
