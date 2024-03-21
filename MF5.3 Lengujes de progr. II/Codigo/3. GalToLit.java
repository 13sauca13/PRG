// Crear un programa para convertir de galones a litros.
// Las variables serán de tipo Double.
// Un galón equivale a 3.7854 litros
// Se usará en un inicio 10 galones y al final el programa imprimirá la frase "10 galones equivale a X litros."

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
