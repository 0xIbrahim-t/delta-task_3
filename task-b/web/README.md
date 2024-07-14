## Web
Develop a simple web app using PHP and MySQL, including a login form that is intentionally susceptible to SQL injection.
Store a hidden flag in the database that is retrievable via this vulnerability.
Create a Python exploit script using the requests module to exploit this vulnerability, bypass the login, and retrieve the hidden flag from the database.
You need not focus much on the design of the website or its contents after the login page.
We encourage you to create and explore interesting SQL injections.


### to set up the website
> docker-compose up -d

### To get the hardcoded value which is in the string_to_value.c which is compiled to a binary file named string_to_value:
> python3 sql_injection.py


#### note
> first i tried using like 'OR '1'='1, it didnt work and i still dont know why
> then i thought of using like adding another row and creating a new user using union, but i forgot that it wont work in places idk the amount of columns the query may have and exact names of the  queries
> hence i finally thought of selecting a row that how i want it to be, and the php file will read the password from what we wanted the selected table to be  

