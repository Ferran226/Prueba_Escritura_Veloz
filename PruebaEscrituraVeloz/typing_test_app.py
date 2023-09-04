import tkinter as tk
from tkinter import messagebox
import random
import timeit
from typing_test_results import TypingTestResults

class TypingTestApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Prueba de Escritura Veloz")

        # Establece las dimensiones de la ventana (ancho x alto)
        self.root.geometry("500x250")  # Puedes ajustar estos valores según tus preferencias

        self.sentences = [
        "El perro marrón saltó sobre el zorro perezoso.",
        "La rápida liebre marrón saltó sobre el perro dormido.",
        "Los cinco boxeadores negros al día buscan su paga.",
        "El veloz murciélago hindú comía feliz cardillo y kiwi.",
        "El exquisito whisky embriagó a mi cómodo jaguar.",
        "Python es un lenguaje de programación poderoso y versátil.",
        "La música clásica es conocida por su belleza y complejidad.",
        "El arte abstracto desafía las convenciones y la percepción.",
        "Los científicos estudian el universo en busca de respuestas.",
        "La naturaleza nos brinda belleza y inspiración inagotables.",
        "Las estaciones del año traen cambios en el clima y la naturaleza.",
        "La educación es la base para un futuro mejor y más brillante.",
        "La aventura espera en cada esquina para aquellos que buscan.",
        "La amistad es un tesoro que perdura a lo largo del tiempo.",
        "La creatividad fluye cuando la mente está abierta y libre.",
        "El trabajo duro y la perseverancia conducen al éxito.",
        "La vida es un viaje emocionante lleno de sorpresas y desafíos.",
        "La tecnología moderna ha transformado la forma en que vivimos.",
        "La sonrisa es un idioma universal que todos comprenden.",
        "Los libros son puertas a otros mundos y aventuras infinitas.",
        "La empatía y la comprensión fortalecen nuestras relaciones.",
        "La gratitud nos recuerda las bendiciones en nuestras vidas.",
        "La paciencia es una virtud que trae recompensas duraderas.",
        "La imaginación nos permite explorar mundos sin límites.",
        "La curiosidad nos impulsa a descubrir y aprender constantemente."
        ]

        self.star_time = None  # Agregar esta línea para inicializar self.star_time
        
        self.results =TypingTestResults()

        self.label = tk.Label(root, text="Escribe la siguiente oración:")
        self.label.pack(pady=10)

        self.sentences_display = tk.Label(root, text="", font=("Arial", 16))  # Cambia el tamaño de fuente a 24
        self.sentences_display.pack()


        self.entry = tk.Entry(root)
        self.entry .pack(pady=20)

        self.star_button = tk.Button(root,text="Comenzar pueba", command=self.star_test)
        self.star_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=15)



    def star_test(self):
        self.reset_game()
        self.results.reset()
        self.curreny_sentence = random.choice(self.sentences)
        self.results.set_correct_sentence(self.curreny_sentence)

        # Mostrar la oración de prueba
        self.sentences_display.config(text=self.curreny_sentence)

        # Inicializar self.star_time aquí
        self.star_time = timeit.default_timer()

        # Deshabilitar el botón "Comenzar prueba"
        self.star_button.config(state="disabled")

        #Configurar la comprobación de entrada de texto cuando se presiona "Enter"
        self.root.bind("<Return>", self.check_for_input)

    def check_for_input(self, event):
        # Verificar si la entrada de texto está vacía cuando se presiona "Enter"
        user_input = self.entry.get().strip().lower()
        if not user_input:
        # Mostrar mensaje de error si está vacía
            messagebox.showerror("Error", "Por favor, escribe la oración antes de comenzar.")
        else:
            # Calcular el resultado directamente aquí
            elapsed_time = timeit.default_timer() - self.star_time
            correct_sentence = self.curreny_sentence.lower()  # Convertir la oración correcta a minúsculas

            accuracy = self.results.calculate_accuracy(user_input, self.curreny_sentence.lower())  # Pasa la oración correcta

            self.results.add_result(elapsed_time, accuracy, self.curreny_sentence)
            self.result_text = f"Tiempo: {elapsed_time:.2f} segundos | Precisión: {accuracy:.2f}%"
            self.result_label.config(text=self.result_text)
            self.entry.config(state="disabled")
            self.star_button.config(state="normal")
            self.root.unbind("<Return>")

            # Llama al método reset_game para reiniciar el juego
            self.reset_game()



    def check_result(self):
        elapsed_time = timeit.default_timer() - self.star_time
        user_input = self.entry.get().lower()  # Convertir la entrada del usuario a minúsculas
        correct_sentence = self.curreny_sentence.lower()  # Convertir la oración correcta a minúsculas

        accuracy = self.results.calculate_accuracy(user_input, self.curreny_sentence.lower())  # Pasa la oración correcta

        self.results.add_result(elapsed_time, accuracy, self.curreny_sentence)
        self.result_text = f"Tiempo: {elapsed_time:.2f} segundos | Precisión: {accuracy:.2f}%"
        self.result_label.config(text=self.result_text)
        self.entry.config(state="disabled")
        self.star_button.config(state="normal")
        self.root.unbind("<Return>")

    # Llama al método reset_game para reiniciar el juego
        self.reset_game()


    def reset_game(self):
        self.curreny_sentence = ""
        self.sentences_display.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.star_button.config(state="normal")

        # Restablecer self.star_time al finalizar una prueba
        self.star_time = None  # Esto asegura que self.star_time sea None cuando no hay prueba en curso



if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()

