import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Grade Calculator")
    logo = tk.PhotoImage(file = "logo.png")
    window.iconphoto(True,logo)
    window.geometry("400x300")
    window.resizable(False,False)
    return window

def home_screen(window):
    title1 = tk.Label(window,text="Grade Calculator",font=("Arial",24,"bold"))
    title1.grid(row=0,column=0)
    title2 = tk.Label(window,text="Calculate and Manage Module Marks",font=("Arial",16,"bold"))
    title2.grid(row=1,column=0,pady=10)
    calculate_button = tk.Button(window,text="Calculate Grade",font=("Arial",12,"bold"))
    calculate_button.grid(row=2,column=0,pady=10)
    saved_modules_button = tk.Button(window,text="View Saved Modules",font=("Arial",12,"bold"))
    saved_modules_button.grid(row=3,column=0,pady=10)
    exit_button = tk.Button(window,text="Exit",font=("Arial",12,"bold"),command=window.destroy)
    exit_button.grid(row=4,column=0,pady=10)

def main():
    window = create_window()
    home_screen(window)
    window.mainloop()


if __name__ == "__main__":
    main()