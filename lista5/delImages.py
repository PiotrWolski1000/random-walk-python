import os
def delImages():
    mydir =  os.getcwd()
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

delImages()