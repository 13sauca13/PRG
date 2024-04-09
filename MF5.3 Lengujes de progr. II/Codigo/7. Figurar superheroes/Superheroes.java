public class Superheroes {
    private String nombre;
    private String descripcion;
    private boolean capa;
    
    public Superheroes() {
        
    }
    
    public Superheroes(String nombre) {
        this.nombre=nombre;
        this.capa=false;
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre=nombre;
    }
    
    public String getDescripcion() {
        return descripcion;
    }
    
    public void setDescripcion(String descripcion) {
        this.descripcion=descripcion;
    }
    
    public boolean getCapa() {
        return capa;
    }
    
    public void setCapa(boolean capa) {
        this.capa=capa;
    }
    
    @Override
    public String toString() {
        return("Nombre del superhéroe: "+nombre+"/n"+descripcion+"/n"+"Lleva capa: "+capa);
    }
}
