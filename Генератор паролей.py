import string,random
def digit(x,l): #Пароль только из цифр
    x=int(x)
    [print(''.join(random.sample(string.digits, x))) for _ in range(int(l))]
def bykvi_and_digit(x,y,l): #Все буквы и цифры
    x = int(x)
    y = int(y)
    for _ in range(int(l)):
        k=random.sample(string.ascii_letters, x)+random.sample(string.digits, int(y))
        random.shuffle(k)
        print(''.join(k))
def small_or_big_bykvi_and_digit(x,y,l,k):
    x = int(x)
    y = int(y)
    if k == 1:
        for _ in range(int(l)):
            k = random.sample(string.ascii_lowercase, x) + random.sample(string.digits, y)
            random.shuffle(k)
            print(''.join(k))
    else:
        for _ in range(int(l)):
            k = random.sample(string.ascii_uppercase, x) + random.sample(string.digits, y)
            random.shuffle(k)
            print(''.join(k))
def bykvi(x,l,k):
    x = int(x)
    if k == 1:
         [print(''.join(random.sample(string.ascii_uppercase, x))) for _ in range(int(l))]
    elif k == 2:
        [print(''.join(random.sample(string.ascii_lowercase, x))) for _ in range(int(l))]
    else:
        [print(''.join(random.sample(string.ascii_letters, x))) for _ in range(int(l))]
def danni():
    print('1) Пароль только из цифр\n2) Пароль из заглавных и маленьких букв\n3) Пароль только из заглавных букв\n4) Пароль только из маленьких букв\n5) Пароль только из маленьких букв и цифр\n6) Паролько только из больших букы и цифр\n7) Пароль из цифр и букв')
print('Добро пожаловать в генератов паролей')
print('Выбирайте, что вас интересует:')
danni()
vvod=input('Введите в формате: <номер пункта,длина пароля,количество паролей>(через пробел)\n').split()
vvod1=['1','2']
if vvod[0] in '567':
    vvod1=input('Введите сколько вы хотите букв и цифр в формате: <количество букв, количество цифр> (через пробел)\n').split()

d={'1': 'digit(vvod[1],vvod[2])',
   '2': 'bykvi(vvod[1],vvod[2],3)',
   '3': 'bykvi(vvod[1],vvod[2],1)',
   '4': 'bykvi(vvod[1],vvod[2],2)',
   '5': 'small_or_big_bykvi_and_digit(vvod1[0],vvod1[1],vvod[2],1)',
   '6': 'small_or_big_bykvi_and_digit(vvod1[0],vvod1[1],vvod[2],2)',
   '7': 'bykvi_and_digit(vvod1[0],vvod1[1],vvod[2])'
   }
while True:
    eval(d[vvod[0]])
    if input('Еще пароли?(Да/Нет)\n').lower()=='да':
        danni()
        vvod = input('Введите в формате: <номер пункта,длина пароля,количество паролей>(через пробел)\n').split()
        vvod1 = ['1', '2']
        if vvod[0] in '567':
            vvod1 = input('Введите сколько вы хотите букв и цифр в формате: <количество букв, количество цифр>(через пробел)\n').split()
    else:
        print('Приходите ещё!')
        break

