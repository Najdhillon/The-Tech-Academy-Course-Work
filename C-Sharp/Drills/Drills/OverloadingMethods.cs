using System;

namespace Drills
{



	class football
	{
		public string playerFirstName;
		public string playerLastName;
		public int playerNumber;
		public int yardsGain;

		//overloading method

		public int move(int num1 = 1, int num2 = 2)
		{
			return num1 + num2;
		}


		public double move(double num1 = 1, double num2 = 2)
		{
			return num1 + num2;
		}
	}

	//overriding methods

	class A
	{
		public virtual void Y()
		{
			Console.WriteLine("A.Y");
		}
	}

	class B : A
	{
		public override void Y()
		{
			Console.WriteLine("B.Y");
		}
	}

	class C : A
	{
		public void Y()
		{
			Console.WriteLine("C.Y");
		}
	}

	class MainClass
	{
		public static void Main (string[] args)
		{
			football newFootball = new football();

			//overloading example

			Console.WriteLine(newFootball.move(1, 3));

			Console.WriteLine(newFootball.move(1.2, 3.2));

			football newPlayer = new football();

			//overriding example

			A ab = new B();
			ab.Y();

			A ac = new C();
			ac.Y();

		}

	}
}
