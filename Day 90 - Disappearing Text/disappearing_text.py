import tkinter as tk
import threading
import time

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        root.title("Dangerous Writing App")
        self.text = tk.Text(root, wrap=tk.WORD)
        self.text.pack()
        self.timer = None
        self.reset_timer()

    def start_timer(self):
        self.timer = threading.Timer(5, self.delete_text)
        self.timer.start()

    def reset_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        self.start_timer()

    def delete_text(self):
        self.text.delete(1.0, tk.END)

    def on_text_change(self, event):
        self.reset_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    app.text.bind("<Key>", app.on_text_change)
    root.mainloop()
