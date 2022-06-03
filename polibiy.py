matrix = [['a', 'b', 'c', 'd', 'e'],
          ['f', 'g', 'h', 'i', 'k'],
          ['l', 'm', 'n', 'o', 'p'],
          ['q', 'r', 's', 't', 'u'],
          ['v', 'w', 'x', 'y', 'z'],
          ['!', '?', '*', '<', '>'],
          ]

matrixHeight = len(matrix)
matrixWidth = len(matrix[0])


def getCryptoChar(char, cipher=True):
    for indexHeight in range(0, matrixHeight):
        for indexWidth in range(0, matrixWidth):
            if char == matrix[indexHeight][indexWidth]:
                if (cipher == True):
                    return matrix[(indexHeight + 1) % matrixHeight][indexWidth]
                else:
                    return matrix[(indexHeight - 1) % matrixHeight][indexWidth]
    return char  # return input character, if not found


def encryption(message):
    newMessage = ""
    for messageIndex in range(0, len(message)):
        newMessage += getCryptoChar(message[messageIndex])
    return newMessage


def decryption(message):
    newMessage = ""
    for messageIndex in range(0, len(message)):
        newMessage += getCryptoChar(message[messageIndex], False)
    return newMessage


def main():
    message = input('input message: ')
    message = message.lower()
    print("Message is: " + message)

    cypherMessage = encryption(message)
    print("cypher message is: " + cypherMessage)

    decypherMessage = decryption(cypherMessage)
    print("decypher message is: " + decypherMessage)


if __name__ == "__main__":
    main()
