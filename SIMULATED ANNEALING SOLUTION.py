#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random, time

#Setting a global value for this in order to see how the order changes per iteration
global shuff_values1

#Creating a dictionary for the coordinates so that we can call key:value pairs
coordinates={"city1":[1,0] ,"city2":[2,0] ,"city3":[3,0],"city4": [4,0],"city5":[5,0],
             "city6":[6,0],"city7":[6,1],"city8":[6,2], "city9":[6,3], "city10":[5,3], 
             "city11":[4,3] , "city12":[3,3],"city13":[2,3],"city14":[1,3],"city15":[1,2]}

#Defining the sfuffling function that shuffles the list of coordinates
cords=[]
def shuff(a):
    global shuff_values1
    
    #Creating a list of all the coordinates
    for i in a.values():
        cords.append(i)

    #Shuffling the keys and coordinates for the initial search
    shuff_keys1=list(a.keys())
    shuff_values1=list(a.values())
    
    random.shuffle(shuff_values1)
    
    #Printing the routes that are created after every recursion
    print(shuff_values1)
    
    
  #Creating x and y coordinate lists for ease of calculation  
    xcords=[]
    ycords=[]
    for i in cords:
        xcords.append(i[0])
        ycords.append(i[1])


    return  xcords, ycords, shuff_keys1, shuff_values1

shuff(coordinates)


#Creating a function that calculates the distance between elements [0] and [1], and [0] and [2]
new_distances=[]
def distance(a):
    
    #Makes sure the whole list shuffles for each iteration so that we can just use the first 3 indices for random calculation of distance.
    shuff(a)
    
    #Getting the values of the first 3 elements of the shuffled values
    root=shuff_values1[0]
    first=shuff_values1[1]
    second=shuff_values1[2]
    
    #Calculating the distance between [0] and [1] and [0] and [2] to be compared in the next function
    dist1=((root[0]-first[0])**2 + (root[1]-first[1])**2)**0.5
    dist2=((root[0]-second[0])**2 + (root[1]-second[1])**2)**0.5
    

    swap (dist1,dist2,a)
           
    new_distances.append(new_distance)
    
    return dist1,dist2


def swap(x,y,a):

    
    T=1   #Initial 100% tolerance that will decrease with each iteration
    
    for root, first, second in distance(a):
        if x>y:#The total distance has increased from previous iteration
            delta=x-y #Finding the change in distance
            p=1/1+2.71828*((abs(delta))/T)  #Tolerance (annealing) function that gets stricter with each iteration
            
            '''if p>=0: #setting an arbitrary threshold that will become stricter with each iteration
                first,second=first,second  #Keeps the values of the cities
            
            else:
                first,second=second,first #Reorders the values of the cities'''
#Swapping the elements of the list if the bad swap is greater than the tolerance
            if p<=0:
                temp = first
                first = second
                second = temp
#Making tolerance stricter with every iteration            
        T=T-0.001
        p=p+0.001
#Calculating new distance and updating it      
        root1=shuff_values1[0]
        first1=shuff_values1[1]
        second1=shuff_values[2]
        
        dist3=sqrt((root1[0]-first1[0])**2 + (root1[1]-first1[1])**2)
        dist4=sqrt((root1[0]-second1[0])**2 + (root1[1]-second1[1])**2)
        new_dist=dist3+dist4
        
    return new_dist, shuff_keys1

dist1, dist2 = distance(coordinates)
current_time = time.time()

#Breaks the code's running after a certain time
while time.time() - current_time != 0:
    swap(dist1,dist2,coordinates)
    if True:
        break



#Gives the final route that 
def get_route(a):
    route=[]
    for i in shuff_values1:
        #Calling the city name
        route.append(a.getkeys[i])
    return route    
print(T)
print("Route to be followed",route)

get_route(coordinates)

