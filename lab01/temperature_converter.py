# CSE325-2026-L01-K7QX

RUN_PROFILE = "manual"

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 30


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C = {fahrenheit}°F")