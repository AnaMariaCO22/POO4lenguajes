

class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ123",new Account("Andrea Herrera","AND123"));
        System.out.println("Car License: "+ car.license);

        Car car2 = new Car("AMQ23",new Account("Andrea Herrera", "AMQ12339846"));
        System.out.println("Car License: "+ car2.license);

        car.printDataCar();
        car2.printDataCar();
    }

}