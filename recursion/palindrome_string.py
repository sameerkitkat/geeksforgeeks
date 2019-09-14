def palindromeString(word, start, end):
    if start == end:
        return True
    if start > end:
        return True
    if word[start] != word[end]:
        return False
    return palindromeString(word, start + 1, end - 1)


input_string = input("Enter string to check :")
print(palindromeString(input_string, 0, len(input_string) - 1))
