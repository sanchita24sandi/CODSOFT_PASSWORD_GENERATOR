import random  # Import the random module to generate random choices
import string  # Import the string module to use predefined string constants

print("Welcome to our Random password generator")  # Print a welcome message

def main():  # Define the main function
    length = int(input("Enter the length of password you want:"))  # Ask the user for the desired password length and convert it to an integer
    
    lowerData = string.ascii_lowercase  # Get all lowercase letters
    upperdata = string.ascii_uppercase  # Get all uppercase letters
    digitD = string.digits  # Get all digits
    symbolsD = string.punctuation  # Get all punctuation symbols
    
    combine = lowerData + upperdata + digitD + symbolsD  # Combine all character sets into one string
    
    x = random.sample(combine, length)  # Randomly select 'length' number of characters from the combined string
    
    password = "".join(x)  # Join the selected characters to form the final password
    
    print(password)  # Print the generated password
    
    main()  # Call the main function again to generate another password if needed

main()  # Call the main function to start the program
