import tkinter as tk


def report(string, isPrinting):
    print_report = isPrinting[0]
    tk_display = isPrinting[1]
    tk_display.insert(tk.END, string)

    if print_report:
        print(string)
