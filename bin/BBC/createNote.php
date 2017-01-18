<html>
	<head>
		<title>新增Section註解</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	</head>

<body>
<?php include "./header.php" ?>
	<form action='createNoteProcess.php' method='post'>
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
		</select><br>
		apk version: <input type="text" name="ver"><br>
		Section: <input type="text" name="section"><br>
		Note: <textarea rows="30" cols="80" name="note"></textarea>
		<input type="submit" value="create Section">
	</form>
</body>
</html>
