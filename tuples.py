# t = ("a","b","c")
#
# print(t)
# print(("a","b","c"))

welcome = "Welcome to my world of python" ,"Anudeep Thota" , 2020
places = "Austin","Dallas","San Marcos"
food = "pizza","Pasta","Burger","Taco"
friends = "we","are","friends"

imelda = "More Mayhem" ,"Imilda May" , 2011 ,[(1,"Song 1") , (2, "Song 2") , (3, "Song 3") , (4, "Song 4")]

album , artist , year , tracks = imelda

print(artist)
print(album)
print(year)
print(tracks)

for song in tracks:
    track , songname = song
    print("\tTrack Number {} , Track Name : {}".format(track, songname))