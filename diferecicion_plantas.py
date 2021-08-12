def preg (text):
  rta = input (f"{text} si(s) no (n): ")
  if rta.startswith("s"):
        return True 
  elif rta.startswith("n"):
        return False 
  else:
        print(f"valor inbalido \"{rta}\" intete otra vez")
        return preg(text)

print("""bienbenido a diferenciacion plantas responde
como te indica para obtener el tipo de planta""")

while True:
    print("starting".center(20,"-"))
    ovada = preg("la forma es ovada")
    if ovada:
        entera = preg("el mages es entero")
        if entera:
            hoja_compuesta = preg("es una hoja compuesta")
            if hoja_compuesta:
                print("es un fresno comun")
                continue
            else:
                print("es una haya faya jaya")
                continue
        elif not entera:
            
            if preg("el magen es dentado"):

                print("es una aladierno aladierna")
                continue
            elif preg("es de mahen lobado"):

                print("es un araoble albar carbuyu montes")
                continue

            elif preg("el magen es espinozo"):
                print("es un acebo acebo carrasco,xardon")
                continue
    elif not ovada:
        lineal = preg("es de forma lineal")

        if lineal:
            compuesta = preg("es una hoja compuesta")
            if compuesta:
                paripinado = preg("la hoja es paripinada")
                if paripinado:
                    print("es tejo texu, teixo")
                    continue
                elif not paripinado:
                    print("es una serbal silvestre capudre alcafrenu")
                    continue
            elif not compuesta:
                entero = preg("es de magen entero")
                if entero:
                    print("es una madroño yerbode, borranchinal")
                    continue
                elif not entero:
                    print("es una laurel llereu")
                    continue
        elif not lineal:
            if preg("es de forma cuneada"):
                if preg("es entera"):
                    print("es salguera negra salguera")
                    continue
                else:
                    print("es una carbayo carbayu")
                    continue

            elif preg("es de forma obicular"):
                if preg("es lobulado"):
                    print("also humerus")
                    continue

                elif preg("es de magen espinozo"):
                    print("es una avellano ablanu")
                    continue

            elif preg("es de forma obtusa"):
                print("es una abedul bedul, abedurlu")
                continue
            elif preg("es de forma palmeada"):
                print("es una espinera blesca")
                continue
                
            elif preg("es de forma triangular"):
                print("es una hoja grande tiar tilero teja")
                continue

            elif preg("es de forma cordada"):
                print("es una carraca ancina")
                continue

            elif preg("es de forma eliptica"):
                print("sauco xubugo,benito")
                continue

            elif preg("es labulada"):
                print("es una rebollo rebolu sanplego")
                continue
     