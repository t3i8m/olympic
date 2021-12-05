def clearing(datas):
    space_index = datas.index(" ")
    first_part = datas[:space_index]
    second_part = datas[space_index+1:]
    first_part, second_part = convert(first_part, second_part)
    return first_part, second_part

def convert(first_number, second_number):
    converted_first_number = str()
    converted_second_number = str()
    i_first = 0
    i_second = 0
    while i_first < len(first_number):
        converted_first_number += str(first_number[i_first])
        i_first+=1
    while i_second < len(second_number):
        converted_second_number += str(second_number[i_second])
        i_second +=1
    return int(converted_first_number), int(converted_second_number)

def all_primes(b):
    all_primes = list()
    for n in range(0, b+1):
        if n == 2:
            all_primes.append(n)
        elif n == 3:
            all_primes.append(n)
        elif n == 1:
            continue
        elif n == 5:
            all_primes.append(n)
        elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            all_primes.append(n)
    return all_primes
    
def counting(a,b):
    primes = all_primes(b)
    result=list()
    i = 0
    for n in primes:
            for i in primes:
                res = n * i 
                if res >=a and res <=b:
                    result.append(res)
                while i < len(result):
                    if result.count(res) >= 2:
                        result.remove(res)
                    i+=1
    if result[:4] == [2,3,5,7]:
        for n in result[:4]:
            result.remove(n)
    print(len(result)) 



datas = list(input())
a, b = clearing(datas)
if a >= 1 and b <= 10**6:
    counting(a,b)
else:
    exit()
