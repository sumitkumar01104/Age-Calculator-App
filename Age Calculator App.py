import tkinter as tk
from datetime import datetime, date

# Function to calculate age
def age():
    Age = str(entry_age.get())  # Example input: '30-06-2004'
    today = date.today()

    try:
         # Convert the input string into a date object using the given format
        DOB = datetime.strptime(Age, "%d-%m-%Y").date()

        # Calculate the age by subtracting birth year from current year
        # Subtract 1 if the birthday hasn't occurred yet this year
        age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

        # Display the result in the label
        label_result.config(text=f"Your Age is: {age} Years", fg="Green")

    except ValueError:
         # If the date format is incorrect, show error message
        label_result.config(text="Invalid date format! Use DD-MM-YYYY", fg="Red")
        
   # Clear the entry field after processing
    entry_age.delete(0,tk.END)
    
# Create the main application window
window = tk.Tk()
window.title("AGE CALCULETOR")
window.geometry("350x500")

# Top label with instructions
label_top = tk.Label(window,text="Enter Your Age:-\n[DD-MM-YYYY]:-",font=("Modern No. 20",16))
label_top.pack(pady=5)

# Entry field for user to type their date of birth
entry_age = tk.Entry(window,font=("arial,16"))
entry_age.pack(pady=5)

# Button to trigger the age calculation
btn_age = tk.Button(window,text="Check Age",command=age,bg="Green",fg="white",font=("Modern No. 20",14))
btn_age.pack(pady=5)

# Label to show the result (age or error)
label_result = tk.Label(window,text="",font=("Modern No. 20",14))
label_result.pack(pady=5)

# Run the Tkinter event loop
window.mainloop()
