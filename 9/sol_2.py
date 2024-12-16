with open("input") as file:

    text = file.read()
    open_pointer = -1
    files = []
    isFile = True
    i = 0
    fileId = 0
    firstOpenPosition = 1
    noChange = 0
    for x in list(text):
        if x != "\n":
            x = int(x)
            if isFile:
                files.append((x, fileId))
                fileId += 1
                lastFilePosition = len(files)-1
            else:
                if x > 0:
                    files.append((x, None))
            isFile = not isFile
            i += 1
    while lastFilePosition > firstOpenPosition and noChange < len(files):
        #print(files, firstOpenPosition, lastFilePosition)
        noChange += 1
        size, fileId = files[lastFilePosition]
        for i in range(firstOpenPosition, lastFilePosition):
            size_space, fileIdSpace = files[i]
            if fileIdSpace is not None:
                continue
            #print(size_space, fileIdSpace, size, fileId)
            if size_space >= size:
                #print("Change")
                noChange = 0
                #print(lastFilePosition, i)
                #print("Before",files)
                files.insert(i, files[lastFilePosition])
                lastFilePosition += 1
                files[i + 1] = (size_space - size, None)
                if files[i+1][0] == 0:
                    files.pop(i+1)
                    lastFilePosition -= 1
                files[lastFilePosition] = (size, None)
                
                j = lastFilePosition+1
                while True:
                    #print("MErging", files)
                    if j < len(files):
                        openSpace, fileId = files[j]
                        if fileId is None:
                            #print("Adidng", openSpace, fileId)
                            files[lastFilePosition] = (files[lastFilePosition][0] + openSpace, None)
                            files.pop(j)
                        else:
                            break
                    else:
                        break
                #print("After", files)
                break
            else:
                continue
        if noChange != 0:
            lastFilePosition -=1
        while True:
            if firstOpenPosition >= 0 and firstOpenPosition < len(files):
                [_, fileId] = files[firstOpenPosition]
                if fileId is None:
                    break
                firstOpenPosition += 1
            else:
                break
        while True:
            if lastFilePosition >= 0:
                [_, fileId] = files[lastFilePosition]

                if fileId is not None:
                    break
                lastFilePosition -= 1
            else:
                break
    result = 0
    counter = 0
    for i in range(len(files)):
        size, fileId = files[i]
        for j in range(size):
            if fileId != None:
                result += counter * fileId
            counter += 1
    print(files)
    print(result)