

class Main{
    public static void main(String[] args) {
        UberX uberx = new UberX("erg", new Account(3,"er","erg","email","erger"), "Chevrolet", "2022");
        uberx.setPassenger(2);
        System.out.println(uberx.getPassenger());

        UberVan uberV = new UberVan("WAS45", new Account(34, "erg", "34dfg", "@email", "gdsfgg"));
        extracted(uberV);
        System.out.println(uberV.getPassenger());
    }

    private static void extracted(UberVan uberV) {
        uberV.setPassenger(6);
    }

}