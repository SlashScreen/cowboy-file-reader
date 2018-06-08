from pathlib import Path

def read(path):
    path = Path(path + '.cowboy')

    if not path.is_file():
        print("ERROR: File not found!")
        quit()

    with open(path) as f:
        file = f.read().splitlines()
        filetype = file[0] #sammy also wrote these 5
        lines = file[1:]

    print(filetype)
    print(lines)
        
    data = {}

    def isFloat(string): #not my code btw
        try:
            float(string)
            return True
        except ValueError:
            return False

    if filetype == 'testdoc' or filetype == 'savegame': #handling for testdoc type
        for line in lines:
            line = line.split(':')
            for i in range(2):
                  line[i] = line[i].strip().lower()
                  if isFloat(line[i]):
                      line[i] = float(line[i])
            data[line[0]] = line[1] #by Sammy
    if filetype == 'text':
        data = lines
    print(data)
    return data

def write(name, doctype, data):
    fileName = name
    newFile = open(name + '.cowboy',"w+")
    newFile.write(doctype)
    newFile.write("\n")
    keys = list(data.keys())
    values = list(data.values())
    for i in range(len(data)):
        out = ''.join('{}:{}'.format(keys[i],values[i]))
        newFile.write(out)
        newFile.write('\n')
    print("Ding!")


#TODO
#Make type handling for savegame, config
#Figure out how to run this from lua, with arguments, and be able to recieve output. not sure how to make diff. file types cooperate?
