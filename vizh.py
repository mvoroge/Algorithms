def form_dict():
    d = {}
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for i in range(len(alphabet)):
        d[i] = alphabet[i]
    return d


def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value)
    return list_code


def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i, key[iter]]
        full += 1
        iter += 1
        if iter >= len_key:
            iter = 0
    return dic


def full_encode(value, key):
    dic = comparator(value, key)
    print('Полное кодирование: ', dic)
    encode_list = []
    d = form_dict()

    for v in dic:
        let_num = (dic[v][0] + dic[v][1]) % len(d)
        encode_list.append(let_num)
    return encode_list


def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value])
    return list_code


def full_decode(value, key):
    dic = comparator(value, key)
    print('Расшифровка: ', dic)
    d = form_dict()
    decode_list = []

    for v in dic:
        let_num = (dic[v][0] - dic[v][1] + len(d)) % len(d)
        decode_list.append(let_num)
    return decode_list


if __name__ == "__main__":
    word = 'СЛОВО'
    key = 'ЯБЛОКО'

    print('Слово: ' + word)
    print('Ключ: ' + key)

    key_encoded = encode_val(key)
    value_encoded = encode_val(word)

    print('Value= ', value_encoded)
    print('Key= ', key_encoded)

    shifre = full_encode(value_encoded, key_encoded)
    print('Шифр=', ''.join(decode_val(shifre)))

    decoded = full_decode(shifre, key_encoded)
    print('Decode list=', decoded)

    decode_word_list = decode_val(decoded)
    print('Word=', ''.join(decode_word_list))

    # decoded_111 = full_decode(decoded, key_encoded)
    # print('Decode list=', decoded_111)
    # decode_word_list_111 = decode_val(decoded_111)
    # print('Word=', ''.join(decode_word_list_111))
