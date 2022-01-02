def namelist(names):
    s = ""
    if len(names) <= 0:
        return f""
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) >= 2:
        for key,name in enumerate(names):
            if key > (len(names) - 2):
                k = s[:-2]
                s = k + " & " + name['name']
            else:
                s = s + name['name'] + ", " 
#             print(key, s)
        return s