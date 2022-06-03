alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
num_AB = {sym: i for sym, i in zip(alphabet, range(len(alphabet)))}
AB = {v: k for k, v in num_AB.items()}
N = 33
k = 16


def cipher(str_):
    ans = ''
    str_.lower()
    for s in str_:
        if s not in list(AB.values()):
            ans += s
        else:
            ans += AB[(num_AB[s] + k) % N]
    return ans


def decipher(str_):
    ans = ''
    str_ = str_.lower()
    for s in str_:
        if s not in list(AB.values()):
            ans += s
        else:
            ans += AB[(num_AB[s] - k) % N]
    return ans


method = 0
while True:
    try:
        method = int(input('Выберите, что хотите сделать. 1 - зашифровать, 2 - расшивровать: '))
    except:
        print('Не то, давай по новой \'1\' или \'2\'...')
        continue
    if method in (1, 2):
        break
    else:
        print('Не то, давай по новой \'1\' или \'2\'...')

while True:
    try:
        k = int(input('Ключ (целое число от 0 до 32): '))
    except:
        print('Не то, давай по новой...')
        continue
    if k in range(N):
        break
    else:
        print('Не то, давай по новой...')

word = input('Введите слово, с которым будем работать: ')
if method == 1:
    print('Ответ: ' + cipher(word))
else:
    print('Ответ: ' + decipher(word))

