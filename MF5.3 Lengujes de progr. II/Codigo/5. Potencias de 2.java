// Potencias de 2 desde 0 hasta 9

package e2t; 

public class PotenciasDe2 {

	public static void main(String[] args) {
		int exponente = 0;
		while (exponente<=9) {
			System.out.println(Math.round(Math.pow(2, exponente)));
			exponente++;
		}
	}
}
