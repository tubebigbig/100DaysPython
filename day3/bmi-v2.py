def bmi_calculation(weight: int, height: float) -> float:
    bmi = weight / height**2
    return round(bmi, 2)


def main():
    height = float(input("Enter your height in m: "))
    weight = int(input("Enter your weight in kg: "))
    bmi = bmi_calculation(height=height, weight=weight)
    print(f"Your BMI is {bmi}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are slightly overweight.")
    elif bmi < 35:
        print("You are obese.")
    else:
        print("You are clinically obese.")


if __name__ == "__main__":
    main()
