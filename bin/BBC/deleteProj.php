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
        <title>刪除專案</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>

<body>
    <table>
        <th>專案</th>
        <th>動作</th>
<?php 
    include "./header.php";
    include "./controller/db.inc";
    $conn = getConnection();
    $project = getTables($conn);
    foreach ($project as $pro) {
        echo "<tr><td>".$pro."</td><td><a href='./deleteProjProcess.php?id=".$pro."'>刪除</a></td></tr>";
    }
?>
    </table>
</body>
</html>
