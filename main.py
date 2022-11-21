from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
counter = 4


# ---------------------------- start writing some text ------------------ #
def start_writing():
    button.place_forget()
    button.config(state=DISABLED)
    list_inputs = []
    canvas.itemconfig(background, image=img2)
    textentry = Text(canvas, font=("Arial", 18, "normal"), bg="#F1EAE0", highlightthickness=5, borderwidth=0,
                     highlightbackground="#3E2D2B", highlightcolor="#3E2D2B", insertbackground="#DE441C")
    textentry.focus()
    canvas.create_window(345, 400, window=textentry, height=400, width=560)

    label = Label(text="", font=("Arial", 30, "normal"), fg="#2A2A2D", bg="#F1EAE0")

    # ------------ restart the application if stop writing --------------- #
    def reset():
        canvas.itemconfig(background, image=img1)
        canvas.place(x=0, y=0)
        button.place(x=200, y=585)
        button.config(state=NORMAL)

    # ------------ START COUNT DOWN IF STOP WRITING AFTER 3 SEC ----------- #
    def start_count_down():
        global counter
        counter -= 1
        label.config(text=f"{counter}")
        label.place(x=650, y=200)
        new_input = textentry.get("1.0", 'end-1c')
        list_inputs.append(new_input)
        for elem in list_inputs:
            if list_inputs.count(elem) == 1 and list_inputs[0] != elem:
                counter = 4
                label.place_forget()
                list_inputs.clear()
                get_input_text()
                return 0
        if counter == 0:
            label.place_forget()
            textentry.destroy()
            counter = 4
            reset()
            return 0
        window.after(1000, start_count_down)

    # ------------ GET THE TEXT THAT THE USER HAS WRITTEN ----------- #
    def get_input_text():
        input_text = textentry.get("1.0", 'end-1c')
        list_inputs.append(input_text)
        for elem in list_inputs:
            if list_inputs.count(elem) > 1:
                list_inputs.clear()
                window.after(1000, start_count_down)
                return 0
        window.after(1000, get_input_text)

    get_input_text()


# ------------ CONFIG THE WINDOW ----------- #
window = Tk()
window.geometry("700x700")
window.title("The Most Dangerous Writing App")

# -------------- CONFIG CANVAS -------------- #
canvas = Canvas(window, width=700, height=700)
img1 = ImageTk.PhotoImage(Image.open("images/background.png"))
img2 = ImageTk.PhotoImage(Image.open("images/start_writing.png"))
background = canvas.create_image(350, 350, image=img1)
canvas.place(x=0, y=0)

# ------------ CONFIG BUTTON ----------- #
button = Button(canvas, text='START', command=start_writing, width=21, height=1, bg="#DF451C", highlightthickness=0,
                borderwidth=0, font=("ariel", "17", "bold"), fg="white")
button.place(x=200, y=585)

window.mainloop()
