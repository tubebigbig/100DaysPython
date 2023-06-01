def bmi_calculation(weight: int, height: float) -> float:
    bmi = weight / height**2
    return round(bmi, 2)


def main():
    height = float(input("Enter your height in m: "))
    weight = int(input("Enter your weight in kg: "))
    bmi = bmi_calculation(weight, height)
    print(bmi)


if __name__ == "__main__":
    main()
