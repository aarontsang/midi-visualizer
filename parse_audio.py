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