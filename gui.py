import pygame
from parse_midi import parse_midi_file

WHITE_KEY_SEMITONES = [0, 2, 4, 5, 7, 9, 11]
BLACK_KEY_SEMITONES = [1, 3, None, 6, 8, 10, None]
BLACK_KEY_XOFFSETS  = [0.6, 1.6, None, 3.6, 4.6, 5.6, None]

WW, WH = 20, 100   # white key width / height
BW, BH = 12, 60    # black key width / height
OCTAVES = 7 # number of octaves to display
START_OCTAVE = 1

FALL_SPACE = 400 # vertical space for notes to fall before reaching the piano keys
PPS = 100 # pixels per second for falling notes, higher = taller

def build_keys():
    """Generates list of keys within the octave range and size."""
    keys = []
    for octave in range(OCTAVES):
        base_x = octave * 7 * WW
        base_note = 12 + (START_OCTAVE + octave) * 12
        for i, semi in enumerate(WHITE_KEY_SEMITONES):
            rect = pygame.Rect(base_x + i * WW, 0, WW - 1, WH)
            keys.append((rect, base_note + semi, False))
        for i, semi in enumerate(BLACK_KEY_SEMITONES):
            if semi is None: continue
            x = base_x + BLACK_KEY_XOFFSETS[i] * WW - BW // 2
            rect = pygame.Rect(x, 0, BW, BH)
            keys.append((rect, base_note + semi, True))
    return keys

def draw_notes(surface, keys, notes, curr):
    key_lookup = {note: (rect, is_black) for rect, note, is_black in keys}
    
    for note in notes[0]:
        if note['pitch'] not in key_lookup:
            continue
        
        rect, is_black = key_lookup[note['pitch']]
        
        note_bottom = FALL_SPACE - (note['start'] - curr) * PPS
        note_top    = FALL_SPACE - (note['end']   - curr) * PPS
        
        if note_bottom < 0 or note_top > FALL_SPACE:
            continue
        
        y1 = max(0, note_top)
        y2 = min(FALL_SPACE, note_bottom)
        
        width = rect.width - 2
        x = rect.x + 1
        color = (80, 180, 255) if not is_black else (50, 140, 220)
        pygame.draw.rect(surface, color, (x, y1, width, y2 - y1))
        pygame.draw.rect(surface, (30, 30, 30), (x, y1, width, y2 - y1), 1)

def draw_piano(surface, keys, active_notes):
    """Draws basic piano keys on the surface, and active notes in a different color."""
    
    for rect, note, is_black in keys:
        if is_black: continue
        shift = rect.move(0, FALL_SPACE)
        color = (80, 180, 255) if note in active_notes else (255, 255, 255)
        pygame.draw.rect(surface, color, shift)
        pygame.draw.rect(surface, (100, 100, 100), shift, 1)

    for rect, note, is_black in keys:
        if not is_black: continue
        shift = rect.move(0, FALL_SPACE)
        color = (80, 180, 255) if note in active_notes else (30, 30, 30)
        pygame.draw.rect(surface, color, shift)

def visualize_midi(midi_file: str, bg_image = None, bg_color = (40, 40, 40), name = "Piano", loop = True):
    notes = parse_midi_file(midi_file)
    pygame.init()
    keys = build_keys()
    width = OCTAVES * 7 * WW

    screen = pygame.display.set_mode((width, WH + FALL_SPACE))

    if bg_image:
        print("Loading background image:", bg_image)
        bg = pygame.image.load(bg_image)
        bg = pygame.transform.scale(bg, (width, WH + FALL_SPACE))
    
    pygame.display.set_caption(name)
    clock = pygame.time.Clock()
    active_notes = set()

    start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        curr = (pygame.time.get_ticks() - start_time) / 1000

        if curr > notes[0][-1]['end'] + 2.5: # loop back after song ends
            start_time = pygame.time.get_ticks()
            curr = 0
        
        print(curr)
        for note in notes[0]:
            if note["start"] + 0.05 < curr < note["end"]:
                active_notes.add(note["pitch"])
            elif curr >= note["end"]-0.05: # small buffer to ensure note is removed after it finishes
                active_notes.discard(note["pitch"])

        if bg:
            screen.blit(bg, (0, 0))
        else:
            screen.fill(bg_color)
        draw_notes(screen, keys, notes, curr)
        draw_piano(screen, keys, active_notes)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()