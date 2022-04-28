
import java.util.Scanner;
import java.util.stream.IntStream;

public class test {
    final int COUNT_OF_APPLES;

    public test() {
        COUNT_OF_APPLES = 0;
    }

    public void houseType(String  house) {

     switch (house) {
         case "gryffindor":
             System.out.println("bravery");
             break;
         case "hufflepuff":
             System.out.println("loyalty");
             break;
         case "slytherin":
             System.out.println("cunning");
             break;
         case "ravenclaw":
             System.out.println("intellect");
             break;
         default:
             System.out.println("not a valid house");
     }
    }
    public static void main(String[] args) {

      Scanner scanner = new Scanner(System.in);
      while (scanner.hasNext()) {
          String number = scanner.nextLine();
          if(Integer.valueOf(number)==0) {
              break;
          }
          if (Integer.valueOf(number)%2==0) {
              System.out.println("even");
          }
          else {
              System.out.println("odd");
          }

      }
    }

}
