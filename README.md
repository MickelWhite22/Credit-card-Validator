# Credit-card-Validator
Validating credit card numbers using Luhn's Algorithm. This script also sanitizes and validates input to ensure the credit card number only consists of integers and meets the 13-digit length requirement.

## Attributes

- Luhn Algorithm: Validates card numbers using the Luhn algorithm.
- Input Sanitization: removes non-digit characters from the input
- Length Validation: Ensures the card number length is between 13 and 19

## Requirements
- Python 3.x

## Explanation
 Step 1: import required module
  ```bash
  import re
  ```
 Step 2: Luhn Check
 - Convert the card number to a list of integers
 - Reverse card number
 - Double every second digit
 - Add the sum of the digits if greater than 9
 - Add all of the digits
 - Check if the final sum is divisible by 10 without a remainder

```bash
   
  def lhun_check(ask):
   digits = [int(digit) for digit in str(ask)] 
   digits.reverse()
   
   for i in range(len(digits)):
      if i % 2 == 1:
         digits[i] *= 2
         if digits[i] > 9:
            digits[i] -= 9
   total_sum = sum(digits)
   return total_sum % 10 == 0
```
Step 3: Logic
- Ask the user for the card number
- Implemented sanitization and validation for added security

```bash
 def sanitize_input(ask):
   sanitized = re.sub(r'\D', '', ask)
   return sanitized
 
def valid_card_number(ask):
   if not re.match(r'^\d{13,19}$', ask):
      return False
   return True

ask = input("Enter your sixteen digit card number: ")
sanitized_numbers = sanitize_input(ask)
if valid_card_number(sanitized_numbers):
    if lhun_check(sanitized_numbers):
        print("The card number is valid")
    else:
        print("The card number is invalid")
else:
    print("Invalid card format.")
```

- Perform Luhn check with message to match outcome

## Usage
- Export code
- Run the script using any version of Python 3
