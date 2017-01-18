<html>
    <head>
        <style>
            table {
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            td, th {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }

            tr:nth-child(even) {
                background-color: #dddddd;
            }
        </style>
        <title></title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>

<body>
<?php
error_reporting(0);
include "./controller/db.inc";
include "./controller/parse.inc";
include "./header.php";
$project = $_POST['project'];
$comment = $_POST['comment'];

$conn = getConnection();
$allDBValue = getValueByProject($conn,$project);
$conn = null;

print_r(parseJson($comment,$allDBValue));
?>
</body>
</html>