import tkinter as tk

window = tk.Tk()
window.geometry('800x600+200+200')
window.title('PokemonMastermind by RaZ')
window.config(bg='black')

label01 = tk.Label(window, bg='white', width=20, text='empty')
label01.pack()

top_frame = tk.Frame(window)
# top_frame.grid(row=0, column=0)

window.mainloop()



