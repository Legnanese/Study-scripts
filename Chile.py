# This script is for maping through dict. the regions & it's capital cities

chile = {
    "1": "Region de Tarapaca",
    "2": "Region de Antofagasta",
    "3": "Region de Atacama",
    "4": "Region de Coquimbo",
    "5": "Region de Valparaiso",
    "6": "Region del Libertador General Bernardo O'Higgins",
    "7": "Region del Maule",
    "8": "Region del Bio Bio",
    "9": "Region de La Araucania",
    "10": "Region de Los Lagos",
    "11": "Region Aisen del General Carlos Ibanez del Campo",
    "12": "Region de Magallanes y de la Antartica Chilena",
    "13": "Region Metropolitana de Santiago",
    "14": "Region de Los Rios",
    "15": "Region de Arica y Parinacota",
}

print "Estas son las regiones de Chile: "

print "-" * 25
for key, region in chile.items():
    print "La region: %s se llama %s" % (key, region)
