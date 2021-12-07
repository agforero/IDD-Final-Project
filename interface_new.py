# tkinter libraries
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
            ret += self.text[k]

        #print(ret) 
        return ret

    def updateText(self, data):
        if data[0] == "WRITING":
            self.address += 1

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
        
        #self.updateText()

    def updateText(self, raw_data):
        print(raw_data)
        f = open("data/data.txt", "r")

        try:
            self.data = f.readlines()[-1].split()
            f.close()

        except:
            f.close()
            sys.exit(0)

        print(self.data)

        # update big text field
        self.fieldText.updateText(self.data)
        self.field.delete("1.0", tk.END)
        self.field.insert(tk.END, self.fieldText.getText())

        # update info bars
        self.sequenceDisp.delete("1.0", tk.END)
        self.charDisp.delete("1.0", tk.END)

        self.sequenceDisp.insert(tk.END, self.data[0])
        self.charDisp.insert(tk.END, self.data[1])

        #self.after(10, self.updateText)
        time.sleep(0.05)

# reading in from MQTT
import paho.mqtt.client as mqtt
import uuid

topic = "IDD/BSKeyboard"
client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

global app
def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)
    app = OutputApp()
    app.mainloop()

def on_message(client, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    app.updateText(msg.payload.decode('UTF-8'))

client.on_connect = on_connect
client.on_message = on_message
client.connect("farlab.infosci.cornell.edu", port=8883)

if __name__ == "__main__":
    print("running!")
    #app = OutputApp()
    #app.mainloop()

    client.loop_forever()
