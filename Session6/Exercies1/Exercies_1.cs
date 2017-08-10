using System;

namespace Exercies1
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Console.Write("What is your height (cm): ");
			float height = Convert.ToInt32(Console.ReadLine ());
			height = height / 100;

			Console.Write ("What is your weight (kg): ");
			int weight = Convert.ToInt32(Console.ReadLine ());

			float BMI = (float) weight / (height * height);
			Console.WriteLine (BMI);

			if (BMI < 16)
			{
				Console.WriteLine("Severely underweight");
			}
			else if (BMI < 18.5)
			{
				Console.WriteLine("Underweight");
			}
			else if (BMI < 25 )
			{
				Console.WriteLine(" Normal ");
			}
			else if (BMI < 30)
			{
				Console.WriteLine("Overweight");
			}
			else
			{
				Console.WriteLine("Obese");
			}
		}
	}
}
