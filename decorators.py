
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작')
#         func(input_text)
#         print('함수 끝')
#     return decorated  # decorated() x
#
# @decorator
# def hello_world(input_text):
#     print(input_text)
#
#
# hello_world('Hello World')

def decorator(func):
    def decorated(length, width):
        if length >= 0 and width >= 0:
            return func(length, width)
        else:
            raise ValueError('e')
    return decorated

@decorator
def size_of_tri(length, width):
    return length * width * 1/2
@decorator
def size_of_rec(length, width):
    return length * width
#
# size_of_tri(-2, -3)
# size_of_rec(3, 5)
#
# class User:
#     def __init__(self, auth):
#         self.is_authenticated = auth
#
# user = User(auth=False)

