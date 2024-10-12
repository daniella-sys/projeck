import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x400")

        self.entry = tk.Entry(self, font=('Arial', 18), borderwidth=2, relief='solid', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='we')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.bind_keys()

    def create_button(self, text, row, col):
        button = tk.Button(self, text=text, font=('Arial', 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(col, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)

    def bind_keys(self):

        for key in '0123456789+-*/.':
            self.bind(f'<Key-{key}>', self.handle_key_press)

        self.bind('<Return>', lambda event: self.on_button_click('='))
        self.bind('<KP_Enter>', lambda event: self.on_button_click('='))

    def handle_key_press(self, event):
        self.on_button_click(event.char)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
