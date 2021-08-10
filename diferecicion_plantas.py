def preg (text):
  rta = input (f"{text} si(s) no (n): ")
  if rta.startswith("s"):
        return True 
  elif rta.startswith("n"):
        return False 
  else:
        print(f"valor inbalido \"{text}\" intete otra vez")
        preg(text)

ovada = preg("la forma es ovada")
if ovada:
    entera = preg("el mages es entero")
    if entera:
        hoja_compuesta = preg("es una hoja compuesta")
        if hoja_compuesta:
            print("es un fresno comun")
        else:
            print("es una haya faya jaya")
    elif not entera:
        
        if preg("el magen es dentado"):

            print("es una aladierno aladierna")
        elif preg("es de mahen lobado"):

            print("es un araoble albar carbuyu montes")

        elif preg("el magen es espinozo"):
            print("es un acebo acebo carrasco,xardon")
elif not ovada:
    lineal = preg("es de forma lineal")
    if lineal:
        compuesta = preg("es una hoja compuesta")
        if compuesta:
            paripinado = preg("la hoja es paripinada")
            if paripinado:
                print("es tejo texu, teixo")
            elif not paripinado:
                print("es una serbal silvestre capudre alcafrenu")
        elif not compuesta:
            entero = preg("es de magen entero")
            if entero:
                print("es una madroño yerbode, borranchinal")
            elif not entero:
                print("es una laurel llereu")
    elif not lineal:
        if preg("es de forma cuneada"):
            if preg("es entera"):
                print("es salguera negra salguera")
            else:
                print("es una carbayo carbayu")

        elif preg("es de forma obicular"):
            if preg("es lobulado"):
                print("also humerus")

            elif preg("es de magen espinozo"):
                print("es una avellano ablanu")

        elif preg("es de forma obtusa"):
            print("es una abedul bedul, abedurlu")

        elif preg("es de forma palmeada"):
            print("es una espinera blesca")
        
        elif preg("es de forma triangular"):
            print("es una hoja grande tiar tilero teja")

        elif preg("es de forma cordada"):
            print("es una carraca ancina")

        elif preg("es de forma eliptica"):
            print("sauco xubugo,benito")

        elif preg("es labulada"):
            print("es una rebollo rebolu sanplego")





        

        