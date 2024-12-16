with open("input") as file:
    text = file.read()
    open_pointer = -1
    open_spaces = []
    files = []
    isFile = True
    fileId = 0
    firstOpenPosition = -1
    j = 0
    for x in list(text):
        if x != "\n":
            x = int(x)
            for i in range(x):
                if isFile:
                    files.append(fileId)
                    lastFilePosition = j
                else:
                    files.append(None)
                    if firstOpenPosition == -1:
                        firstOpenPosition = j
                j += 1
            if isFile:
                fileId+=1
            isFile = not isFile
    
    while lastFilePosition > firstOpenPosition:
        files[firstOpenPosition] = files[lastFilePosition]
        files[lastFilePosition] = None
        while True:
            x = files[firstOpenPosition]
            if x != None:
                firstOpenPosition+=1
            else:
                break
        while True:
            x = files[lastFilePosition]
            if x == None:
                lastFilePosition-=1
            else:
                break
    result = 0
    for i in range(len(files)):
        x = files[i]
        if x != None:
            result += x*i
    print(result)