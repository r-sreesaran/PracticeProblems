package main.java.arrays;

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger;

/* Name of the class has to be "Main" only if the class is public. */
class LittleElephantAndCandies
{
    public static void main (String[] args) throws java.lang.Exception
    {

        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int j=0;j<t;j++)
        {
            BigInteger sum=BigInteger.valueOf(0);
            int N=sc.nextInt();
            //long C=sc.nextLong();
            BigInteger C=sc.nextBigInteger();
            //int a[]=new int[N];
            for(int i=0;i<N;i++)
            {
                sum=sum.add(BigInteger.valueOf(sc.nextInt()));
            }

            int c;
            c=C.compareTo(sum);

            if(c==1 || c==0)
            {
                System.out.println("Yes");
            }
            else
            {
                System.out.println("No");
            }

        }
    }
}