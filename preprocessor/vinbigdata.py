import os

import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
from pathlib import Path

def prepare_align(config):
    corpus_path = Path(config["corpus_path"])
    mfa_data_path = Path(config["mfa_data_path"])
    
    os.makedirs(mfa_data_path, exist_ok=True)

    data_paths = [d for d in corpus_path.iterdir()]
    for data_path in tqdm(data_paths):
        link_file = mfa_data_path / data_path.name
        if not link_file.exists():
            link_file.symlink_to(data_path.resolve())
