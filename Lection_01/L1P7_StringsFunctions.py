text = 'съешь еще этих мягких французских булО!к'
print(len(text))                        # 39
print('еще' in text)                    # True
print(text.isdigit())                   # False
print(text.islower())                   # True
print(text.replace('еще','ЕЩЁ'))        #
print(text[0])                          # с
print(text[len(text)-2:])               # !к
print(text[-6])                         # б
print(text[6:-18])                      # еще этих мягких
print(text[0:len(text):6])              # сеикакл
print(text[::6])                        # сеикакл

# print()
# for c in text:
#     print(c)

# print()
# help(text.istitle) 