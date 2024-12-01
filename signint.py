import tkinter as tk

root = tk.Tk()
root.title("drum roll plese...")
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg="black")

label = tk.Label(root, text="what is the secret password?", font=('arial', 15), fg="white", bg="black")
label.pack()

myentry = tk.Entry(root)
myentry.pack()

btn1 = tk.Button(root, text="click me if you dare...", font=('arial', 16),bg="white", fg="black",)
btn1.pack()

root.mainloop()