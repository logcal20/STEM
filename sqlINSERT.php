<?php

$servername = "localhost";
$username = "user";
$password = "password";
$dbname = "school";
$name = 'logan';
$age = 17;
$gradeLevel = 12;

$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("connection failed:".$conn->connect_error);
}

$sql = "INSERT INTO students (name, age, gradeLevel) VALUES ('$name', '$age', '$gradeLevel')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
