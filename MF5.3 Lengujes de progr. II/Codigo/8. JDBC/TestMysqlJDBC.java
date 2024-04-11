import java.sql.*;

public class TestMysqlJDBC {
    public static void main(String[] args) {
        // Cadena de conexion hacia la base de datos
        //La cadena tiene el formato: jdbc:mysql//servidor:puerto/esquema? y asi deberia funcionar, aunque añadimos opciones:
        //No usaremos SSL, habilitamos la zona horaria y establecemos UTC. Finalmete, "allowPublicKeyRetrieval" está en desuso, pero evita problemas con librerias antiguas
        var url = "jdbc:mysql://localhost:3306/e2t?useSSL=false&useTimezone=true&serverTimezone=UTC&allowPublicKeyRetrieval=true";
        
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            // al getConnection hay que darle como argumentos la url, el usuario y la contraseña
            Connection conexion = DriverManager.getConnection(url,"root","admin");
            Statement instruccion = conexion.createStatement();
            var sql = "SELECT id_persona, nombre, apellido, email, telefono FROM persona";
            ResultSet resultado = instruccion.executeQuery(sql);
            while (resultado.next()) {
                System.out.print("Id persona: " + resultado.getInt("id_persona") + " ");
                System.out.print("Nombre: " + resultado.getString("nombre") + " ");
                System.out.print("Apellido: " + resultado.getString("apellido") + " ");
                System.out.print("Email: " + resultado.getString("email"));
                System.out.print("Telefono: " + resultado.getString("telefono") + " ");
                System.out.println("");
            }
            // Al finalizar hay que cerrar las conexiones por orden inverso a como se crearon
            resultado.close();
            instruccion.close();
            conexion.close();
        } catch (ClassNotFoundException | SQLException ex){
            ex.printStackTrace(System.out);
            System.out.println("MAL");
        }
    }
}
