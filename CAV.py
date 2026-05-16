from list_maker import check_if_zero, gk_spjeld, change_format, test_spjeld, calculator

gk_spjeld_path = 'excel_ark/GK_Spjeld.xlsx'
df = gk_spjeld(gk_spjeld_path)
er_verdi = change_format(df)

test_spjeld_path = "excel_ark/Spjeldliste CAV ved Qbrann Bygg 11, 21, 22, 23.xlsx"



def main(fil):
    brann_spjeld = test_spjeld(fil)
    print("")
    print(fil[-24:-5])

    for_loop_count = 0
    value_missing = 0
    spjeld_type_mangler = 0
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
                er_max_prosent = er_verdi["MAX"][i]
                er_min_prosent = er_verdi["MIN"][i]
                er_flow= er_verdi["FLW"][i]
                funnet_spjeld.append(tfm)
                if isinstance(nom, int):
                    er_min = (nom / 100) * er_min_prosent  
                    er_max = (nom / 100) * er_max_prosent
                else:
                    value_missing += 1
                    continue


                if "CAV" in decription.upper():
                    if check_if_zero(er_min, skal_brann):
                        print(f"{tfm} {check_if_zero(er_min, skal_brann)}")
                    elif calculator(er_min, skal_brann):
                        print(f"{tfm} {calculator(er_min, skal_brann)}")

                elif "VAV" in decription.upper():
                    if check_if_zero(er_min, skal_min):
                        print(f"{tfm} {check_if_zero(er_min, skal_min)}")
                    elif calculator(er_min, skal_min):
                        print(f"{tfm} {calculator(er_min, skal_min)}")
                
                else: 
                    if check_if_zero(er_min, skal_brann):
                        print(f"{tfm} {check_if_zero(er_min, skal_brann)}")
                    elif calculator(er_min, skal_brann):
                        print(f"{tfm} Spjeld type ikke funnet i beskrivelse, sjekker mot CAV verdi. {calculator(er_min, skal_brann)}")
                    
            


    print("")
    print(f"Antall spjeld funnet: {for_loop_count} av {len(brann_spjeld['Tag'])}. Spjeld uten nom {value_missing} Spjeld uten CAV eller VAV i beskrivelse {spjeld_type_mangler}")
    
    if len(brann_spjeld["Tag"]) != len(funnet_spjeld):
        print("")
        print("Spjeld som ikke er funnet i listen fra OneCo:")
        for i in range(len(brann_spjeld["Tag"])):
            if brann_spjeld["Tag"][i] not in funnet_spjeld:
             print(brann_spjeld['Tag'][i])
            



main(test_spjeld_path)