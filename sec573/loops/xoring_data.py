def xoring_strings(str1, str2):
    result = ""
    for index, a_char in enumerate(str2):
        result += chr(ord(str1[index]) ^ ord(a_char))
    return result

str1 = "Hello, World!"
str2 = "1234567890"

print(xoring_strings(str1, str2))