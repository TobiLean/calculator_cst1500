from tkinter import *
import math as m
from time import sleep
from threading import Thread

# create main calculator window
window = Tk()
window.title('Calculator')
window.geometry("400x570")
window.resizable(False, False)
window.config(bg = "black")

# Variables
equation = ""
resultant = ""
yesno = "True"
pixelVirtual = PhotoImage(width=1, height=1)


# Frames
frame1 = LabelFrame(master=window, width=400, height=160, bg='gray16')
frame1.place(x=0, y=0)

frame2 = LabelFrame(master=window, width=400, height=110, bg='black')
frame2.place(x=0, y=165)

frame3 = LabelFrame(master=window, width=300, height=350, bg='black')
frame3.place(x=0, y=300)

frame4 = LabelFrame(master=window, width=80, height=308, bg='black')
frame4.place(x=298, y=300)

hScroll = Scrollbar(frame1, orient="horizontal")
hScroll.place(x=0, y=140, width=400)


# Display input
def result(string):
    """
    Displays input on the screen of calculator
    :param string: string to be displayed
    :return: Text widget with input
    """
    global equation

    resultText = Text(frame1, width = 50, height = 2, wrap = NONE, xscrollcommand = hScroll.set,
             font="Helvetica 18 bold", bg="orangered4")
    resultText.insert(END, f"{string}")
    hScroll.config(command= resultText.xview)
    resultText.place(x=0, y=0)
    window.bind("<BackSpace>", lambda x: resultText.delete("end-2c"))

    if string == "c":
        equation = ""

    return resultText


# Collect user input
def display(value):
    """
    Concatenates button values to equation string
    :param value: values of the button pressed
    :return: updated equation string
    """
    global equation

    equation += value
    result(equation)

    if value == "c":
        result(value)

    return equation


# solve scientific equations eg. sin, log
def scientificCalc(event):
    """
    Handles scientific equations
    :param event:
    :return:
    """
    global equation
    global resultant

    key = event.widget
    text = key["text"]
    number = equation
    try:
        if text == "√":
            equation = str(m.sqrt(float(number)))
        if text == "sin":
            equation = str(m.sin(float(number)))
        if text == "cos":
            equation = str(m.cos(float(number)))
        if text == "tan":
            equation = str(m.tan(float(number)))
        if text == "log":
            equation = str(m.log10(float(number)))
        if text == "ln":
            equation = str(m.log(float(number)))
        if text == "e":
            if number == "":
                equation = str(m.e)
            else:
                equation = str(m.e ** float(number))
        if text == "π":
            if number == "":
                equation = str(m.pi)
            else:
                equation = str(float(number) * m.pi)
    except:
        resultant = "Error!"
        equation = ""


# Solve and display all forms of calculations
def calculate():
    """
    Calculates equation string/ user input
    :return: None
    """
    global equation
    global resultant
    resultant = ""

    if equation != "":
        try:
            resultant = eval(equation)
        except:
            resultant = "error"
            equation = ""

    equationText = Text(frame1, width=50, height=2, wrap=NONE, font="Helvetica 18 bold", bg="gray38")
    equationText.place(x=0, y=80)
    equationText.insert(END, f"{resultant}")
    hScroll.config(command=equationText.xview)

    # save equations to file for history function
    with open("History.txt", "a", ) as file:
        file.write(f"{resultant} \n")


# Save previous equations
def history():
    """
    Imports history module
    :return:
    """
    window.destroy()
    import History


# override run function of the threading module
class CustomThread(Thread):
    def run(self):
        sleep(1)
        Thread(target=calculate())


thread = CustomThread()
if len(equation) > 13:
    thread.start()

# Images for buttons
photo1 = PhotoImage(file="assets/btn1-02.png")
photo2 = PhotoImage(file="assets/btnx-02.png")
photo3 = PhotoImage(file="assets/btnx-03.png")
photo4 = PhotoImage(file="assets/btnx-04.png")
photo5 = PhotoImage(file="assets/tkinter_design_b5-02-02.png")
photo6 = PhotoImage(file="assets/btnx-05.png")
photo7 = PhotoImage(file="assets/btnx-06.png")
photo8 = PhotoImage(file="assets/btnx-07.png")
photo9 = PhotoImage(file="assets/btnx-08.png")
photo0 = PhotoImage(file="assets/btn0-02.png")
photoDot = PhotoImage(file="assets/spc-02.png")
photoEquals = PhotoImage(file="assets/spc-03.png")
photoPlus = PhotoImage(file="assets/spc-04.png")
photoDiv = PhotoImage(file="assets/spc-05.png")
photoMinus = PhotoImage(file="assets/spc-06.png")
photoMultiply = PhotoImage(file="assets/spc-07.png")
photoPower = PhotoImage(file="assets/func_pwr.png")
photoSin = PhotoImage(file="assets/func_sin.png")
photoCos = PhotoImage(file="assets/func_cos.png")
photoTan = PhotoImage(file="assets/func_tan.png")
photoLog = PhotoImage(file="assets/func_log.png")
photoHistory = PhotoImage(file="assets/func_hist.png")
photoRoot = PhotoImage(file="assets/func_root.png")
photoE = PhotoImage(file="assets/func_e.png")
photoLBracket = PhotoImage(file="assets/func_left_bracket.png")
photoRBracket = PhotoImage(file="assets/func_right_bracket.png")
photoLn = PhotoImage(file="assets/func_ln.png")
photoPi = PhotoImage(file="assets/func_pi.png")
photoClear = PhotoImage(file="assets/func_clear.png")


# clears the calculator
def clr():
    global equation
    equation = ""


# Main Buttons
num7_btn = Button(frame3, image=photo7, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("7"))
num7_btn.grid(row=0, column=0)
window.bind("7", lambda x: display("7"))
num8_btn = Button(frame3, image=photo8, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("8"))
num8_btn.grid(row=0, column=1)
window.bind("8", lambda x: display("8"))
num9_btn = Button(frame3, image=photo9, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("9"))
num9_btn.grid(row=0, column=2)
window.bind("9", lambda x: display("9"))
num4_btn = Button(frame3, image=photo4, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("4"))
num4_btn.grid(row=1, column=0)
window.bind("4", lambda x: display("4"))
num5_btn = Button(frame3, image=photo5, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("5"))
num5_btn.grid(row=1, column=1)
window.bind("5", lambda x: display("5"))
num6_btn = Button(frame3, image=photo6, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("6"))
num6_btn.grid(row=1, column=2)
window.bind("6", lambda x: display("6"))
num1_btn = Button(frame3, image=photo1, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("1"))
num1_btn.grid(row=2, column=0)
window.bind("1", lambda x: display("1"))
num2_btn = Button(frame3, image=photo2, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("2"))
num2_btn.grid(row=2, column=1)
window.bind("2", lambda x: display("2"))
num3_btn = Button(frame3, image=photo3, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("3"))
num3_btn.grid(row=2, column=2)
window.bind("3", lambda x: display("3"))
bnum0_btn = Button(frame3, image=photo0, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("0"))
bnum0_btn.grid(row=3, column=0)
window.bind("0", lambda x: display("0"))
dot_btn = Button(frame3, text=".", image=photoDot, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("."))
dot_btn.grid(row=3, column=1)
window.bind(".", lambda x: display("."))
eq_btn = Button(frame3, text="=", image=photoEquals, width=98, height=68, borderwidth=0, highlightthickness=0, command=calculate)
eq_btn.grid(row=3, column=2)
window.bind("<Return>", lambda x: calculate())
window.bind("=", lambda x: calculate())

# Operation Buttons
division_btn = Button(frame4, text="÷", image=photoDiv, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("/"))
division_btn.grid(row=0, column=0)
window.bind("/", lambda x: display("/"))
multiply_btn = Button(frame4, text="×", image=photoMultiply, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("*"))
multiply_btn.grid(row=1, column=0)
window.bind("*", lambda x: display("*"))
addition_btn = Button(frame4, text="+", image=photoPlus, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("+"))
addition_btn.grid(row=2, column=0)
window.bind("+", lambda x: display("+"))
subtract_btn = Button(frame4, text="−", image=photoMinus, width=98, height=68, borderwidth=0, highlightthickness=0, command=lambda: display("-"))
subtract_btn.grid(row=3, column=0)
window.bind("-", lambda x: display("-"))

# scientific buttons are pressed after the number you want to calculate e.g. press 2 then pi to get 6.28
# Scientific/ other functions buttons
power_btn = Button(frame2, text="x^", image=photoPower, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1, command=lambda: display("**"))
power_btn.grid(row=0, column=0)
sqrt_btn = Button(frame2, text="√ ", image=photoRoot, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
sqrt_btn.bind("<Button-1>", scientificCalc)
sqrt_btn.grid(row=1, column=0)
sin_btn = Button(frame2, text="sin", image=photoSin, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
sin_btn.bind("<Button-1>", scientificCalc)
sin_btn.grid(row=0, column=1)
e_btn = Button(frame2, text="e", image=photoE, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
e_btn.bind("<Button-1>", scientificCalc)
e_btn.grid(row=1, column=1)
cos_btn = Button(frame2, text="cos", image=photoCos, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
cos_btn.bind("<Button-1>", scientificCalc)
cos_btn.grid(row=0, column=2)
bracket1_btn = Button(frame2, text="(", image=photoLBracket, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1, command=lambda: display("("))
bracket1_btn.bind("<Button-1>", scientificCalc)
bracket1_btn.grid(row=1, column=2)
tan_btn = Button(frame2, text="tan", image=photoTan, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
tan_btn.grid(row=0, column=3)
tan_btn.bind("<Button-1>", scientificCalc)
bracket2_btn = Button(frame2, text=")", image=photoRBracket, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1, command=lambda: display(")"))
bracket2_btn.grid(row=1, column=3)
bracket2_btn.bind("<Button-1>", scientificCalc)
log_btn = Button(frame2, text="log", image=photoLog, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
log_btn.grid(row=0, column=4)
log_btn.bind("<Button-1>", scientificCalc)
ln_btn = Button(frame2, text="ln", image=photoLn, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
ln_btn.grid(row=1, column=4)
ln_btn.bind("<Button-1>", scientificCalc)
history_btn = Button(frame2, text="Hist", image=photoHistory, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1, command=history)
history_btn.grid(row=0, column=5)
pi_btn = Button(frame2, text="π", image=photoPi, font=("Arial", 10, "bold"), width=65, height=42.5, borderwidth=1, highlightthickness=1)
pi_btn.grid(row=1, column=5)
pi_btn.bind("<Button-1>", scientificCalc)
clear_btn = Button(frame2, text="Clear", image=photoClear, font=("Arial", 10, "bold"), width=300, height=35, borderwidth=1, highlightthickness=1, command= clr)
window.bind("c", lambda x: display("c"))
clear_btn .grid(row=3, columnspan=6)

window.mainloop()
