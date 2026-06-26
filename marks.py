import os

def num_categories():
    prompt = "Enter number of categories: "
    categories = get_valid_int(prompt)
    return categories

def calc_average(category):
    total = 0.0
    
    print(f"\nEntering {category} marks")
    prompt1 = "Enter number of marks: "
    num_marks = get_valid_int(prompt1)
    prompt2 = "Enter mark(%): "

    for i in range(num_marks):
        mark = get_valid_float(prompt2)
        while mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100")
            mark = get_valid_float(prompt2)
        total += mark

    average = total/num_marks

    return average

def get_weights(category):
    print(f"Entering {category} weighting")
    prompt = "Enter weighting: "
    weight = get_valid_float(prompt)
    while weight < 0 or weight > 100:
        print("Error: Weight must be between 0 and 100")
        weight = get_valid_float(prompt)
    weight /= 100
    return weight

def results(final):
    return "PASS" if final >= 50.0 else "FAIL"

def display(name,avgs,weights,final,result,modname):
    size = len(name)
    print("-----------------\n\n")
    print(f"Module name: {modname}")
    print("-----------------\n\n")
    for i in range(size):
        print(f"{name[i]}\n")
        print(f"Average is: {avgs[i]:.2f}%\n")
        print(f"weight is: {weights[i] * 100:.2f}%\n\n")
    print("-----------------\n")
    print(f"Final mark: {final:.2f}%\n")
    print(f"Result: {result}")

def yes_or_no_validation(letter,prompt):
    while letter.lower() != "y" and letter.lower() != "n":
        print("Error: Please enter y or n only")
        letter = input(prompt)
    return letter.lower()

def save_module(module_name,final_mark,result,category_name,weights,avgs):
    folder = "modulemarks"
    filename = module_name + ".txt"
    path = os.path.join(folder,filename)
    with open(path,"w") as file:
        size = len(category_name)
        file.write("-----------------\n\n")
        file.write(f"Module name: {module_name}\n\n")
        file.write("-----------------\n\n")
        for i in range(size):
            file.write(f"{category_name[i]}\n")
            file.write(f"Average is: {avgs[i]:.2f}%\n")
            file.write(f"weight is: {weights[i] * 100:.2f}%\n\n")
        file.write("-----------------\n")
        file.write(f"Final mark: {final_mark:.2f}%\n")
        file.write(f"Result: {result}\n\n")

def view_saved_modules():
    folder = "modulemarks"
    filename = input("Enter module name: ") + ".txt"
    path = os.path.join(folder,filename)
    try:
        with open(path,"r") as file:
            contents = file.read()
        print(contents)

    except FileNotFoundError:
        print("Module not found.")

def calculate_module():
    module_name = input("Enter module name: ")
    if not overwrite(module_name):
        print("Calculation cancelled.")
        return
    category_names = []
    category_averages = []
    category_weights = []
    final_mark = 0.0
    total_weight = 0.0
    categories = num_categories()
    for i in range(categories):
        category = input("Category name: ")
        category_names.append(category)
        
        average = calc_average(category)
        category_averages.append(average)
        
        weight = get_weights(category)
        category_weights.append(weight)
        
        final_mark += average * weight
        total_weight += weight
    
    if abs(total_weight-1.0) > 0.001:
        print("Error: Weightings must add to 100%")
        return

    result = results(final_mark)

    display(category_names,category_averages,category_weights,final_mark,result,module_name)
    
    prompt = "Save Module? (y/n): "
    saved = input(prompt)
    if yes_or_no_validation(saved,prompt) == "y":
        save_module(module_name,final_mark,result,category_names,category_weights,category_averages)

def list_saved_modules():
    files = os.listdir("modulemarks")
    if len(files) == 0:
        print("No saved modules found.")
        return
    print("\nSaved Modules:\n")
    
    for file in files:
        if file.endswith(".txt"):
            module_name = file.removesuffix(".txt")
            print(module_name)

def delete_module():
    module_name = input("Enter module name: ")
    folder = "modulemarks"
    filename = module_name + ".txt"
    path = os.path.join(folder,filename)
    if os.path.exists(path):
        prompt = f"Delete {module_name}? (y/n): "
        choice = input(prompt)
        if yes_or_no_validation(choice,prompt) == "y":
            os.remove(path)
            print("Module successfully deleted")
        else:
            print("Module deletion cancelled")
    else:
        print("Module not found")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a value greater that 0")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def overwrite(module_name):
    folder = "modulemarks"
    filename = module_name + ".txt"
    path = os.path.join(folder,filename)
    if os.path.exists(path):
        prompt = f"Module {module_name} already exists.\nOverwrite {module_name}? (y/n): "
        choice = input(prompt)
        if yes_or_no_validation(choice,prompt) == "y":
            return True
        else:
            return False
    else:
        return True
    

def menu():
    print("1. Calculate Module Marks")
    print("2. View Module")
    print("3. List saved modules")
    print("4. Delete module")
    print("5. Exit\n")
    
    choice = input("Choice: ")
    return choice

def calc_average(marks):
    nums = len(marks)
    total = 0.0
    for i in range(len(marks)):
        total += marks[i]
    average = total / nums
    return average

def calculate_final_mark(category_averages,weights):
    final_mark = 0.0
    for i in range(len(category_averages)):
        final_mark += category_averages[i] * weights[i]
    return final_mark

def main():
    while True:
        choice = menu()

        if choice == "1":
            calculate_module()
        
        elif choice == "2":
            view_saved_modules()
        
        elif choice == "3":
            list_saved_modules()
        
        elif choice == "4":
            delete_module()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid Choice")
    


if __name__ == "__main__":
    main()