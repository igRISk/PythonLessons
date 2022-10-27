# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

txt = input('Please enter some text: ')

def rle(text):
    text_rle = []
    char = text[0]
    s = 1
    for i in range(1, len(text)):
        if text[i] == char:
            s +=1
        else:
            text_rle.append([char, s])
            char = text[i]
            s = 1
    text_rle.append([char, s])
    return text_rle

def unpack(rle_text):
    unpacked_text =''
    for i in range(0, len(rle_text)):
        unpacked_text += rle_text[i][0] * int(rle_text[i][1])
    return unpacked_text

txt_compressed = rle(txt)
print(txt_compressed)

txt_unpacked = unpack(txt_compressed)
print(txt_unpacked)


## Способ 2:

def rle2(text):
    text_rle = ''
    char = text[0]
    s = 1
    for i in range(1, len(text)):
        if text[i] == char:
            s +=1
        else:
            if s == 1:
                text_rle += char
            else:
                text_rle += str(s) + char
            char = text[i]
            s = 1
    if s == 1:
        text_rle += char
    else:
        text_rle += str(s) + char  
    return text_rle

def unpack2(rle_text):
    unpacked_text =''
    i = 0
    while i < len(rle_text):
        if rle_text[i].isdigit() and i < len(rle_text):
            unpacked_text += int(rle_text[i]) * rle_text[i+1]
            i += 1 
        else:
            unpacked_text += rle_text[i]
        i += 1
    return unpacked_text

txt_compressed2 = rle2(txt)
print(f'\n{txt_compressed2}')

txt_unpacked2 = unpack2(txt_compressed2)
print(txt_unpacked2)