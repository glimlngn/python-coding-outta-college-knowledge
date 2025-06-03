from tkinter import * # type: ignore

window = Tk()
window.title("Km to Miles Converter")
window.config(padx=20, pady=20)

# Labels
label_miles = Label(text="Km")
label_miles.grid(row=0, column=2)

label_isequalto = Label(text="is equal to")
label_isequalto.grid(row=1, column=0)

label_km = Label(text="Miles")
label_km.grid(row=1, column=2)

label_numkm = Label(text=0)
label_numkm.grid(row=1, column=1)

# Entry
input = Entry(width=30, justify="center")
input.grid(row=0, column=1)

# Button
def button_clicked(): 
    display = input.get()
    label_numkm.config(text=round(int(display)*1.60934, 4))
    
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()