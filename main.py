import random

# Step 1: Define player database
LEGENDS = [
    {"name": "Cristiano Ronaldo", "position": "Forward", "number": 7, "skills": {"attack": 95, "midfield": 80, "defense": 40}, "ballon_dor": True},
    {"name": "Lionel Messi", "position": "Forward", "number": 10, "skills": {"attack": 98, "midfield": 85, "defense": 30}, "ballon_dor": True},
    {"name": "Zinedine Zidane", "position": "Midfield", "number": 5, "skills": {"attack": 85, "midfield": 95, "defense": 60}, "ballon_dor": True},
    {"name": "Zinedine Zidane", "position": "Midfield", "number": 5, "skills": {"attack": 85, "midfield": 95, "defense": 60}, "ballon_dor": True},
    {"name": "Paolo Maldini", "position": "Defender", "number": 3, "skills": {"attack": 40, "midfield": 60, "defense": 95}, "ballon_dor": False},
    {"name": "Lev Yashin", "position": "Goalkeeper", "number": 1, "skills": {"attack": 0, "midfield": 20, "defense": 98}, "ballon_dor": True},
    {"name": "Johan Cruyff", "position": "Forward", "number": 14, "skills": {"attack": 92, "midfield": 90, "defense": 50}, "ballon_dor": True},
    {"name": "George Best", "position": "Forward", "number": 7, "skills": {"attack": 88, "midfield": 75, "defense": 40}, "ballon_dor": True},
    {"name": "Franz Beckenbauer", "position": "Defender", "number": 6, "skills": {"attack": 65, "midfield": 85, "defense": 92}, "ballon_dor": True},
]

# Step 2: Initialize players and their teams
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.stats = {"attack": 0, "midfield": 0, "defense": 0}
    
    def add_player(self, player):
        self.players.append(player)
        for key in self.stats:
            self.stats[key] += player["skills"][key]
    
    def calculate_strength(self):
        return sum(self.stats.values())

# Create 8 teams
teams = [Team(f"Team {i+1}") for i in range(8)]

# Step 3: Draft system
def draft_player(team, round_criteria, available_players):
    # Filter players based on criteria
    eligible_players = [p for p in available_players if round_criteria(p)]
    if not eligible_players:
        print(f"No players available for {team.name} this round!")
        return None
    
    # Let the team draft a player
    draft_pick = random.choice(eligible_players)  # Simulating a random pick for now
    team.add_player(draft_pick)
    available_players.remove(draft_pick)
    print(f"{team.name} drafts {draft_pick['name']}!")

# Step 4: Define round criteria
rounds = [
    lambda p: p["number"] == 7,                          # Round 1: Players with #7
    lambda p: p["ballon_dor"],                           # Round 2: Ballon d'Or winners
    lambda p: p["position"] == "Defender",              # Round 3: Defenders
    lambda p: p["position"] == "Goalkeeper",            # Round 4: Goalkeepers
]

# Step 5: Simulate the draft
available_players = LEGENDS[:]
for i, round_criteria in enumerate(rounds):
    print(f"\n=== Round {i+1} ===")
    for team in teams:
        draft_player(team, round_criteria, available_players)

# Step 6: Match simulation
def simulate_match(team1, team2):
    t1_strength = team1.calculate_strength()
    t2_strength = team2.calculate_strength()
    t1_score = random.randint(0, 3) + t1_strength // 100
    t2_score = random.randint(0, 3) + t2_strength // 100
    print(f"{team1.name} ({t1_score}) vs {team2.name} ({t2_score})")
    if t1_score > t2_score:
        return team1
    elif t2_score > t1_score:
        return team2
    else:
        return random.choice([team1, team2])  # Random tie-breaker

# Step 7: Knockout tournament
def knockout_tournament(teams):
    print("\n=== Knockout Stage ===")
    while len(teams) > 1:
        next_round = []
        for i in range(0, len(teams), 2):
            winner = simulate_match(teams[i], teams[i+1])
            next_round.append(winner)
            print(f"{winner.name} advances!")
        teams = next_round
    print(f"\nChampion: {teams[0].name}")

# Start the tournament
knockout_tournament(teams)

