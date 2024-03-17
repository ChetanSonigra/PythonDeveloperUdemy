"""
    You've already learned 2 of those pillars, through the video lessons, downloadable notes, and practice exercises. These are:

Inheritance

Polymorphism

To learn the remaining 4 pillars (which are rather conceptual), I have prepared for you this special article, that will surely help you understand them easily:



Cohesion
Cohesion refers to the degree of relationship between the elements of a module. When we design a function, we must identify in a very specific way what task it is going to perform, reducing its purpose to a single and well-defined objective.

For a function to be cohesive it must do only one thing, and if it has to do more than one thing, there must exist a high relationship to each other. The more unrelated things a function does, the more difficult it is to understand the code.

There are two types of cohesion:

Weak cohesion: indicates that the relationship between the elements is low, and therefore they do not have a single functionality.

Strong cohesion: indicates that there is a high relationship between the existing elements within the module. This should be our goal when designing programs.

A very clear example of weak or strong cohesion could be the following:

We want to have a function called sum_numbers(), which purpose is to add two numeric arguments. A strongly cohesive version of this function would be the following:

def sum_numbers(num1, num2):
      result = num1+num2
      return result
The problem would occur if the programmer felt like putting everything in one place, and in addition to adding two numbers, use this function to:

Ask the user to enter those numbers (instead of asking for them in another function and passing them as arguments),

And since he’s going to need those numbers to be float(), he’s also going to do the conversion within the same function.

The result of adding these functionalities would be a weak cohesion function:

def sum_numbers():
    num1 = float(input('Choose a number: ')
    num2 = float(input('Choose another number: ')
    result = num1+num2
    return result
You might be thinking that these two extra features aren't that big of a deal, but let's say a person wants to use our sum_numbers() function, but already has the numbers, and does not want to ask for them on the screen. Our function just wouldn't work for them.

For the function to have strong cohesion, it would be convenient if sum_numbers() performs a single, well-defined task, which is to sum.

Of course this is a very simple example, in which the implications would not be so dramatic, but it is important to look for the functions to perform a single task, or at least a highly-related set of tasks.

The advantages of designing code with strong cohesion are:

Reduce the complexity of the module, since it will have a smaller number of operations

Modules can be reused more easily

The system will be easier to maintain

Cohesion is linked to another of the pillars called coupling. Normally strong cohesion is related to weak coupling.



Coupling
Coupling is a concept that refers to how related or dependent two classes/modules are toward each other. It measures the dependency between two different modules or classes. We can talk about two types of coupling:

Weak/Low coupling implies that there is no dependency between one module and others. This is the ideal situation because changing something major in one class should not affect the other.

Strong/high coupling, which is the opposite situation, and indicates that the module has internal dependencies with others.

This is a pillar linked to cohesion, since weak coupling is usually associated with strong cohesion. The latter is the situation to look for when writing code. That is, we seek that a class or function does not have dependencies with other classes or functions, and that the tasks they perform are related to each other. This simplifies the reading and maintenance of the code, while allowing it to be reused in other programs. High coupling would make it difficult to change and maintain your code; since classes are closely knit together, making a change could require an entire system revamp.

To complete our understanding, let's imagine the opposite situation: a highly coupled code.

If we would like to reuse a module that depends on others, we should "bring" also all dependencies as well, otherwise it would result in errors and loss of functionality.

If we make a change in a module that depends on others, the effects of this change may affect the other modules that are dependent on the previous one.

It is very important to pay attention to it as our programs grow and become more complex, where these types of situations can begin to occur inadvertently. If this happens, a change to one class can make another class unusable, causing it to stop working. A tight coupling situation can lead to errors that are difficult to debug.

Let's look at the following example:

class Pet:
    has_legs = True
    pass
class Dog:
    def run(self, speed):
        if Pet.has_legs:
            self.speed = speed
my_pet = Dog()
my_pet.run("fast")
print(my_pet.speed)
We have a Pet class that defines a class attribute has_legs. On the other hand, the Dog class bases the behavior of the run() method on the has_legs attribute of the Pet class. We have strong coupling, since there is a dependency between the function of one class with the attribute of another.

If your program must contain external dependencies, you must ensure that they are essential and properly justified to minimize the adverse effects mentioned above.



Abstraction
Abstraction is the pillar of object-oriented programming that is related to hiding all the complexity that some code can have inside, offering an interface with high-level functions, usually simple to use, to interact with the application interface without really knowing what’s inside.

Think about how many engineering objects or applications you use in your day-to-day life, which have a simple interface and complex behavior inside.

What would happen if, to be able to drive, we had to know every detail of how a car works, from the turning of its gears to the electrical circuit that powers the mechanism that raises and lowers the windows? To operate the latter all a driver needs to do is push a button and it performs the expected action. This button abstracts the driver from a complex system and provides them with a simple interface to achieve their goal. If we programmed it, these methods could be raise() and lower(), and inside them, they would need to distribute energy and trigger mechanisms in the different sectors of the vehicle.

This is what our code should aim at: no matter how complex it needs to be inside, well implemented abstraction allows us to offer simple and predictable methods according to what their name suggests.



Encapsulation
Encapsulation is the pillar of object-oriented programming that is related to hiding certain internal states of an object from the outside, so that it is the object itself that accesses or modifies them, but such action cannot be carried out from the outside, by calling the methods or attributes directly.

Although in some languages (such as Java), it may be a common procedure, Python does not implement it by default, but offers an alternative way to achieve it. This is done by prefixing two underscores (__) when naming a method or attribute. In this way, they will be defined as "private", and only the object itself will be able to access them.

class Person:
    public_attribute = "Show"   # Accessible from outside
    __private_attribute = "Hidden"  # Not accessible
    # Not accessible from outside
    def __hidden_method(self):
        print("This method is hidden")
        self.__variable = 0
    # Accessible from outside
    def normal_method(self):
        # The method is accessible from inside
        self.__hidden_method()
student = Person()
# student.__hidden_method()  # This method is not accessible from outside
student.hidden_method()      # This method is accessible
There is a little trick (not recommended) to access hidden attributes and methods. These methods are to be called with a somewhat different name:



instance + _ + ClassName + hidden method/attribute

student._Person__hidden_method()
print(student._Person__private_attibute)
    """