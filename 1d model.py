import numpy as np 
from neutrons import neutrons

L=100 # Length of rod (cm)
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
       if 0<location<L:# If neutron is in rod, it is added to total count
           ncount += 1
           
print('Number of neutrons in rod =',ncount)