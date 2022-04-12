from simplecrypt import decrypt

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()
    with open('passwords.txt', 'rb') as passwd:
        for line in passwd:
            try:
                output = decrypt(line.decode("utf-8"), encrypted)
            except :
                print(line.strip(), " - неправильный пароль")
            else:
                print(line.strip(), '- правильный пароль. Текст:', output.decode('utf8'))






















# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
#
# with open("passwords.txt", "rb") as x:
#
#     password = x.read()
#     print(password)
#     print(encrypted)
#     try:
#         for i in password.strip():
#             print(i)
#             plaintext = decrypt(i, encrypted)
#             print(plaintext.decode('utf8'))
#     except :
#         pass



#
# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
#
# with open("passwords.txt", "rb") as inp:
    # print(inp.read())
    # inp = inp.read()
    # print(inp.decode("utf-8"))
    # print(encrypted)
    # pwds = [s.decode("utf-8") for s in inp.read().split()]
    # for s in inp:
    #     print(s)
    # print(pwds)
    # for pwd in pwds:
    #     print(pwd)
    #     try:
            # print('Succesfully: ' + decrypt(pwd, encrypted).decode('utf8'))
            # break
        # except:
            # print('Password ' + pwd + ' didnt match')