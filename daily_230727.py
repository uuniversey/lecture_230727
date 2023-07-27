

# 1466. hw_8_2


# def check_number():

#     try:
#         num = int(input())
#         if num > 0:
#             print('양수입니다.')
#         elif num == 0:
#             print('0입니다.')
#         else:
#             print('음수입니다.')
#     except ValueError:
#         print('잘못된 입력입니다.')

# check_number()



# 1467. hw_8_4

# class UserInfo:
#     def __init__(self):
#         self.user_data = {}

#     def get_user_info(self):

#         try:
#             name = input('이름을 입력하세요: ')
#             age = int(input('나이를 입력하세요: '))
#             self.user_data['이름을 입력하세요'] = name
#             self.user_data['나이를 입력하세요'] = age
#             print('사용자 정보:')
#             print('이름:', name)
#             print('나이:', age)

#         except ValueError:
#             print('나이는 숫자로 입력해야 합니다.')
        
#     def display_user_info(self):
#         if not self.user_data.get('나이를 입력하세요'):
#             print('사용자 정보가 입력되지 않았습니다.')
#         else:
#             print(f"이름을 입력하세요: {self.user_data.setdefault('이름을 입력하세요')}")
#             print(f"나이를 입력하세요: {self.user_data.setdefault('나이를 입력하세요')}")

# user = UserInfo()
# user.get_user_info()
# user.display_user_info()



# 1461. ws_8_1

# class Animal:
    
#     num_of_animal = 0

#     def __init__(self,name):
#         self.name = name


# class Dog(Animal):
    
#     def __init__(self,name):
#         super().__init__(name)
#         Pet.num_of_animal += 1
        

# class Cat(Animal):

#     def __init__(self,name):
#         super().__init__(name)
#         Pet.num_of_animal += 1
    
        
# class Pet(Dog, Cat):
   
#    def __init__(self,name):
#         self.name = name    

#    @classmethod
#    def access_num_of_animal(cls):
#        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'
       
   
# dog = Dog('dog')
# print(Pet.access_num_of_animal())
# cat = Cat('cat')
# print(Pet.access_num_of_animal())



# 1462. ws_8_2

# class Animal:
    
#     num_of_animal = 0
#     def __init__(self):
#        return


# class Dog(Animal):
#    def bark(self):
#        print('멍멍!')


# dog1 = Dog()
# dog1.bark()



# 1463. ws_8_3

# class Animal:
    
#     num_of_animal = 0
#     def __init__(self):
#        return


# class Cat(Animal):
#    def meow(self):
#        print('야옹!')

# cat1 = Cat()
# cat1.meow()



# 1464. ws_8_4

# class Animal:
    
#     num_of_animal = 0
#     def __init__(self, sound):
#         self.sound = sound


# class Dog(Animal):
#    def bark(self):
#        print('멍멍!')


# class Cat(Animal):
#    def meow(self):
#        print('야옹!')


# class Pet(Dog, Cat):

#     sound = '그르르'
        
#     def make_sound(self):
#         print(Pet.sound)
    
#     def play(self):
#         print('애완동물과 놀기')

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()



# 1465. ws_8_5

class Dog():
    
    sound = '멍멍'


class Cat():

    sound = '야옹'

   
class Pet1(Dog, Cat):

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

class Pet2(Cat, Dog):

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

print(Pet1())
print(Pet2())