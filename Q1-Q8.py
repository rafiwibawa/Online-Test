# Q1
print('===Q1===')
n = 6
for i in range(0, n):
    for j in range(0, n - 1):
        print('* ', end='')
    n -= 1
    print('')

# Q2
print('===Q2===')
n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print('* ', end='')
    print('')

# Q3
print('\n===Q3===')
n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print('* ', end='')
    print('')
n = 5
for i in range(0, n):
    for j in range(0, n - 1):
        print('* ', end='')
    n -= 1
    print('')

# Q4
print('===Q4===')
faktorial = 1
bil = int(input("Masukkan bilangan : "))
for i in range(1, bil + 1):
    faktorial = faktorial * i
print('Bilangan Factorial ', bil, '! adalah : ', faktorial)

# Q5
print('===Q5===')
string = input("Masukkan String : ")
string = string.strip()
i = len(string)
space_count = string.count(' ')

new_length = i + space_count * 2

index = new_length - 1

string = list(string)

for f in range(i - 2, new_length - 2):
    string.append('0')

for j in range(i - 1, 0, -1):

    if string[j] == ' ':
        string[index] = '0'
        string[index - 1] = '2'
        string[index - 2] = '%'
        index = index - 3
    else:
        string[index] = string[j]
        index -= 1

print(''.join(string))

# Q6
print('===Q6===')


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


n = int(input("Input n  : "))
fi = fib(n)
print('Output : ', fi)

# Q7
print('===Q7===')


def uniqueCharacters(str):

    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if(str[i] == str[j]):
                return False
    return True


str = "rafi2019"  # true
# str = "rafirafi" #false

if(uniqueCharacters(str)):
    print('Input : ', str, "\nOutput : true")
else:
    print('Input : ', str, "\nOutput : false")

# Q8
print('===Q8===')
array = [2, 4, 5, 1, 8, 12, 7]
print("Nilai terbesar adalah : ", max(array))
print("Nilai terkecil adalah : ", min(array))
