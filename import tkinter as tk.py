#Codigo da aula pratica do Professor Zena
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

class QRcodeapp:
    def __init__(self, root):
        self.root = root
        self.root.title("gerador de QRcode")

        self.entry = tk.Entry(root, width= 30)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.button = tk.Button(root, text="gerar", command=self.gerar_qr)
        self.button.grid(row=0, column=1, padx=10, pady=10)

        self.label = tk.Label(root)
        self.label.grid(row=1, column=0, columnspan=2)
    
    def gerar_qr(self):
        texto = self.entry.get()

        if not texto:
            messagebox.showwarning("Aviso", "digite algum texto!")
            return
        
        qr = qrcode.make(texto)

        qr = qr.resize ((200, 200))

        self.qr_img = ImageTk.PhotoImage(qr)

        self.label.config(image=self.qr_img)

root= tk.Tk()

app = QRcodeapp(root)

root.mainloop()