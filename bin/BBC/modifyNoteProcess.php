<?php
include "./controller/db.inc";
include "./header.php";
$project = $_POST['project'];
$section = $_POST['section'];
$note = nl2br($_POST['note']);

//$note = preg_replace( '!<br.*>!iU', "\n", $note );

$conn = getConnection();
print_r(modifySection($conn,$project,$section,$note));
$conn=null;