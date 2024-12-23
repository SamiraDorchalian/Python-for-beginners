user_number = int(input('Enter number: '))

is_prime = True

for i in range(2, user_number):
    if user_number % i == 0:
        is_prime = False
        print(f'{user_number} % {i}')
        break

if is_prime == True:
    print(f'{user_number} is Prime.')
else:
    print(f'{user_number} is not Prime.')