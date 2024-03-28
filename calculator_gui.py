import tkinter as tk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('Calculator')
        self.equation = tk.StringVar()

        self.display = tk.Entry(self.window, textvariable=self.equation)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', '**', 'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        current_equation = str(self.equation.get())
        if button == '=':
            try:
                result = str(eval(current_equation))
                self.equation.set(result)
            except Exception as e:
                self.equation.set("Error")
        elif button == 'C':
            self.equation.set('')
        else:
            self.equation.set(current_equation + button)

if __name__ == "__main__":
    window = tk.Tk()
    gui = CalculatorGUI(window)
    window.mainloop()