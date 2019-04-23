def returnExt(filename):
    l = len(filename)
    ext = ""
    for i in range(l):
        if filename[i] == ".":
            for j in range(i+1,l):
                ext += filename[j]

    return ext

import os

# getting current working dir
cwd = os.getcwd()

# all files and folders present in cwd
files = os.listdir(cwd)

# initializing a dir
d = dict()

for file in files:
    if os.path.isdir(file):
        pass
    else:
        # getting file extension from file name
        ext = returnExt(file)
        try:
            d[ext].append(file)
        except KeyError:
            d[ext] = [file]

for key in d:
    try:
        path = cwd+"\\"+key
        # creating a new directory with extension name
        os.mkdir(path)
        for file in d[key]:
            oldloc = cwd+"\\"+file
            newloc = path+"\\"+file
            # moving file to newly created folder
            os.rename(oldloc, newloc)
    except FileExistsError:
        pass

files = os.listdir(cwd)
print(cwd," is neat and clean, with following folders")
for file in files:
    print(file)
