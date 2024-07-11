#1 Данный код выделяет из списка простые и не простые числа и выводит их в отдельные списки используя функцию def
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# primes = []
# non_primes = []
#
# for number in numbers:
#     if is_prime(number):
#         primes.append(number)
#     else:
#         non_primes.append(number)
#
# print("Primes:", primes)
# print("Non-primes:", non_primes)
#
# Primes: [2, 3, 5, 7, 11, 13]
# Non-primes: [1, 4, 6, 8, 9, 10, 12, 14, 15]



#2 Данный код выводит простые и непростые числа из предоставленного списка в отдельные списки через функию for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number < 2:
        not_primes.append(number)
        continue

    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Non-primes:", not_primes)

