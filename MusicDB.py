songs = []

def AddSong(title, artist, album):
    song = dict(Title = title, Artist = artist, Album = album) #Create song record.
    songs.append(song) #add it to the list

def GetSongNumber(number): #list song.
    try:
        int(number)
    except: 
         return None
    if(number < 1):     
        return None
    if((number // 1) > songs.count):
        return None
    else:    
        return songs[(number // 1) -1]
        


