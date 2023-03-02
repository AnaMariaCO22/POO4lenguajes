import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car{
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatMaterial;

    public UberVan(String license, Account driver){
        super(license, driver);
       }
       @Override
       public void setPassenger(Integer passengers) {
           if(passengers==6){
            this.passenger=passengers;
        }else{
            System.out.println("Necesitas asignar 6 pasajeros");
        }
       }
}
