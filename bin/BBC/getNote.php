<?php

include "./controller/db.inc";

$proj = $_GET['pro'];
$conn = getConnection();
$notes = getValueByProject($conn,$proj);
$conn = null;
echo json_encode($notes);
return;
//print_r(parseJson($comment,$a));
