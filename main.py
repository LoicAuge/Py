#ch = 'Esope reste ici et se repose'
#print(len(ch))

#ch = 'Esope reste ici et se repose'
#print(ch[6:11])

#ch = 'Esope reste ici et se repose'
#print(ch[-6:])

#ch = 'Esope reste ici et se repose'
#print(ch[ch.find("i",0,len(ch))])
"""
meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s' 
tempDeg = "24°"
vitVent = "12km/h"
hum = "45%"
print(meteo %(tempDeg,vitVent,hum))
"""
"""
meteo = 'aujourd’hui, il fait %s , la vitesse du vent est %s ,l’humidité est %s' 
tempDeg = "beau"
vitVent = "faible"
hum = "correcte"
print(meteo %(tempDeg,vitVent,hum))
"""
"""
chaineA = "cette chaine"
chaineB = "contient %s caractères"
chaineC = "par contre"
chaineD = "celle-ci"
print(chaineA,chaineB %len(chaineA+chaineB))
print(chaineD,chaineB %len(chaineC+chaineB+chaineD),chaineC)
"""

chaineA = "cette chaine"
chaineB = "contient %s caractères"
chaineC = "par contre"
chaineD = "celle-ci"
chaineBnew = chaineB.replace("%s", "{}")
chaineE = chaineA + " " + chaineBnew
chaineF = chaineD + " " + chaineBnew + " " + chaineC

print(chaineE.format(len(chaineE)))
print(chaineF.format(len(chaineF)))
