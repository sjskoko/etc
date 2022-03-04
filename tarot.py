import numpy as np




def card_pick(num=1, shuffle=1):

    suit_list = ['wand', 'cup', 'sword', 'pentacle']
    minor_list = [str(i) for i in range(1, 11)] + ['page', 'knight', 'queen', 'king']

    result = [] 

    for i in range(num):
        for _ in range(shuffle):
            card = np.random.randint(0, 78)

        if card >= 22:
            sign = 'miner'
            suit = suit_list[(card-22)//14]
            card_number = minor_list[(card-22)%14]

            result.append(suit + '_' + card_number)
        else:
            
            result.append('major number ' + str(card))
    
    return result

card_pick(2, 39)