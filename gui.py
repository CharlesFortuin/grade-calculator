import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Grade Calculator")
    logo = tk.PhotoImage(file = "logo.png")
    window.iconphoto(True,logo)
    window.geometry("700x700")
    window.resizable(False,False)
    return window

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def show_home_screen(window):
    title1 = tk.Label(window,text="Grade Calculator",font=("Arial",24,"bold"))
    title1.grid(row=0,column=0)
    title2 = tk.Label(window,text="Calculate and Manage Module Marks",font=("Arial",16,"bold"))
    title2.grid(row=1,column=0,pady=10)

    
    calculate_button = tk.Button(window,text="Calculate Grade",font=("Arial",12,"bold"),command=lambda: show_module_info(window))
    calculate_button.grid(row=2,column=0,pady=10)


    saved_modules_button = tk.Button(window,text="View Saved Modules",font=("Arial",12,"bold"))
    saved_modules_button.grid(row=3,column=0,pady=10)


    exit_button = tk.Button(window,text="Exit",font=("Arial",12,"bold"),command=window.destroy)
    exit_button.grid(row=4,column=0,pady=10)

def show_module_info(window):
    clear_window(window)
    title = tk.Label(window,text="Module Information",font=("Arial",16,"bold"))
    title.grid(row=0,column=0)

    module_name_label = tk.Label(window,text="Module Name: ",font=("Arial",12,"bold"))
    module_name_label.grid(row=1,column=0)
    module_name_box= tk.Entry(window)
    module_name_box.grid(row=1,column=1)

    module_categories_label = tk.Label(window,text="Number of Assessment Categories: ",font=("Arial",12,"bold"))
    module_categories_label.grid(row=2,column=0)
    module_categories_box= tk.Entry(window)
    module_categories_box.grid(row=2,column=1)

    next_button = tk.Button(window,text="Next",font=("Arial",12,"bold"),command=lambda: handle_module_info(window,module_name_box,module_categories_box))
    next_button.grid(row=3,column=0)

def handle_module_info(window,module_name_box,assessment_categories_box):
    module_name = module_name_box.get()
    assessment_categories = int(assessment_categories_box.get())
    print(module_name)
    print(assessment_categories)

    show_assessment_screen(window,module_name,assessment_categories)

def show_assessment_screen(window,module_name,assessment_categories):
    clear_window(window)
    title = tk.Label(window,text="Assessment Information",font=("Arial",16,"bold"))
    title.grid(row=0,column=0)

    mod_name = tk.Label(window,text=f"Module Name: {module_name}",font=("Arial",12,"bold"))
    mod_name.grid(row=1,column=0)

    category_name_boxes = []
    weight_percentage_boxes = []
    num_marks_boxes = []

    for i in range (assessment_categories):
        start_row = 2 + i*4

        assessment_num = tk.Label(window,text=f"Assessment {i+1}",font=("Arial",12,"bold"))
        assessment_num.grid(row=start_row,column=0)

        category_name = tk.Label(window,text="Category Name: ",font=("Arial",12,"bold"))
        category_name.grid(row=start_row+1,column=0)
        category_name_box = tk.Entry(window)
        category_name_box.grid(row=start_row+1,column=1)
        category_name_boxes.append(category_name_box)

        weight_percentage = tk.Label(window,text="Weight(%): ",font=("Arial",12,"bold"))
        weight_percentage.grid(row=start_row+2,column=0)
        weight_percentage_box = tk.Entry(window)
        weight_percentage_box.grid(row=start_row+2,column=1)
        weight_percentage_boxes.append(weight_percentage_box)

        num_marks = tk.Label(window,text="Number of Marks: ",font=("Arial",12,"bold"))
        num_marks.grid(row=start_row+3,column=0)
        num_marks_box = tk.Entry(window)
        num_marks_box.grid(row=start_row+3,column=1)
        num_marks_boxes.append(num_marks_box)
    
    next_button = tk.Button(window,text="Next",font=("Arial",12,"bold"),command=lambda: handle_assessment_info(window,module_name,category_name_boxes,weight_percentage_boxes,num_marks_boxes))
    next_button.grid(row=start_row+4,column=0)

def handle_assessment_info(window,module_name,categories_arr,weight_arr,num_marks_arr):
    category_names = []
    weight_percentages = []
    number_of_marks = []
    for name in categories_arr:
        category_names.append(name.get())
    for weight in weight_arr:
        weight_percentages.append(float(weight.get()))
    for marks in num_marks_arr:
        number_of_marks.append(int(marks.get()))
    print(category_names)
    print(weight_percentages)
    print(number_of_marks)

    show_mark_entry_screen(window,module_name,category_names,weight_percentages,number_of_marks)

def show_mark_entry_screen(window,module_name,categories_arr,weight_arr,num_marks_arr):
    clear_window(window)
    title = tk.Label(window,text="Marks Entry",font=("Arial",16,"bold"))
    title.grid(row=0,column=0)

    mod_name = tk.Label(window,text=f"Module Name: {module_name}",font=("Arial",12,"bold"))
    mod_name.grid(row=1,column=0)

    marks_arr = []

    current_row = 2

    for i in range(len(categories_arr)):
        current_assessment_marks = []

        category_name = tk.Label(window,text=f"{categories_arr[i]}",font=("Arial",12,"bold"))
        category_name.grid(row=current_row,column=0)
        current_row += 1

        for j in range(num_marks_arr[i]):
            mark_number = tk.Label(window,text=f"Mark {j+1}",font=("Arial",12,"bold"))
            mark_number.grid(row=current_row,column=0)
            mark_box = tk.Entry(window)
            mark_box.grid(row=current_row,column=1)
            current_assessment_marks.append(mark_box)
            current_row += 1
        marks_arr.append(current_assessment_marks)
        current_row+=1
        

    calc_button = tk.Button(window,text="Calculate",font=("Arial",12,"bold"),command=lambda: handle_marks(window,module_name,categories_arr,weight_arr,marks_arr))
    calc_button.grid(row=current_row+1,column=0)

def handle_marks(window,module_name,categories_arr,weight_arr,marks_arr):
    all_marks = []
    for i in range(len(marks_arr)):
        current_mark = []
        for j in range(len(marks_arr[i])):
            current_mark.append(float(marks_arr[i][j].get()))
        all_marks.append(current_mark)

    pass

def main():
    window = create_window()
    show_home_screen(window)
    window.mainloop()


if __name__ == "__main__":
    main()