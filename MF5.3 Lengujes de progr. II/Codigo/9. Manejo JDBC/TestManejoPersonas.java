package test;

import datos.*;
import java.util.*;
import domain.*;

public class TestManejoPersonas {
    public static void main(String[] args) {
        PersonaDAO personaDAO = new PersonaDAO();
        List<Persona> personas = personaDAO.seleccionar();
        //Persona personaNueva = new Persona ("Carlos", "Espada", "carlos@mail.com", "123456789");
        //Persona personaModificar = new Persona (1, "Sofia", "Garcia", "sofia@email.com", "123456789");
        Persona personaBorrar = new Persona(1);
        
        //personaDAO.insertar(personaNueva);
        //personaDAO.actualizar(personaModificar);
        personaDAO.borrar(personaBorrar);
        
        for (Persona persona : personas) {
            System.out.println("Personas: " + persona);
        }
    }
}
