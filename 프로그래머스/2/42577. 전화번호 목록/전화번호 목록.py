def solution(phone_book):
    phone_set = set(phone_book)

    for num in phone_book:
        for i in range(1, len(num) + 1):
            if num[:i] in phone_set and num[:i] != num:
                return False
    return True
