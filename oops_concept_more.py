class Team:
    def __init__(self, po, manager, developer, tester):
        self.po = po
        self.manager = manager
        self.developer = developer
        self.tester = tester

    def role1(self):
        print(f"{self.manager} is taking the Project and Team management responsibility")

    
team1 = Team("Unknown", "Magnus", "Petter", "vijay")

print(team1.manager)
print(team1.developer)
print(team1.tester)

team1.role1()
