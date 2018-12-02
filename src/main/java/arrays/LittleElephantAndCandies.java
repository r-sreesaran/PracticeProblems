package main.java.arrays;

import java.math.BigInteger;

class LittleElephantAndCandies {

     static void isItpossible(String params[],String candiesSplit[]) {

        BigInteger candy = BigInteger.valueOf(Long.getLong(params[0]));
        BigInteger elephants = BigInteger.valueOf(Long.getLong(params[1]));
        BigInteger totalCandies=BigInteger.valueOf(0);
        if(candy.compareTo(elephants)<=0) {
            System.out.println("No");
            return;
        }

        for(String value: candiesSplit) {
            totalCandies = totalCandies.add(BigInteger.valueOf(Long.valueOf(value))) ;
        }
        if(totalCandies.compareTo(elephants)>=0) {
            System.out.println("No");
            return;
        }
        System.out.println("Yes");
    }

    public static void main(String args[]) {
        BigInteger totalNoOfTestcases=BigInteger.valueOf(Long.valueOf(args[0]));
        String params[] = args[1].split("");
        String candiesSplit[] = args[2].split("");

        if(BigInteger.valueOf(candiesSplit.length).compareTo(BigInteger.valueOf(Long.valueOf(params[1])))<0) {
            System.out.println("No");
            return;
        }
        isItpossible(params,candiesSplit);

    }
}
