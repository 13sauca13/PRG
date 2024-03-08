# Hacer una calculadora de subnetting

# Introducción de datos
'''
ip=input("Introduce la IP: ")
mask=input("Introduce la máscara: ")
'''
'''
# Clase "Red"
class Red:
    def __init__(self,ip,mascara):
        self.ip=ip
        self.mascara=mascara

    def troceo_ip(self):
        # Corte de cada octeto de ip:
        self.oct_1=self.ip.partition(".")
        self.oct_2=self.oct_1[2].partition(".")
        self.oct_3=self.oct_2[2].partition(".")
        self.oct_4=self.oct_3[2]
        self.oct_1=self.oct_1[0]
        self.oct_2=self.oct_2[0]
        self.oct_3=self.oct_3[0]
        self.oct_4=self.oct_4[0]
        return(self.oct_1)

    def troceo_mask(self):
        # Corte de la mascara
        mask_1=self.mascara.partition(".")
        self.mask_2=self.mask_1[2].partition(".")
        self.mask_3=self.mask_2[2].partition(".")
        self.mask_4=self.mask_3[2]
        mask_1=mask_1[0]
        self.mask_2=self.mask_2[0]
        self.mask_3=mask_3[0]
        self.mask_4=self.mask_4[0]
        return(self.mask_2)      
    
    def ip_red(self):
        if troceo_ip=="192":
            return("ok")
        else:
            return("no")

    def broadcast(self):
        pass
'''
def troceo(ip):
    oct_1=ip.partition(".")
    oct_2=oct_1[2].partition(".")
    oct_3=oct_2[2].partition(".")
    oct_4=oct_3[2]
    ip=[(oct_1[0]),
        (oct_2[0]),
        (oct_3[0]),
        (oct_4[0])]
    return(ip)

def ip_red(ip,mascara):
    red=[]
    for i in range(4):
        red.append(int(ip[i])&int(mascara[i]))
    return(red)

def broadcast(ip,mascara):
    broadcast=[]
    for i in range(4):
        broadcast.append(int(ip[i])|~int(mascara[i])&255)
    return(broadcast)

def hosts_disponibles(ip,mascara):
    

ip="192.168.0.256"
mascara="255.255.0.0"

print(ip_red(troceo(ip),troceo(mascara)))
print(broadcast(ip_red(troceo(ip),troceo(mascara)),troceo(mascara)))
