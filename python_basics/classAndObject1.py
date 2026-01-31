class myclass:
    x=5
a1 = myclass()
print(a1.x)
# Output: 5
#del a1 for deleting the object a1
class person:
    species="Homo Sapiens"
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country
    def __str__(self):
        return f"{self.name}, {self.age} years old, from {self.city}, {self.country}"
    def greet(self):
        return "Hello my name is "+ self.name
    def welcome(self):
        message=self.greet()
        print(message + " I am from "+ self.city +", "+ self.country+", and i am "+ str(self.age)+" years old.")
p1=person("John",36,"New York","USA")
print(p1.name)
print(p1.species)
p1.greet()
p1.welcome()
p1.age=40
print(p1.age)
print(p1.city)
print(p1.country)
print(p1)
class playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
        print(f"Added {song} to the playlist {self.name}")
    def del_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed {song} from the playlist {self.name}")
    def show_songs(self):
        print(f"Songs in the playlist {self.name}:")
        for song in self.songs:
            print(song)
my_playlist=playlist("My Favorites")
my_playlist.add_song("Song A")
my_playlist.add_song("Song B")
my_playlist.show_songs()
my_playlist.del_song("Song A")
my_playlist.show_songs()