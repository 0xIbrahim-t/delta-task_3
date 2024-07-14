<?php
$con = mysqli_connect("localhost", "root", "password", "users_db") or die("Connection Failed");
session_start();

if ($_SERVER['REQUEST_METHOD'] == "POST"){
    $username = $_POST["username"];
    $password = $_POST["password"];

    $result = mysqli_query($con, "select * from users where username = '$username'");

    if ($result && mysqli_num_rows($result) > 0){
        $user_data = mysqli_fetch_assoc($result);
        if ($user_data['password'] == $password){
            $_SESSION['username'] = $user_data['username'];
            header("Location: flag.php");
            die;
        }
        else{
            echo "incorrect password";
        }
    }
    else{
        echo "user does not exist";
    }
}
?>
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <div class="card" style="margin-top: 8%; margin-left: 18%; margin-right: 18%;margin-bottom: 10%; width: auto;">
        <div class="card-header">
          <h2 style="font-weight: bold; text-align: center;">Login</h2>
        </div>
        <div class="card-body">
            <form method="POST">
                <div class="form">
                    <label for="username">username:</label>
                    <input type="text" name="username" class="form-control" id="floatingInput" required>
                </div>
                <br>
                <div class="form">
                    <label for="password">password:</label>
                    <input type="password" name="password" class="form-control" id="floatingInput" required>
                </div>
                <br>
            <div class="text-center">
                <button type="submit" class="btn btn-primary">Login</button>
            </div>
            </form>
        </div>
    </div>
  </body>
</html>
