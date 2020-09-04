using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data.SqlClient;

namespace scholar.Entities
{
    public class Paper
    {
        public string name { get; set; }
        public string url { get; set; }
        public string user_id { get; set; }
        public int id { get; set; }
        public int year { get; set; }
        public int cit { get; set; }

        public Paper()
        {

        }

        public List<Paper> getPapersByUserid(string user_id)
        {
            List<Paper> papers = new List<Paper>();
            SqlConnectionStringBuilder builder = new SqlConnectionStringBuilder();
            builder.DataSource = "DESKTOP-RS7QS73";
            builder.UserID = "root";
            builder.Password = "root";
            builder.InitialCatalog = "WEB_SCRAPING";

            SqlConnection con = new SqlConnection(builder.ConnectionString);

            String query = "SELECT * FROM papers WHERE user_id='" + user_id + "'";
            using (SqlCommand command = new SqlCommand(query, con))
            {
                con.Open();
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while(reader.Read())
                    {
                        Paper paper = new Paper();
                        paper.id = reader.GetInt32(0);
                        paper.name = reader.GetString(1);
                        paper.year = reader.GetInt32(2);
                        paper.cit = reader.GetInt32(3);
                        paper.url = reader.GetString(4);
                        paper.user_id = reader.GetString(5);
                        papers.Add(paper);
                    }
                }
            }
            return papers;
        }
    }
}