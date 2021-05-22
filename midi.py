from mido import Message, MidiTrack, MidiFile

#these dicts are kind of a silly way of doing it but i didn't want to think of a better one at the time
note_to_number = {
    'A': 21,
    'A#': 22,
    'B': 23,
    'C': 24,
    'C#': 25,
    'D': 26,
    'D#': 27,
    'E': 28,
    'F': 29,
    'F#': 30,
    'G': 31,
    'G#': 32
}

number_to_note = {
    "21": "A",
    "22": "A#",
    "23": "B",
    "24": "C",
    "25": "C#",
    "26": "D",
    "27": "D#",
    "28": "E",
    "29": "F",
    "30": "F#",
    "31": "G",
    "32": "G#",
    "33": "A",
    "34": "A#",
    "35": "B"
}

def to_file(data):
    #mido actually has really great documentation about this sort of thing starting here (https://mido.readthedocs.io/en/latest/midi_files.html#opening-a-file), so i'm not going to dive
    #deep into implementation details specifically regarding saving to and loading from midi files
    file = MidiFile()
    track = MidiTrack()
    
    data = data.split(" ")
    
    for note in data:
        #this is some fairly moronic string math to convert from letter name to midi number
        letter = note[:-1]
        number = note_to_number[letter] + (12 * int(note[-1]))
        
        track.append(Message("note_on", note=number, velocity=63, time = 480))
        
    file.tracks.append(track)
    
    return file

def from_file(file):
    output = []
    
    for message in file.tracks[3]:       
        if message.type == "note_on":
            #we take the octaves (amount of 12 that fit in) and set them aside, and then with the remainder (note number in lower octave) we find the note letter name
            (quotient, remainder) = divmod(message.note, 12)
            result = number_to_note[str(remainder + 24)] + str(quotient - 1) #here we add those extra octaves back in. the adding two octaves in one place and subtracting one later
                                                                             #lets the numbers nicely line up to the keys in number_to_note. it's SUPER weird but it seems to work so I kept it.
            output.append(result)
    
    return " ".join(output)