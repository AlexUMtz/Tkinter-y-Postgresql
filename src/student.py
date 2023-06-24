from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E
import psycopg2

root = Tk()  # Instancia de TK
root.title("Python & PostgreSQL")  # Titulo de la Aplicación


def save_new_student(name, age, address):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()


# Canvas -> Tipo de contenedor
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()  # Espaciado
# frame.config(bg="#fff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add a Student")
label.grid(row=0, column=1)

# Name Input
label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)  # Input
entry_name.grid(row=1, column=1)

# Age Input
label = Label(frame, text="Age")
label.grid(row=2, column=0)

entry_age = Entry(frame)  # Input
entry_age.grid(row=2, column=1)

# Address Input
label = Label(frame, text="Address")
label.grid(row=3, column=0)

entry_address = Entry(frame)  # Input
entry_address.grid(row=3, column=1)

# Boton
button = Button(frame, text="Add", command=lambda: save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
))
button.grid(row=4, column=1, sticky=W+E)

root.mainloop()  # Ejecutar ventana
