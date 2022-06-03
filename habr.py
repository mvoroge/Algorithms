key = [4643634, 1234125, 8975321, 6756421, 96874621, 5314123]

text = []

for __ in list(input('Введите сообщение: ')):
    text.append(ord(__))

print(f'Численное представление сообщения: {text}')

etext = []

__key = 0
for __ in range(0, len(text)):
    etext.append(text[__]+key[__key])
    if __key == len(key)-1:
        __key = 0
    else:
        __key += 1

print(f'Зашифрованный вид: {etext}')

unetext = []

__key = 0
for __ in range(0, len(etext)):
    unetext.append(chr(etext[__]-key[__key]))
    if __key == len(key)-1:
        __key = 0
    else:
        __key += 1

print(f'Расшифрованное сообщение: {unetext}')
