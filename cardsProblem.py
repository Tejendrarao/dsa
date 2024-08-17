def checkCard(card_array, key):

    min = count = 0
    max = len(card_array)-1
    first_mid = ((min+max)//2)
    while(count <= first_mid+1):
        mid = ((min+max)//2)
        if(mid != 0 and card_array[0]<key):
            if(card_array[mid]==key):
                return mid
            elif(card_array[mid]<key):
                max = mid
            elif(card_array[mid]>key):
                min = mid
        else:
            return -1
        
        count += 1


result = checkCard([13, 11, 10, 7, 4, 3, 1, 0],33)
print(result) 