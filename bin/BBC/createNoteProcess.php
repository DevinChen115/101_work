<?php
include "./controller/db.inc";
include "./header.php";

$project = $_POST['project'];
$ver = $_POST['ver'];
$section = $_POST['section'];
$note = nl2br($_POST['note']);


// $project = 'cm';
// $ver='123';
// $section='223';
// $note='許功蓋';

/*
$sql = 'INSERT INTO '.$project.'(version,section,note) 
SELECT * FROM (SELECT "'.$ver.'","'.$section.'","'.$note.'") AS tmp
WHERE NOT EXISTS(
  SELECT section FROM '.$project.' WHERE section = "'.$section.'"
) LIMIT 1';
*/

//$sql = 'INSERT INTO '.$project.' VALUES("'.$section.'","'.$ver.'","'.$note.'");';

$conn = getConnection();
print_r(insertSection($conn,$project,$section,$ver,$note));
$conn=null;
