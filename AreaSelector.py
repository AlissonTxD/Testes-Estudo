import tkinter as tk

class AreaSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Selecione uma área da tela")
        
        # Remove bordas da janela
        self.master.overrideredirect(True)
        
        # Configura a transparência da janela
        self.master.attributes("-alpha", 0.3)
        
        # Ajusta a janela para cobrir a tela inteira
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0")
        
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.canvas = tk.Canvas(self.master, cursor="cross", bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.rect = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        # Cria um retângulo com bordas mais grossas
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=3)

    def on_mouse_drag(self, event):
        curX, curY = (event.x, event.y)
        
        # Atualiza o retângulo durante o arrasto
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        self.end_x = event.x
        self.end_y = event.y

        print(f"Coordenadas: ({self.start_x}, {self.start_y}) -> ({self.end_x}, {self.end_y})")

        # Fecha a janela após a seleção
        self.master.quit()

def selecionar_area():
    root = tk.Tk()
    selector = AreaSelector(root)
    root.mainloop()

    return (selector.start_x, selector.start_y), (selector.end_x, selector.end_y)

# Exemplo de uso
if __name__ == "__main__":
    coordenadas = selecionar_area()
    print(f"Coordenadas selecionadas: {coordenadas}")
