using System;

namespace drillsexercise
{
	class MainClass
	{
		public static void Main(string[] args)
		{

			// Exercise 1

			int x;
			int y;
			int z;

			Console.WriteLine("Enter a value: ");
			x = int.Parse(Console.ReadLine());

			Console.WriteLine("Enter a value: ");
			y = int.Parse(Console.ReadLine());

			Console.WriteLine("Enter a value: ");
			z = int.Parse(Console.ReadLine());

			if (x > y)
				if (x > z) Console.Write("The greatest value is:{0}.", x);
				else Console.Write("The greatest value is:{0}.", z);
			else if (y > z) Console.Write("The greatest value is:{0}.", y);
			else Console.Write("The greatest value is:{0}.", z);

			//Exercise 2

			float quiz;
			float midterm;
			float final;
			float avg;

			Console.WriteLine("Enter your quiz score: ");
			quiz = float.Parse(Console.ReadLine());

			Console.WriteLine("Enter your midterm: ");
			midterm = float.Parse(Console.ReadLine());

			Console.WriteLine("Enter your final score: ");
			final = float.Parse(Console.ReadLine());

			avg = (quiz + midterm + final) / 3;

			if (avg >= 90) 
			{
					Console.WriteLine("You got an A!");
			}
			else if ((avg >= 70) && (avg <90))
				{
					Console.WriteLine("You got an B!");
				}

			else if ((avg >= 50) && (avg < 70))
			{
				Console.WriteLine("You got an C!");
			}

			else if (avg < 50)
			{
				Console.WriteLine("You got an D!");
			}

		}
	}
}
