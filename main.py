from src import window_manager as wm

scale = 10

root= wm.initialize_window()
wm.load_input_frame(root)

root.mainloop()

x = input()
