import tkinter as tk
from tkinter import font  # Import the font module
from gpiozero import LED

# Connecting LEDs to GPIO pins
blue_led = LED(17)
orange_led = LED(27)
red_led = LED(22)

# Dictionary to keep track of LED states
led_states = {
    1: blue_led,
    2: orange_led,
    3: red_led
}

def toggle_led(value):
    """Toggle the selected LED's state and update radio button selection."""
    current_led = led_states[value]
    if current_led.is_lit:
        current_led.off()
        selected_led.set(0)  # Unselect the radio button if the LED is turned off
    else:
        turn_off_all_leds()
        current_led.on()
        selected_led.set(value)  # Set the radio button selection

def turn_off_all_leds():
    """Turn off all LEDs."""
    for led in led_states.values():
        led.off()

def exit_app():
    """Cleanup GPIO pins and close the GUI window."""
    turn_off_all_leds()
    win.destroy()

# Create the main window
win = tk.Tk()
win.title("LED Control")

# Define a custom font
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Frame for the radio buttons
frame = tk.Frame(win)
frame.pack(padx=100, pady=100)

# Radio button selection variable
selected_led = tk.IntVar(value=0)  # Default value set to 0

# Radio buttons for each LED
radio_buttons = {
    1: tk.Radiobutton(frame, text="Blue LED", variable=selected_led, value=1, command=lambda: toggle_led(1), font=custom_font, bg = 'lightblue'),
    2: tk.Radiobutton(frame, text="Orange LED", variable=selected_led, value=2, command=lambda: toggle_led(2), font=custom_font, bg = 'orange'),
    3: tk.Radiobutton(frame, text="Red LED", variable=selected_led, value=3, command=lambda: toggle_led(3), font = custom_font, bg = 'red')
}
for idx, rb in radio_buttons.items():
    rb.grid(row=idx-1, column=0)

# Exit button
exit_button = tk.Button(win, text="Exit", command=exit_app, font=custom_font)
exit_button.pack(pady=5)

# Start the GUI event loop
win.protocol("WM_DELETE_WINDOW", exit_app)
win.mainloop()
