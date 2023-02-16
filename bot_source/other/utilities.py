import random

f = open("bot_source\other\Coin.txt", 'r', encoding='UTF-8')
coin = f.read().split('\n')
f.close()

f = open("bot_source\other\Predictions.txt", 'r', encoding='UTF-8')
prediction = f.read().split('\n')
f.close()

def get_coinflip_util():
    answer = random.choice(coin)
    return answer

def get_prediction_util():
    answer = random.choice(prediction)
    return answer