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



bmi_output = calculate_bmi(1.75, 70)



print("BMI output is ", bmi_output)



#calculate_bmi(1.75, 70)

