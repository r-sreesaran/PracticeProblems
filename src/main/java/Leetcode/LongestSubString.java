package Leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LongestSubString {

    public int lengthOfLongestSubstring(String s) {
        int longestLength=0;
        int length=0;
        List<String > alreadypresent = new ArrayList<String>();

        String [] characters = s.split("");
        if (characters.length==0 || characters.length ==1) {return  s.length();}

        for (String character:characters) {
           if(!alreadypresent.contains(character)) {
               length++;
               alreadypresent.add(character);
           }
           else {
               longestLength = length >longestLength ? length:longestLength;
               length =1;
               alreadypresent = new LinkedList<String>();
               alreadypresent.add(character);
           }
        }
        longestLength = length >longestLength ? length:longestLength;
        return  longestLength;
    }

    public static void main(String[] args) {
        LongestSubString lss = new LongestSubString();
        //System.out.printf("length of longest substring is" + lss.lengthOfLongestSubstring("abcabcbb"));
        LinkedList<String> sequences = new LinkedList<String>();
        sequences.add("bbbbb");
        sequences.add("pwwkew");
        sequences.add("abcabcbb");
        sequences.add("au");
        sequences.add("dvdf");
        for (String sequence:sequences) {
            System.out.println("length of longest substring of "+ sequence+" is" + lss.lengthOfLongestSubstring(sequence));
        }

    }
}
