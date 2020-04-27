from tkinter import *
from encryptionMethods import encryptText

root = Tk()
root.resizable(False, False)

# Create canvas
canvas = Canvas(root,  height = 400, width = 400 , bg = "#263D42")
canvas.pack()

# Create frame
inputFrame = Frame(root, bg = "white")
inputFrame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

# Input data
lblInputData = Label(inputFrame,
                    text = "Enter the String: ",
                    padx = 20,
                    pady = 20,
                    bg = "white"
                    ).grid(row = 1)
inputData = Entry(inputFrame)
inputData.grid(row = 1, column = 1)

# Create Tkinter variable
tk_var = StringVar(root)

#Dictionary with options
options = { 'Shift Cipher',
            'Mono Alphabetic Cipher',
            'Play Fair Cipher',
            'Hill Cipher',
            'Polyalphabetic Cipher',
            'Transposition Cipher'
            }
tk_var.set('Choose Encrpytion Method')

dropDownList = OptionMenu(inputFrame, tk_var, *options).place(relx = 0.25, rely = 0.2)

lblOutputData = Label(inputFrame,
                    text = "Encrypted String:",
                    padx = 20,
                    pady = 20,
                    bg = "white"
                    )
lblOutputData.place(relx = 0.2, rely = 0.6)

def handleBtnClick():
    outputData = encryptText(inputData.get(), tk_var.get())
    lblOutputData.config(text = outputData)

submitButton = Button(inputFrame, text = "Sort", command = handleBtnClick).place(relx = 0.4, rely = 0.4)


if(__name__ == "__main__"):
    root.mainloop()



