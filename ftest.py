f = open('dummy.txt', 'r')
for i in f:
    print(i, end = '')
f.close()
f = open('dummy.txt', 'a')
f.write('text added by program')
f.write('text added by program2')
f.close()
f = open('dummy.txt', 'r')
for i in f:
    print(i, end = '')
f.close()
