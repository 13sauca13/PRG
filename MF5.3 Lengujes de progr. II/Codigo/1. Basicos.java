public class Basicos {

	public static void main(String[] args) {
		// La clase Math contiene un método sqrt para hacer raices cuadradas.
		double p=625;
		System.out.println(Math.sqrt(p));
		
		// Elevar un número al cuadrado y redondearlo
		System.out.println(Math.round(Math.pow(4.25, 2)));
		
		// Hallar la raiz cuadrada de la variable p y almacenar ese valor en otra variable
		double q=Math.sqrt(p);
		System.out.println(q);
		
		// Imprime un valor con solo 2 decimales
		double x=4.25;
		double y=Math.sqrt(x);
		System.out.printf("%1.2f",y);
		System.out.println();
		
		//Busqueda de caracteres y trabajo con strings
		String pedro="hola zagales";
		System.out.println(pedro.charAt(5));
	}

}
