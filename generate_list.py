# umbenennen aller Dateien
# v1.0 oktober 2015


from glob import glob
import os

dirname = "letters/"
imgfiles = glob(dirname + "*.png")
imgfiles.extend(glob(dirname + '*.jpg'))
imgfiles.extend(glob(dirname + '*.jpeg'))

imgfiles.sort()

print(  "b = new Array(" )

i = 1
for f in imgfiles:
	f = f.replace("\\", "/" )
	if i < len(imgfiles ) :
		print(  "\"" + f + "\", " )
	else:
		print( "\"" + f + "\"")
	i = i + 1
 
print( " );" );

