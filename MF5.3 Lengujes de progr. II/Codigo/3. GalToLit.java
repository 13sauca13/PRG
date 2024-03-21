/* Crear un programa para convertir de galones a litros.
Las variables serán de tipo Double.
Un galón equivale a 3.7854 litros
Se usará en un inicio 10 galones y al final el programa imprimirá la frase "10 galones equivale a X litros." */

package e2t;

import javax.swing.*;

public class GalToLit {

	public static void main(String[] args) {
		Double galones;
		galones= (double) 10;
		
		Double litros;
		litros= galones*3.7854;
		
		System.out.printf("10 galones equivale a %1.4f litros",litros);	
	}
}

/* En lugar de poner 10 galones, el usuario introducirá por consola el valor.
Ha de aparecer en consola un mensaje para solicitar los galones
El resulktado final igual que en la primera parte */

		Scanner galones= new Scanner(System.in);
		System.out.println("Introduzca la cantidad de galones a convertir");
		Double gals = galones.nextDouble();
		Double litros = gals*3.7854;
		System.out.printf("%1.0f galones equivale a %1.4f litros",gals,litros);
	}
}

/* Sabiendo que el deposito de combustible del vshículo es de 56 litro y que consume 2 galones cada 62.13 millas,
Cuántos kilómetros puede recorer el vehículo.
El resultado será una frase con la distancia a 2 decimales */
		Double deposito = (double) 56;
		Double depositoGal = deposito/3.7854;
		Double consumo = (double) 2;
		Double distancia = (double) 62.13*1.609;
		Double autonomia = (double) (depositoGal/consumo)*distancia;
		
		System.out.printf("El vehículo con capacidad de depósito %1.0f litros puede recorrer %1.2f kilómetros", deposito,autonomia);
		
	}
}
