class StringClass:
    def __init__(self):
        self.myString = ""

    def get_String(self):
        self.myString = input("Enter string: ")

    def print_String(self):
        print("Uppercase string:", end=" ")
        print(self.myString.upper())


str = StringClass()
str.get_String()
str.print_String()
