temperature = float(input(" What is the measure of the degrees: "))
provided_unit = input(" Is it in celsius(c) or fahrenheit(f): ")
if provided_unit.lower() == "c":
    temperature = (temperature*(9/5)) + 32
    print(f'{temperature} fahrenheit')
elif provided_unit.lower() == "f":
    temperature = (temperature-32) * (5/9)
    print(f'{temperature} celcius')
else:
    print(" I don't understand that, sorry. ")
