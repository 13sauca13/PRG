public class Figura {
    private String codigo;
    private double precio;
    
    public Figura() {    
        Superheroes superheroe;
        superheroe = new Superheroes();
        Dimension dimensiones;
        dimensiones = new Dimension();   
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return ("Pruebas");
    }
    
    public double subirPrecio(double cantidad) {
        this.precio = this.precio+cantidad;
    }
    
}
