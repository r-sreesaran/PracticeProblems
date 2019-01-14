package main.java.threads;

import java.util.Random;

public class Threads implements Runnable {
int i =0;
    @Override
    public void run() {
        try {
            i = new Random().nextInt(1000);
            System.out.println("random number "+i);
            Thread.sleep(i);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) throws InterruptedException {
Thread sample;
        for (int i=0;i<5;i++) {
            sample = new Thread(new Threads());
            sample.start();
            //sample.join();
        }
    }
}
