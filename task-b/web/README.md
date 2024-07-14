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

