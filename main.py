from fun import count_vowels, reverse_string, is_palindrome
def main():
    gn_string = input("Enter a string: ")
    vowels = count_vowels(gn_string)
    print(f"'{gn_string}' has {vowels} vowels.")
    reversed_str = reverse_string(gn_string)
    print(f"Reverse : '{gn_string}' - '{reversed_str}'.")
    if is_palindrome(gn_string):
        print(f"'{gn_string}' is a palindrome!")
    else:
        print(f"'{gn_string}' is not a palindrome.")
if __name__ == "__main__":
    main()
