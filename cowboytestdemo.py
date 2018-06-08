import readcowboy

x = (input("file: ")).lower();
dat = readcowboy.read(x)
#print(dat)
o = (input("file to write: ")).lower();
t = (input("type: ")).lower();
readcowboy.write(o,t,dat)
