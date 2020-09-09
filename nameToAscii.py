def convert (name):
    chars=""
    for i in range(len(name)):
        tempChar = hex(ord(name[i]))
        tempChar = str(tempChar)
        tempChar = tempChar.replace('0x','')
        chars = chars + " " +tempChar
    print (chars)
    

#Meter nombre en el parámetro y ejecutar el script
convert("Jose")
