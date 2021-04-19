# Asian Option Pricing
In this method we calculate the call/put of an asian options using Monte Carlo simulation.

An Asian option is an option type where the payoff depends on the average price of the underlying asset over a certain period of time as opposed to standard options (American and European) where the payoff depends on the price of the underlying asset at a specific point in time (maturity). These options allow the buyer to purchase (or sell) the underlying asset at the average price instead of the spot price. Asian options are also known as average options. There are various ways to interpret the word “average,” and that needs to be specified in the options contract. Typically, the average price is a geometric or arithmetic average of the price of the underlying asset at discreet intervals, which are also specified in the options contract. Asian options have relatively low volatility due to the averaging mechanism. They are used by traders who are exposed to the underlying asset over some time, such as consumers and suppliers of commodities, etc. (https://www.investopedia.com/terms/a/asianoption.asp)

As Monte Carlo simulation is an approximation method it contains an error. That's the reason why we calculate the price of the Vanilla options using Monte Carlo simulation and Black and Scholes method so as to see the error between the the theoretical price and the simulated price. This error will be added in the Asian Options (call or put) price so as to be more precise 

Here you can find additional information about: 
Monte Carlo Simulations: https://www.investopedia.com/terms/m/montecarlosimulation.asp
Black and Scholes: https://www.investopedia.com/terms/b/blackscholes.asp

Here you can find an excel file to see exactly how this method works.
