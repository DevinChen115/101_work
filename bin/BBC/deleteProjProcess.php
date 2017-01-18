<?php
include "./controller/db.inc";
include "./header.php";

$project = $_GET['id'];
$conn = getConnection();
print_r(deleteProject($conn,$project));
$conn=null;
