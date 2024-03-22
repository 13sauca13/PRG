// Crea un programa que imprima el abecedario

package e2t;

public class Abecedario {

	public static void main(String[] args) {
		char letra = 'a';
		while (letra!='z'+1) {
			System.out.println(letra);
			letra++;
		}
	}
}
