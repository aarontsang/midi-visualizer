import sys
from parse_midi import parse_midi_file
from gui import visualize_midi
from parse_audio import parse_audio_file

if __name__ == "__main__":
    #python main.py -m <midi-file> -b <bg_image> -c <bg_color> -n <name> -l <loop> -a <audio-file>
    if len(sys.argv) < 2:
        print("Usage: python main.py -m <midi-file> -b <bg_image> -c <bg_color> -n <name> -l <loop> -a <audio-file>")
        sys.exit(1)
    
    midi_file = None
    bg_image = None
    bg_color = (40, 40, 40)
    name = "Piano"
    loop = True
    audio_file = None

    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == "-m":
            midi_file = sys.argv[i + 1]
        elif sys.argv[i] == "-b":
            bg_image = sys.argv[i + 1]
        elif sys.argv[i] == "-c":
            color_str = sys.argv[i + 1]
            bg_color = tuple(map(int, color_str.split(",")))
        elif sys.argv[i] == "-n":
            name = sys.argv[i + 1]
        elif sys.argv[i] == "-l":
            loop = sys.argv[i + 1].lower() == "true"
        elif sys.argv[i] == "-a":
            audio_file = sys.argv[i + 1]

    if not midi_file and not audio_file:
        print("Error: MIDI file or Audio file is required. Use -m <midi-file> or -a <audio-file> to specify the file.")
        sys.exit(1)
    
    if midi_file:
        visualize_midi(midi_file, bg_image, bg_color, name, loop)
    elif audio_file:
        #TODO: implement audio to midi conversion and visualization
        pass
        '''
         midi_file = parse_audio_file(audio_file, "midi_out/" + audio_file + "_midi")
        visualize_midi(midi_file, bg_image, bg_color, name, loop)
        '''
       