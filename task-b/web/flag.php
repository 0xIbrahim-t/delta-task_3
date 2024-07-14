<?php
session_start();
if (isset($_SESSION["username"])){
    echo "you have found the flag!!!";
}
else{
    header("Location: login.php");
    die;
}
?>
