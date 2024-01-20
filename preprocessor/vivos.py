import os

import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
from pathlib import Path

def prepare_align(config):
    corpus_path = Path(config["corpus_path"])
    test_path = Path(config["test_path"])
    test_prompt_path = Path(config["test_prompt_path"])
    train_path = Path(config["train_path"])
    train_prompt_path = Path(config["train_prompt_path"])
    mfa_data_path = Path(config["mfa_data_path"])
    
    os.makedirs(mfa_data_path, exist_ok=True)

    with open(corpus_path / train_prompt_path, 'rt') as f:
        lines = f.readlines()
        for line in tqdm(lines):
            line_parts = line.split(' ')
            spk_parts = line_parts[0].split('_')
            wav_file = corpus_path / train_path / Path(spk_parts[0]) / Path(line_parts[0] + ".wav")
            link_wav_file = mfa_data_path / wav_file.name
            if wav_file.exists() and not link_wav_file.exists():
                link_wav_file.symlink_to(wav_file.resolve())
                
            txt_file = mfa_data_path / wav_file.with_suffix("").with_suffix(".txt").name
            
            with open(txt_file, 'wt') as fw:
                fw.writelines(line.replace(f'{line_parts[0]} ','').lower())

    with open(corpus_path / test_prompt_path, 'rt') as f:
        lines = f.readlines()
        for line in tqdm(lines):
            line_parts = line.split(' ')
            spk_parts = line_parts[0].split('_')
            wav_file = corpus_path / test_path / Path(spk_parts[0]) / Path(line_parts[0] + ".wav")
            link_wav_file = mfa_data_path / wav_file.name
            if wav_file.exists() and not link_wav_file.exists():
                link_wav_file.symlink_to(wav_file.resolve())
                
            txt_file = mfa_data_path / wav_file.with_suffix("").with_suffix(".txt").name
            
            with open(txt_file, 'wt') as fw:
                fw.writelines(line.replace(f'{line_parts[0]} ','').lower())
