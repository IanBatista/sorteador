import random
import tkinter as tk


class SorteadorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorteador de números")

        # Obtém as dimensões da tela do computador
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Define a geometria da janela para ficar centralizada na tela
        window_width = 400
        window_height = 300
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.sorteados = []

        self.label = tk.Label(
            self.master, text="Número sorteado:", font=("Arial", 18))
        self.label.pack(pady=10)

        self.numero_label = tk.Label(
            self.master, text="", font=("Arial", 36, "bold"))
        self.numero_label.pack(pady=10)

        self.sortear_button = tk.Button(
            self.master, text="Sortear", font=("Arial", 14), command=self.sortear)
        self.sortear_button.pack(pady=10)

        self.historico_label = tk.Label(
            self.master, text="Histórico de números sorteados:", font=("Arial", 12))
        self.historico_label.pack()

        self.historico_text = tk.Text(
            self.master, height=5, font=("Arial", 12))
        self.historico_text.pack()

        self.fechar_button = tk.Button(self.master, text="Fechar", font=(
            "Arial", 14), command=self.master.quit)
        self.fechar_button.pack(pady=10)

    def sortear(self):
        numero = random.randint(1, 10)
        self.numero_label.config(text=str(numero))
        self.sorteados.append(numero)
        self.historico_text.insert("end", f"{numero}\n")


root = tk.Tk()
app = SorteadorApp(root)
root.mainloop()
