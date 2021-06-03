import os
from shutil import copyfile
folder = input('Enter the name of directory: ')
os.mkdir(folder)
src = '../../cp-templates/template.py'
dst = folder + '/problem'
for i in range(1,4):
    dst1 = dst + str(i) +'.py'
    copyfile(src, dst1)
f = open(folder+'/input.txt', 'w')
f.close()