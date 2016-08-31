using System;

namespace DeriveClassDrill
{
	//public access modifier

	class A
	{
		public int x;
		public int y;
	}

	//private access modifier

	class b
	{
		private int age;

		public int Age
		{
			get { return age; }

			set { this.age = value; }
		}
	}

	//protected

	class C
	{
		protected int x;
	}

	class D : C
	{
		public int X
		{
			get { return x; }
			set { this.x = value; }
		}
	}

	//internal

	public class BC
	{
		internal static int intM = 0;
	}

	//protected internal

	public class Tri
	{
		private int whe = 3;

		protected internal int Whe
		{
			get { return whe; }
		}
	}

	class MainClass
	{
		public static void Main(string[] args)
		{
			//public

			A aA = new A();

			aA.x = 10;
			aA.y = 10;

			Console.WriteLine(aA.x + aA.y);

			//private

			b Bb = new b();

			Bb.Age = 120;

			Console.WriteLine(Bb.Age);


			//protected

			D dd = new D();

			dd.X = 1;

			Console.WriteLine(dd.X);

			//internal

			BC bbcc = new BC();

			//cannot be accessed

			//Console.WriteLine(bbcc.intM);

			//protected internal

			Tri tt = new Tri();

			Console.WriteLine(tt.Whe);
		}
	}
}
