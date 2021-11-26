# Lista de entregaveis de Python, Orientacao a Objeto
# André Leão, Engenharia Eletrônica e de Computação





class Team:

    def __init__(self, name, points):
        self.name = name 
        self.score = points

    def __str__(self):
        # Informs team's name and score 
        out = f"The Team {self.name} has scored {self.score} points at the league."
        return out

    def __repr__(self):
        # represents Teams with name and score
        return f'{self.name}({self.score})'

    def __add__(self, rival): 
        # add scores 
        return (self.score + rival.score)
    
    def __sub__(self, rival):
        # subtracts scores
        return (self.score - rival.score)

    def __gt__(self, rival):
        # compares if more than
        return (self.score > rival.score)
    
    def __lt__(self, rival):
        # compares if less than
        return (self.score < rival.score)
    
    def __eq__(self, rival):
        # compares if equal
        return (self.score == rival.score)
    
    def __ne__(self, rival):
        # compares if not equal
        return (self.score != rival.score)
    
    def __ge__(self, rival):
        # compares if more ou equal
        return (self.score >= rival.score)
    
    def __le__(self, rival):
        # compares if less or equal
        return (self.score <= rival.score)


fla = Team('Flamengo', 67)
flu = Team('Fluminense', 10)
vas = Team('Vasco', 20)
bot = Team('Botafogo', 15)

teams = [fla, flu, bot, vas]
print(teams)
teams.sort()
print(teams)
