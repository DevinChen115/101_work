<?php
include "./controller/db.inc";
include "./header.php";
$project = $_POST['pro'];

$conn = getConnection();
print_r(createProject($conn,$project));
$conn=null;
