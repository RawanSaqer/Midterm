


### 1) Write Python code to generate the following sequnece of numbers without loop:
[ 2  4  6  8 10 12 14 16 18]

## write your code here ()
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] 
  
# use anonymous function to filter and comparing  

res1=list(filter(lambda x:x%2==0,my_list))

  
# printing the result 
print(res1) 


### 2) In one line of code, write a code to check if 7 is exist in the following list:


lst100=[4,20, 4, 5, 7]
f= 7 in lst100
print(f)
lst101=[33,2, 4, 8, 10]
b= 7 in lst101
print(b)
## write your code here


### 3) Convert the following function into lambda function:

def myFun1(a,b):
    return a+b+10

# write your code here
add_=lambda a,b:a+b+10

### 4) Convert the following function into lambda function:


def myFun2(lst):
    res=[]
    for l in lst:
        res.append(l**3)
    return res


lst=[2,3,5,7]
print(myFun2(lst))
# write your code here

a=map(lambda x:x**3,lst)
print(list(a))


### 5) Convert the following function into list comprehension to get the same result:

def myFun3(lst):
    res=[]
    for i in lst:
        if i >=20:
            res.append(i)
        else:
            res.append(i+10)
    return res
lst1=[50,22,3,4,2]
print(myFun3(lst1))

## write your code here

squares_cubes = [i if i>=20 else i+10 for i in lst1]
 
print(squares_cubes)

### 6)	Create a square matrix randomly with size m x m, divide the matrix into blocks dxd and the maximum of each block shown in the Figure below: 

![Screen%20Shot%202020-10-29%20at%209.19.16%20AM.png](attachment:Screen%20Shot%202020-10-29%20at%209.19.16%20AM.png)

import numpy as np 
import threading
import time

def getMax(arr2D):
    
    assert arr2D.shape[0]==arr2D.shape[1], "arr must be square"
    assert arr2D.shape[0]%2 == 0, "arr size must divideable into equal n_sections"
   
    arr1 = np.array_split(arr2D,4)
     
    a_1 =np.amax(arr1[0])
    a_2 =np.amax(arr1[1])
    a_3 =np.amax(arr1[2])
    a_4 =np.amax(arr1[3])
    print(arr2D[0])
    print(arr2D[1])
    print(arr2D[2])
    print(arr2D[3])
    
    new_arr = [a_1,a_2,a_3,a_4]
    
   
    
    return new_arr
re = getMax(arr2D)
print(re)
arr2D = np.arange(16).reshape(4,4)    
Z=threading.Thread(target=getMax, args=(arr2D,)) 
Z.daemon = True
Z.start()
    
print(Z)

### 7) Define a class called covid_19_info that provides information about convId19 in some cities of Saudi Arabia.  The information includes (death, recovered, and infected). Your code must contain the following:
- Add_new_statistic() method, this method aims to add the convId19 info for given city if the city is added first time. 
- update_info()aims to update the info about the convId19 if the city is already exist in the list
- there is a variable is called risk_level which aims to provide the risk level for the city. The risk level is categorized into three levels as follows:
    - Green if the death<100 and infected < 500
    - Yellow if the death>500 and <1000 and infected <3000
    - Red if the death>1000 and infected >=3000
- risk_level must be updated automatically
- printInfo() aims to print the CovID-19 information for each city (city name, death, recovered, and infected). The cities are sorted descending based on the number of deaths. 



class covid_19_inf:
    pass
    ### write your code here 
cities=[]
tabuk=covid_19_inf('Tabuk')
wajh=covid_19_inf('Wajh')
duba=covid_19_inf('Duba')
haqil=covid_19_inf('Haqil')
cities=[tabuk, wajh, duba, hqil]
### write your code here

class covid_19_inf:
    cities=[]
     
    
    
    def __init__(self, city, deth, infected, heal):
        
        self.city = city
        self.deth = deth
        self.infected = infected
        self.heal = heal
        
        covid_19_inf.cities.append(self)
        
        
    def update_info(self,city):
        for i in range(len(cities)):
            if cities[i]==city:
                
                deth_number  =input("number of deth")
                deth = int(deth_number)
                infe_number  =input("number of infected ")
                infected = int(infe_number)
                heal_number  =input("number of recovered")
                heal = int(heal_number)
                if deth<100 and infected <500:
                    risk = "Green"
                elif deth >500 and 1000> infected <3000 :
                    risk = "Yellow"
                elif deth >1000 and infected >=3000:
                    risk = "Red"
        cities.appened(covid_19_inf(city, deth, infrcted, heal, risk))
        sorted(cities, key=lambda cities: cities[1])
        
            
        
        
        
       
        
        
    def statics_inf(self, city, deth, infected, heal,risk):
        if city in cities :
            self.update_info(city);
        else:
            city = input("enter city name")
            deth_number  =input("number of deth")
            deth = int(deth_number)
            infe_number  =input("number of infected ")
            infected = int(infe_number)
            heal_number  =input("number of recovered")
            heal = int(heal_number)
            if deth<100 and infected <500:
                risk = "Green"
            elif deth >500 and 1000> infected <3000 :
                risk = "Yellow"
            elif deth >1000 and infected >=3000:
                risk = "Red"
        cities.appened(covid_19_inf(city, deth, infrcted, heal, risk))
        sorted(cities, key=lambda cities: cities[1])
    
    def prin_info(self,city,deth,infected,heal):
        print(self.city, self.deth, self.infected, self.heal)
           

            
            
            
tabuk = covid_19_inf("Tabuk", 50, 500,350)
s =tabuk.prin_info("Tabuk", 50, 500,350)
print(s)
wajh = covid_19_inf("Wajh", 250, 30000,3520)
duba = covid_19_inf("Duba", 250, 30000,3520)


length = len(covid_19_inf.cities)
i = 0
while i<length:
    print(covid_19_inf.cities[i]) 
    i+=1
    

