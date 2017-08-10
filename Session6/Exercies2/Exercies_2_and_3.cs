using System;

namespace Exercies2
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			// Ex 2: too ez with C#
			Console.Write ("Hello ");
			Console.Write (", my name is ");
			Console.Write ("B-max ");

			Console.WriteLine ("");
			// Ex 3 : Programs that scale
			Console.Write ("Input Colums: ");
			int colums = Convert.ToInt32(Console.ReadLine ()); 

			Console.Write ("Input Rows: ");
			int rows = Convert.ToInt32(Console.ReadLine ());

			for (int i = 0; i < rows; i++)
			{
				for (int j = 0; j < colums; j++) 
				{
					if (i % 2 == 0) 
					{
						Console.Write ("x*");
					} 
					else 
					{
						Console.Write ("*x");
					}
				}
				Console.WriteLine ();
			}
		}
	}
}
