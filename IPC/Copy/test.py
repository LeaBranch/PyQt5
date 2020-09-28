import sys, os, time, math

name = sys.argv[1]
fdr = open(name, "r")
size = os.path.getsize(name)
onePer = size / 100
newOnePer = math.ceil(onePer) 

new_name = name.split('.')
fin_name=new_name[0] + "(1)." + new_name[1]
fdw = open(fin_name, "w")

count = 0
while(count < size):
    text = fdr.read(newOnePer)
    fdw.write(text)
    count = count + 1

fdr.close()
fdw.close()