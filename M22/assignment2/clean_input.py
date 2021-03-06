'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    """clean"""
    regex = re.compile("[^a-z,0-9]")
    return regex.sub("", string)
def main():
    """call function"""

    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
