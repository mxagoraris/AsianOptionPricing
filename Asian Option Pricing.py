import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#function that calculates European's option price using
#Black and Scholes method 
def BlackScholesPrice (S,K,r,sigma,d,t,optionType):
    d1 = (np.log(S/K) + (r-d + np.power(sigma,2)/2)*t)/(sigma*np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    if optionType == "CALL" or optionType == "C":
        P =  S*stats.norm.cdf(d1) - K * np.exp(-(r-d)*t) * stats.norm.cdf(d2)
    else:
        P = K * np.exp(-(r-d)*t) * stats.norm.cdf(-d2) - S*stats.norm.cdf(-d1)
    return P

#call option price
vol = 0.2
r = 0.025
d = 0.01
t = 3/12
s0 = 11
k = 12

#we can read it, but for our calculations 
# we will just define it
#optionType = input("Give as the option type Call or Put: ").upper()

optionType1 = "Call"
optionType1 = optionType1.upper()

BSPriceCall = BlackScholesPrice(s0,k,r,vol,d,t,optionType1)

optionType2 = "Put"
optionType2 = optionType2.upper()

BSPricePut = BlackScholesPrice(s0,k,r,vol,d,t,optionType2)

#Now we will do a Monte Carlo simulation

npaths = 100000
nsteps = 1

#we create with a random number generator an array of elements which contains 
#npaths number using normal distribution 
h = np.random.randn(npaths,nsteps)

#in that step we normalize the mean and the variance using z score and 
#on the same time we make our distribution semetrical combining our random 
#paths and there opposites
h2 = stats.zscore(np.block([[h],[-h]]))

St = s0*np.exp((r-d-np.power(vol,2)/2)*t+vol*np.sqrt(t)*h2)
CallPayoff = np.maximum(St-k,0)
PutPayoff = np.maximum(k-St,0)
SimCallPrice = np.mean(CallPayoff) * np.exp(-r*t)
SimPutPrice = np.mean(PutPayoff) * np.exp(-r*t)

#In order to calculate our Asian option we need to find the error between
#our two methods. Asian Option price can be calculated only with a monte carlo
#simulation as it cannot be calculated using a conventional method


Call_error = BSPriceCall - SimCallPrice
Put_error = BSPricePut - SimPutPrice

npaths1 = 100000
nsteps1 = 3
dt = 1.0/12

h_a = stats.zscore(np.random.randn(npaths1,nsteps1))
st3d = np.zeros((npaths1,nsteps1),dtype = float)

#we define the first column with euler's equation
st3d[:,0] = s0*np.exp((r-d-np.power(vol,2)/2)*dt+vol*np.sqrt(dt)*h_a[:,0])
for i in range(2):
    st3d[:,i+1] = st3d[:,i] * np.exp((r-d-np.power(vol,2)/2)*dt+vol*np.sqrt(dt)*h_a[:,i+1])

Smean = st3d.mean(axis=1)
asian_call_payoffs = np.maximum(Smean-k, 0)
asian_call_price = asian_call_payoffs.mean()*np.exp(-r*t)
asian_put_payoffs = np.maximum(k-Smean,0)
asian_put_price = asian_put_payoffs.mean()*np.exp(-r*t)

print("Asian Call Price: ", asian_call_price+Call_error)
print("Asian Put Price: ", asian_put_price+Put_error)

print("Vanilla Put: ", BSPriceCall)
print("Vanilla Put: ", BSPricePut)










