##
# Author: Bryce Perry 
# Association: RoboGuitar Project by TeamBDC 
# at University of California Irvine 
# 03/2023
##

"""MusicalNotes.py contains:\n
Song class for constructing and saving song info into formatted data structure and for export of completed song to a .txt file.\n
Notes class which contains a dictionary of notes and frequencies and other helpful methods"""




class Song: 

    """Song class to contain notes and their timestamp for specified song item. Song class should be initialized with song name as argument.
    ie: song name should match the .mp3 or .wav file name that it is associated with (eg: song class for PurpleHaze.mp3 should have "PurpleHaze" passed as its argument). 
    method addNotes() to add one or multiple notes at a certain timestamp and (preferred) optionally their duration.
    method save() to write song name and noteList data structure to a .(?) file. File will be saved as SongName.(?) which should match the .wav or .mp3 file name."""
    def __init__ (self, songName):
        self.song= songName    
        self.noteList= []# data structure of format [[timestamp1, [[note1, duration], [note2, duration]], [timestamp2, [[note1, duration] ...]
    #adding duration of note played is optional. if duration is not added, the assumption is that it is played for 0.5 seconds 
    
    def addNotes(self, notes, timestamp, durations):#you may pass one or multiple notes, but only for one time period each.
        notes=list(notes)
        durations= list(durations)
        while(len(durations)<len(notes)):
            durations.append(0.5)
        noteDurPair=[]
        for n in range(len(notes)): 
            noteDurPair.append([notes[n], durations[n]])
        self.noteList.append([timestamp, noteDurPair])

    def save(self):
        songName = self.song +".txt"
        with open(songName, 'w') as file: 
            for timestamp, notes in self.noteList:
                note_str = " ".join([f"{n[0]},{n[1]}\t" for n in notes])
                file.write(f"{timestamp}\n {note_str}\n")
               


class Note: 
    """Contains: \n
        Array of tuples NotesFreq. foo[bar][0] = note. foo[bar][1]= fundamental frequency.
            "b" is used as symbol for "flat". sharps are not listed, as they overlap with the flats.
            eg: "D#3" will not return a value. use "Eb3" instead
        Method closestNote() to find closest note(s), given fundamental frequenc(y/ies). 
            eg: closest(165.21) will return E3. closest(123, 555) will return ['B2', 'Db5']
        Method closestFreq() does the same thing, but returns the frequency value instead of the note key
        Method closestNoteFreq() returns both as an array/ 2D array
        methods do not check if frequencies are harmonics of eachother, so they should be evaluated beforehand"""
    
    NotesFreq= [("C3" , 130.81), ("C4" , 261.63), ("C5" , 523.25),
                ("Db3", 138.59), ("Db4", 277.18), ("Db5", 554.37),
                ("D3" , 146.83), ("D4" , 293.66), ("D5" , 587.33),
                ("Eb3", 155.56), ("Eb4", 311.13), ("Eb5", 622.25),
                ("E2" , 82.41) , ("E3" , 164.81), ("E4" , 329.63), ("E5" , 659.25),
                ("F2" , 87.31) , ("F3" , 174.61), ("F4" , 349.23), ("F5" , 698.46),
                ("Gb2", 92.50) , ("Gb3", 185.00), ("Gb4", 369.99), ("Gb5", 739.99),
                ("G2" , 98.00) , ("G3" , 196.00), ("G4" , 392.00),
                ("Ab2", 103.83), ("Ab3", 207.65), ("Ab4", 415.30),
                ("A2" , 110.00), ("A3" , 220.00), ("A4" , 440.00),
                ("Bb2", 116.54), ("Bb3", 233.08), ("Bb4", 466.16),
                ("B2" , 123.47), ("B3" , 246.94), ("B4" , 493.88),
                (None , 77.78), (None  , 783.99)] #frequencies below median(77.78, 82.41) can be assumed noise and return None
                                                  #frequencies above median(739.99, 783.99) can be assumed noise (or not playable) and return None
    def closestNote(self, *frequency):
        if len(frequency) == 1:
            frequency = frequency[0]
            closest = min(Note.NotesFreq, key=lambda x: abs(x[1] - frequency))
            return closest[0]
        else:
            return [self.closestNote(f) for f in frequency]

    def closestFreq(self, *frequency):
        if len(frequency) == 1:
            frequency = frequency[0]
            closest = min(Note.NotesFreq, key=lambda x: abs(x[1] - frequency))
            return closest[1]
        else:
            return [self.closestFreq(f) for f in frequency]
    def closestNoteFreq(self, *frequency):
        if len(frequency) == 1:
            frequency = frequency[0]
            closest_freq = self.closestFreq(frequency)
            closest_note = self.closestNote(closest_freq)
            return [closest_note, closest_freq]
        else:
            return [self.closestNoteFreq(f) for f in frequency]
        

nt=Note()
print(nt.closestNote( 765, 762, 400, 80.1, 80.2))

sg= Song("TestSong")

durs=[1,1,2,3]
nts=nt.closestNote( 765, 762, 400, 80.1, 80.2)
sg.addNotes(notes=["A4", "B4", "A3", "B3" ], durations=durs, timestamp=2.11)
sg.addNotes(nts, durations=[1], timestamp=3.35)
##print(sg.noteList)
sg.save()