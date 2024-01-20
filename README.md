1. Download vivos dataset
wget http://ailab.hcmus.edu.vn/assets/vivos.tar.gz
tar -xvf vivos.tar.gz

2. Download VinBigData dataset
https://drive.google.com/file/d/1vUSxdORDxk-ePUt-bUVDahpoXiqKchMx/view
Extract compressed file.

3. Update corpus_path and output path (mfa_data_path) in config/preprocess.yaml

4. python prepare_align.py ./config/preprocess.yaml 

5. mfa align -t ./temp ./mfa_data/vivos ./mfa/vi_lexicon.dict ./mfa/vi_mfa.zip ./preprocessed_data/TextGrid/vivos1

python fix_align.py preprocessed_data/TextGrid/vivos1 preprocessed_data/TextGrid/vivos

rm -r ./preprocessed_data/TextGrid/vivos1

mfa align -t ./temp ./mfa_data/vinbigdata ./mfa/vi_lexicon.dict ./mfa/vi_mfa.zip ./preprocessed_data/TextGrid/vinbigdata1

python fix_align.py preprocessed_data/TextGrid/vinbigdata1 preprocessed_data/TextGrid/vinbigdata

rm -r ./preprocessed_data/TextGrid/vinbigdata1

6. python preprocess.py ./config/preprocess.yaml 
