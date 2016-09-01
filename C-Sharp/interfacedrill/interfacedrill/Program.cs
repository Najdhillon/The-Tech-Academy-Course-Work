using System;

namespace interfacedrill
{
	interface Shape
	{
		void area();
	}

	class Rectangle : Shape
	{
		void Shape.area()
		{
			
		}
	}
	 
	class MainClass
	{
		public static void Main(string[] args)
		{
			Shape ob = new Rectangle();

			ob.area();
		}
	}
}
