public class UberX extends Car{
    private static final Account Account = null;
    String brand;
    String model;

    public UberX(String license,Account driver, String brand, String model){
        super(license, Account);
        this.brand = brand;
        this.model=model;
        
    }
}
