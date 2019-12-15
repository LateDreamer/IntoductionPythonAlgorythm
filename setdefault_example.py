def usual_dict(dict_data):
    """ dict[key] 사용 """
    newdata = {}
    for k, v in dict_data:
        if k in newdata:
            newdata[k].append(v)
        else:
            newdata[k] = [v]
    return newdata

def setdefault_dict(dict_data):
    """ setdefault() 메서드 사용 """
    newdata = {}
    for k,v in dict_data:
        newdata.setdefault(k,[]).append(v)
    return newdata

def test_setdef():
    dict_data = (("key1","value1"),
    ("key1","value2"),
    ("key2","value3"),
    ("key2","value4"),
    ("key2","value5"))
    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))

if __name__ == "__main__":
    test_setdef()