def binary_search(lo,hi,condition):
    while lo<=hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1 
        else:
            lo = mid +1 

def locate_cards(cards, key):
    lo, hi = 0, len(cards)-1
    def condition(mid):
        if cards[mid] == key:
            if cards[mid+1] == key:
                return 'right'
            else:
                return 'found'
        elif cards[mid] <= key:
            return 'left'
        else:
            return 'right'
    return binary_search(lo,hi,condition)

def checkCard(card_array, key):
    min = count = 0
    max = len(card_array)-1
    while min <= max:
        mid = ((min+max)//2)
        if(card_array[mid]==key and card_array[mid-1] != key):
            return mid
        elif(card_array[mid]<=key):
            max = mid-1
        elif(card_array[mid]>=key):
            min = mid-1
        count += 1
    
    return -1


result = locate_cards([11,11,11,11, 11, 10, 7, 4,3,3, 3, 1, 0],11)
print(result) 