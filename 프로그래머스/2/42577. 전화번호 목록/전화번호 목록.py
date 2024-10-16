def solution(phone_book):
    phone_set = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number) + 1):
            if number[:i] in phone_set and number[:i] != number:
                return False
    return True
