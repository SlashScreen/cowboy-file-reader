# cowboy-file-reader
This is the read/writer for my filetype, .cowboy, I made as a multi-purpose sort of file I would use for config, dialog, savegame, etc.
The two .cowboy files are to test reading and writing

cowboytestdemo.py is a demonstration diece on how to use the module
readcowboy.py is the module itself, and doesn't do anything on its own

# Module Documentation

read(path)
reads the file specified at *path*. *The .cowboy extension is added at the end automatically.*
write(name,doctype,data)
writes to a new file, and creates one if there isn't one already there. 
*name* is the filename (again, automatically adds extension)
*doctype* is the document type. Refer to style guide.
*data* is an array or whatever of data that can be put into text form.

# .cowboy Style Guide
.cowboy files aren't super forgiving. it goes as follows:

document_type
dataA:1
dataB:Ralph
dataC:5.0

document_type: all lowercase, can be 1 of several types that are more or less handled differently: "testdoc", "savegame", "text"
data: this reads sorta like JSON, in that instead of an = there is a :, because it looks cooler. there are syntax requirements, however, that are listed below.
1. Each data point must be on a new line (no minification, sorry!)
2. Data points can be as far away from eachother as you like, as long as they are on the same line. Ex. "a    :      5.3"
3. Data point can only equal 1 value. you can't do "a:3:6" because it will ignore everything past the second colon.
4. Numbers are always detected and converted automatically to floats. Ex. "a:3" will be converted "a:3.0" either in memory when the file is read or in the file itself if it is writing.
