from itertools import permutations

def is_possible(arr, s):
    # Create a set of all unique characters in the array of strings
    unique_chars = set(''.join(arr) + s)
    
    # Generate all possible mappings of characters to digits
    for mapping in permutations(range(10), len(unique_chars)):
        # Create a dictionary to store the mapping
        char_to_digit = {char: digit for char, digit in zip(unique_chars, mapping)}
        
        # Encode each string in the array using the mapping
        encoded_arr = [int(''.join(str(char_to_digit[char]) for char in string)) for string in arr]
        
        # Encode the target string using the mapping
        encoded_s = int(''.join(str(char_to_digit[char]) for char in s))
        
        # Check if the sum of the encoded strings is equal to the encoded target string
        if sum(encoded_arr) == encoded_s:
            return True
    
    return False

arr = ["SEND", "MORE"]
s = "MONEY"

if is_possible(arr, s):
    print("Yes")
else:
    print("No")
