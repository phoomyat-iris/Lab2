print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ",weight)

    bmi = weight / (height * height)
    print("value of bmi is: ", bmi)
    if bmi < 18.5:
        print("BMI is underweight")
    elif bmi >= 18.5 and bmi <24.9:
        print("BMI is normal weight")
    else:
        print("BMI is overweight")

    return bmi

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input() #no input type
    str_list = user_input.split(",") #spliting the input
    float_list = [] 
    for i in str_list:
        float_list.append(float(i)) # adding the input into the list
    return float_list

def calc_average(num_list):
    total = 0
    for i in num_list:
        total = total + i
    average = total / len(num_list)
    return average

def find_min_max(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    return [min_temp, max_temp]

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    min_max = find_min_max(num_list)

    print(num_list)
    print("Average temperature:", average)
    print("Minimum temperature:", min_max[0])
    print("Maximum temperature:", min_max[1])

if __name__ == "__main__":
    main()

#bmi_output = calculate_bmi(1.75, 70)

#print("BMI output is ", bmi_output)

#calculate_bmi(1.75, 70)

