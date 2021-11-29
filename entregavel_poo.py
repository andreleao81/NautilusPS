# OOP Python list


class Team:

    def __init__(self, name, points, wins, losses, draws, goals_difference ):
        self.name = name 
        self.points = points
        self.w = wins
        self.l = losses
        self.d = draws
        self.gd = goals_difference

    def __str__(self):
        # Informs team's name and score 
        out = f"The Team {self.name} has scored {self.points} points at the league.\
            \nCurrently, {self.name} has {self.w} wins, {self.l} defeats and {self.d} draws, with {self.gd} as it's goals difference."
        return out

    def __repr__(self):
        # represents Teams with name and league points
        return f'{self.name}({self.points})'

    def __add__(self, rival): 
        # add points 
        return (self.points + rival.points)
    
    def __sub__(self, rival):
        # subtracts points
        return (self.points - rival.points)

    def __gt__(self, rival):
        # compares if more than
        return (self.points > rival.points)
    
    def __lt__(self, rival):
        # compares if less than
        return (self.points < rival.points)
    
    def __eq__(self, rival):
        # compares if equal
        return (self.points == rival.points)
    
    def __ne__(self, rival):
        # compares if not equal
        return (self.points != rival.points)
    
    def __ge__(self, rival):
        # compares if more ou equal
        return (self.points >= rival.points)
    
    def __le__(self, rival):
        # compares if less or equal
        return (self.points <= rival.points)

# format : team = Team (name, points, wins, losses, draws, goals_difference)

