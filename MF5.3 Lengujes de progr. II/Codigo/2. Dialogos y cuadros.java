package e2t;

import javax.swing.*;

public class Prueba {

	public static void main(String[] args) {
		String pepe;
		pepe=JOptionPane.showInputDialog("Escoje uno de estos colores:\nRosa \nAzul \nVerde \nGris");
		
		switch(pepe) {
		case "Rosa":
			JOptionPane.showMessageDialog(null, "El rosa es un color muy gay");
			break;
		case "Azul":
			JOptionPane.showMessageDialog(null, "El razul es el color del mar");
			break;
		case "Verde":
			JOptionPane.showMessageDialog(null, "El varde me gusta");
			break;
		case "Gris":
			JOptionPane.showMessageDialog(null, "Ese color es demasiado sosos");
			break;
		default:
			JOptionPane.showMessageDialog(null, "Ese color no estaba en la lista");
			break;
		}
	}

}
