'''
for i in range(11):
    print(i)
'''
'''
i=0
while (i<11):
    print(i)
    i+=1
'''
'''
for i in range(21):
    if i%2==0:
        print(i)
'''
'''
for i in range(21):
    if i%2!=0:
        print(i)
'''
'''
for i in range(10,0,-1):
    print(i)
'''
'''
for i in range (11):
    print(i)
'''
'''
n=int(input())
fact=1
for i in range (1,n+1):
    fact=fact*i
print(fact)
'''
'''
n=int(input())
for i in range (11):
    print(f'{n}*{i}={n*i}')
'''

'''
s='123459'
length=0
for i in s:
    length+=1
print(length)
'''
n=1234
s=False
fs=0
if n<0:
     s=True
while(n!=0):
    mv=n%10
    n=n//10
    if n==0:
         fs=fs+(mv*(10**0))
    else:
         fs=fs+(mv*(10**(len(str(n)))))
    print(mv,n,fs,10**(len(str(n))))
if s:
     print(-1*fs)
else:
     print(fs)

