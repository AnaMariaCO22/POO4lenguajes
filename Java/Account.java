public class Account {
    Integer id;
    String name;
    String document;
    String email;
    String password;

    public Account( Integer id,String name,String document,String email,String password){
        this.id=id;
        this.name=name;
        this.document=document;
        this.email=email;
        this.password=password; 
    }

        void printDataCar(){
        System.out.println("Id: "+ this.id + "Name Driver: "+this.name + "Document: "+this.document+ "Email: "+this.email+ "Password: "+this.password);
    }
        
}
