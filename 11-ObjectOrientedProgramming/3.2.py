class Music():
    def __init__(self,artist, track_title, album, year):
        self.artist=artist
        self.track_title=track_title
        self.album=album
        self.year=year
    def __str__(self):
        return f'\nArtist: {self.artist} \nTitle: {self.track_title} \nAlbum: {self.album} \nYear: {self.year}'

song1 = Music('Lucio Corsi', 'Volevo essere un duro','Volevo essere un duro',2025)
song2 = Music('Vance Joy','Riptide','Dream your live away',2014)
print(song1)
print(song2)