#!/usr/bin/env python3

# tkinter libraries
from datetime import datetime
import tkinter as tk
import tkinter.font as tkFont
import time
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
            if k % 2 == 0:
                ret += self.text[k]

        return ret

    def updateText(self, data):
        #print(data[0])
        if data[0] == "WRITING":
            self.address += 1
            time.sleep(1)

        try: self.char = data[1]
        except: self.char = "?"

        self.text[self.address] = self.char

class OutputApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("BSKeyboard IDE")

        # text field
        font_size = 12
        self.uni = tkFont.Font(family="Courier", size=font_size)
        self.field = tk.Text(self, height=20, font=self.uni, width=64)
        self.field.pack(side=tk.TOP)
        self.fieldText = FieldText()

        # current sequence and char
        self.botDisplay = tk.Frame(self)
        self.botDisplay.pack(side=tk.TOP)

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

        # save button, below everything else
        self.buttonDisplay = tk.Frame(self)
        self.buttonDisplay.pack(side=tk.TOP)

        self.saveButtonPadding = tk.Label(self.buttonDisplay, text=" ", font=self.uni)
        self.saveButtonPadding.pack(side=tk.TOP)

        self.saveButton = tk.Button(self.buttonDisplay, text="Save", command=self.writeOut)
        self.saveButton.pack(side=tk.TOP)
        
        self.updateText()

    def updateText(self):
        f = open("data/data.txt", "r")

        try:
            self.data = f.readlines()[-1].split()

        except:
            f.close()
            sys.exit(0)

        #print(self.data)

        # update big text field
        self.fieldText.updateText(self.data)
        self.field.delete("1.0", tk.END)
        self.field.insert(tk.END, self.fieldText.getText())

        # update info bars
        self.sequenceDisp.delete("1.0", tk.END)
        self.charDisp.delete("1.0", tk.END)

        self.sequenceDisp.insert(tk.END, self.data[0])
        self.charDisp.insert(tk.END, self.data[1])

        self.after(10, self.updateText)

    def writeOut(self):
        now = datetime.now()
        current_time = now.strftime("%m_%d_%y_%H_%M_%S")
        with open(f"saved/{current_time}.py", 'w') as s:
            s.write(self.fieldText.getText())

if __name__ == "__main__":
    print("running!")
    app = OutputApp()
    app.mainloop()
