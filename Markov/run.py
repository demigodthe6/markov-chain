"""
This program prompts you to insert lyric urls from azlyrics.
It mixes up the lyrics and gives you a new song in the same words by using a Markov Chain Generator
"""
from fetch_data import get_data
from markov_python.cc_markov import MarkovChain
import textwrap

num = int(raw_input("How many songs do you want to mash up? "))

def get_songs():
	for i in range(num):
		mc.add_string(get_data())

mc = MarkovChain()
get_songs()
song_length = int(raw_input('How many words do you want in this song? '))
output = mc.generate_text(song_length)
output = " ".join(output)
print textwrap.fill(output,20)