from pathlib import Path

def sjoin(list):
    string = ''
    for i in range(len(list)):
        string = string.join(list[i])
    return string

def read(path):
    path = Path(path + '.cowboy')

    if not path.is_file():
        print("ERROR: File not found!")
        quit()

    with open(path) as f:
        file = f.read().splitlines()
        filetype = file[0] #sammy also wrote these 5
        lines = file[1:]

    
    #print(filetype)
    #print(lines)
        
    data = {}

    def isFloat(string): #not my code btw
        try:
            float(string)
            return True
        except ValueError:
            return False

    if filetype == 'testdoc' or filetype == 'savegame' or filetype == 'datasheet' or filetype == 'config':
        for line in lines:
            line = line.split(':')
            for i in range(2):
                  line[i] = line[i].strip().lower()
                  if isFloat(line[i]):
                      line[i] = float(line[i])
            data[line[0]] = line[1] #by Sammy
    if filetype == 'text':
        for i in range(len(lines)):
            line = lines[i].split('\n')
            #print (line)
            data[i] = lines[i] 
    if filetype == 'asciidata':
        art = []
        for i in range(len(lines)):
            line = str(lines[i].split('\n'))
            line = line[:-2]
            line = line[2:]
 #           line = str(line)
            print (line)
            art.append(line)
            slicestart = 0
            sliceend = 0
            if "%start%" in line:
                slicestart = i
            if "%end%" in line:
                sliceend = i
                data[i] = lines[slicestart:sliceend]
                print(slicestart, sliceend)
            #print (line)
  
        
        
        #print(data)
            #print (line)
            #data[i] = lines[i] 
    #print(data)
    return data

def write(name, doctype, data):
    fileName = name
    newFile = open(name + '.cowboy',"w+")
    newFile.write(doctype)
    newFile.write("\n")
    keys = list(data.keys())
    values = list(data.values())
    for i in range(len(data)):
        if doctype == 'text':
            out = ''.join('{}'.format(values[i]))
        else:
            out = ''.join('{}:{}'.format(keys[i],values[i]))
        newFile.write(out)
        newFile.write('\n')
    #print("Ding!")


#TODO
#Figure out how to run this from lua, with arguments, and be able to recieve output. not sure how to make diff. file types cooperate?
