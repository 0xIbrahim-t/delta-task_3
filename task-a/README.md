# Task-A

## To start the server

> docker-compose up -d

Mukund wants to create a secure CLI multiplayer quiz game where he can challenge his imaginary friends, have a good time, and compete for a spot on the leaderboard. Let’s get started!

### 1. Make a server and client
  Use any programming language of your choice (Python is recommended) to create a client-server architecture with sockets. The server should accept multiple clients at the same time.
  Allow users to add new MCQ quiz questions with answers.
  Allow users to answer questions (not made by themselves) and add those points to the leaderboard in a DB.
  Allow users to see the leaderboard.

### 2. Add authentication
  Implement user authentication while conecting to the server.
  Allow new users to make an account with a new username and password, and securely store the password in the DB.

### 3. Dockerise the server
  Using docker-compose, dockerise the server and the db.
  Ensure that restarting Docker will not destroy the data from the database.
