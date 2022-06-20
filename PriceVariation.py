from web3 import Web3
from pycoingecko import CoinGeckoAPI
from matplotlib import pyplot as plt
import numpy as np
import datetime

#chainlink price extract
web3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/34ed41c4cf28406885f032930d670036')) # Change this to use your own Infura ID
abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
addr = '0x9326BFA02ADD2366b30bacB125260Af641031331'

contract = web3.eth.contract(address=addr, abi=abi) # Set up contract instance

i=0
RoundId = 36893488147419116354

diffArr=[]
dateArr=[]

while i<30 :
    validRoundId= RoundId-i*48
    historicalData = contract.functions.getRoundData(validRoundId).call()
    datestamp = datetime.datetime.fromtimestamp(historicalData[2]).strftime('%d-%m-%Y')

    #coingecko price extract
    cg = CoinGeckoAPI()
    data = cg.get_coin_history_by_id(id='ethereum',date=datestamp, localization='false')
    diff=(historicalData[1]/100000000)-(data['market_data']['current_price']['usd'])
    print(diff)
    print(datestamp)
    diffArr.append(diff)
    dateArr.append(datestamp)
    i += 1

xpoints = diffArr
ypoints = dateArr



plt.plot(ypoints, xpoints)
plt.xticks(rotation='vertical')
plt.show()







#coingecko price extract
#cg = CoinGeckoAPI()
#data = cg.get_coin_history_by_id(id='ethereum',date=datestamp, localization='false')
#print(data['market_data']['current_price']['usd'])
#print(datestamp)


