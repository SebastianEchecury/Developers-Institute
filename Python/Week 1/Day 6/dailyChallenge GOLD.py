alphabet = [chr(x) for x in range(97, 123)]
message = input("Enter a message: ")
leftShift = int(input("Enter quantity of left shifts: "))

messageList = list(message)

op = input("Decrypt (1) Encrypt (2): ")

if op == "1":
    for idx, x in enumerate(messageList):
        if x != ' ':
            pos = alphabet.index(x)
            if pos + leftShift >= len(alphabet)-1:
                posAux = pos + leftShift - len(alphabet)
            else: posAux = pos + leftShift
            messageList[idx] = alphabet[posAux]
    print("Mensaje Desencriptado:\n{}".format(''.join(messageList)))
elif op == "2":
    for idx, x in enumerate(messageList):
        if x != ' ':
            pos = alphabet.index(x)
            messageList[idx] = alphabet[pos - leftShift]
    print("Mensaje Encriptado:\n{}".format(''.join(messageList)))



