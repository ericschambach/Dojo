using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore.Migrations;

namespace userdashboard.Migrations
{
    public partial class SecondMigration : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "user_level",
                table: "Users",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "user_level",
                table: "Users");
        }
    }
}
