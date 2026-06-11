import pyautogui, time, threading
import keyboard as kb

SCROLL_VALUE = -1

scrolling = False
scroll_thread = None

def loop():
    global SCROLL_VALUE
    while scrolling:
        pyautogui.scroll(SCROLL_VALUE)
def toggle_scroll():
    global scrolling, scroll_thread
    scrolling = not scrolling  # Inverte o estado (Liga/Desliga)
    
    if scrolling:
        print("Scrolling iniciado...")
        scroll_thread = threading.Thread(target=loop)
        scroll_thread.daemon = True
        scroll_thread.start()
    else:
        print("Scrolling parado.")


kb.add_hotkey("l", toggle_scroll)

kb.add_hotkey("x", lambda: exit())

print("Pressione 'L' para iniciar/parar o scroll. Pressione 'X' para sair.")
kb.wait()
