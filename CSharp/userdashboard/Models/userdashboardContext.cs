using Microsoft.EntityFrameworkCore;
 
namespace userdashboard.Models
{
    public class userdashboardContext : DbContext
    {
        public DbSet<User> Users { get; set; }
        // public DbSet<Group> Groups { get; set; }
        // public DbSet<Membership> Memberships { get; set; }
        // public DbSet<Player> Players { get; set; }
        // public DbSet<Team> Teams { get; set; }
       

        // base() calls the parent class' constructor passing the "options" parameter along
        public userdashboardContext(DbContextOptions<userdashboardContext> options) : base(options) { }
    }
}