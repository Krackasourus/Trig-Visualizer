from src import draw
from src import triangle
import tkinter as tk
import turtle


def initialize_window():
    def move_window(event):
        root.geometry(f"+{event.x_root}+{event.y_root}")
    root = tk.Tk()
    root.title("Trigonometric visualizer")
    root.iconbitmap("src/logo.ico")
    root.overrideredirect(True)

    handle_frame = tk.Frame(root, height=25, relief="raised")
    handle_frame.grid(row=0, column=0, columnspan=3, sticky="we")

    title_label = tk.Label(handle_frame, text="Trigonometric Visualizer")
    title_label.grid(row=0, column=0, sticky="nwse", padx=(0, 630))

    exit_app = tk.Button(handle_frame, width=3, text="X", bg="red", command=exit)
    exit_app.grid(row=0, column=1, sticky="e")

    root_frame = tk.Frame(root, relief="sunken")
    root_frame.grid(row=1, sticky="we")

    canvas = tk.Canvas(root_frame)
    canvas.config(width=600, height=600)
    canvas.grid(row=0, rowspan=6, column=0, columnspan=6, padx=3, pady=3)

    screen = turtle.TurtleScreen(canvas)
    draw.draw_grid(canvas)

    handle_frame.bind('<B1-Motion>', move_window)
    title_label.bind('<B1-Motion>', move_window)

    return root_frame


def input_widget(parent, string, x, y):
    widget_frame = tk.Frame(parent, relief="raised")
    widget_label = tk.Label(widget_frame, text=f"{string}:", width=2)
    widget_input = tk.Entry(widget_frame, width=4)

    widget_label.pack(side=tk.LEFT)
    widget_input.pack(side=tk.RIGHT)

    widget_frame.grid(row=x, column=y, padx=1, pady=1)

    return widget_input


def load_input_frame(root_frame):

    input_frame = tk.LabelFrame(root_frame, text="Create Triangle", relief="sunken", width=300)
    input_frame.grid(row=0, rowspan=3, column=7, columnspan=2, sticky="nwe")

    i1 = input_widget(input_frame, "A", 0, 0)
    i2 = input_widget(input_frame, "B", 0, 1)
    i3 = input_widget(input_frame, "C", 0, 2)

    i4 = input_widget(input_frame, "a", 1, 0)
    i5 = input_widget(input_frame, "b", 1, 1)
    i6 = input_widget(input_frame, "c", 1, 2)

    output_frame = tk.LabelFrame(root_frame, text="Steps", relief="sunken", width=300)
    output_frame.grid(row=1, rowspan=2, column=7, columnspan=2, sticky="nswe")

    output_box = tk.Text(output_frame, width=20)
    output_box.config(font=10)
    output_box.pack(fill="x", expand=True)

    button_calc = tk.Button(input_frame, text="Calculate", width=8)
    button_calc.grid(row=2, rowspan=2, column=0, columnspan=2, sticky="nswe")

    button_draw = tk.Button(input_frame, text="Draw", width=8, command="hi")
    button_draw.grid(row=2, column=2)

    button_erase = tk.Button(input_frame, text="Erase", width=8)
    button_erase.grid(row=3, column=2)
