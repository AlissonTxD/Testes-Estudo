from tkinter import *

def janela_base():
    baseroot = Tk()
    baseroot.title('Janela Base')
    baseroot['bg'] = '#036767'
    #dimensoes janela
    largura = 700
    altura = 450    
    #Centralizador de Janela
    largura_screen = baseroot.winfo_screenwidth()
    altura_screen = baseroot.winfo_screenheight()
    posx = (largura_screen/2) - (largura/2)
    posy = (altura_screen/2) - (altura/2)
    baseroot.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    #cria o canvas e colocar as bordas
    canvas = Canvas(baseroot,bg = "#036767",width = largura,height = altura,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0,0,4,altura,fill="black",outline="")
    canvas.create_rectangle(0,0,largura,4,fill="black",outline="")
    canvas.create_rectangle((largura - 4),0,largura,altura,fill="black",outline="")
    canvas.create_rectangle(0,(altura-4),largura,altura,fill="black",outline="")
    #Colocar resto do codigo Abaixo
    #nonfigurações da janela
    #baseroot.overrideredirect(True)#desabilitarbordas da janela
    #baseroot.resizable(False, False)#permitir ou nao mudança no tamanho
    #baseroot.attributes("-topmost", True)#manter acima de tudo
    #inicia janela
    baseroot.mainloop()
janela_base()

