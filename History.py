from tkinter import *


window1 = Tk()
window1.title('Calculator History')
window1.geometry("400x567")
window1.configure(bg="gray16")
window1.resizable(False, False)


def back():
    window1.destroy()
    import main


# Horizontal scrollBar
hScroll = Scrollbar(window1, orient="horizontal")
hScroll.place(x=0, y=565, width=400)

# Button to navigate back to calculator window
back_icon = PhotoImage(file="back.png")
back_btn = Button(window1, text="back", image=back_icon , width=20, height=20, borderwidth=0, highlightthickness=0, bg="white", command=back)
back_btn.place(x=2, y=2)

# Opens history text file and reads contents of previous calculations
with open("History.txt", "r") as file2:
    content = file2.read()

# Text widget to show the calculator history
result = Text(window1, width=50, height=567, wrap=NONE, xscrollcommand=hScroll.set,
              font = "Helvetica 18 bold", bg="gray16", fg="white")

# Displays the previous calculations
result.insert(END, content)

hScroll.config(command=result.xview)
result.place(x=0, y=30)

"""
Shows the user previous calculations made but its functions are quite limited 
as it doesn't show the corresponding input (e.g. 6+2 only shows the output 8). However, user can
copy the answers and navigate back to the calculator and paste it to be used again.
"""


window1.mainloop()
