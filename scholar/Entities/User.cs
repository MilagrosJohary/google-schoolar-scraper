using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data.SqlClient;

namespace scholar.Entities
{
    public class User
    {
        public String id { get; set; }
        public String name { get; set; }
        public String image { get; set; }
        public List<Paper> papers { get; set; }
        public User(String id, String name, String image)
        {
            this.id = id;
            this.name = name;
            this.image = image;
        }
        public User()
        {

        }
        public User getUserByUsername(string username)
        {
            User user;
            SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
            builder.DataSource = "DESKTOP-RS7QS73";
            builder.UserID = "root";
            builder.Password = "root";
            builder.InitialCatalog = "WEB_SCRAPING";

            SqlConnection con = new SqlConnection(builder.ConnectionString);

            String query = "SELECT TOP (1) * FROM users WHERE name LIKE '%" + username + "%'";
            using (SqlCommand command = new SqlCommand(query, con))
            {
                con.Open();
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    reader.Read();
                    user = new User(reader.GetString(0), reader.GetString(1), reader.GetString(2));
                }
            }
            return user;
        }
    }
}