# MonteCarloMod

# Notes re: building predictive model for stock price
- assumption: ex. is similar to stock price?!

## Background 
- formula that model random movment
- "Brownian Movement"

Drift + Random Stochastic Variable 

Today's Price = Yesterday's Price * e**r

- Drift is expected rate of return
-  i.e. The rate with greatest odds of occurring
Standard Monte Carlo use average of the historical periodical daily returns 

Average of hist periodical daily return - (variance /2)

## Central Limit Theorum
-if we graph enough periodical daily return of an asset, the graph should form normal distribution 
- r = according to CLT, should be normally distributed
- i.e. Rates of daily change in the future will also be normally distributed 

Amount change in price = Fixed Drift Rate + Random Stochastic Variable

## IN Excel 

NORMSINV(Percent) = z score 
e.g. NORMSINV(.95) =1.645 standard deviation above the mean

NORMSINV(Random())

