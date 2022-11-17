"""
Simple example of static method.
Static methods are used rarely. They have neither the self nor the cls parameter.
In fact, these could be ordinary functions.
"""


class ExampleOfStaticMethod:
    @staticmethod
    def say_hello():
        print("Hello")


ExampleOfStaticMethod.say_hello()
