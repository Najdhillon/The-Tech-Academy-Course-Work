using System;

namespace delegateEx
{
	//Delegate

	delegate double MathAction(double num);

	class DelegateTest
	{

		static double Double(double input)
		{
			return input * 2;
		}

		static void Main()
		{

			MathAction ma = Double;

	
			double multByTwo = ma(4.5);
			Console.WriteLine("multByTwo: {0}", multByTwo);

		}

	}
}
