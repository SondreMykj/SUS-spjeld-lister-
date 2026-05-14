from list_maker import check_if_cav, check_if_zero, gk_spjeld, change_format, test_spjeld, calculator
import glob

gk_spjeld_path = 'excel_ark/GK_Spjeld.xlsx'
df = gk_spjeld(gk_spjeld_path)
er_verdi = change_format(df)

#test_spjeld_path = "excel_ark/Spjeldliste CAV ved Qbrann Bygg 11, 21, 22, 23.xlsx"
test_spjeld_path = "excel_ark/CAV_og_VAV"
filer = sorted(glob.glob(test_spjeld_path + "/*.xlsx"))






def main(fil):
    brann_spjeld = test_spjeld(fil)
    print("")
    print(fil[-19:-5])

    for_loop_count = 0
    min_value_missing = 0
    funnet_spjeld = []


    for i in range(len(er_verdi["TFM"])):
        for j in range(len(brann_spjeld["Tag"])):
            if er_verdi["TFM"][i] == brann_spjeld["Tag"][j]:

                for_loop_count += 1
                decription = brann_spjeld["Description"][j]
                tfm = er_verdi["TFM"][i]
                skal_max = brann_spjeld["Qmax"][j]
                skal_min = brann_spjeld["Qmin"][j]
                skal_brann = brann_spjeld["Qbrann"][j]
                
                nom = brann_spjeld["Qnom"][j]
                er_max = er_verdi["MAX"][i]
                er_min_prosent = er_verdi["MIN"][i]
                er_flow= er_verdi["FLW"][i]
                er_min = (nom / 100) * er_min_prosent  
                funnet_spjeld.append(tfm)

                er = er_min
                skal_cav = skal_brann
                skal_vav = skal_max

                cav_or_vav = check_if_cav(decription)

                if cav_or_vav == "CAV":
                    if check_if_zero(er, skal_cav):
                        continue
                    if calculator(er, skal_cav):
                        continue
                    print(f"{tfm}: CAV verdi er {round(er, 2)} m3/h skal ha {round(skal_cav, 2)} m3/h")

                elif cav_or_vav == "VAV":
                    if check_if_zero(er, skal_vav):
                        continue
                    if calculator(er, skal_vav):
                        continue
                    print(f"{tfm}: VAV verdi er {round(er, 2)} m3/h skal ha {round(skal_cav, 2)} m3/h")

                else:
                    if check_if_zero(er, skal_cav):
                        continue
                    if calculator(er, skal_cav):
                        continue
                    print(f"{tfm}: CAV verdi er {round(er, 2)} m3/h skal ha {round(skal_cav, 2)} m3/h... Navn ineholder ikke CAV eller VAV. Så har gått ut ifra at det er CAV")

                    
            


    print("")
    print(f"Antall spjeld funnet: {for_loop_count} av {len(brann_spjeld['Tag'])}")
    print("")
    print("Spjeld som ikke er funnet i listen fra OneCo:")
    for i in range(len(brann_spjeld["Tag"])):
        if brann_spjeld["Tag"][i] not in funnet_spjeld:
            print(brann_spjeld['Tag'][i])
            



for fil in filer:
    main(fil)
   

           