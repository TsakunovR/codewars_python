"""
Classy Extensions(https://www.codewars.com/kata/55a14aa4817efe41c20000bc/python)

Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).
"""


class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'
