t = float(input(" What is the measure of the degrees: "))
p = input(" Is it in celsius(c) or fahrenheit(f): ")
if p.lower() == "c":
    t = (t*(9/5)) + 32
    print(f'{t} fahrenheit')
elif p.lower() == "f":
    t = (t-32) * (5/9)
    print(f'{t} celcis')
else:
    print(" I don't understand that, sorry. ")
