import json

AddSong(title, artist, album)= 
    print("please enter song title: ")
    print("please enter song album: ")
    print("please enter song artist: ")

GetSongNumber(number)=
    if(number < 1):     
        return None
    if((number // 1) > songs.count):
        return None
    else:    
        return songs[(number // 1) -1]
        

