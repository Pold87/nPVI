from __future__ import print_function
import nPVIchanger as changer
import music21 as m21

output = "/home/pold/npvi/jap20metrical.mid"

base_path = "/home/pold/Dropbox/Uni/Radboud/Music_Cognition/nPVI/songs/"

song = m21.converter.parse(base_path + 'Japanese_folk_song.xml')

# Create a changer object
# Changer objects can manipulate the nPVI of songs
# They are constructed by passing a song (the 'old song') and
# create a 'new song' based on the chosen modifications
song_changer = changer.nPVI_changer(song)

# Incrementally find nPVI by permutating notes
# max_sd makes sure that the found song is metric,
# by specifying, that the standard deviation of successive
# beats is small.

song_changer.find_incrementally_from_lowest(20, 2.5, max_sd=0.005)

print("nPVI is: ")
print(song_changer.get_new_nPVI())

# Write song to MIDI file
song_changer.new_song.write("midi", output)
