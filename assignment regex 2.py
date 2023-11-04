#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


#Question 1


# In[3]:


sample_text=  'Python Exercises, PHP exercises.'


# In[4]:


print(re.sub("[ ,.]",":",sample_text))


# In[5]:


#Question 2


# In[6]:


data={'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}


# In[7]:


df=pd.DataFrame(data)


# In[9]:


df


# In[11]:


df['SUMMARY']=df['SUMMARY'].str.replace('[^a-zA-Z\s]','',regex=True)
df


# In[12]:


#Question 3


# In[23]:


regex_pattern=re.compile(r"\b\w{4}\b")


# In[20]:


matches=regex_pattern.findall("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")


# In[24]:


print(matches)


# In[16]:


#Question 4


# In[22]:


regex_pattern1=re.compile(r"\b\w{3,5}\b")


# In[26]:


matches1=regex_pattern1.findall("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")


# In[27]:


print(matches1)


# In[28]:


#Question 5


# In[60]:


def funcrem(str):
    regex_pattern=re.compile(r'[()]')
    matches=regex_pattern.sub('',str)
    return matches
str="[example(.com), hr@fliprobo(.com), github(.com), Hello (Data Science World), Data (Scientist)]"


# In[61]:


matches1=funcrem(str)
print(matches1)


# In[62]:


#Question 6


# In[241]:


with open(r"C:\Users\Home\Desktop\sample.txt") as file:
     text=file.read()
print(text)
for line in file:
           matches=(re.sub(r'^\s+," ",line))
print(matches)


# In[106]:


#Question 7


# In[108]:


sample_text="ImportanceOfRegularExpressionsInPython"


# In[109]:


expected_output=re.findall('[A-Z][a-z]*',sample_text)


# In[110]:


print(expected_output)


# 

# In[114]:


#Question 8


# In[160]:


def func(str):
    pattern='(\d+)([A-Za-z]+)'
    matches=re.sub(pattern,r' \1 \2',str)
    return matches
sample_text="RegularExpression1IsAn2ImportantTopic3InPython"
expected_output=func(sample_text)
print(expected_output)


# In[147]:


#Question 9 


# In[264]:


def func(str):
    pattern='(?<=[a-z])([A-Z\d])'
    matches=re.sub(pattern,r' \1',str)
    return matches
sample_text="RegularExpression1IsAn2ImportantTopic3InPython"
expected_output=func(sample_text)
print(expected_output)


# In[146]:


#Question 10


# In[127]:


df=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')


# In[129]:


df


# In[130]:


df['first_five_letters']=df['Country'].str[:6]


# In[132]:


print(df.first_five_letters)


# In[133]:


#Quesion 11


# In[165]:


pattern=('\w*')
string1="abc00123xyz456_0%$"
string2="abc00123xyz456_0"
matches=re.match(pattern,string1)
print(matches)


# In[166]:


matches=re.match(pattern,string2)
print(matches)


# In[167]:


#Question 12


# In[182]:


pattern=(r'^9*')
str1="9 The place value of one’s, a number from 1 to 9."
matches=re.match(pattern,str1)
print(matches)


# In[183]:


#Question 13


# In[50]:


target_string="192.001.168.002"
result=re.sub(r'0',"",target_string)
print(result)


# In[43]:


#Question 14


# In[45]:


with open(r"C:\Users\Home\Desktop\sample3.txt") as file:
    text=file.read()
print(text)


# In[55]:


date_match=re.findall('August 15th 1947',text)
print(date_match)


# In[41]:


#Question 15


# In[42]:


sample_text="The quick brown fox jumps over the lazy dog."
pattern= ['fox','dog','horse']
for p in pattern:
    matches=re.search(p,sample_text)
    if(matches):
        print(matches)
    else:
        print("not found")


# In[384]:


#Question 16


# In[394]:


sample_text='The quick brown fox jumps over the lazy dog.'
pattern='fox'
matches=re.search(pattern,sample_text)
print(matches)
print(matches.start())


# In[57]:


#Question 17


# In[392]:


pattern="exercises"
sample_text='Python exercises, PHP exercises, C# exercises'
matches=re.search(pattern,sample_text)
print(matches)


# I GOT STUCK AT THIS CODE AND HENCE STARTED FROM 30th Q. I HAVE DONE ALL Q. PLEASE SEE BELOW. SINCE THIS IS MY STARTING , PLEASE EXCUSE ME THIS TIME. WILL KEEP THE MOTIVATION MORE NEXT TIME.

# In[56]:


#Question 30


# In[218]:


def funct(stri):
    pattern=re.compile(r'\b\w{2,4}\b')
    matches=pattern.sub(' ',stri)
    return matches
stri="[The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly.]"
expected=funct(stri)
print(expected)


# In[219]:


#Question 29


# In[234]:


pattern=r'\d{2}-\d{2}-\d{4}'
with open(r"C:\Users\Home\Desktop\sample1.txt") as file:
    text=file.read()
print(text)


# In[236]:


date_match=re.findall(pattern,text)

for date in date_match:
    print(date)


# In[242]:


#Question 28


# In[253]:


def funcremosplchar(str4):
    pattern4=re.compile(r'<U\+\w{4}>')
    
    matches4=pattern4.sub(' ',str4)
    return(matches4)
str4="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
print(funcremosplchar(str4))


# In[254]:


#Question 27


# In[263]:


pattern5=(r'#\w*')
str5=("""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo""")
matches5=re.findall(pattern5,str5)
for hashtag in matches5:
    print(hashtag)


# In[265]:


#Question 26


# In[270]:


pattern=(r".*[a-zA-z0-9]$")
str6="INdia is A beautiful country!"
str7="INDIA is a beautiful country123"
if re.match(pattern,str6):
    print("Matched")
else:
    print("Not Matched")
if re.match(pattern,str7):
    print("Matched")
else:
    print("Not Matched")


# In[271]:


#Question 25


# In[272]:


str8="Hello hello world world"
pattern=r'\b(\w+)(?:\W+\1\b)+'
matches8=re.sub(pattern,r'\1',str8)
print(matches8)


# In[273]:


#Question 24


# In[282]:


pattern=r'([A-Z]+[a-z]+)'
str9="CamelCase is Commonly used In Programming Languages.This is an ExampleOfCamelCase."
matches9=re.findall(pattern,str9)
print(matches9)


# In[283]:


#Question 23


# In[299]:


str4="RegularExpressionIsAnImportantTopicInPython"
x=re.findall(r'[A-Z][a-z]*',str4)
print(x)


# In[300]:


#Question 22


# In[302]:


sample_text="My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
x=re.findall('\d+',sample_text)
print(x)


# In[303]:


y=map(int,x)
print(max(y))


# In[304]:


#Question 21


# In[3]:



str11="Anna is 12 years old.She weighs 45 kgs and has 155 cms height. She has 2 pets."
for j in str11:
    matches=re.search(r'(\d+)',str11)
print(matches)
print(matches.start())


# In[325]:


#Question 20


# In[327]:


def funcdecimal(str12):
    pattern=re.compile(r'\b\d+\.\d{1,2}\b')
    x=re.findall(pattern,str12)
    return x
sample_text="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
expected_output=funcdecimal(sample_text)
print(expected_output)


# In[328]:


#Question 19


# In[338]:


def funcreversedt(str13):
    pattern=re.compile(r'(\d{4})-(\d{2})-(\d{2})')
    matches=pattern.sub("\\3-\\2-\\1",str13)
    return matches
str13= "2023-11-14"
print(funcreversedt(str13))


# In[339]:


#Question 18


# In[390]:


string=["An Amzing and powerful language is Phyton.","Phyton is user friendly."]
for j in string:
    y=re.search("Phyton",j)
    print(y)
    print(y.start(),"\n")

