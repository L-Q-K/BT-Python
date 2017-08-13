using System;
using System.Linq;

namespace Exercies2
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Random r = new Random();
			Console.Write ("So phan tu: ");
			int n = Convert.ToInt32 (Console.ReadLine ());
			//Create Array:
			int[] numbersArray = new int[n];


			for (int i = 0; i < n; i++) {
				numbersArray[i]= r.Next(0, 100);
				Console.Write(" {0},", numbersArray[i] );
				}

			Console.WriteLine ();
			//Get maxNum
			int maxNumber = numbersArray.Max ();

			int x = 2;
			int greatestDivirsor = 1;
			bool divisibleCheck = true;

			//Get greatestCommonDivirsor
			while (x <= maxNumber) { 
				divisibleCheck = true;
				for (int j = 0; j < n; j++) {
					if (numbersArray[j] % x != 0){
						divisibleCheck = false; // Neu nhu co mot so khong chia het cho x thi x k phai UCLN
					}
				}

				if (divisibleCheck) {
					greatestDivirsor = x; //divisibleCheck == true thi x la mot UCLN tam thoi
				}

				x++;
			}

			Console.WriteLine ("UCLN = " + greatestDivirsor); //Vi cac phan tu la random nen chu yeu = 1 

		}
	}
}

