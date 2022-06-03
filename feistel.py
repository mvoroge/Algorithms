ROUNDS = 64
KEY = 'vqwertrew'
my_text = 'Hello, world!'


def to_feistel(text):
    shifr_ = []
    key_pos = 0

    if len(text) % 2 != 0:
        text = text + ' '

    # Разделяем текст на блоки по 2 символа
    blocks = [text[i:i + 2] for i in range(0, len(text), 2)]

    for block in blocks:
        L, R = ord(block[0]), ord(block[1])
        end = 0
        for i in range(ROUNDS):
            K = ord(KEY[key_pos % len(KEY)])
            R, L = L, R ^ (L ^ K)
            key_pos += 1
            end = (chr(R) + chr(L))
        shifr_.append(end)
    return shifr_, key_pos


def de_feistel(shifr_text, key_pos):
    defshifr = []
    key_pos -= 1

    for s in shifr_text[::-1]:
        L, R = ord(s[0]), ord(s[1])
        end = 0
        for i in range(ROUNDS):
            K = ord(KEY[key_pos % len(KEY)])
            R, L = L, R ^ (L ^ K)
            key_pos -= 1
            end = (chr(L) + chr(R))
        defshifr.append(end)

    defshifr = ''.join(defshifr)[::-1]
    return defshifr


print('\nЗашифрованный текст:')
shifr, KEY_POS = to_feistel(my_text)
print(''.join(shifr))

print('\nРасшифрованный текст:')
old_text = de_feistel(shifr, KEY_POS)
print(old_text)
