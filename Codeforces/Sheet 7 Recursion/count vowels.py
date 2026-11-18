s=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
i=0
def fun(s,vowels,count,i):
    if i==len(s):
        return count
    if s[i] in vowels :
        count+=1
    i+=1
    return fun(s,vowels,count,i)

print(fun(s,vowels,count,i))