def str_copmpression(s):
    count, last = 0, ""
    list_aux = []
    for i , c in enumerate(s):
        #print(i,c)
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))
    return "".join(list_aux)

if __name__ == "__main__":
    result = str_copmpression("aabcccccaaa")
    print(result)