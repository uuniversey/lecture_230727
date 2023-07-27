

# 상속


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'안녕, {self.name}입니다.')


# class Professor(Person):

#     def __init__(self, name, age, department):
#         super().__init__(name, age) # 1번을 대체
#         # 상속이 많아졌을 때 유연하게 대처할 수 있다.
#         self.department = department


# class Student(Person):
    
#     def __init__(self, name, age, gpa):
#         Person.__init__(self, name, age) # 1번
#         self.gpa = gpa


# p1 = Professor('박교수', 49, '컴공')
# s1 = Student('김학생', 20, 3.5)

# p1.talk()
# s1.talk()



# 다중 상속

# class Person:

#     def __init__(self, name):
#         self.name = name

#     def greeting(self):
#         return (f'안녕, {self.name}')


# class Mom(Person):
#     gene = 'XX'

#     def __init__(self, name):
#         super().__init__(name)

#     def swim(self):
#         return '엄마가 수영'


# class Dad(Person):
#     gene = 'XY'

#     def __init__(self, name):
#         super().__init__(name)

#     def walk(self):
#         return '아빠가 걷기'
    

# class FirstChild(Dad, Mom):

#     def __init__(self, name):
#         super().__init__(name)

#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
        

# baby1 = FirstChild('아가')
# print(baby1.cry()) # 첫째가 응애
# print(baby1.swim()) # 첫째가 수영
# print(baby1.walk()) # 아빠가 걷기
# print(baby1.greeting()) # 안녕, 아가
# print(baby1.gene) # XY



# 복수 예외 처리 연습

# try:
#     num = int(input('100으로 나눌 값을 입력하시오 : '))
#     print(100 / num)

# except ZeroDivisionError:
#     print('0 은 나눌 수가 없단다')
# except ValueError:
#     print('숫자를 한글로 어떻게 나눠')
# except:
#     print('에러 발생')



# 연습 2

# try:
#     num = int(input('100으로 나눌 값을 입력하시오 : '))
#     print(100 / num)

# except BaseException:
#     print('0 은 나눌 수가 없단다')
# except ValueError:
#     print('숫자를 한글로 어떻게 나눠')
# except:
#     print('에러 발생')

# BaseException가 ValueError가 더 하위 클래스이기 때문에 하위 클래스의 예외는 무효가 된다.