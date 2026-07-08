import tkinter as tk
from tkinter import messagebox
from marks import ( calc_average, 
                    calculate_final_mark, 
                    results, save_module, 
                    get_saved_modules, 
                    load_module,
                    delete_saved_module,
                    module_exists)

TITLE_FONT = ("Arial", 18, "bold")
SUBTITLE_FONT = ("Arial", 14)
LABEL_FONT = ("Arial", 12)
BUTTON_FONT = ("Arial", 12, "bold")

ENTRY_WIDTH = 30
BUTTON_WIDTH = 20

PAD_X = 10
PAD_Y = 5

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
    clear_window(window)
    title1 = tk.Label(window,text="Grade Calculator",font=("Arial", 24, "bold"))
    title1.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)
    title2 = tk.Label(window,text="Calculate and Manage Module Marks",font=TITLE_FONT)
    title2.grid(row=1,column=0,pady=10)

    
    calculate_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Calculate Grade",font=BUTTON_FONT,command=lambda: show_module_info(window))
    calculate_button.grid(row=2,column=0,pady=10)


    saved_modules_button = tk.Button(window,
        width=BUTTON_WIDTH,text="View Saved Modules",font=BUTTON_FONT,command=lambda: show_saved_modules(window))
    saved_modules_button.grid(row=3,column=0,pady=10)


    exit_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Exit",font=BUTTON_FONT,command=window.destroy)
    exit_button.grid(row=4,column=0,pady=10)

def show_module_info(window):
    clear_window(window)
    title = tk.Label(window,text="Module Information",font=TITLE_FONT)
    title.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)

    module_name_label = tk.Label(window,text="Module Name: ",font=BUTTON_FONT)
    module_name_label.grid(row=1,column=0, padx=PAD_X, pady=PAD_Y)
    module_name_box= tk.Entry(window, width=ENTRY_WIDTH)
    module_name_box.grid(row=1,column=1, padx=PAD_X, pady=PAD_Y)

    module_categories_label = tk.Label(window,text="Number of Assessment Categories: ",font=BUTTON_FONT)
    module_categories_label.grid(row=2,column=0, padx=PAD_X, pady=PAD_Y)
    module_categories_box= tk.Entry(window, width=ENTRY_WIDTH)
    module_categories_box.grid(row=2,column=1, padx=PAD_X, pady=PAD_Y)

    error_label = tk.Label(window,text="",fg="red")
    error_label.grid(row=3,column=0, padx=PAD_X, pady=PAD_Y)

    next_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Next",font=BUTTON_FONT,command=lambda: handle_module_info(window,module_name_box,module_categories_box,error_label))
    next_button.grid(row=4,column=0, padx=PAD_X, pady=PAD_Y)

def handle_module_info(window,module_name_box,assessment_categories_box,error_label):
    error_label.config(text="")
    module_name = module_name_box.get().strip()

    if not module_name:
        error_label.config(text="Please Enter a Module Name")
        return

    try:
        assessment_categories = int(assessment_categories_box.get())
        if assessment_categories <= 0:
            error_label.config(text="Please Enter a Positive Whole Number")
            return
    except ValueError:
        error_label.config(text="Please Enter a Valid Number")
        return


    print(module_name)
    print(assessment_categories)

    show_assessment_screen(window,module_name,assessment_categories)

def show_assessment_screen(window,module_name,assessment_categories):
    clear_window(window)
    title = tk.Label(window,text="Assessment Information",font=TITLE_FONT)
    title.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)

    mod_name = tk.Label(window,text=f"Module Name: {module_name}",font=BUTTON_FONT)
    mod_name.grid(row=1,column=0, padx=PAD_X, pady=PAD_Y)

    category_name_boxes = []
    weight_percentage_boxes = []
    num_marks_boxes = []

    for i in range (assessment_categories):
        start_row = 2 + i*4

        assessment_num = tk.Label(window,text=f"Assessment {i+1}",font=BUTTON_FONT)
        assessment_num.grid(row=start_row,column=0, padx=PAD_X, pady=PAD_Y)

        category_name = tk.Label(window,text="Category Name: ",font=BUTTON_FONT)
        category_name.grid(row=start_row+1,column=0, padx=PAD_X, pady=PAD_Y)
        category_name_box = tk.Entry(window, width=ENTRY_WIDTH)
        category_name_box.grid(row=start_row+1,column=1, padx=PAD_X, pady=PAD_Y)
        category_name_boxes.append(category_name_box)

        weight_percentage = tk.Label(window,text="Weight(%): ",font=BUTTON_FONT)
        weight_percentage.grid(row=start_row+2,column=0, padx=PAD_X, pady=PAD_Y)
        weight_percentage_box = tk.Entry(window, width=ENTRY_WIDTH)
        weight_percentage_box.grid(row=start_row+2,column=1, padx=PAD_X, pady=PAD_Y)
        weight_percentage_boxes.append(weight_percentage_box)

        num_marks = tk.Label(window,text="Number of Marks: ",font=BUTTON_FONT)
        num_marks.grid(row=start_row+3,column=0, padx=PAD_X, pady=PAD_Y)
        num_marks_box = tk.Entry(window, width=ENTRY_WIDTH)
        num_marks_box.grid(row=start_row+3,column=1, padx=PAD_X, pady=PAD_Y)
        num_marks_boxes.append(num_marks_box)
    error_label = tk.Label(window,text="",fg="red")
    error_label.grid(row=start_row+4, padx=PAD_X, pady=PAD_Y)
    next_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Next",font=BUTTON_FONT,command=lambda: handle_assessment_info(
        window,module_name,category_name_boxes,weight_percentage_boxes,num_marks_boxes,error_label))
    next_button.grid(row=start_row+5,column=0, padx=PAD_X, pady=PAD_Y)

def handle_assessment_info(window,module_name,categories_arr,weight_arr,num_marks_arr,error_label):
    error_label.config(text="")
    category_names = []
    weight_percentages = []
    number_of_marks = []
    for name in categories_arr:
        category = name.get().strip()
        if not category:
            error_label.config(text="Category Names Cannot Be Empty")
            return
        category_names.append(category)

    for name in category_names:
        if category_names.count(name) > 1:
            error_label.config(text="Category Names Must Be Unique")
            return
    
    for weight in weight_arr:
        try:
            value = float(weight.get())
        except ValueError:
            error_label.config(text="Please Enter Valid Weight Values")
            return
        if value < 0 or value > 100:
            error_label.config(text="Weights Must Be Between 0 and 100")
            return

        weight_percentages.append(value/100)
    
    for marks in num_marks_arr:
        try:
            number = int(marks.get())
        except ValueError:
            error_label.config(text="Please Enter a Valid Number of Marks")
            return
        if number <= 0:
            error_label.config(text="Number of Marks Must Be Greater Than 0")
            return
        number_of_marks.append(number)

    total_weight = sum(weight_percentages)

    if abs(total_weight - 1.0) > 0.001:
        error_label.config(text="Weights must add up to 100%.")
        return
    print(category_names)
    print(weight_percentages)
    print(number_of_marks)

    show_mark_entry_screen(window,module_name,category_names,weight_percentages,number_of_marks)

def show_mark_entry_screen(window,module_name,categories_arr,weight_arr,num_marks_arr):
    clear_window(window)

    canvas = tk.Canvas(window, highlightthickness=0)
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)

    scroll_frame = tk.Frame(canvas)

    canvas_window = canvas.create_window(
        (0, 0),
        window=scroll_frame,
        anchor="nw"
    )

    def resize_frame(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", resize_frame)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    canvas.bind_all(
        "<MouseWheel>",
        lambda event: canvas.yview_scroll(int(-event.delta / 120), "units")
    )

    title = tk.Label(scroll_frame,text="Marks Entry",font=TITLE_FONT)
    title.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)

    mod_name = tk.Label(scroll_frame,text=f"Module Name: {module_name}",font=BUTTON_FONT)
    mod_name.grid(row=1,column=0, padx=PAD_X, pady=PAD_Y)

    marks_arr = []

    current_row = 2

    for i in range(len(categories_arr)):
        current_assessment_marks = []

        category_name = tk.Label(scroll_frame,text=categories_arr[i],font=BUTTON_FONT)
        category_name.grid(row=current_row,column=0, padx=PAD_X, pady=PAD_Y)
        current_row += 1

        for j in range(num_marks_arr[i]):
            mark_number = tk.Label(scroll_frame,text=f"Mark {j+1}(%)",font=BUTTON_FONT)
            mark_number.grid(row=current_row,column=0, padx=PAD_X, pady=PAD_Y)

            mark_box = tk.Entry(scroll_frame, width=ENTRY_WIDTH)
            mark_box.grid(row=current_row,column=1, padx=PAD_X, pady=PAD_Y)

            current_assessment_marks.append(mark_box)
            current_row += 1

        marks_arr.append(current_assessment_marks)
        current_row += 1

    error_label = tk.Label(scroll_frame,text="",fg="red")
    error_label.grid(row=current_row+1,column=0, padx=PAD_X, pady=PAD_Y)

    calc_button = tk.Button(
        scroll_frame,
        text="Calculate",
        font=BUTTON_FONT,
        command=lambda: handle_marks(
            window,
            module_name,
            categories_arr,
            weight_arr,
            marks_arr,
            error_label
        )
    )
    calc_button.grid(row=current_row+2,column=0, padx=PAD_X, pady=PAD_Y)

def handle_marks(window,module_name,categories_arr,weight_arr,marks_arr,error_label):
    error_label.config(text="")
    all_marks = []
    for i in range(len(marks_arr)):
        current_mark = []
        for j in range(len(marks_arr[i])):
            try:
                mark = float(marks_arr[i][j].get())
            except ValueError:
                error_label.config(text="Please Enter Valid Mark Values")
                return
            if mark < 0 or mark > 100:
                error_label.config(text="Marks Must Be Between 0 and 100")
                return
            
            current_mark.append(mark)
        all_marks.append(current_mark)
    category_averages = []
    for category_marks in all_marks:
        average = calc_average(category_marks)
        category_averages.append(average)
    final_mark = calculate_final_mark(category_averages,weight_arr)
    result = results(final_mark)
    show_results_screen(window,module_name,categories_arr,weight_arr,category_averages,final_mark,result)

def show_results_screen(window,module_name,categories_arr,weight_arr,category_averages,final_mark,result):
    clear_window(window)
    title = tk.Label(window,text="Results",font=TITLE_FONT)
    title.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)

    mod_name = tk.Label(window,text=f"Module Name: {module_name}",font=BUTTON_FONT)
    mod_name.grid(row=1,column=0, padx=PAD_X, pady=PAD_Y)

    for i in range(len(categories_arr)):
        start_row = 2 + i*4
        category = tk.Label(window,text=f"{categories_arr[i]}",font=BUTTON_FONT)
        category.grid(row=start_row,column=0, padx=PAD_X, pady=PAD_Y)

        average = tk.Label(window,text="Average: ",font=BUTTON_FONT)
        average.grid(row=start_row+1,column=0, padx=PAD_X, pady=PAD_Y)

        average_display = tk.Label(window,text=f"{category_averages[i]:.2f}%",font=BUTTON_FONT)
        average_display.grid(row=start_row+1,column=1, padx=PAD_X, pady=PAD_Y)

        weight = tk.Label(window,text="Weight: ",font=BUTTON_FONT)
        weight.grid(row=start_row+2,column=0, padx=PAD_X, pady=PAD_Y)

        weight_display = tk.Label(window,text=f"{weight_arr[i]*100:.3f}%",font=BUTTON_FONT)
        weight_display.grid(row=start_row+2,column=1, padx=PAD_X, pady=PAD_Y)

    finalmark = tk.Label(window,text="Final Mark: ",font=BUTTON_FONT)
    finalmark.grid(row=start_row+4,column=0, padx=PAD_X, pady=PAD_Y)

    finalmark_display = tk.Label(window,text=f"{final_mark:.2f}%",font=BUTTON_FONT)
    finalmark_display.grid(row=start_row+4,column=1, padx=PAD_X, pady=PAD_Y)

    result_display = tk.Label(window,text=f"{result}",font=BUTTON_FONT)
    result_display.grid(row=start_row+5,column=0, padx=PAD_X, pady=PAD_Y)

    save_mod_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Save Module",font=BUTTON_FONT,command=lambda: handle_save(window,module_name,final_mark,result,categories_arr,weight_arr,category_averages,start_row,save_mod_button))
    save_mod_button.grid(row=start_row+7,column=0, padx=PAD_X, pady=PAD_Y)

    back_home_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Home",font=BUTTON_FONT,command=lambda: handle_home(window))
    back_home_button.grid(row=start_row+11,column=0, padx=PAD_X, pady=PAD_Y)

def handle_save(window,module_name,final_mark,result,categories_arr,weight_arr,category_averages,start_row,save_mod_button):
    if not module_exists(module_name):
        save_module(module_name,final_mark,result,categories_arr,weight_arr,category_averages)
        status = tk.Label(window,text="Module saved successfully!",font=BUTTON_FONT,fg="green")
        status.grid(row=start_row+9,column=0, padx=PAD_X, pady=PAD_Y)
        save_mod_button.config(state="disabled")
    else:
        overwrite = messagebox.askyesno("Module Exists",f"'{module_name}' already exists.\n\nDo you want to overwrite it?")
        if overwrite:
            save_module(module_name,final_mark,result,categories_arr,weight_arr,category_averages)
            status = tk.Label(window,text="Module saved successfully!",font=BUTTON_FONT,fg="green")
            status.grid(row=start_row+9,column=0, padx=PAD_X, pady=PAD_Y)
            save_mod_button.config(state="disabled")


def handle_home(window):
    show_home_screen(window)

def show_saved_modules(window):
    clear_window(window)

    title = tk.Label(window,text="Saved Modules",font=TITLE_FONT)
    title.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)

    modules = get_saved_modules()
    module_list = tk.Listbox(window)
    module_list.grid(row=1,column=0, padx=PAD_X, pady=PAD_Y)
    for module in modules:
        module_list.insert(tk.END,module)

    open_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Open",font=BUTTON_FONT,command=lambda: handle_open(window,module_list))
    open_button.grid(row=2,column=0, padx=PAD_X, pady=PAD_Y)
    delete_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Delete",font=BUTTON_FONT,command=lambda: handle_delete(window,module_list))
    delete_button.grid(row=3,column=0, padx=PAD_X, pady=PAD_Y)
    home_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Home",font=BUTTON_FONT,command=lambda: show_home_screen(window))
    home_button.grid(row=4,column=0, padx=PAD_X, pady=PAD_Y)

def handle_open(window,module_list):
    selected = module_list.curselection()
    if not selected:
        return
    module_name = module_list.get(selected[0])
    contents = load_module(module_name)
    if contents is None:
        return
    show_saved_module(window,module_name,contents)

def handle_delete(window,module_list):
    selected = module_list.curselection()
    if not selected:
        return
    module_name = module_list.get(selected[0])
    delete_saved_module(module_name)
    show_saved_modules(window)


def show_saved_module(window,module_name,contents):
    clear_window(window)

    title = tk.Label(window,text=f"{module_name}",font=TITLE_FONT)
    title.grid(row=0,column=0, padx=PAD_X, pady=PAD_Y)

    info = tk.Label(window,text=f"{contents}",font=BUTTON_FONT)
    info.grid(row=1,column=0, padx=PAD_X, pady=PAD_Y)

    home_button = tk.Button(window,
        width=BUTTON_WIDTH,text="Home",font=BUTTON_FONT,command=lambda: show_home_screen(window))
    home_button.grid(row=2,column=0, padx=PAD_X, pady=PAD_Y)

def main():
    window = create_window()
    show_home_screen(window)
    window.mainloop()


if __name__ == "__main__":
    main()