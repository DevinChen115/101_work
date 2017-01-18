<html>
    <head>
        <title>首頁</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>

<body>
<?php include "./header.php" ?>
<form action="focusCloud.php" method="post">
    Project:
        <select name='project'>
            <?php
                    include "./controller/db.inc";
                    $conn = getConnection();
                    $project = getTables($conn);
                    print_r($project);
                    foreach ($project as $pro) {
                    echo '<option value="'.$pro.'">'.$pro.'</option>';
                    $conn = null;
                    }
            ?>
        </select><br><br>
    <textarea rows="30" cols="80" name="comment"></textarea>
    <input type="submit" value="GOGO">
</form>
</body>
</html>
