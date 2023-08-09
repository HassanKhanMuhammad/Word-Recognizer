from tkinter import *

# GUI(ed) version of Word Recogniser.
# TODO: give the exact location (row, column) of the word in question

window = Tk()
window.geometry("350x300")
window.title("Word Recogniser")

fileLabel = Label(window, text="Enter the PATH of your file:")
fileEntry = Entry(window)

wordLabel = Label(window, text="Enter the Word you are looking for:")
wordEntry = Entry(window)

def submit():
    fileInput, wordInput = fileEntry.get(), wordEntry.get()

    with open(fileInput, "r") as f:
        content = f.read()
        
        if wordInput or wordInput.lower() in content:
            l = Label(window, text=f"{wordInput} is in {fileInput}")
            l.pack()
        else:
            l = Label(window, f"{wordInput} is not in {fileInput}")
            l.pack()

submitButton = Button(window, text="Submit", command=submit)

# packing
fileLabel.pack()
fileEntry.pack()
wordLabel.pack()
wordEntry.pack()
submitButton.pack()

window.mainloop()
