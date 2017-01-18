<html>
    </head>
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
        <title>修改Section註解</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
    </head>

<body>
    <form action='modifyNoteProcess.php' method='post'>
    <?php include "./header.php" ?>
    選擇專案:
    <select id="project" name="project">
        <option value="">請選擇</option>
        <?php

            include "./controller/db.inc";
            $conn = getConnection();
            $project = getTables($conn);
            foreach ($project as $pro) {
            echo '<option value="'.$pro.'">'.$pro.'</option>';
            $conn = null;
            }
        ?>
    </select><br><br>
    選擇Section:
    <select id="section" name="section">
        <option value="">請選擇</option>
    </select><br><br>
        Note:<br><br> 
        <textarea rows="30" cols="80" name="note" id="note"></textarea>
        <input type="submit" value="Modify Section">
    </form>
</body>
</html>

<script>
        $(function(){
            $('#project').change(function(){
                var proj = $('#project').val()
                $('#section').empty().append("<option value=''>請選擇</option>");
                var i = 0;
                $.ajax({
                    type: "GET",
                    url: "getNote.php",
                    data:{
                        pro: $('#project').val()
                    },
                    datatype: "json",
                    success: function(result){
                        var jsonObj = $.parseJSON(result);
                        if(result == ""){
                            $('#section').val();
                        }
                        while(i < jsonObj.length){
                            $("#section").append("<option value='" + jsonObj[i]['section'] + "'>" + jsonObj[i]['section'] + "</option>");
                            i++
                        }
                    },
                    error: function(xhr, status,msg){
                        console.error(msg);
                    }
                })
            });

            $('#section').change(function(){
                $('#note').empty();
                var i = 0;
                $.ajax({
                    type: "GET",
                    url: "getNote.php?",
                    data:{
                        pro: $('#project').val()
                    },
                    datatype: "json",
                    success: function(result){
                        var jsonObj = $.parseJSON(result);
                        if(result == ""){
                            $('#note').val();
                        }
                        while(i < jsonObj.length){
                            if(jsonObj[i]['section'] == $('#section').val()){
                                $("#note").append(jsonObj[i]['note']);
                            }
                            i++;
                        }
                    },
                    error: function(xhr, status,msg){
                        console.error(msg);
                    }
                })
            });
        });
        </script>