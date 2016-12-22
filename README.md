Setup instructions:
- Install mysql:

*sudo apt-get update*

*sudo apt-get install mysql-server*
- Create database on localhost with user=root and password=123
- For Linux *sudo apt-get install python-mysqldb* (how we did it, you have to have the package to run our code)
- go into mysql server using:

*mysql -u root -h localhost -p* with the password 123
- run the stats file using *\. stats.sql* command in mysql
- The database should now be set up.

