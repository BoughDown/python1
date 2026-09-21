"""
Model Indi Assignment by Tommy Bough

The assignment is to add comments and docstrings to the provided template.
"""

# Imports a random choice.
from random import choice

# Creates lists of the following: locations, humans, and dogs.
locations = []
humans = []
dogs = []

def ball_string(balls):
    """
    Returns how many balls there are, and prints out a readable list based on how many balls there are.
    """
    if len(balls) == 0:
        return 'no balls'
    elif len(balls) == 1:
        return f'{balls[0].name}'
    elif len(balls) == 2:
        return f'{balls[0].name} and {balls[1].name}'
    else:
        return_string = ''
        for ball in balls[:-1]:
            return_string += ball.name + ', '
        return_string += f'and {balls[-1].name}'
        return return_string

# Creates a class of humans to call actions for.
class Human:
    """
    A class for human type objects, to be used in the Indi ball game.

    Attributes:
        balls (list): The humans inventory of balls.
        name: The humans name.
    Methods:
        throw_ball
    """

    def __init__(self, name):
        self.balls = []
        self.name = name

    def action(self):
        """
        Creates actions for the humans to play or not play with Indi. 

        If the user chooses yes, then the ball is thrown, if not, they keep the ball in their hands.
        """
        if self.balls != []:
            print(f'\nYou now have {ball_string(self.balls)} in your hands...')
            action = input('Throw the ball?\n')
            if action.lower() in ['yes', 'y']:
                self.throw_ball(choice(self.balls), choice(locations))
            else:
                print('You really are heartless aren\'t you?')

    def throw_ball(self, ball, target_location):
        """
        This functions alloqs the human to be able to throw the ball to different locations in a set list.
        """
        target_location.balls.append(ball)
        self.balls.remove(ball)
        print(
            f'You have thrown {ball.name}, it is now in the {target_location.name}.\n'
        )

# Creates the class of locations for the balls to be found or thrown in.
class Location:
    """
    A class for location type objects, to be used in the Indi ball game.
    
    Attributes:
        balls (list): The locations inventory of balls.
        name: The locations name.
    """
    def __init__(self, name, balls):
        self.name = name
        self.balls = balls

# Allows the balls to have attributes, for example, for said balls to be thrown.
class Ball:
    """
    A class for ball type objects, to be used in the Indi ball game.
    
    Attributes:
        name: The balls name.
    """
    def __init__(self, name):
        self.name = name

# Creates the class of Dog, and gives functions assigned to that class.
class Dog:
    """
    A class for dog type objects, to be used in the Indi ball game.
    
    Attributes:
        balls (list): The dogs inventory of balls.
        name: The dogs name.
    Methods:
        give_ball: Gives the ball to the human.
        look_for_ball: Looks for a ball in a specific location.
    """
    def __init__(self, name):
        self.name = name
        self.balls = []

    def action(self):
        """
        Gives an action to the class of dog. Giving them the ability to give balls to the human class, or look for balls in locations.
        """
        if self.balls != []:
            self.give_ball(choice(humans), choice(self.balls))
        else:
            self.look_for_ball(choice(locations))

    def give_ball(self, human, ball):
        """
        Once a ball is given to a human, the ball is removed from the dog and is given to the humans hands.
        """
        self.balls.remove(ball)
        human.balls.append(ball)
        print(f'{self.name} has given the {ball.name} to {human.name}')

    def look_for_ball(self, target_location):
        """
        Gives the dog the action of looking for a ball in a specific location.

        If a ball is found:
            The dog keeps the ball
        If a ball is not found:
            A text shows that he looks hopelessly after searching the specific location.
        """
        if target_location.balls != []:
            target_ball = choice(target_location.balls)
            self.balls.append(target_ball)
            target_location.balls.remove(target_ball)
            print(
                f'{self.name} has found the {target_ball.name} in the {target_location.name}.'
            )
        else:
            print(
                f'{self.name} looks hopelessly about after searching the {target_location.name}.'
            )

# Creates a list of locations, as well as placing diffrent balls in each location.
locations = [
    Location('Living Room', [Ball('Pink Torus')]),
    Location(
        'Kitchen',
        [Ball('Sal the Snake'),
         Ball('Pink Ellipsoid'),
         Ball('Blue Chuckit')]),
    Location('Under the Couch',
             [Ball('Pink Ball'),
              Ball('Green Ellipsoid'),
              Ball('Blue Torus')]),
    Location('Dining Room', []),
    Location(
        'Yard',
        [Ball('Larry the Lizard'), Ball('S toy')])
]

# Assigns the human, Joe, to the human list.
Joe = Human('Joe')
humans.append(Joe)
# Assigns the dog, Indi, to the dog list.
Indi = Dog('Indi')
dogs.append(Indi)

# Indi and Joe will always attempt actions if the circumstances are true.
while True:
    Indi.action()
    Joe.action()