#Say "Hello, World!" With Python
print("Hello, World!")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)
    
#Python If-Else
if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2!=0: #odd
        print("Weird")
    else:
        if n>20:
            print("Not Weird")
        elif n>=6:
            print("Weird")
        else:
            print("Not Weird")
            
#Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)
        
#Loops
if __name__ == '__main__':
    n = int(raw_input())
    x=0
    while x<n:
        print(x*x) 
        x=x+1
        
#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:    
                leap=True
    return leap

year = int(raw_input())

#Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    s=""
    for i in range(1,n+1):
        s=s+str(i)
    print(s)

#List Comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    l=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
    print(l)
    
#Nested Lists
if __name__ == '__main__':
    
    l=[]
    mini=float("inf")
    num=1
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        l.append([name,score])
        if mini>score:
            mini=score
            num=1
        elif mini==score:
            num+=1
    
    l=sorted(l,key=lambda x: x[1])
    l=l[num:]
    min2=l[0][1]
    x=0
    name=[]
    while (x<len(l) and l[x][1]==min2 ):
        name.append(l[x][0])
        x+=1
    name.sort()
    for el in name:  
        print(el)  
        
#Finding the percentage
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    
    punteggio=student_marks[query_name]
    sum=0
    lenght=len(punteggio)
    for el in punteggio:
        sum+=el
    sum=sum/lenght
    print(format(sum, '.2f'))  
    
#Find the Runner-Up Score!    
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    mas=arr[-1]
    while n-1>=0 and arr[n-1]==mas:
        arr.pop()
        n-=1 
    print(arr[n-1])
    
#Lists
if __name__ == '__main__':
    list=[]
    x=0
    N = int(raw_input())
    while x<N:
        comando= str(raw_input())
        lista=comando.split()
        com=lista[0]
        valori=lista[1:]
        if com=="insert":
             list.insert(int(valori[0]),int(valori[1]))
        elif com=="print":
             print(list)
        elif(com=="remove"):
             list.remove(int(valori[0]))
        elif(com=="append"):
             list.append(int(valori[0]))
        elif(com=="sort"):
             list.sort()
        elif(com=="pop"):
             list.pop()
        elif(com=="reverse"):
             list.reverse()
        x+=1
        
#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print(hash(t))

#sWAP cASE
def swap_case(s):
    s=s.swapcase()
    return s

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
    
#String Split and Join
def split_and_join(line):
    # write your code here
    return "-".join(line.split())

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
    
#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first,last))

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
    
#Mutations
def mutate_string(string, position, character):
    string=string[0:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
    
#Find a string
def count_substring(string, sub_string):
    inizio=sub_string[0]
    add=True
    intero=0
    for char in range(0,len(string)):
        if string[char]==inizio and char+len(sub_string)-1<len(string):
            ck=1
            while ck<len(sub_string) and add:
                if string[char+ck]!=sub_string[ck]:
                    add=False
                ck+=1
            if add:
                intero+=1
            add=True
     
    return intero

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count

#String Validators
if __name__ == '__main__':
    s = raw_input()

isalnum=False
isalpha=False
isdigit=False
lower=False
upper=False
for char in s:
    if  not isalnum and char.isalnum() :
        isalnum=True
    if not isalpha and char.isalpha():
        isalpha=True
    if not isdigit and char.isdigit():
        isdigit=True
    if not lower and char.islower():
        lower=True
    if not upper and char.isupper():
        upper=True
        
print(isalnum)
print(isalpha)
print(isdigit)
print(lower)
print(upper)

#Text Wrap
import textwrap

def wrap(string, max_width):
    result=""
    numero=len(string)/max_width
    for i in range(0,round(numero)+1):
        result=result+string[i*max_width:(i+1)*max_width]+"\n"
    result=result[:-1]
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
#String Formatting
def print_formatted(number):
    # your code goes here
    lunghezza = len("{0:b}".format(number))
    for i in range(1,number+1):
        print ("{:{lar}d} {:{lar}o} {:{lar}X} {:{lar}b}".format(i,i,i,i, lar=lunghezza))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
#I have seen the discussions for this exercise
#n,m = map(int,input().split())  
for i in range(1,n,2): 
    print((i * ".|.").center(m, "-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,-1,-2): 
    print((i * ".|.").center(m, "-"))  


#Capitalize!    
def solve(s):
    l=s.split(" ")
    for pos in range(len(l)):
        l[pos]=l[pos].capitalize()
    stringa=" ".join(l)
    return stringa

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
  
# I have seen the discussions to overcome the time limit
#The Minion Game
def minion_game(string):
    # your code goes here
    Kcont=0
    Scont=0
    lung=len(string)
    for pos in range(len(string)):
        if string[pos] in "AEIOU":
            Kcont+=lung-pos
        else:
            Scont+=lung-pos
    if Scont>Kcont:
        print("Stuart {}".format(Scont))
    elif Kcont>Scont:
        print("Kevin {}".format(Kcont))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    cont=0
    l=[]
    sub=[]
    for el in range(len(string)):
        if cont==k-1:
            if not string[el] in sub:
                sub.append(string[el])
            l.append(sub)
            cont=0
            sub=[]
        else:
            if not string[el]  in sub:
                sub.append(string[el])
            cont+=1
    for el in l:
        print("".join(el))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
    

#Introduction to Sets
def average(array):
    # your code goes here
    insieme=set(array)
    mas=sum(insieme)
    return mas/len(insieme)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
#Symmetric Difference
if __name__ == '__main__':
    n1=int(input())
    l1=input().split()
    s1=set(l1)
    n2=int(input())
    l2=input().split()
    s2=set(l2)
    diff1=s1.difference(s2)
    diff2=s2.difference(s1)
    res=diff1.union(diff2)
    l=[]
    for el in list(res):
        l.append(int(el))
    l=sorted(l)
    for el in l:
        print(el)
        
#Set .add()
n=int(input())
s=set()
for row in range(n):
    nome=str(input())
    s.add(nome)
print(len(s))
   
#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
num=int(input())
for el in range(num):
    row=input().split()
    if len(row)>1:
        valore=int(row[1])
        if row[0]=="discard":
            s.discard(valore)
        else:
            s.remove(valore)
    else:
        s.pop()
somma=sum(s)
print(somma)

#Set .union() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
tot=s1.union(s2)
print(len(tot))

#Set .intersection() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
inter=s1.intersection(s2)
print(len(inter))

#Set .difference() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
print(len(s1-s2))

#Set .symmetric_difference() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
print(len(s1.symmetric_difference(s2)))

#Set Mutations
n1=int(input())
s1=set(map(int,input().split()))
righe=int(input())
for el in range(righe):
    comando=str(input().split()[0])
    s2=set(map(int,input().split()))
    if comando=="intersection_update":
        s1.intersection_update(s2)
    elif comando=="update":
        s1.update(s2)
    elif comando=="symmetric_difference_update":
        s1.symmetric_difference_update(s2)
    else:
        s1.difference_update(s2)
print(sum(s1))

#The Captain's Room
n1=int(input())
s1=list(map(int,input().split()))
in1=set()
in2=set()
for el in s1:
    if el not in in1:
        in1.add(el)
    elif el  in in1:
        in2.add(el)
res=in1-in2
print(res.pop())

#Check Subset
t=int(input())
for el in range(t):
    n1=int(input())
    s1=set(map(int,input().split()))
    n2=int(input())
    s2=set(map(int,input().split()))
    if len(s1-s2)==0:
        print(True)
    else:
        print(False)

#Check Strict Superset
s1=set(map(int,input().split()))
n1=int(input())
val=True
for el in range(n1):
    s2=set(map(int,input().split()))
    if len(s1-s2)>=1 and len(s2-s1)==0:
        val=True
    else:
        val=False
        break
print(val)

#No Idea!
n,m=input().split()
n=int(n)
m=int(m)
l=list(map(int,input().split()))
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
cont=0
for el in l:
    if el in s1:
        cont+=1
    elif el in s2:
        cont-=1
print(cont)

#collections.Counter()
from collections import Counter
n1=int(input())
c=Counter(map(int,input().split()))
n=int(input())
tot=0
for el in range(n):
    row=input().split()
    taglia,costo=row
    if c[int(taglia)]>0:
       tot+=int(costo)
       c[int(taglia)]=c[int(taglia)]-1 
print(tot)

#Collections.OrderedDict()
from collections import OrderedDict
n=int(input())
diz=OrderedDict()
for el in range(n):
    *item,costo=input().split()
    item=" ".join(item)
    if item not in diz:
        diz[item]=int(costo)
    else:
        diz[item]+=int(costo)
        
for item,costo in diz.items():
    print("{} {}".format(item,costo))

#Collections.namedtuple()
from collections import namedtuple
n=int(input())
head=input().split()
l=[]
for el in range(n):
    Point2= namedtuple("head",head)
    riga=input().split()
    s=Point2(riga[0],riga[1],riga[2],riga[3])
    l.append(s)
sum=0
for el in l:
    t=int(getattr(el,'MARKS'))
    sum+=t

print(sum/n)
    
    
#Word Order
n=int(input())
diz={}
distinct=n
for pos in range(n):
    word=input()
    if word not in diz.keys():
        diz[word]=(pos,1)
    else:
        distinct=distinct-1
        diz[word]=diz[word][0],diz[word][1]+1
print(distinct)
for el in sorted(diz.values(),key=lambda a: a[0]):
    print(el[1],end=" ")
    
#Collections.deque()
from collections import deque
d=deque()
n=int(input())
for el in range(n):
    commando=input().split()
    if len(commando)>1:
        if commando[0]=="appendleft":
            d.appendleft(commando[1])
        elif commando[0]=="append":
            d.append(commando[1])
    else:
        if commando[0]=="popleft":
            d.popleft()
        else:
            d.pop()            
print(" ".join(d))

#DefaultDict Tutorial
from collections import defaultdict
d = defaultdict(list)
n,m=map(int,input().split())
for el in range(n+m):
    stringa=input()
  
    if el<n:
        if stringa not in d:
            d[stringa].append(el+1)
        else:
            d[stringa].append(el+1)
    
    else:
        if stringa in d:
            for c in d[stringa]:
                print(c,end=" ")
            print()
        else:
            print(-1)
            
#Calendar Module
import calendar
mese,giorno,anno=map(int,input().split())
giorni= ['MONDAY', "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(giorni[calendar.weekday(anno, mese, giorno)])

#Exceptions
n=int(input())
for el in range(n):
    try:
        a,b=map(int,input().split())
        div=a//b
        print(div)
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e1:
        print("Error Code:",e1)

#Zipped!
n,x=map(int,input().split())
l=[]
for  el in range(x):
    row=map(float,input().split())
    l.append(row)

f=zip(*l)
for el in f:
    tot=sum(el)/len(el)
    print(tot)
    
#Athlete Sort   
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda x:x[k])
    for el in arr:
        print(*el,sep=" ")

#ginortS

stringa=input()
even=[]
odd=[]
lower=[]
upper=[]

for char in stringa:
    if char.isdigit() and int(char)%2==0:
        even.append(char)
    elif char.isdigit():
        odd.append(char)
    elif char.islower():
        lower.append(char)
    else:
        upper.append(char)
            
even.sort()
odd.sort()
lower.sort()
upper.sort()
finale=""

for el in [lower,upper,odd,even]:
    if el:
       finale=finale+"".join(el) 
print(finale)

#Map and Lambda Function
cube = lambda x:x*x*x # complete the lambda function x

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n>1:
        l=[0,1]
        for el in range(2,n):
            valore=l[el-1]+l[el-2]
            l.append(valore)
    return l

    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#Detect Floating Point Number
import re
reg='^[+-]?[0-9]*\.[0-9]+$'
    
n=int(input())
for _ in range(n):
    num=input() 
    if re.search(reg, num):
        print("True")
    elif not re.search(reg,num):
        print("False")

#Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(), Groups() & Groupdict()
import re
stringa=input()
m=re.search(r'(([0-9a-zA-Z]))\1+',stringa)
if (m):
    print(m.group(1))
else:
    print(-1)

#Re.findall() & Re.finditer()
import re
stringa=input()
l= re.findall(r'(?<=[^AEIOUaeiou])([aeiouAEIOU]{2,})[^AEIOUaeiou]',stringa)
if len(l)==0:
    print(-1)
else:
    for el in l:
        print(el)

#Validating phone numbers
import re
n=int(input())
for _ in range(n):
    m=re.match('[789]\d{9,9}$',input())
    if(m):
        print("YES")
    else:
        print("NO")

#Re.start() & Re.end()
import re
stringa=input()
k=input()
M=list(re.finditer('(?='+k+')',stringa))

if (M):
    for el in M:
        print("({}, {})".format(el.start(),el.end()+len(k)-1))
else :
    print("(-1, -1)")

#Validating and Parsing Email Addresses
import email.utils
import re
n=int(input())
for el in range(n):
    nome,email2=email.utils.parseaddr(input())
    m=re.match(r'[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',email2)
    if (m):
        print(email.utils.formataddr((nome, email2)))
        
#Hex Color Code
import re
n=int(input())
pattern=r'[\s:](#[0-9a-fA-Z]{6}[^\n]|#[0-9a-fA-Z]{3}[^\n])'
for num in range(n):
    stringa=input()
    l=re.findall(pattern,stringa)
    for el in l:
        if len(el)>=1:
            print(el[:-1])

#Regex Substitution
import re
n=int(input())
pattern='(\s[&]{2}\s)|(\s[|]{2}\s)'
for num in range(n):
    riga=input()
    fs=re.sub(pattern,lambda m: ' and ' if ' && '==m.group()  else ' or ',riga)
    fs=re.sub(pattern,lambda m: ' and ' if ' && '==m.group()  else ' or ',fs)
    
    if fs:
        print(fs)
    else:
        print(riga)

#Validating UID
import re
pattern1=".*[A-Z].*[A-Z].*"
pattern2=".*[0-9].*[0-9].*[0-9].*"
pattern3="[a-zA-Z0-9]{10}"
pattern4=r".*(.).*\1.*"
l=[pattern1,pattern2,pattern3,pattern4]
n=int(input())
check=True
for _ in range(n):
    stringa= input()
    for el in range(4):
        m=re.match(l[el],stringa)
        if (not m) and el!=3:
            check=False
        elif m and el==3:
            check=False
    if (check and len(stringa)==10):
        print("Valid")
    else:
        print("Invalid")
    check=True

#HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        self.attributi(attrs)
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        self.attributi(attrs)
    def attributi(self,attrs):
        for nome,valore in attrs:
            print("-> {} > {}".format(nome,valore))
n=int(input())
parser = MyHTMLParser()
t=""
for _ in range(n):
    t=t+input()
parser.feed(t)    

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
          print (">>> Multi-line Comment\n", data,sep="")
        else:
            print(">>> Single-line Comment\n",data,sep="")
    def handle_data(self, data):
        if data!="" and data!="\n":
            print (">>> Data\n", data,sep="")
 
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        self.attributi(attrs,tag)
    def attributi(self,attrs,tag):
        if tag=="object":
                for nome,valore in attrs:
                    if nome=="type":
                        print("-> {} > {}".format(nome,valore))
                    if nome=="data":
                        print("-> {} > {}".format(nome,valore))
                    if nome=="width":
                        print("-> {} > {}".format(nome,valore))
                    if nome=="height":
                        print("-> {} > {}".format(nome,valore))

        else:
            for nome,valore in attrs:
                print("-> {} > {}".format(nome,valore))
         
n=int(input())
parser = MyHTMLParser()
t=""
for _ in range(n):
    t=t+input()
t.strip()
parser.feed(t) 


#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    cont=0
    for child in node.iter():
        cont+=len(child.attrib)
    return cont

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr,float)
    a1=numpy.flipud(a) 
    return a1
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape
import numpy
line=input()
l=line.split()
array = numpy.array(l,int)
array.shape=(3,3)
print (array)

#Transpose and Flatten
import numpy
n,m=map(int,input().split())
m=[]
for _ in range(n):
    r=input().split()
    m.append(r)
a = numpy.array(m,int)
print(numpy.transpose(a))
print(a.flatten())

#Concatenate
import numpy
n,m,p=map(int,input().split())
l=[]
l1=[]
for pos in range(n+m):
    if pos<n :
        l.append(input().split())
    else:
        l1.append(input().split())
     
a = numpy.array(l,int)
a1 = numpy.array(l1,int)

print (numpy.concatenate((a, a1), 0))

#Zeros and Ones
import numpy
a=tuple(map(int,input().split()))
print(numpy.zeros(a, dtype = int))
print(numpy.ones(a, dtype =int))

#Eye and Identity
import numpy
numpy.set_printoptions(legacy="1.13")
n,m=map(int,input().split())
print(numpy.eye(n, m, k = 0)) 

#Array Mathematics
import numpy
n,m=map(int,input().split())
l=[]
l2=[]
for pos in range(2*n):
    if pos<n:
        l.append(list(map(int,input().split())))
    else:
        l2.append(list(map(int,input().split())))

l=numpy.array(l)
l2=numpy.array(l2)

print (numpy.add(l, l2))
print (numpy.subtract(l, l2))
print (numpy.multiply(l, l2))      
print (numpy.floor_divide(l,l2))
print (numpy.mod(l, l2)) 
print (numpy.power(l, l2)) 

#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy="1.13")
a=list(map(float,input().split()))
a=numpy.array(a)
print (numpy.floor(a))
print (numpy.ceil(a))
print (numpy.rint(a))

#Sum and Prod
import numpy
n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(input().split())

a=numpy.array(l,int)
print(numpy.prod(numpy.sum(a,0)))

#Min and Max
import numpy
n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(input().split())
a=numpy.array(l,int)
print(numpy.max(numpy.min(a,1)))

#Mean, Var, and Std
import numpy
n,m=map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
a=numpy.array(l)
print(numpy.mean(a,1))
print(numpy.var(a,0))
print(round(numpy.std(a),11))

#Dot and Cross
import numpy
n=int(input())
l=[]
l1=[]
for num in range(n*2):
    if num<n:
        l.append(input().split())
    else:
        l1.append(input().split())
        
l=numpy.array(l,int)
l1=numpy.array(l1,int)
print(numpy.dot(l,l1))


#Inner and Outer
import numpy
l=input().split()
l2=input().split()
l=numpy.array(l,int)
l2=numpy.array(l2,int)

print(numpy.inner(l,l2))
print(numpy.outer(l,l2))


#Polynomials
import numpy
l=input().split()
l=numpy.array(l,float)
x=int(input())
print(numpy.polyval(l,x))

#Linear Algebra
import numpy
n=int(input())
l=[]
for _ in range(n):
    l.append(input().split())
l=numpy.array(l,float)
print (round(numpy.linalg.det(l),2))




#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    cont=0
    max=0
    for el in candles:
        if max<el:
            max=el
            cont=1
        elif max==el:
            cont+=1
    return cont
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    
#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1<v2:
        slower=v1
        faster=v2
    else:
        slower=v2
        faster=v1
    if x1<x2:
        far=x1
        ahead=x2
    else:
        far=x2
        ahead=x1
    if (far==x1 and slower==v1):
        return "NO"
    if (far==x2 and slower==v2):
        return "NO"
    while far<ahead:
        far+=faster
        ahead+=slower
        if far==ahead:
            return "YES"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
    
#Viral Advertising
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    #creo array di tuple
    #ogni giorno faccio utilizzo il giorno precedente per calcolare
    a=[2]
    inizio=2
    for el in range(1,n):
        valore=math.floor(inizio*3/2)
        a.append(valore)
        inizio=valore
    return sum(a)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    n=str(n)
    tot=0
    for char in n:
        tot+=int(char)
    tot=tot*k
    tot=str(tot)
    cont=0
    while len(tot)!=1:
        for char in tot:
            cont+=int(char)
        tot=str(cont)
        cont=0
    return int(tot)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

    
#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    value=arr[n-1]
    index=n-2
    while index>=0:
        if arr[index]<value: 
            arr[index+1]=value
            print(*arr)
            break

        elif arr[index]>=value: 
            arr[index+1]=arr[index] 
            print(*arr)
        if index==0:
            arr[0]=value
            print(*arr)    
        index=index-1
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    
#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for pos in range(1,n): 
        value=arr[pos]
        x=pos-1
        while arr[x]>value and x>=0:
            arr[x+1]=arr[x]
            arr[x]=value
            x-=1
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
