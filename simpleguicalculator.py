import tkinter as tk


def button_click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_field.set(result)
            expression = str(result)
        except Exception as e:
            input_field.set("Error")
            expression = ""
    elif text == "C":
        input_field.set("")
        expression = ""
    else:
        expression += text
        input_field.set(expression)


app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x400")
expression = ""
input_field = tk.StringVar()


entry = tk.Entry(app, textvar=input_field, font="Arial 20", justify='right')
entry.pack(fill="both", ipadx=8, pady=10)


button_frame = tk.Frame(app)
button_frame.pack()

buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:  # 4 buttons per row
        col = 0
        row += 1


app.mainloop()
