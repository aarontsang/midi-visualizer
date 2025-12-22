import pretty_midi
import sys

def parse_midi_file(midi_file: str):
    midi = pretty_midi.PrettyMIDI(midi_file)
    
    notes = []
    for instrument in midi.instruments:
        print(f"Instrument: {instrument.name or 'Unknown'}")

        notes.append([])
        for note in instrument.notes:
            notes[-1].append({
                "pitch": note.pitch,
                "start": note.start,
                "end": note.end,
            })
    return notes

if __name__ == "__main__":
    midi = pretty_midi.PrettyMIDI("midi_out/c-major-scale_basic_pitch.mid")
    
    notes = []
    for instrument in midi.instruments:
        print(f"Instrument: {instrument.name or 'Unknown'}")

        notes.append([])
        for note in instrument.notes:
            notes[-1].append({
                "pitch": note.pitch,
                "start": note.start,
                "end": note.end,
            })
    print(notes)