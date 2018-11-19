import dir2.dir1.A
#from dir2.dir1 import A

print(dir2.dir1.A.foo())
dir2.dir1.A.x = 7
print(dir2.dir1.A.foo())

