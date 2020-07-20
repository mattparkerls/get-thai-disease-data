import requests
import time
from urllib.request import urlopen

# example ระดับอำเภอ monthly cases & deaths rtf download url http://www.boe.moph.go.th/boedb/surdata/y63/Am_mcd_Cholera_63.rtf

years = ["58","59","60","61","62","63"] # last 6 years
diseases = ['STDChancroid', 'STDNSU', 'Genital_Herpes', 'Pesticide_poisoning', 'Gasvapor', 'PhysicalHazard', 'HepatitisE', 'HFM', 'CassavaPoi', 'TetanusNeo', 'Suicide', 'DHF', 'Malaria', 'TBotherorgan', 'Rabies', 'Herpes', 'Dysentery_uns', 'Chickenpox', 'DSS', 'STDLGV', 'Pediculosis', 'AFP', 'Diarrhoea', 'HepatitisC', 'Filariasis', 'TetanusExcNeo', 'Condyloma', 'Pneumoconiosis', 'Polio', 'Tropical', "Rey's", 'Measles', 'Typhoid', 'Cholera', 'HepatitisA', 'Rubella', 'Diphtheria', 'Measles_com', 'InfeciousYaws', 'HaeConjunc', 'Amoebiasis', 'HepatitisD', 'Pertussis', 'Meningitis_uns', 'Dysen_Bacillary', 'Influenza', 'DF', 'DrugPoi', 'Chikungunya', 'Liverfluke', 'Pneumonia', 'Brucellosis', 'Mumps', 'KalaAzar','Scarlet', 'Capillariasis', 'TBpulmonary', 'Genital', 'Enterovirus', 'Snake', 'Trichinosis', 'Enteric_uns', 'Syphilis', 'Heavymetal', 'ScrubTyphus', 'Botulism', 'Melioidosis', 'Japanese_B', 'Lepto', 'Gonorrhoea', 'Encep_uns', 'PUO', 'Petroleum', 'HepatitisB', 'Leprosy', 'Foodpoi', 'Zika', 'Lead', 'Dysentery_Amoebic', 'TBmeningitis', 'OtherSTI', 'Hepatitis_uns', 'Vaginal', 'Eosinophilic', 'Meningo_mening', 'Anthrax', 'AEFI', 'Mushroom', 'Streptococcus_suis']

for disease in diseases:
    for year in years:
        URL = 'http://www.boe.moph.go.th/boedb/surdata/y' + year + '/Am_mcd_' + disease + '_' + year + '.rtf'
        headers = { 
            "Referer": "http://www.boe.moph.go.th/boedb/surdata/disease.php"
        }
        # try the call
        response = requests.get(URL, headers=headers)
        print(disease+'_'+year+' status_code: '+str(response.status_code))
        if response.status_code == 404:
            continue
        else:
            start = 'y' + year + '/Am_mcd_'
            end = '.rtf'
            filename = URL[URL.find(start)+len(start):URL.rfind(end)]
            open(filename, 'wb').write(response.content)
            time.sleep(1)