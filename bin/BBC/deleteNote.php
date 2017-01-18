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
        <title>刪除Section註解</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
    </head>

<body>
    <?php include "./header.php" ?>
    選擇專案:
    <select id="project">
        <option value="">請選擇</option>
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
    <table id="notes">
        <script>
        $(function(){
            $('#project').change(function(){
                var proj = $('#project').val()
                $('#notes').empty().append("<th>Section</th><th>Note</th><th>Action</th>");
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
                            $('#notes').empty().append("");
                        }
                        while(i < jsonObj.length){
                            $("#notes").append("<tr><td>"+jsonObj[i]['section']+"</td><td>"+jsonObj[i]['note']+"</td><td><a href='./deleteNoteProcess.php?pro="+proj+"&delSection="+jsonObj[i]['section']+"'>刪除</a></td></tr>");
                            i++
                        }
                    },
                    error: function(xhr, status,msg){
                        console.error(msg);
                    }
                })
            });
        });
        </script>
    </table>
</body>
</html>