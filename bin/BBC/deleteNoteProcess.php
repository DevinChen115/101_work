<?php

include "./controller/db.inc";
include "./header.php";

$section = $_GET['delSection'];
$proName = $_GET['pro'];

$conn = getConnection();
$notes = deleteSection($conn,$proName,$section);
$conn = null;
print_r($notes);
