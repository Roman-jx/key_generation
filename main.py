from random import *
generator_passwords = [chr(i).upper() for i in range(48, 58)] + [chr(i).lower() for i in range(65, 91)] + [chr(i).upper() for i in range(97, 123)]
new_password = []
jpw = "".join([chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 96)])
shuffle(generator_passwords)
for i in generator_passwords:
    new_password.append(i)

np = "".join(new_password).strip(f'{jpw}')
np2 = np[:len(np)//2][::-1] + np[len(np)//2:][::-1]
passwords = {
    'key1': str(np),
    'key2': str(np2),
    'freak': int(eval('888'))
}
c = 0
while c < int(len(passwords.keys()) - 2):
    print('Would you like to see your info?')
    user = input('==> @Write: "see" to see the keys.\n==> @Write: "no" if will not check.\n==> Enter root password: ')
    print('=' * 100)
    if user == 'see':
        for k, v in passwords.items():
            print(f'*\t{k} ==> {v}')
        print('=' * 100)
    elif user == 'no':
        c += 1

k = 0
while k < int(len(passwords.keys()) - 2):
    print('Do you want to copy password?')
    user = input('==> @Write "y" if you want to generate the key.\n==> @Write "n" if you don\'t want to create.\n==> Enter your answer(Y/N): ').lower().strip(' ')
    if user == 'y' or user == 'n':
        print('=' * 100)
        with open('password.txt', 'w') as fil:
            fil.write(f'@First key: {passwords["key1"]}')
            fil.write(f"\n{'-'*150}\n")
            fil.write(f"@Second key:{passwords['key2']}")
            fil.close()
        print('(Success)Check list.')
        print('=' * 100)
    k += 1

j = 0
while j < int(len(passwords.keys()) - 2):
    print('Do you want to clear your list?')
    user = input('==> Don\'t write the answer if you don\'t copy the text!!!\n==> Enter your answer(Y/N): ').lower().strip(' ')
    if user == 'y':
        print('=' * 100)
        with open('password.txt', 'w') as fil:
            fil.truncate(0)
        print('(Success)Check list.')
        print('=' * 100)
    j += 1