import pretty_midi

def parse_midi_file(midi_file: str):
    midi = pretty_midi.PrettyMIDI(midi_file)    
    notes = []
    for instrument in midi.instruments:
        print(f"Instrument: {instrument.name or 'Unknown'}")

        notes.append([])
        for note in instrument.notes:
            
            start = note.start
            end = note.end
            pitch = note.pitch

            key = pretty_midi.note_number_to_name(pitch)
            notes[-1].append({
                "pitch": pitch,
                "key": key,
                "start": note.start,
                "end": note.end
            })
    return notes