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
        for i in range(len(lines)):
            line = lines[i].split('\n')
            entrycode = ''
            entryline = 0
            exitline = 0
            art = []
            if "###" in lines[i]:
                entrycode = str(lines[i]).replace('###','')
                entryline = i
                art.clear()
                #while not lines[i] == 'end':
                
            if not lines[i]=='end':
                print(lines[i])
                art.append(lines[i])#.join("\n")
                #print(art[i])
            elif lines[i]=='end':
                exitline = i
                #artData = list(art.values())
                print(art)
                #print(lines[entryline:exitline])
                data[entrycode] = art#lines[entryline:exitline]#str(entryline) + str(exitline)
 
        
        
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
        elif doctype == 'asciidata':
            newFile.write('{}'.format(keys[i]))
            newFile.write('\n')
            out = ''.join('{}\n'.format(str(values[i]))) #keys[i],
        else:
            out = ''.join('{}:{}'.format(keys[i],values[i]))
        newFile.write(out)
        newFile.write('\n')
    #print("Ding!")


#TODO
#Figure out how to run this from lua, with arguments, and be able to recieve output. not sure how to make diff. file types cooperate?
