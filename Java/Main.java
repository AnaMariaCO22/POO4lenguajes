

class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car();
        car.license="AMQ123";
        car.driver ="Andres Herrera";
        System.out.println("Car License: "+ car.license);

        Car car2 = new Car();
        car2.license="AMQ123";
        car2.driver ="Andrea Herrera";
        System.out.println("Car License: "+ car2.license);

        car.printDataCar();
        car2.printDataCar();
    }

}