using System;
namespace StringApplication
{
   

   class StringProg
   {
      static void Main(string[] args)
      {
         //String class

         string str1 = "This is test";
         string str2 = "This is text";

         Console.WriteLine("String lenght: " + str1.lenght);

         //String Builder

         StringBuilder builder = new StringBuilder();
            
         for (int i = 0; i < 10; i++)
         {
             builder.Append(i).Append(" ");
         }
         Console.WriteLine(builder);
      }
   }
}