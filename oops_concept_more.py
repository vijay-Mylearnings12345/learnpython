class Team:
    def __init__(self, po, manager, developer, tester):
        self.po = po
        self.manager = manager
        self.developer = developer
        self.tester = tester

    def role1(self):
        print(f"{self.po} is taking the Project and Team management responsibility")

    
team1 = Team("Unknown", "Magnus", "Petter", "vijay")
team2 = Team("Alex", "Marten", "Peter", "Victor")

print(team1.manager)
print(team1.developer)
print(team1.tester)

print(team2.manager)
print(team2.developer)
print(team2.tester)

team1.role1()
team2.role1()
