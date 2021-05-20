import matplotlib.pyplot as plt
on = True
investments=[]
investmentRates=[]
timeAxis=[]
def findAndGraphInvestments(worth, rate, time,additionalMoneyPerYear):
  xAxisTemp=[]
  yAxisTemp=[]
  for i in range(time):
    xAxisTemp.append(i+1)
    worth+= additionalMoneyPerYear
    worth = worth*rate
    yAxisTemp.append(worth)
  return xAxisTemp,yAxisTemp

if __name__ == "__main__":
  investmentAmt = int(input('How many investments do you want to compare?\n'))
  additionalMoneyPerYear = float(input('How much money do you plan to add to your investments per year?\n'))

  for i in range(investmentAmt):
    investmentWorth = float(input(f'What is the worth of investment #{i+1}?\n'))
    investments.append(investmentWorth)
    i = []
  investmentTime = int(input('How many years do you want to put your money in for?\n'))

  for i in range(investmentAmt):
    investmentRate = (float(input(f'What percent is the interest rate for investment {i+1}?\n')))
    investmentRates.append((investmentRate/100)+1)

  for i in range(investmentAmt):
    xAxisTemp, yAxisTemp = findAndGraphInvestments(investments[i], investmentRates[i], investmentTime,additionalMoneyPerYear) 
    plt.xlabel('Time in years')
    plt.ylabel('Money')
    plt.title(f'Worth of {investmentAmt} investments over {investmentTime} years')
    plt.plot(xAxisTemp,yAxisTemp, label='Investment' + f' {i+1}')
    plt.legend(loc = 'upper left')
  plt.show()
