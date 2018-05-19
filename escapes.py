print("\\")
print("\'")
print('\"') # special characters escapes
print("one\aword") # does nothing
print("two\bwords") # backspace, removing the character on the left
print("three\fwords") # same as \n\t
print("four\nwords") # newline, same as pressing enter key
print("five_more\rwords")
# "words" have 5 characters, and \r will replace the first 5 characters
# replaces "five_" with "words"
print("six\twords") # same as pressing tab key
print("seven\vwords") # same as \f
