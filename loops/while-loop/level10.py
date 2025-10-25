""""Write a program that finds the largest individual digit in a number.

input : 268937
op: 9 """
n = int(input("Enter a number: "))

# Initialize max_digit to 0. Since all digits are 0-9, this is a safe starting point.
max_digit = 0

# Store the original number for the print statement (optional but helpful)
original_n = n 

# The loop runs as long as there are digits left in n
while n > 0:
    # 1. Extract the last digit
    digit = n % 10

    # 2. Comparison Logic: Check if the currently extracted digit is larger 
    #    than the largest one we have recorded so far.
    if digit > max_digit:
        # 3. Update: If it is larger, set it as the new maximum.
        max_digit = digit

    # 4. Removal: Remove the last digit to prepare for the next iteration
    n //= 10

print(f"The largest individual digit in {original_n} is: {max_digit}")
n = int(input("Enter a number: "))
