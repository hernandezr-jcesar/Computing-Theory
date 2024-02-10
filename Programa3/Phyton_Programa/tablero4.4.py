import tkinter as tk

class App():
    def __init__(self, L_QUADRADO):
        self.L_QUADRADO = L_QUADRADO
        self.imagenes = {}

        self.ventana =  tk.Tk()
        self.ventana.title("Motor de ajedrez")

        self.ventana.geometry(f"{str(L_QUADRADO*4)}x{str(L_QUADRADO*4)}")
        self.ventana.resizable(0,0)

        self.interfaz =  tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def dibujarTablero(self):
        #self.interfaz.create_rectangle(x0,y0,x1,y1,fill =)
        for i in range(4):
            for j in range(4):
                if (i+j) % 2 == 0:
                    self.interfaz.create_rectangle(i * self.L_QUADRADO, j * self.L_QUADRADO, (i + 1) * self.L_QUADRADO,(j + 1) * self.L_QUADRADO, fill ="#dfc07f")
                else:
                    self.interfaz.create_rectangle(i * self.L_QUADRADO, j * self.L_QUADRADO, (i + 1) * self.L_QUADRADO,(j + 1) * self.L_QUADRADO, fill="#7a4f37")

    def cargarImagenes(self):
        piezas = []


MotorDeAjedrez = App(70)
MotorDeAjedrez.dibujarTablero()

MotorDeAjedrez()