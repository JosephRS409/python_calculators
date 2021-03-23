temperature = float(input("What is the temperature? "))
standard = input("Celcius or Fahrenheit? (F/C): ").lower()
# windspeed = float(input("What is the windspeed? "))

def windchill(temperature, windspeed):
    pass
# Test, verify, then move on if working.
# One step at a time
    value = 35.74 + (.6215 * temperature) - 35.75 * (windspeed ** 0.16) + 0.4275 * (temperature * (windspeed ** 0.16))
    # return f"{value:.2}"
    return round(value, 2)

def temp_converter_to_f(c):
    fahrenheit = c * (9 / 5) + 32
    return fahrenheit # can't create a variable and return it at the same time

if standard == "c":
    temperature = temp_converter_to_f(temperature)

    # def temp_choice(celcius, fahrenheit):
    # pass
for windspeed in range(5, 61, 5):
    pass
    print(f"At temperature {temperature}, and windspeed {windspeed} mph, the windchill is {windchill(temperature, windspeed):.2f}F.")
print("Have a great day!")