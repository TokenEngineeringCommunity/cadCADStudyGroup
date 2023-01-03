import matplotlib as mpl
import matplotlib.pyplot as plt
import math 
import random 
import numpy as np
import pandas as pd
from typing import List

ir: float #initial bootstrapped reserve
mcv: float #mcap vol token 
mcs: float #mcap stable token
r: float  #reserve asset variable
sv: float # supply of volatile token 
ss: float # supply of stable coin
pv: float #price of volatile token
ps: float #price of stable coin
deltaR: float
deltaSV: float
deltaSS: float
deltaPV: float
deltaPS: float
t: float #time state variable
choice: str
timesteps: List[float]


def initialize():
    global ir, mcv, mcs, r, sv, ss, pv, ps, deltaR, deltaSV, deltaSS, deltaPV, deltaPS, t, timesteps
    global rresult, svresult, ssresult, pvresult, psresult, deltaRresult, deltaSVresult, deltaSSresult
    global deltaPVresult, deltaPSresult, choice, choiceresult    
    
    ir = 1.0 
    mcv = 2*ir
    mcs= 0.5*ir 
    ss = mcs 
    sv = (2*(ss**0.5))**(0.5)
    pv = (2*sv)*(ss**(0.5))
    ps = (0.5*(sv**2))/(ss**(0.5))
    r = (sv**2) * (ss**(0.5))
    deltaR = 0
    deltaSV = 0 
    deltaSS = 0 
    deltaPV = 0 
    deltaPS = 0  
    t = 0
    choice = 'mintboth'
    timesteps = [t]
    rresult = [r]
    svresult = [sv]
    ssresult = [ss]
    pvresult = [pv]
    psresult = [ps]
    deltaRresult = [deltaR]
    deltaSVresult = [deltaSV] 
    deltaSSresult = [deltaSS] 
    deltaPVresult = [deltaPV] 
    deltaPSresult = [deltaPS]
    choiceresult = [choice]


def observe():
    global r, sv, ss, pv, ps, t, rresult, svresult, ssresult, pvresult, psresult, deltaR, deltaSV, deltaSS, deltaPV, deltaPS   
    global deltaRresult, deltaSVresult, deltaSSresult, deltaPVresult, deltaPSresult, timesteps, choice, choiceresult
    
    timesteps.append(t)
    rresult.append(r)
    svresult.append(sv)
    ssresult.append(ss)
    pvresult.append(pv)
    psresult.append(ps)
    deltaRresult.append(deltaR)
    deltaSVresult.append(deltaSV) 
    deltaSSresult.append(deltaSS) 
    deltaPVresult.append(deltaPV) 
    deltaPSresult.append(deltaPS)
    choiceresult.append(choice)

    

def update(randchoice):
    global r, sv, ss, pv, ps, t, deltaR, deltaSV, deltaSS, deltaPV, deltaPS, choice 
    
    choice = randchoice 
    
    if randchoice == 'mintboth':
        amount = random.uniform(0.1, r)
        newr = r + amount
        deltaR = newr - r
        r = newr
        mcx = 2*r
        mcy= 0.5*r 
        newss = mcy 
        newsv = (2*(newss**0.5))**(0.5)
        deltaSV = newsv - sv
        deltaSS = newss - ss 
        sv = newsv
        ss = newss
        newpv = (2*sv)*(ss**(0.5))
        newps = (0.5*(sv**2))/(ss**(0.5))
        deltaPV = newpv - pv
        deltaPS = newps - ps
        pv = newpv 
        ps = newps
        t = t + 1  

        
    if randchoice == 'sellV':
        amount = random.uniform(0.05, sv)
        newsv = sv - amount
        deltaSV = newsv - sv
        ss = ss
        deltaSS = 0
        newr = (newsv**2) * (ss**(0.5))     
        deltaR =  newr - r 
        r = newr
        newpv = (2*newsv)*(ss**(0.5))          
        newps = (0.5*(newsv**2))/(ss**(0.5))
        deltaPV = newpv - pv
        deltaPS = newps - ps
        pv = newpv
        ps = newps
        sv = newsv
        t = t + 1  
        
    if randchoice == 'mintV':
        amount = random.uniform(0.1, sv)
        newsv = sv + amount
        ss = ss
        deltaSV = newsv - sv
        deltaSS = 0
        newr = (newsv**2) * (ss**(0.5))
        deltaR = newr - r
        r = newr
        newpv = (2*newsv)*(ss**(0.5)) 
        newps = (0.5*(newsv**2))/(ss**(0.5))
        deltaPV = newpv - pv
        deltaPS = newps - ps
        pv = newpv
        ps = newps
        sv = newsv
        t = t + 1

    if randchoice == 'sellS':
        amount = random.uniform(0.1, ss)
        newss = ss - amount
        deltaSS = newss - ss
        sv = sv
        deltaSV = 0
        newr = (sv**2) * (newss**(0.5))     
        deltaR = newr - r 
        r = newr
        newpv = (2*sv)*(newss**(0.5))          
        newps = (0.5*(sv**2))/(newss**(0.5))
        deltaPV = newpv - pv
        deltaPS = newps - ps
        pv = newpv
        ps = newps
        ss = newss
        t = t + 1

    if randchoice == 'mintS':
        amount = random.uniform(0.1, ss)
        newss = ss + amount
        sv = sv
        deltaSS = newss - ss
        deltaSV = 0
        newr = (sv**2) * (newss**(0.5))
        deltaR = newr - r
        r = newr
        newpv = (2*sv)*(newss**(0.5)) 
        newps = (0.5*(sv**2))/(newss**(0.5))
        deltaPV = newpv - pv
        deltaPS = newps - ps
        pv = newpv
        ps = newps
        ss = newss
        t = t + 1    
        
    
    

def runSim():
    initialize()
    while t < 30:
        choices = ['mintV', 'sellV', 'mintboth', 'mintS', 'sellS'  ] 
        randchoice = random.choice(choices)
        update(randchoice)
        observe()
        
    reserve = pd.DataFrame(rresult)
    vsupply = pd.DataFrame(svresult)
    ssupply = pd.DataFrame(ssresult)
    vprice = pd.DataFrame(pvresult)
    sprice = pd.DataFrame(psresult)
    rchange = pd.DataFrame(deltaRresult)
    vchange = pd.DataFrame(deltaSVresult)
    schange = pd.DataFrame(deltaSSresult)
    pvchange = pd.DataFrame(deltaPVresult)
    pschange = pd.DataFrame(deltaPSresult)
    newchoice = pd.DataFrame(choiceresult)
    mergeddf = pd.concat([reserve, vsupply, ssupply, vprice, sprice, rchange, vchange, schange, pvchange, pschange, newchoice], axis = 1)
    mergeddf.columns = ['reserve', 'vol token supply', 'stable coin supply', 'vol token price', 'stable coin price', 'change in reserve', 
                        'change in vol token supply', 'change in stable coin supply', 'change in vol token price', 'change in stable coin price', 'type']
    
    mergeddf.to_csv('myfile.csv')
    return (mergeddf)



def showGraphs():
    plt.plot(psresult, 'b-')
    #plt.plot(yresult, 'g--')
    #plt.plot(xresult, yresult)
    #plt.show()

    
