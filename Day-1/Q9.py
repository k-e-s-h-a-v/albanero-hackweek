def stonks(priceArr):
    profit = 0
    for i in range(1,len(priceArr)):
        if(priceArr[i] > priceArr[i-1]):
            profit += priceArr[i] - priceArr[i-1]
    return profit

# examples
examples=[[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]]
for i in examples:
    print('for',i,'profit =',stonks(i))
