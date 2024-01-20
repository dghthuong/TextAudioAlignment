import os
import glob
import sys

# old_path = 'preprocessed_data/infore/TextGrid/infore1'
# new_path = 'preprocessed_data/infore/TextGrid/infore/'

old_path = sys.argv[1]
new_path = sys.argv[2]

def fix_grid(in_file, out_file):
    if os.path.exists(in_file):
        with open(in_file, 'r', encoding='utf-8') as fin:
            with open(out_file, 'w', encoding='utf-8') as fout:
                is_start = False
                for line in fin:
                    if is_start:
                        if 'text = ""' in line:
                            fout.write(line.replace('text = ""', 'text = "sp"').rstrip() + '\n')
                        else:
                            fout.write(line.rstrip() + '\n')
                    else:
                        if 'name = "phones"' in line:
                            is_start = True
                        fout.write(line.rstrip() + '\n')
                print(' - Fixed: ', os.path.basename(in_file))



# for textgrid in os.listdir(old_path):
#     fin = os.path.join(old_path, speaker, textgrid)
#     if os.path.isfile(fin):
#         fout = os.path.join(new_path, speaker)
#         os.makedirs(fout, exist_ok=True)
#         fout = os.path.join(fout, textgrid)
#         fix_grid(fin, fout)
        
grids = glob.glob(old_path+'/**/*.TextGrid', recursive=True)

if not os.path.exists(new_path):
    os.makedirs(new_path)

for fin in grids:
    if os.path.isfile(fin):
        fout = os.path.join(new_path, os.path.basename(fin))
        fix_grid(fin, fout)

print('Done!')