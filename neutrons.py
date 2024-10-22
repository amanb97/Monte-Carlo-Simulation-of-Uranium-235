from math import cos, log, pi, sqrt
from numpy import random

def neutrons():
    """Number of secondary neutrons produced in each fission.

    Returns an integer number of neutrons, with average 2.5."""
    i=int(random.normal()+3.0)
    if (i<0): return 0
    else: return i

def diffusion():
    """Distance diffused by a neutron before causing fission.

    Returns a random number with probability density p(s) =
    s^2 exp(-3s^2/R^2). This distribution has a mean of 1, so
    multiply by R to get the physical distance."""
    a=cos(2.0*pi*random.random())
    return sqrt(-0.667*(log(random.random())+log(random.random())*a*a))

