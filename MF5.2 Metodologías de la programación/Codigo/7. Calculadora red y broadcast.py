class Calculadora:
    def __init__(self,ip,mascara):
        oct_1=ip.partition(".")
        oct_2=oct_1[2].partition(".")
        oct_3=oct_2[2].partition(".")
        oct_4=oct_3[2]
        self.ip=[(oct_1[0]),(oct_2[0]),(oct_3[0]),(oct_4[0])]
        oct_1=mascara.partition(".")
        oct_2=oct_1[2].partition(".")
        oct_3=oct_2[2].partition(".")
        oct_4=oct_3[2]
        self.mascara=[(oct_1[0]),(oct_2[0]),(oct_3[0]),(oct_4[0])]

    def ip_red(self):
        red=[]
        for i in range(4):
            red.append(str(int(self.ip[i])&int(self.mascara[i])))
        return(".".join(red))

    def broadcast(self):
        broadcast=[]
        for i in range(4):
            broadcast.append(str(int(self.ip[i])|~int(self.mascara[i])&255))
        return(".".join(broadcast))

    @staticmethod
    def prefijo_a_mask(prefijo):
        prefijo=int(prefijo)
        oct=prefijo//8
        i=0
        mascara=[]
        while i<oct:
            mascara.append("255")
            i+=1
        oct2=prefijo%8
        if oct2!=0:
            oct22=128
            oct2-=1
            x=128
            while oct2>0:
                oct22+=(x//2)
                x//=2
                oct2-=1
            mascara.append(str(oct22))
        while len(mascara)<4:
            mascara.append("0")
        return(".".join(mascara))


ip=input("Introduzca la la dirección IP: ")
mascara=input("Introduzca la máscara de subred (enprefijo u octetos decimales): ")

if len(mascara)>7:
    red1=Calculadora(ip,mascara)
elif 1<=int(mascara)<=32:
    red1=Calculadora(ip,Calculadora.prefijo_a_mask(mascara))
else:
    print("No es posible crear su red, compruebe los datos")

if ip==red1.ip_red():
    print(f"\nLa IP {ip} que ha introducido, con máscara {mascara} se corresponde con una dirección de red")
elif ip==red1.broadcast():
    print(f"\nLa IP {ip} que ha introducido, con máscara {mascara} se corresponde con la dirección de broadcast para la red {red1.ip_red()}")
else:
   print(f"\nLa IP {ip} que ha introducido, con máscara {mascara} se corresponde con una dirección de host.\nLa dirección de red con esos datos es {red1.ip_red()} con broadcast {red1.broadcast()}")
