def is_prime(num):
    if num%1==0 and num!=1:
        if num==2 and num%2==0:
            return True
        elif num==3 and num%3==0:
            return True
        elif num==5 and num%5==0:
            return True
        elif num==7 and num%7==0:
            return True
        elif num%5==0:
            return False
        elif num%2==0:
            return False
        elif num %3==0:
            return False
        else:
            return True
    else:
        return False
print(is_prime(18))