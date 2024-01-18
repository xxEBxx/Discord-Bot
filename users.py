import json
import os

class Server:
    def __init__(self):
        self.player_data = {}
        self.people = {}
        self.load_data()

    def save_data_to_file(self, filename, data_to_write):
        json_file_path = os.path.join(os.path.dirname(__file__), 'Data', filename)

        with open(json_file_path, 'w') as file:
            json.dump(data_to_write, file)

    def load_data_from_file(self, filename):
        json_file_path = os.path.join(os.path.dirname(__file__), 'Data', filename)

        with open(json_file_path, 'r') as file:
            data_read = json.load(file)

        return data_read

    def load_data(self):
        try:
            self.player_data = self.load_data_from_file("player_data.json")
        except FileNotFoundError:
            self.player_data = {} 

        try:
            self.people = self.load_data_from_file("people.json")
        except FileNotFoundError:
            self.people = {} 

    def save_data(self):
        # Create a copy of the data dictionaries without methods/functions
        clean_player_data = {key: value for key, value in self.player_data.items() if isinstance(value, (str, int, float, bool, list, dict, type(None)))}
        clean_people_data = {key: value for key, value in self.people.items() if isinstance(value, (str, int, float, bool, list, dict, type(None)))}

        # Save the cleaned data to JSON files
        self.save_data_to_file("player_data.json", clean_player_data)
        self.save_data_to_file("people.json", clean_people_data)

server = Server()

class User:
    def __init__(self,user_id: int,username,games_played={},warning=0,
                 is_banned=False,money=0,words={},role="member",behave=0):
        self.user_id = user_id
        self.games_played = games_played # Dictionary to store game playtime
        self.warnings =warning
        self.is_banned = is_banned
        self.money=money
        self.behave=behave
        self.username=username
        self.words=words
        self.role =role
        
    def to_dict(self):
        user_dict = {
            "user_id": self.user_id,
            "behave":self.behave,
            'games_played': self.games_played,
            'warnings': self.warnings,
            'banned': self.is_banned,
            'money': self.money,
            "username":self.username,
            "words" : self.words,
            "role" :self.role
            
        }
        return user_dict

    def add_game_playtime(self, game_name, playtime):
        self.games_played[game_name] = playtime

    def remove_game(self, game_name):
        if game_name in self.games_played:
            del self.games_played[game_name]

    def add_behave(self):
        #warn starts from 2 bad behaviours 
        if self.behave==1:
            self.add_warning()
            self.behave=0
            return
        self.behave=1
        
    def add_warning(self):
        if self.warnings==2:
            self.ban_user()
            self.warnings=0
            return 
        self.warnings += 1

    def ban_user(self):
        self.is_banned = True

    def unban_user(self):
        self.is_banned = False

    def get_total_playtime(self):
        return sum(self.games_played.values())

    def get_game_playtime(self, game_name):
        return self.games_played.get(game_name, 0)

    def __str__(self):
        return f"User ID: {self.user_id}\nGames Played: {self.games_played.keys()}\nWarnings: {self.warnings}\nIs Banned: {self.is_banned}"



