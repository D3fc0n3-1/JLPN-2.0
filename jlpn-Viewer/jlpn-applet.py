import tkinter as tk
from tkinter import messagebox
import webbrowser

class JNLPApplet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JNLP Applet")

        self.url_label = tk.Label(self.root, text="Enter JNLP URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self.root)
        self.url_entry.pack()

        self.launch_button = tk.Button(self.root, text="Launch", command=self.launch_jnlp)
        self.launch_button.pack()

    def launch_jnlp(self):
        url = self.url_entry.get()
        if url == "":
            messagebox.showerror("Error", "Please enter a URL")
            return

        webbrowser.open(url)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = JNLPApplet()
    app.run()