import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.textWidget = tk.Text(self.root, height = 30, width = 70)
        self.textWidget.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.YES)
        #Create Menu
        self.topMenu = tk.Menu(self.root)
        self.root.config(menu=self.topMenu)
        #Add menus to menu
        self.fileMenu = tk.Menu(self.topMenu)
        self.topMenu.add_cascade(label="File", menu=self.fileMenu)

        self.fileMenu.add_command(label="Open", command = self.open)
        self.fileMenu.add_command(label="Save", command = self.save)
        self.fileMenu.add_command(label="Save As", command = self.saveAs)
        self.fileMenu.add_command(label="New Tab", command = self.newTab)
        self.fileMenu.add_command(label="New Window", command = self.newWindow)
    def save(self):
        pass
    def saveAs(self):
        pass
    def open(self):
        pass
    def newTab(self):
        pass
    def newWindow(self):
        pass
def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()