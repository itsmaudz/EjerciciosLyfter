class Head:
    pass

class Hand:
    pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    pass

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, torso):
        self.torso = torso

# Create the hands
right_hand = Hand()
left_hand = Hand()

# Create the arms and connect the hands
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

# Create the feet
right_feet = Feet()
left_feet = Feet()

# Create the legs and connect the feet
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

# Create the head
head = Head()

# Create the torso and connect all body parts
torso = Torso(
    head,
    right_arm,
    left_arm,
    right_leg,
    left_leg
)

# Create the human
human = Human(torso)


print(human.torso.right_arm.hand)
print(type(human))
print(type(human.torso))
print(type(human.torso.right_arm))
print(type(human.torso.right_arm.hand))