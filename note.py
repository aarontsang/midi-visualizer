import pretty_midi

class Note:
    def __init__(self, pitch: int, start: float, end: float):
        self.pitch = pitch
        self.start = start
        self.end = end

    @property
    def duration(self) -> float:
        return self.end - self.start
    
    def pitch_name(self) -> str:
        return pretty_midi.note_number_to_name(self.pitch)