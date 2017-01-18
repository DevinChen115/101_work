<?php
error_reporting(0);

$product=$_POST["product"];
$ver=$_POST["ver"];
//$mcc=$_POST["mcc"];
$mcc="null";
if( $_POST["mcc"] != ""){
	$mcc = $_POST["mcc"];
}

$section=$_POST["section"];
$hosts="ws.ksmobile.net";
print_r("Hosts: 152 正式的測試<br>");


$url="";
$pkg="";

//print_r("Hosts: ");
print_r("Version: ".$ver."<br>");
print_r("MCC: ".$mcc."<br>");

switch($product) {
	case "CM":
		$pkg="";
		break;
	case "KBD":
		$pkg="";
		break;
	case "CMS":
		$pkg="";
		break;
	case "PG_A":
		$pkg="";
		break;
	case "PG_I":
		$pkg="";
		break;
}

$url="https://".$hosts."/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
        "&channelid=200001&osversion=5.1&mcc=".$mcc."&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=".$pkg."&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";



/*
if(($product == "CM") && ($mcc == "")){
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=null&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.cleanmaster.mguard&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";	
}elseif (($product == "CM") && ($mcc != "")) {
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=".$mcc."&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.cleanmaster.mguard&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";
}elseif(($product == "KBD") && ($mcc == "")){
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=null&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.ijinshan.kbatterydoctor_en&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";	
}elseif (($product == "KBD") && ($mcc != "")) {
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=".$mcc."&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.ijinshan.kbatterydoctor_en&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";
}elseif(($product == "CMS") && ($mcc == "")){
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=null&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.cleanmaster.security&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";	
}elseif (($product == "CMS") && ($mcc != "")) {
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=".$mcc."&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.cleanmaster.security&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";
}elseif(($product == "PG_A") && ($mcc == "")){
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=null&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.roidapp.photogrid&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";	
}elseif (($product == "PG_A") && ($mcc != "")) {
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=".$mcc."&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.roidapp.photogrid&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";
}elseif(($product == "PG_I") && ($mcc == "")){
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=null&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.YunFang.PhotoGrid&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";	
}elseif (($product == "PG_I") && ($mcc != "")) {
	$url="https://ws.ksmobile.net/api/GetCloudMsgAdv?lan=zh_TW&apkversion=".$ver.
	"&channelid=200001&osversion=5.1&mcc=".$mcc."&device=Nexus_5X&resolution=1794*1080&mem_size=1814&pkg=com.YunFang.PhotoGrid&version=1&aid=3fbc7b3dbc9ae595&branch=google&mnc=null&gaid=null&net=1&dpi=2.625&hunter_v=22";
}
*/

$newUrl = createNewUrl($url);

$clould_result = array();
foreach($newUrl as $url){
	$clould_result[] = parseJson(getHtmlContent($url),$section);
}
?>

<pre><?php print_r(newParse($clould_result,$section)); ?></pre>
<pre><?php print_r($clould_result); ?></pre>

<?php
function createNewUrl($url){
	$result = array();
	$endOfAid = array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f");
	$splitUrl = explode("aid=",$url);

	for($i=0;$i<16;$i++){
		$splitUrl[1][15]=$endOfAid[$i];
		$result[$endOfAid[$i]] = $splitUrl[0]."aid=".$splitUrl[1];
	}
	return $result;
}


function getHtmlContent($url){ 	
	$html = file_get_contents($url);
	return $html; 
}

function parseJson($json,$section){
	$json_array = json_decode($json,true);
	$section_array = explode("|",$section);
//	print_r($section_array);
	$result = array();
	$result["aid"] = $json_array["aid"];
	$data = $json_array["data"];
	$max = sizeof($data);
	for($i=0; $i<=$max;$i++){
		foreach($section_array as $val){
			if ($data[$i]["section"] == $val){
				$result[] = $data[$i];
			}
		}
	}
	return $result;
}

function newParse($input_array,$section){
	$section_array = explode("|",$section);
	$endOfAid = array("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f");
	foreach($section_array as $item){
		$result[$item] = array();
		for($i=0;$i<=15;$i++){
			//array_push($result[$item],"aid_".$endOfAid[$i]);
			foreach($input_array[$i] as $content){
				if($content["section"] == $item){
					//array_push($content, "aid_".$endOfAid[$i]);
					//array_push($result[$item],"aid_".$endOfAid[$i],$content["key_value"]);
					$result[$item][$endOfAid[$i]] =  $result[$item][$endOfAid[$i]].$content["key_value"];
				}
			}
		}
	}
	return $result;
}
