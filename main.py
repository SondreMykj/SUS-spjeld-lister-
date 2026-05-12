import glob
from list_maker import gk_spjeld, change_format, test_spjeld, calculator

gk_spjeld_path = 'excel_ark/GK_Spjeld.xlsx'
test_spjeld_path = "excel_ark/del_11_nord"
filer = sorted(glob.glob(test_spjeld_path + "/*.xlsx"))



def main(fil):
    
    df = gk_spjeld(gk_spjeld_path)
    er_verdi = change_format(df)
    brann_spjeld = test_spjeld(fil)
    print("")
    print(fil[-19:-5])
    for_loop_count = 0
    min_value_missing = 0

    for i in range(len(er_verdi["TFM"])):
        for j in range(len(brann_spjeld["TFM"])):
            

            if er_verdi["TFM"][i] == brann_spjeld["TFM"][j]:

                for_loop_count += 1

                decription = brann_spjeld["Navn"][j]
                tfm = er_verdi["TFM"][i]
                
                skal_max = brann_spjeld["Qmax"][j]
                skal_min = brann_spjeld["Qmin"][j]
                skal_brann = brann_spjeld["Qbrann"][j]
                nom = brann_spjeld["Qnom"][j]

                er_max = er_verdi["MAX"][i]
                er_min_prosent = er_verdi["MIN"][i]
                er_flow= er_verdi["FLW"][i]
                er_min = (nom / 100) * er_min_prosent


                if skal_min == 0:
                    print(f"{tfm}: brann spjeld liste mangler verdi")
                    min_value_missing += 1
                elif er_min == 0:
                    print(f"{tfm}: Ingen verdier i liste fra OneCo")
                    min_value_missing += 1


                if "CAV" in decription:
                    if calculator(er_min, skal_brann):
                        continue
                    else:    
                        print(f"{tfm}: Brann verdi er {round(er_min, 2)} m3/h skal ha {round(skal_brann, 2)} m3/h")
                else:
                    continue
                    if calculator(er_min, skal_min, nom):
                        continue
                    else:
                        print(f"{tfm}: Brann verdi er {er_min} m3/h skal ha {skal_brann} m3/h")


    print(f"Antall spjeld funnet: {for_loop_count} av {len(brann_spjeld['TFM']) - min_value_missing}")
            



for fil in filer:
    main(fil)
   

           