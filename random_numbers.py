import random



def main(): # Has no parameters
    numbers = [16.2, 75.1, 52.3] #Creates a list named numbers like this:
    words = ['join', 'love', 'smile', 'love', 'cloud', 'head']

    print(numbers) #Prints the numbers list
    append_random_numbers(numbers) #Calls the append_random_numbers function with only one argument to add one number to numbers
    print(numbers) #Prints the numbers list
    #Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    append_random_numbers(numbers, 3)

    print(numbers) #Prints the numbers list

    
    append_random_words(words, 3)
    print (words)


def append_random_numbers(numbers_list, quantity=1):

    for i in range(quantity):
        random_number=random.uniform(0,100)
        addednumber=round(random_number,1)
        numbers_list.append(addednumber)

def append_random_words(words_list, quantity=1):
    
    random_number=random.uniform(1, quantity)
    integer=round(random_number)
    for element in range(0,6):
        words_list.append(words_list[element])
        
        # Call main to start this program.
if __name__ == "__main__":
    main()

