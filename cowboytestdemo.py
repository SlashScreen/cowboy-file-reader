import readcowboy

x = (input("file: ")).lower();
dat = readcowboy.read(x)
o = (input("file: ")).lower();
readcowboy.write(o,"testdoc",dat)
