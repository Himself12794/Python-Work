from FileUtilities import openFileReadRobust
from csc220a3 import text2notes
from music import *

source = openFileReadRobust ()
notes = text2notes (source.read ())
source.close ()
rhythms = [SN] * len (notes)

theme = Phrase ()   
theme.addNoteList (notes, rhythms)

Write.midi (theme, 'mysong.mid')
Play.midi (theme)