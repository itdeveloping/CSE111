# Example 2

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]
    family= ['Dad','Mom','Dany','Ali','Becky']


    # Print the Fahrenheit temperatures.
    #print(f"Fahrenheit: {fahr_temps}")
    print (family)
    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    #cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    #print(f"Celsius: {cels_temps}")
def greetings(list)
    NewList="Hello "

def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    main()