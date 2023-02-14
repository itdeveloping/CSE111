import random

def append_random_numbers(numbers_list, quantity=1):
    random_number=random.uniform(1, quantity)
    addednumber=round(random_number,1)
    numbers_list.append(addednumber)

def append_random_words(words_list, quantity=1):
    random_number=random.uniform(1, quantity)
    integer=round(random_number)
    for element in words_list[1,integer]:
        words_list.append(element)

def main(): # Has no parameters
    numbers = [16.2, 75.1, 52.3] #Creates a list named numbers like this:
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']

    print(numbers) #Prints the numbers list


    append_random_numbers(numbers) #Calls the append_random_numbers function with only one argument to add one number to numbers

    print(numbers) #Prints the numbers list
    #Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    quantity=random.uniform(1, 60)
    append_random_numbers(numbers, quantity)

    print(numbers) #Prints the numbers list

    quantity=random.uniform(1, 6)
    append_random_words(words, quantity)
    print (words)
# Call main to start this program.
if __name__ == "__main__":
    main()

