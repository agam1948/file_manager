import os
@staticmethod

def read(path):
    return open(path,'r').read()


def write(path,wtr):
    open(path,'w').write(wtr)


def add_to_file(path,wta):
    open(path,'w').write(read(path)+wtr)


def delete(path):
    os.system('del '+path)


def combine(path1,path2,path3):
    f1 = read(path1)
    f2 = read(path2)
    write(path3,f1+f2)
    
