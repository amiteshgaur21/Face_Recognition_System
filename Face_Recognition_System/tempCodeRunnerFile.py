from tkinter import Tk, ttk

def filter_options(event):
  selected_value = combobox.get()
  options_to_show = ["Option 1", "Option 2"]  # Exclude "Option 3"
  if selected_value not in options_to_show:
    options_to_show.append(selected_value)  # Show previously hidden option when selected elsewhere
  combobox.config(values=options_to_show)

root = Tk()
root.title("My App")
root.geometry("500x400")
root.maxsize(800, 600)
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.bind("<<ComboboxSelected>>", filter_options)
combobox.pack()

root.mainloop()
