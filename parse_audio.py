import sys
import logging
import os
from basic_pitch.inference import predict_and_save
from basic_pitch import ICASSP_2022_MODEL_PATH

def parse_audio_file(audio_file: str, output_midi: str):
    logger = logging.getLogger(__name__)
    logger.info(f'[AUDIO PARSING] Parsing audio file: {audio_file}')

    if not os.path.exists(output_midi):
        logger.info(f'[AUDIO PARSING] MIDI Folder does not exist. Creating: {output_midi}')
        os.makedirs(output_midi)

    predict_and_save(
        [audio_file],
        output_midi,
        save_midi=True,
        sonify_midi=False,
        save_model_outputs=False,
        save_notes=False,
        model_or_model_path=ICASSP_2022_MODEL_PATH,
    )

    logger.info(f'[AUDIO PARSING] MIDI saved to: {output_midi}')

if __name__ == "__main__":
    logging.basicConfig(filename='midi_output.log', level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    logger = logging.getLogger(__name__)
    logger.info('[AUDIO PARSING] Started')
    
    try:
        if len(sys.argv) < 2:
            logger.error('[AUDIO PARSING] No audio file provided. Please provide a .wav file as an argument.')
            logger.info('[AUDIO PARSING] Terminating...')
            sys.exit(1)

        audio_file = sys.argv[1]

        if not os.path.isfile(audio_file):
            logger.error(f'[AUDIO PARSING] File not found: {audio_file}')
            logger.info('[AUDIO PARSING] Terminating...')
            sys.exit(1)

        if not audio_file.endswith('.wav'):
            logger.error('[AUDIO PARSING] Unsupported file format. Please provide a .wav file.')
            logger.info('[AUDIO PARSING] Terminating...')
            sys.exit(1)

        logger.info(f'[AUDIO PARSING] Parsing audio file: {audio_file}')

        output_midi = 'midi_out'
        logger.info(f'[AUDIO PARSING] Saving MIDI to: {output_midi}')

        if not os.path.exists(output_midi):
            logger.info(f'[AUDIO PARSING] MIDI Folder does not exist. Creating: {output_midi}')
            os.makedirs(output_midi)

        print('Audio File:', audio_file)
        print('Output MIDI File:', output_midi)
        predict_and_save(
            [audio_file],
            output_midi,
            save_midi=True,
            sonify_midi=False,
            save_model_outputs=False,
            save_notes=False,
            model_or_model_path=ICASSP_2022_MODEL_PATH,
        )

        logger.info(f'[AUDIO PARSING] MIDI saved to: {output_midi}')
        logger.info('[AUDO PARSING] Finished')
    finally:
        logging.shutdown()