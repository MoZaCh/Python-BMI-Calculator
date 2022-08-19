
def bmi_calculator(height, weight):

    height = float(height)  # Converting string to float
    weight = float(weight)
    bmi = weight / height**2  # Formula to work out BMI
    bmi = int(bmi)
    print(f'Your BMI: {bmi}')
    return bmi


if __name__ == '__main__':
    print("This is a test!")
