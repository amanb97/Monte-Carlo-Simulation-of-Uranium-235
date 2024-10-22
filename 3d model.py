import numpy as np 
from neutrons import neutrons,diffusion

L=100 # Side Length of Cube (cm)
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
           
print('Number of neutrons in rod =',ncount)
