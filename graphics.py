import pygame

#this is just here so we don't have to do dictionary-ing like in midi.py
notes = ['G', 'A', 'B', 'C', 'D', 'E', 'F']

def draw_note(surface, sharp, pos, note):
    #get rid of the octave number (we're squishing all of this into one octave
    note = note[:-1]
    #get rid of the accidental, it is irrelevant to height
    if len(note) == 2:
        minus_accidental = note[:-1]
    else:
        minus_accidental = note
    #fins our y position based on the note
    y = (540 + (8*20) - (notes.index(minus_accidental)*20))
    
    #draw the note further to the right if that's what is asked for in the pos argumet, and make the note lighter if it is to the right
    if pos == 'left':
        x = 225
        color = 1
    else:
        x = 1000
        color = (75, 75, 75)
    
    #draw our note
    pygame.draw.circle(surface, color, (x, y), 25, 7)
    #draw our sharp if necessary
    if len(note) == 2:
        surface.blit(sharp, sharp.get_rect().move([x-75, y-25]))