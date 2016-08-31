using System;

namespace sealedclass
{
	class A
	{
		public int x = 1;
	}

	sealed class B : A 
	{
		
	}

	//class C:B
	// sealed modifier prevents C to derive from class B

	class MainClass
	{
		public static void Main(string[] args)
		{
			B ab = new B();
			Console.WriteLine(ab.x);



		}
	}
}
