# Fridge program
"""
Get the user to enter a fridge temperature in celsius.
<   0: Print "Fridge too cold"
0 - 4: Print "Fridge ok"
> 4  : Print "Fridge too warm"
>6   : Print "Fridge is broken"
temp is temperature
"""

print("")
temp = input("Input the fridge temperature in celsius: ")
temp = float(temp)
if temp < 0:
    print("Fridge too cold")
elif temp <= 4:
    print("Fridge ok")
elif temp <= 6:
    print("Fridge too warm")
else:
    print("Fridge is broken")
