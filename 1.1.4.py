class SpaceShip():
    def __init__(self, fuel, ship, speed):
        self.fuel = fuel
        self.ship = ship
        self.speed = speed

    def spaceship(self):
        return f'{self.fuel} {self.ship} {self.speed}'


class CrewMember():
    def __init__(self, hp, skills, role):
        self.hp = hp
        self.skills = skills
        self.role = role

    def members(self):
        return f'{self.hp} {self.skills} {self.role}'


class Mission():
    def __init__(self, goal, resources, events):
        self.goal = goal
        self.resources = resources
        self.events = events

    def missions(self):
        return f'{self.goal} {self.resources} {self.events}'


Spaceship = SpaceShip('100', '96%', '600км/ч')
print(Spaceship.spaceship())

member = CrewMember('100', 'ремонт корабля, посадка, взлет', 'капитан, инженер, пилот')
print(member.members())

mission = Mission('долететь до марса', 'железно, нефть', 'встреча с астеройдом через 12 часов')
print(mission.missions())
