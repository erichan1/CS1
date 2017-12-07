//Language: Java
//Compiled Using: javac
//Input for your program will be provided from STDIN
//Print out all output from your program to STDOUT

import java.util.Scanner;

//Your submission should *ONLY* use the following class name
public class CodeConTests
{
    public static void main(String[] args)
    {
        if(isPalindrome("opipipo")) {
          System.out.println("true");
        }
        else {
          System.out.println("false");
        }
    }

    public static boolean isPalindrome(String str) {
        boolean isPal = true;
        int length = str.length();
        for(int i = 0; i<(length/2); i++) {
            if(str.charAt(i) != str.charAt(length-i-1)) {
                isPal = false;
            }
        }
        return isPal;
    }
}
