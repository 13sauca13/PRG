/*
 * Realizar un programa que calcule el volúmen de una caja
 */        
import java.util.*;

public class Caja {
    int alto;
    int ancho;
    int profundidad;
        
    public void setMedidas (int alto, int ancho, int profundidad) {
        this.alto=alto;
        this.ancho=ancho;
        this.profundidad=profundidad;
    }
    
    int Volumen () {
        int volumen;
        volumen=alto*ancho*profundidad;
        return volumen;
    }
}

class Caja1{
    public static void main(String[] args) {
        Caja Caja1;
        Caja1 = new Caja();
        
        //Pedimos las medidas al usuario con Scanner
        //Primero creamos el objeto de la clase Scanner
        Scanner obj1= new Scanner(System.in);
        //Enviamos el prompt al usuario
	System.out.println("Introduzca el alto");
        //Capturamos lo que el usuario escribe como entrada
        int alt=obj1.nextInt();
        
        Scanner obj2= new Scanner(System.in);
        System.out.println("Introduzca el ancho");
        int anch=obj2.nextInt();
        Scanner obj3= new Scanner(System.in);
        System.out.println("Introduzca la profundidad");
        int prof=obj3.nextInt();
        
        Caja1.setMedidas(alt, anch, prof);
        //Caja1.setMedidas(alt,anch,prof);
        System.out.println(Caja1.Volumen());
    }
}
