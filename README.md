# IDD-Final-Project

## Part 1: Project Plan

![image](https://user-images.githubusercontent.com/55858146/142953195-ba493678-5346-4109-8164-6e5dece8221d.png)

### The Big Idea:

So, you know how keyboards let you press buttons to input a character? What if instead you had to use a series of switches to input the *binary* value of the character? Introducing: Binary Switch Keyboard, or BSKeyboard for short!

You might be asking: why on Earth would I ever want this? Well, many people would appreciate the practice and familiarity in binary the BSKeyboard provides. Not only that, but it can be a fun way to input characters instead of your usual boring old keyboard. By no means is it terribly practical for writing papers or creating code, but it's at least a flex to type out a document using nothing but a series of 0s and 1s.

In the image above, you can see a rough sketch of how the device would work. You have a series of lights corresponding to the status of a switch, and, well, a series of switches to input your values. The switches can be substituted for copper tape as a tap-based alternative, and the individual LED lights conveying on/off status can be switched for a single display housing a series of 8 lights (where the first light is on if the first switch is on, the second light is on if the second switch is on, and so forth). I'll probably end up using copper tape, since it's easier to acquire.

When the user wants to input their character, they can press the button on the side of the device (seen here as the purple dashed button on the side). This will send the character as input out to the computer. I'll probably have to create a little IDE for taking in characters, since I'm not sure how I'd just, you know, output a character like keyboards do. That said, the device would be pretty simple to understand and use -- then comes the part where the user inputs characters.

Here is a table of ASCII characters and their corresponding binary values:

![asciitable](https://alpharithms.s3.amazonaws.com/assets/img/ascii-chart/ascii-table-alpharithms-scaled.jpg)

So, for example, if a user wanted to punch in a lowercase `m`, they'd need to input the binary value `01101101` (109 in decimal). Thus, they'd turn the second, third, fifth, sixth and eighth switches on. Then, they'd hit the purple button, and an `m` would be typed into the small IDE I build for the project.

### Timeline:

1. 11/22: Project Plan submitted.
2. 11/30: Functional check-off submitted. At this point, I'll have a cardboard prototype ready.
3. 12/7: Either I'll have enhanced the cardboard prototype, or I'll use the Maker Lab to build the device out of wood.
4. 12/13: Submit write-up and documentation.

### Parts Needed:

If I could get 8 on/off switches, it would certainly make the device "cooler", but the device would function just fine with the use of copper tape instead. Everything else, aside from the wood in the Maker Lab, I have already.

### Risks:

The device, at its core, should be *fun* to use. It will be useful for teaching people about binary, but beyond that, the learning will only be affective if the device isn't tedious or annoying to operate. Thus, I'll have to pay special attention to HCI for this device: is it nice to hold? Are the inputs responsive? Does it accurately render characters when the characters are punched in?

### Fall-back plan:

If this plan doesn't end up working out, I could also make a camera that tracks the movement of your head and turns to match it (useful for vloggers and the like).

## Part 2: Prototype

### Requirements:

`pip install -r ../Interactive-Lab-Hub/Lab\ 4/requirements.txt`
`pip install sparkfun-qwiic-button`