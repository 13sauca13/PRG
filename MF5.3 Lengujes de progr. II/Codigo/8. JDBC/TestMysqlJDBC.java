package test;

import java.sql.*

public class TestMysqlJDBC {
    public static void main(String[] args) {
        // Cadena de conexion hacia la base de datos
        //La cadena tiene el formato: jdbc:mysql//servidor:puerto/esquema? y asi deberia funcionar, aunque añadimos opciones:
        //No usaremos SSL, habilitamos la zona horaria y establecemos UTC. Finalmete, "allowPublicKeyRetrieval" está en desuso, pero evita problemas con librerias antiguas
        var url = "jdbc:mysql//localhost:3306/e2t?useSSL=false&useTimezone=true&serverTimezone=UTC&allowPublicKeyRetrieval=true";
        
        try {
            Class.forName("com.sql.cj.jdbc.Driver");
            // al getConnection hay que darle como argumentos la url, el usuario y la contraseña
            Connection conexion = DriverManager.getConnection(url,"admin","admin");
        } catch (ClassNotFoundException | SQLException ex){
            ex.printStackTrace(System.out);
        }
    }
}
