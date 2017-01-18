<?php

function parseJson($json,$dbValue){
    $json_array = json_decode($json,true);
    $result = array();
    $data = $json_array["data"];
    $max = sizeof($data);
    $result = "<table><th>Section值</th><th>註解</th><th>版本</th>";
    //$flag = false;

    foreach($dbValue as $val){
	$flag = false;
        for($i=0; $i<=$max;$i++){
            if ($data[$i]["section"] == $val["section"]){
                $result = $result.'<tr><td>'.$data[$i]["section"].'<br>'.$data[$i]["key_value"].'</td><td>'.$val["note"].'</td><td>'.$val["version"].'</td></tr>';
		$flag = true;
            }
        }
	if(!$flag){
        	$result = $result.'<tr><td>在提供的雲控中找不到'.$val["section"].'</td><td>'.$val["note"].'</td><td>'.$val["version"].'</td></tr>';
	}
    }    

    $result = $result."</table>";
    return $result;
}
