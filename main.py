import tkinter as tk
from calculator_gui import CalculatorGUI

def main():
    window = tk.Tk()
    CalculatorGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()