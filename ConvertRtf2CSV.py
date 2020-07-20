from striprtf.striprtf import rtf_to_text
import os
import csv
import io
import re
import pandas as pd

rtfdirectory = '/path/to/rtf/files/'

for file in os.scandir(rtfdirectory):
    with io.open(os.path.expanduser(file.path), 'r', encoding='utf8', errors='ignore') as rtf_file:
        filename = os.path.basename(file).split('.')[0] + '.csv'
        output = rtf_file.read()
        txt = rtf_to_text(output)
        lines = txt.splitlines()
        tbl = []
        for line in lines:
            if not re.search(r'Report|cases|ZONE|Center', line):
                if line:
                    tbl.append(line.split('\t'))
        try:
            df = pd.DataFrame(tbl, columns=['empty', 'label', 'total_cases', 'total_death',
                'cases_01', 'death_01',
                'cases_02', 'death_02',
                'cases_03', 'death_03',
                'cases_04', 'death_04',
                'cases_05', 'death_05',
                'cases_06', 'death_06',
                'cases_07', 'death_07',
                'cases_08', 'death_08',
                'cases_09', 'death_09',
                'cases_10', 'death_10',
                'cases_11', 'death_11',
                'cases_12', 'death_12'
                ])
        except Exception:
            print ("Could not convert: " + filename)
            continue
        else:
            df.to_csv (r'/path/where/to/save/csvs/'+filename, index = False, header=True)

