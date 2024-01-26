few_shots = [
    {'Question' : "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "91"},
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': "22292"},
    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "16725.4"} ,
     {'Question' : "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?" ,
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
      'SQLResult': "Result of the SQL query",
      'Answer' : "17462"},
    {'Question': "How many white color Levi's shirt I have?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"
     },
    {'Question': "how much sales amount will be generated if we sell all large size t shirts today in nike brand after discounts?",
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike' and size="L"
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"
    },
    {'Question': "which database we are using?",
     'SQLQuery' : "SELECT database()",
     'SQLResult': "Result of the SQL query",
     'Answer' : "atliq_tshirts"
     },
     {'Question': "what's the name of our store?",
     'SQLQuery' : "SELECT database()",
     'SQLResult': "Result of the SQL query",
     'Answer' : "atliq_tshirts"
     },
     {
     'Question': "what is the number of red t-shirts do we have and also tell the brands of all of them?",
    'SQLQuery': "SELECT brand, count(*) FROM t_shirts WHERE color = 'Red' GROUP BY brand",
    'SQLResult': "Result of the SQL query",
    'Answer': "Van Huesen : 4, Levi : 3 , Nike : 4 , Adidas : 5"
     },
    {
    'Question': "give all brands name and average t-shirt price of all brands",
    'SQLQuery': "SELECT brand, count(*), avg(price), as avg_price from t_shirts GROUP BY brand",
    'SQLResult': "Result of the SQL query",
    'Answer': "Van Huesen : 32.8571, Levi : 24.7143, Nike : 25.6154, Adidas : 34.1765"
    }

]
