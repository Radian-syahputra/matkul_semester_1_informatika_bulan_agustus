def is_palindrome(x : int) -> bool :
    if x < 0 or (x % 10 == 0 and x != 0) :
        return False

    half : int = 0
    while x > half :
        half = half * 10 + (x % 10)
        x = x // 10
        
    return x == half or x == half // 10 
    