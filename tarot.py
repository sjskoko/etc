import numpy as np

temp = []
for i in range(10000):
    temp.append(np.random.randint(0, 78))



def card_pick(num=1, seed=None):
    if seed:
        np.random.seed(seed)
    suit_list = ['wand', 'cup', 'sword', 'pentacle']
    minor_list = [str(i) for i in range(1, 11)] + ['page', 'knight', 'queen', 'king']

    result = [] 

    for i in range(num):
        card = np.random.randint(0, 78)

        if card >= 22:
            sign = 'miner'
            suit = suit_list[(card-22)//14]
            card_number = minor_list[(card-22)%14]

            result.append(suit + '_' + card_number)
        else:
            
            result.append('major number ' + str(card))
    
    return result


deck = sorted(set([card_pick() for _ in range(1000000)]))

card_pick()