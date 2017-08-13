using System;

namespace Exercies1
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.Write ("So phan tu: ");
			int n = Convert.ToInt32 (Console.ReadLine ());

			//Create List: 
			int[] decimalList = new int[n];
			int[] binaryList = new int[n];

			for (int i = 10; i < 10 + n; i++) {
				decimalList[i-10] = i*2;

				//Convert to Binary
				//Google is fcking god =))
				binaryList[i-10] = Convert.ToInt32 ( Convert.ToString (decimalList[i-10],2));
				Console.WriteLine ("Binary number of " + decimalList[i-10] + " is " + binaryList[i-10]);

			}
		}
	}
}

