import re

def sanitize_input(ask):
   sanitized = re.sub(r'\D', '', ask)
   return sanitized

def valid_card_number(ask):
   if not re.match(r'^\d{13,19}$', ask):
      return False
   return True

def lhun_check(ask):
   digits = [int(digit) for digit in str(ask)] 
   digits.reverse()
   
   for i in range (len(digits)):
      if i % 2 == 1:
         digits[i] *= 2
         if digits[i] > 9:
            digits[i] -= 9
   total_sum = sum(digits)
   return total_sum % 10 == 0
            

ask = input("Enter your sixteen digit card number: ")
sanitized_numbers = sanitize_input(ask)
if valid_card_number(sanitized_numbers):
    if lhun_check(sanitized_numbers):
        print("The card number is valid")
    else:
        print("The card number is invalid")
else:
    print("Invalid card format.")
   
