package Interface;

public class test implements interface1,interface2 {

    public void sample() {
        System.out.println("test");
    }

    public void method1() {
        System.out.println("test2");
    }

    public static void main(String[] args) {
        test instance = new test();
        instance.method1();


    }
}
