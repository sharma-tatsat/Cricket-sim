class teams :
    def __init__(self,name,players):
        self.name = name
        self.players = players
    
    
india_players = [
        'Abhishek Sharma',
        'Vaibhav Sooryavanshi',
        'Devdutt Paddikal',
        'Shreyas Iyer',
        'Rajat Patidar',
        'Hardik Pandya',
        'Axar Patel',
        'Mohsin Khan',
        'Jasprit Bumrah',
        'Bhuvaneshwar Kumar',
        'Anshul Kamboj'
]
    
    
southafrica_players = [
        'Quinton deKock',
        'Ryan Rickleton',
        'Aiden Markram',
        'Dewald Brewis',
        'Heinrich Klassen',
        'David Miller',
        'Corbin Bosch',
        'Keshav Maharaj',
        'George Linde',
        'Kagiso Rabada',
        'Lungi Ngidi'
]
        
    
india = teams("india" , india_players)
    
print(india.name)
print(india.players)
    