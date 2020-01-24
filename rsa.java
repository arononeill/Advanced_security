import java.util.*;
import java.math.*;

class rsa {
	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		int first_prime,second_prime, multiplied_prime;
		int num_minus_one,index;
		// e is the public key and d is the private key
		int e, d = 0;
		double c;
		BigInteger returned_message;

		System.out.println("Enter a number to be encrypted and decrypted using the RSA algorithm");
		int message=scanner.nextInt();
		System.out.println("Please enter the 1st prime number");
		first_prime = scanner.nextInt();
		System.out.println("Please enter the 2nd prime number");
		second_prime = scanner.nextInt();

		multiplied_prime = first_prime * second_prime;
		// num_minus_one is the multiplication of the 2 entered primes with one less value
		num_minus_one = (first_prime-1) * (second_prime-1);
		System.out.println("the value of num_minus_one = " + num_minus_one);

		for(e = 2; e < num_minus_one; e++) {
			if (gcd(e, num_minus_one) == 1) {
				break;
			}
		}
		System.out.println("e is " + e);

		for(index = 0; index <= 9; index++) {
			int z = 1 + (index * num_minus_one);
			if (z % e == 0) {
				d = z/e;
				break;
			}
		}

		System.out.println("d is " + d);
		c = (Math.pow(message,e)) % multiplied_prime;
		System.out.println("Encrypting...");
		System.out.println(c);

        /*converting int value of multiplied_prime to BigInteger. BigInteger is used for very big integer calculations
        that are outside the limit of all available primitive data types */
		BigInteger N = BigInteger.valueOf(multiplied_prime);

		//converting float value of c to BigInteger
		BigInteger C = BigDecimal.valueOf(c).toBigInteger();
		returned_message = (C.pow(d)).mod(N);
		System.out.println("Decrypting...");
		System.out.println(returned_message);

	}

	static int gcd(int e, int num_minus_one) {
		if (e == 0)
			return num_minus_one;
		else
			return gcd(num_minus_one % e, e);
	}
}