def solution(phone_book):
    hashDict = {}
    
    for nums in phone_book:
        hashDict[nums] = 1
    for nums in phone_book:
        arr = ''
        for n in nums:
            arr += n
            if arr in hashDict and arr != nums:
                return False
    return True