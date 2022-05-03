package stratergy;

public class StrategyPattern {
    public static void main(String[] arguments) {
        // Prepare strategies
        BillingStrategy normalStrategy    = BillingStrategy.NORMAL;
        BillingStrategy happyHourStrategy = BillingStrategy.HAPPY_HOUR;

        CustomerBill firstCustomer = new CustomerBill(normalStrategy);

        // Normal billing
        firstCustomer.add(100, 1);

        // Start Happy Hour
        firstCustomer.setStrategy(happyHourStrategy);
        firstCustomer.add(100, 2);

        // New Customer
        CustomerBill secondCustomer = new CustomerBill(happyHourStrategy);
        secondCustomer.add(80, 1);
        // The Customer pays
        firstCustomer.print();


        // End Happy Hour
        secondCustomer.setStrategy(normalStrategy);
        secondCustomer.add(130, 2);
        secondCustomer.add(250, 1);
        secondCustomer.print();
    }
}
