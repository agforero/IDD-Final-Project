# tkinter libraries
import tkinter as tk
import tkinter.font as tkFont
import sys

def arrToInt(arr):
    to_read = arr[::-1]
    ret = 0
    base = 1
    for i in range(8):
        ret += to_read[i] * base
        base *= 2

    return ret

class FieldText():
    def __init__(self):
        self.text = {}
        self.address = 0

    def getText(self):
        if len(list(self.text.keys())) == 0: return ""

        ret = ""
        sortedKeys = list(self.text.keys())
        sortedKeys.sort()

        for k in sortedKeys:
            ret += self.text[k]

        print(ret) 
        return ret

    def updateText(self, data):
        if data[0] == "WRITING":
            print("incrementing address")
            self.address += 1

        try: self.char = data[1]
        except: self.char = "?"

        self.text[self.address] = self.char

class OutputApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("BSKeyboard IDE")

        # text field
        self.uni = tkFont.Font(family="Courier", size=16)
        self.field = tk.Text(self, height=40, font=self.uni, width=64)
        self.field.pack(side=tk.TOP)
        self.fieldText = FieldText()

        # current sequence and char
        self.botDisplay = tk.Frame(self)
        self.botDisplay.pack(side=tk.BOTTOM)

        # declaring elements
        self.sequenceLabel = tk.Label(self.botDisplay, text="current sequence: ", font=self.uni)
        self.sequenceDisp = tk.Text(self.botDisplay, height=1, font=self.uni, width=25)

        self.charLabel = tk.Label(self.botDisplay, text="current char: ", font=self.uni)
        self.charDisp = tk.Text(self.botDisplay, height=1, font=self.uni, width=25)

        # packing elements in order
        self.sequenceLabel.pack(side=tk.LEFT)
        self.sequenceDisp.pack(side=tk.LEFT)

        self.charDisp.pack(side=tk.RIGHT)
        self.charLabel.pack(side=tk.RIGHT)
        
        self.updateText()

    def updateText(self):
        f = open("data/data.txt", "r")

        try: self.data = f.readlines()[-1].split()
        except: sys.exit(0)

        # update big text field
        self.fieldText.updateText(self.data)
        self.field.delete("1.0", tk.END)
        self.field.insert(tk.END, self.fieldText.getText())

        # update info bars
        self.sequenceDisp.delete("1.0", tk.END)
        self.charDisp.delete("1.0", tk.END)

        self.sequenceDisp.insert(tk.END, self.data[0])
        self.charDisp.insert(tk.END, self.data[1])

        f.close() # might have to flip this line and the one below it
        self.after(10, self.updateText)

if __name__ == "__main__":
    app = OutputApp()
    app.mainloop()