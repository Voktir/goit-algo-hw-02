from collections  import deque

def is_palindrome(imp_str: str) -> bool:
    
    # Приводимо символи до нижнього регістру, видаляємо пробіли
    imp_str = imp_str.lower().replace(' ', '')
    
    # Додаємо символи до двосторонньої черги
    d = deque(imp_str)
    
    # Перевіряємо чергу на паліндром
    while len(d)>1:
        if d.popleft() != d.pop():
            return False
    return True    

# Тестуємо:
print(is_palindrome("Козак з казок"))  
print(is_palindrome("123 3 2 1"))
print(is_palindrome("1234 3 2 1"))
print(is_palindrome("124 3 2 1"))