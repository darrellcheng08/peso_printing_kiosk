<?php 
$server= 'localhost';
$username ='root';
$password = '';
$database = 'kioskdb';

$con = mysqli_connect($server, $username, $password, $database);
mysqli_select_db($con, $database);
if (!$con)
{
	die('Could not connect: ' . mysqli_error($con));
}
?>