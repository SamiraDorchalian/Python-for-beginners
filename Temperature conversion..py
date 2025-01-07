import tkinter as tk

window = tk.Tk()

fahrenheit_val = tk.StringVar()
#Label
lbl_result = tk.Label(
    master=window,
    text='Enter your number...',
)
#program logic with fun
def convert_fahrenheit_to_celsius(*args):
    #user input value
    fahrenheit_input = fahrenheit_val.get()
    try:
        fahrenheit_value = float(fahrenheit_input)
        # convert to celsius
        lbl_result['text']= (fahrenheit_value-32)*5/9
    except ValueError:
        if fahrenheit_input != '':
            # if user input is not valid
            lbl_result['text']= 'You should enter a number.'
        else:
            # if user input is empty
            lbl_result['text']= 'You input is empty.'

window.bind('<Return>', convert_fahrenheit_to_celsius)

# Label
lbl_fahrenheit = tk.Label(
    master=window,
    text='Fahrenheit: ',
)
# Entry => get value input
ent_fahrenheit = tk.Entry(
    master=window,
    width=50,
    textvariable=fahrenheit_val,
)
# Button
btn_calc = tk.Button(
    master=window,
    text='Calc',
    command=convert_fahrenheit_to_celsius,
)
# Window design with grid
lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)
#Label
lbl_celsius = tk.Label(
    master=window,
    text='Celsius: ',
)
# Window design with grid
lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))
# Change the text of the window header/title
window.title('Temperature Conversion')
window.mainloop()