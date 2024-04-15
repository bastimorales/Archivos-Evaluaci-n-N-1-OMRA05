numero = int(input("Introduzca el numero de ACL que desea crear ->"))

if numero>=1 and numero<=99:
    print ("La ACL",numero,"corresponde a una ACL estandar")
elif numero>=100 and numero <=199:
    print ("La ACL",numero,"corresponde a una ACL extendida")
else:
    print ("La ACL",numero,"no corresponde a una ACL estandar ni extendida")