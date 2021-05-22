# midi markov
This code will take a midi file and use a markov chain to generate semi-coherent midi data from that file.
## dependencies
An installation of Python 3 is necessary for this code to run. Additionally, you will need to install the following modules with pip:
- mido
- pygame

## usage 
You should run `main.py` from the command line. It takes two arguments:
- mode ("live" or "file")
- input midi file (path to a file you want it to process)
For example, you could run:
```
python3 main.py file input.mid
```