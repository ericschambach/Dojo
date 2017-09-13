using System;
using System.Collections.Generic;
using System.Linq;
using DbConnection;

namespace mysqlOne
{
    class Program
    {
        static void Main(string[] args)
        {
                    // DbConnector.Execute("INSERT INTO users (FirstName,LastName,FavoriteNumber) VALUES ('Michael','Myers',31)");
                    // DbConnector.Execute("INSERT INTO users (FirstName,LastName,FavoriteNumber) VALUES ('Jason','Voorhees',13)");
                    // DbConnector.Execute("INSERT INTO users (FirstName,LastName,FavoriteNumber) VALUES ('Freddy','Krugger',666)");
                    List<Dictionary<string, object>> x = DbConnector.Query("SELECT FirstName, LastName, FavoriteNumber FROM users");
                    foreach(var i in x)
                    {
                        foreach(KeyValuePair<string,object> y in i)
                        {
                            Console.Write("{0} ",y.Value);
                        }

                        Console.WriteLine();
                    }
                    // Console.WriteLine("Hello World");
        }
    }
}
