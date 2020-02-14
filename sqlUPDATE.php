<?php
$servername = "localhost";
$username = "user";
$password = "password";
$dbname = "school";

$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("connection failed:".$conn->connect_error);
}

$sql = "UPDATE students SET name='cole' WHERE name='logan'";
$result =$conn->query($sql);

if ($conn->query($sql) === TRUE) {
    echo "Record updated.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
