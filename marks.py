def num_categories():
    categories = int(input("Enter number of categories: "))
    return categories

def calc_average(category):
    total = 0.0
    
    print(f"\nEntering {category} marks")
    
    num_marks = int(input("Enter number of marks: "))

    for i in range(num_marks):
        mark = float(input("Enter mark(%): "))
        while mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100")
            mark = float(input("Enter mark(%): "))
        total += mark

    average = total/num_marks

    return average

def get_weights(category):
    print(f"Entering {category} weighting")
    weight = float(input("Enter weighting: "))
    while weight < 0 or weight > 100:
        print("Error: Weight must be between 0 and 100")
        weight = float(input("Enter weighting: "))
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

def save_module_validation(letter):
    while letter.lower() != "y" and letter.lower() != "n":
        print("Error: Please enter y or n only")
        letter = input("Save Module? (y/n): ")
    return letter.lower()

def save_module(module_name,final_mark,result,category_name,weights,avgs):
    with open("saved_modules.txt","a") as file:
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
    

def main():
    module_name = input("Enter module name: ")
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
    
    saved = input("Save Module? (y/n): ")
    if save_module_validation(saved) == "y":
        save_module(module_name,final_mark,result,category_names,category_weights,category_averages)
    


if __name__ == "__main__":
    main()