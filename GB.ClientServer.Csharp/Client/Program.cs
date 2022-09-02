// создавая общее пространство имён - мы можем подключать 
namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Это наш клиент");
            OurClient ourClient = new OurClient();
        }
    }
}