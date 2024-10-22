import numpy as np 
from neutrons import neutrons,diffusion
import matplotlib.pyplot as plt

#################################################################################################
#Question 8.3

def Counts(L): #Function counts the amount of neutrons in rod of length L
    a=1.7 # Mean free path for neutron to bounce off of nucleus
    b=21 # Mean free path for neutron to hit a nucleus and cause fission
    RMS=(2*a*b)**(1/2) # Average distance from starting point to fission
    ncount=0 # Count of Neutrons in rod

    for i in range(100): # Generates 100 initial fissions
        initial=L*np.random.random() # Location of initial fission along rod
        for j in range(neutrons()): # Secondary neutrons produced using value from neutrons()
            direction = np.random.random() #Outputs a value from 0 to 1 
            if direction >0.5: # If direction is greater than 0.5 neutron moves right
                location = initial + RMS
            else: # If direction is less than 0.5 neutron moves left
                location = initial - RMS
            if 0<location<L: # If neutron is in rod, it is added to total count
                ncount += 1
    return(ncount)
           
Larr=np.arange(10,100,0.01) # Stores the values of rod length (x axis)
narr=[] # Stores count
crit=[] # Stores values of rod length at count = 100

for i in np.arange(10,100,0.01): # Works out the count for specified range starting from 10cm
    Count=Counts(i)
    narr.append(Count)
    if Count==100:
        crit.append(i) # If counts are at 100, the rod length is noted
 
plt.figure(dpi=500,figsize=[12,8])    
plt.scatter(Larr,narr,s=5,color='k') 
plt.title('Counts as Rod Length Increases')   
plt.xlabel('Rod Length (cm)')
plt.ylabel('Counts')
plt.savefig('Bonus 8_3')

critvalue=np.mean(crit) #Calculates Critical Value by taking mean of rod length at 100 counts
print('8.3')
print('Rod Length (cm) at 100 Counts (Critical Value) =',critvalue)
print('At 100 Counts ',np.min(crit),'< L(cm) <',np.max(crit))


#################################################################################################
#Question 8.5

def Counts3D(L):

    a=1.7 # Mean free path for neutron to bounce off of nucleus
    b=21 # Mean free path for neutron to hit a nucleus and cause fission
    RMS=(2*a*b)**(1/2) # Average distance from starting point to fission
    ncount=0 # Count of Neutrons in Cube

    for i in range(100):
        xi=L*np.random.random() # Location of initial x fission
        yi=L*np.random.random() # Location of initial y fission
        zi=L*np.random.random() # Location of initial z fission
        s=diffusion()*RMS # Probability to diffuse distance s scaled by RMS
        for j in range(neutrons()): # Secondary neutrons produced using value from neutrons()
            direction = np.random.random() #Outputs a value from 0 to 1 
            phi = 2.0*np.pi*np.random.random () #Defines angle phi
            theta = np.arccos(2.0*np.random.random()-1.0) #Defines angle theta
            if direction >0.5:# If direction is greater than 0.5 neutron moves right
                x = xi + s*np.sin(theta)*np.cos(phi)
                y = yi + s*np.sin(theta)*np.sin(phi)
                z = zi + s*np.cos(theta)
            else: # If direction is less than 0.5 neutron moves left
                x = xi - s*np.sin(theta)*np.cos(phi)
                y = yi - s*np.sin(theta)*np.sin(phi)
                z = zi - s*np.cos(theta)
            if 0<x<L and 0<y<L and 0<z<L: # If neutron is in cube, it is added to total count
                ncount += 1
    return(ncount) #Returns final Count
           
Larr=np.arange(10,60,0.01)  # Stores the values of Side Length 
narr=[]# Stores count
crit=[] # Stores values of rod length at count = 100

for i in np.arange(10,60,0.01): # Works out the count for specified range starting from 10cm
    Count=Counts3D(i)
    narr.append(Count)
    if Count==100:
        crit.append(i) # If counts are at 100, the rod length is noted
 
plt.figure(dpi=500,figsize=[12,8])    
plt.scatter(Larr,narr,s=5,color='k') 
plt.title('Counts as Side Length Increases (3D) ')   
plt.xlabel('Side Length (cm)')
plt.ylabel('Counts')
plt.savefig('Bonus 8_5')
critvalue=np.mean(crit) #Calculates Critical Value by taking mean of side length at 100 counts
print('')
print('8.5')
print('Side Length (cm) at 100 Counts =',np.mean(crit))
print('At 100 Counts ',np.min(crit),'< L(cm) <',np.max(crit))

#Calculates the mass
length=critvalue*(10**-2) #cm to m
vol=length**3
density = 18700 #18.7 Mg to kg
mass=density*vol
print('')
print('Mass of Cube = ',mass,'kg')
