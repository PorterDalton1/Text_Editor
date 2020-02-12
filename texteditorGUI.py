import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.textWidget = tk.Text(root, height = 30, width = 70)
        self.textWidget.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.YES)

def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()