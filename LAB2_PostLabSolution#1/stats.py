#Define these functions in a module named stats.py
def mode(words):
    #Each function should return 0 if the list is empty
    if len(words) == 0:
        return 0;
    else:
        theDictionary = {}
        for word in words:
            number = theDictionary.get(word, None)
            if number == None:
                # word entered for the first time
                theDictionary[word] = 1
            else:
                # word already seen, increment its number
                theDictionary[word] = number + 1

        # Find the mode by obtaining the maximum value
        # in the dictionary and determining its key
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key
                break

def median(numbers):
    # Sort the list and print the number at its midpoint
    if len(numbers) == 0:
        return 0;
    else:
        numbers.sort()
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1]) / 2
    
#Also include a function named mean, which computes the average of a set of numbers.
def mean(numbers):
    if len(numbers) == 0:
        return 0;
    else: 
        mean = sum(numbers) / len(numbers) if numbers else 0
        #return a single number
        return mean
    
#Include a main function that tests the three statistical functions with a given list
def main():
    fileName = input("Enter the file name: ")
    f = open(fileName, 'r')
    # Input the text, convert it to numbers, and
    # add the numbers to a list
    numbers = []
    for line in f:
        words = line.split()
        for word in words:
            numbers.append(float(word))
    #Each function should expect a list of numbers as an argument
    print("The mode is:", mode(numbers));
    print("The median is:", median(numbers));
    print("The mean is:", mean(numbers));

if __name__=="__main__":
    main()