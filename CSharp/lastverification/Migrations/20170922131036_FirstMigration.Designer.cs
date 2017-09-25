using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using beltexam.Models;

namespace beltexam.Migrations
{
    [DbContext(typeof(beltexamContext))]
    [Migration("20170922131036_FirstMigration")]
    partial class FirstMigration
    {
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
            modelBuilder
                .HasAnnotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.SerialColumn)
                .HasAnnotation("ProductVersion", "1.1.2");

            modelBuilder.Entity("beltexam.Models.Auction", b =>
                {
                    b.Property<int>("AuctionId")
                        .ValueGeneratedOnAdd();

                    b.Property<int>("Bid");

                    b.Property<string>("CreatedUser");

                    b.Property<DateTime>("Created_at");

                    b.Property<string>("Description");

                    b.Property<DateTime>("EndDate");

                    b.Property<string>("HighestBidder");

                    b.Property<int>("MinimumBid");

                    b.Property<string>("ProductName");

                    b.Property<DateTime>("Updated_at");

                    b.HasKey("AuctionId");

                    b.ToTable("Auctions");
                });

            modelBuilder.Entity("beltexam.Models.User", b =>
                {
                    b.Property<int>("UserId")
                        .ValueGeneratedOnAdd();

                    b.Property<DateTime>("Created_at");

                    b.Property<string>("FirstName");

                    b.Property<string>("LastName");

                    b.Property<string>("Password");

                    b.Property<DateTime>("Updated_at");

                    b.Property<string>("Username");

                    b.Property<int>("Wallet");

                    b.HasKey("UserId");

                    b.ToTable("Users");
                });
        }
    }
}
