# Example 4

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]
    family=['oscar','mercedes','daniela','alicia','rebeca']
    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")
    print(family)

    # Define a lambda function that converts
    # a Fahrenheit temperature to Celsius and
    # returns the Celsius temperature.
    cels_from_fahr = lambda fahr: round((fahr - 32) * 5 / 9, 1)
    greeting = lambda list: f'Hello {list.title()}'
    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))
    newlist=list(map(greeting, family))
    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")
    print(newlist)
    
def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()