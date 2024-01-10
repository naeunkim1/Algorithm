def solution(phone_book):
    phoneDict = {}
    for phone in phone_book:
        phoneDict[phone] = 1
    for phone in phone_book:
        arr = ''
        for num in phone:
            arr+=num
            if arr in phoneDict and arr != phone:
                return False
    return True