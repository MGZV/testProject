def reverse():
    with open('dataset_24465_4.txt', 'r') as f:
        temp_tuple = tuple()
        f = f.readlines()
        for line in f:
            line = line.strip()
            print(line)
            temp_tuple = temp_tuple + (line,)
        print(temp_tuple)
        temp_tuple = temp_tuple[::-1]
        print(temp_tuple)
        with open('reply_24465_4', 'w') as ff:
            contents = '\n'.join(temp_tuple)
            ff.write(contents)
reverse()