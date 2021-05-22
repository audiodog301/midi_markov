from sys import argv
from markov import find_chances, train, generate_out, Procedural
from midi import from_file, to_file
from graphics import draw_note
from mido import MidiFile
import pygame

def main(): 
    #make sure we have the right number of arguments
    if len(argv) != 3:
        print("You must enter two argumets.")
        return
        
    #this should be fairly self-explanatory if you've read the commends in markov.py
    if argv[1] == "file":
        data = from_file(MidiFile(argv[2]))
        model = find_chances(train(data, " "))
    
        result = generate_out(model, 32)
    
        to_file(result).save("result.mid")
    #ABANDON ALL HOPE. This is a mess of hardcoded values and ill-conceived formulas
    elif argv[1] == "live":
        #this should also be fairly self-explanatory.
        data = from_file(MidiFile(argv[2]))
        model = find_chances(train(data, " "))
        generator = Procedural(model)
        
        #make out window
        pygame.init()
        size = (width, height) = 1920, 1080
        screen = pygame.display.set_mode(size)
        
        #place a bunch of stuff
        staff_y = height/2
        staff_spacing = 40
        
        clef_x = 125
        
        #initialize our images
        bassclef = pygame.transform.scale2x(pygame.image.load("bassclef.png"))
        bassclefrect = bassclef.get_rect()
        bassclefrect = bassclefrect.move([0, staff_y-5])
        
        sharp = pygame.image.load("sharp.png")
        
        white = (255, 255, 255)
        
        #grab our first two notes
        notes = [generator.generate(), generator.generate()]
        
        while True:
            for event in pygame.event.get():
                #make sure the program doesn't run forever
                if event.type == pygame.QUIT:
                    exit()
            
            #draw our background
            screen.fill(white)
            
            #draw our staff
            for i in range(5):
                pygame.draw.line(screen, (125, 125, 125), (0, staff_y+(staff_spacing*i)), (width, staff_y+(staff_spacing*i)), 7)
            
            #draw our barlines
            pygame.draw.line(screen, (125, 125, 125), (clef_x, staff_y), (clef_x, staff_y + (4*staff_spacing)), 7)
            pygame.draw.line(screen, (125, 125, 125), ((width-clef_x)/2, staff_y), ((width-clef_x)/2, staff_y+(4*staff_spacing)), 7)
            
            #draw our clef
            screen.blit(bassclef, bassclefrect)
            
            #draw our notes
            draw_note(screen, sharp, 'left', notes[0])
            draw_note(screen, sharp, 'right', notes[1])
            
            #move our notes over so that the future one is present and there's a new future one
            notes[0] = notes[1]
            notes[1] = generator.generate()
            
            #render all of these changes
            pygame.display.flip()
            
            #wait a bit for the next note
            pygame.time.delay(1000)
        

if __name__ == "__main__":
	main()