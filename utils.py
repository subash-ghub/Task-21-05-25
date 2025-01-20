def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
def reverse_string(input_string):
    return input_string[::-1]
def is_palindrome(input_string):
    cleaned_string = "".join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
