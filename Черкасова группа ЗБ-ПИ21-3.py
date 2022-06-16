
def fact(x):
    if (x==1 or x==0) :
        return 1
    else:
         return x*fact(x-1)
#print('Введите x')
#x=int(input())
#print(fact(x))

def filter_even(li):
    list1=list(filter(lambda x: x%2==0,li))
    return list1
s=[10,2,37,45,88,90,45379,678]
#print(filter_even(s))

def square(li):
    list1=list(map(int,li))
    list2=list(map(lambda x: x*x,list1))
    return list2
s=['1','2','40','80','16','9']
#print(square(s))

def bin_search(li,element):
    index=-1
    for i in range(len(li)):
        if li[i]==element:
            index=i
            return index
    if index==-1:
        return -1
li=[1,6,17,28,56,90,106,345,5678,35670]
#print('Введите элемент, чтобы узнать его индекс')
element=int(input())
#print(bin_search(li,element))

def is_palindrome(string):
    s=''
    s1=''
    string=string.upper()
    for i in string:
        if i.isalpha()==1:
            s+=i
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    if s==s1:
         a='YES'
    else:
         a='NO'
    return a
#print('Введите строку ')
#string=str(input())
#print(is_palindrome(string))

def calculate(path2file):
    f=open(path2file)
    d=path2file.readlines()
    s=''
    znak=''
    chislo1=''
    chislo2=''
    answer=''
    rezult=''
    for i in d:
        s+=i
    s=s.replace('\n','    ')
    s=s.split('    ')
    i=0
    while i+2<len(s):
        znak=s[i]
        chislo1=s[i+1]
        chislo2=s[i+2]
        i+=3  
        if znak=='+':
            answer=answer+str(int(chislo1)+int(chislo2))+','
        if znak=='-':
            answer=answer+str(int(chislo1)-int(chislo2))+','
        if znak=='*':
            answer=answer+str(int(chislo1)*int(chislo2))+','
        if znak=='**':
            answer=answer+str(int(chislo1)**int(chislo2))+','
        if znak=='//':
            answer=answer+str(int(chislo1)//int(chislo2))+','
        if znak=='%':
            answer+=str(int(chislo1)%int(chislo2))+','
    for i in range(len(answer)-1):
        rezult+=answer[i]   
    f.close()
    return rezult
#print(calculate(f))


def substring_slice(path2file_1,path2file_2):
    f1=open(path2file_1)
    f2=open(path2file_2)
    f1=f1.readlines()
    f2=f2.readlines()
    s=''
    end=''
    start=''
    i=0
    n=0
    stroka=''
    for j in f1:
        stroka+=j
    answer=''
    for k in f2:
        s+=k
    s=s.split()
    while i+1<len(s):
        start=int(s[i])
        end=int(s[i+1])+1
        i+=2     
        for j in range(len(f1)):
            if n==j:
                a=f1[j]
                for g in range(len(a)):
                    answer=answer+a[start:end]+' '
                    break                   
        n+=1      
    f1.close()
    f2.close()
    return answer


import json
def decode_ch(sting_of_elements):
    periodic_table=json.load(open('названия.json',encoding='utf-8'))
    s=sting_of_elements
    list1=[]
    answer=''
    for i in range(len(s)-1):
        if (s[i].isupper()==1 and s[i+1].islower()==1):
            list1.append(s[i:i+2])
        else:
            list1.append(s[i])
    if s[-1].isupper()==1:
        list1.append(s[-1])
    for i in list1:
        if i.islower()==1:
            list1.remove(i)
    for i in list1:
        answer+=periodic_table[i]
    return answer
s='NOTiFICaTiON'
#print(decode_ch(s))

import statistics
class Student:
    def __init__(self,name,surname,grades):
        self.name=name
        self.surname=surname
        self.fullname=name+' '+surname
        self.grades=grades
        self.a=0
        self.b=''
    def greeting(self):
        print('Hello, I am '+str(self.fullname))   
    def mean_grade(self):
        self.a=statistics.mean(self.grades)
        print('Среднее значение оценок равно '+str(self.a))
        self.is_otlichnik() 
    def is_otlichnik(self):
        if self.a >=4.5:
            return print('YES')
        else:
            return print('NO')
    def __add__(self,other):
        return self.name+' is friends with '+ other.name
    def __str__(self):
        return self.fullname
list1=[3,3,4,5,5,3,3]
list2=[4,5,5,5,5,5]
s1=Student('Дамир','Стоноров',list1)
s2=Student('Олег','Боярский',list2)
#print(s1)
s1.greeting()
s1.mean_grade()
#print()
#print(s2)
s2.greeting()
s2.mean_grade()
#print()
#print(s1+s2)
