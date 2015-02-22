<?php


$jData = fopen("data.json","r+");
$rawData = fread($jData,filesize("data.json"));
$data = json_decode($rawData,true);

fclose($jData);

$request = $_SERVER['REQUEST_URI']; 
$queryList = str_ireplace("/",",",$request);

$elements = str_getcsv($request,'/');
#note that elements[0] is blank



if(strcasecmp($elements[1],"corals") == 0) {
	$rMethod = $_SERVER['REQUEST_METHOD'];




	#URL sanitization
	if(count($elements) > 3) {
		if($rMethod == "GET") {
			header("404 page not found. There are no resources at that address.",true,400);
			echo "404 page not found\n";
		}
		else {
			header("400 The action could not be performed");
			echo "400 the action could not be performed\n";
		}
	}
	#If just corals/, print corals
	else if($rMethod == "GET") {
		if(count($elements) == 2 or $elements[2] == "") {
			header("emitting corals: ",true,200);
			foreach(array_keys($data["corals"]) as $label) {
				echo $label . ":\n";
				foreach(array_keys($data["corals"][$label]) as $attribute){
					echo "\t" . $attribute . ": " . $data["corals"][$label][$attribute] . "\n";
				}
			}
		}
		else{
			#search for specific coral, see if found
			$item = $elements[2];
			if(array_key_exists($item,$data["corals"])) {
				header("200 coral found",true,200);
				echo $item . ":\n";
				foreach(array_keys($data["corals"][$item]) as $attribute){
					echo "\t" . $attribute . ": " . $data["corals"][$item][$attribute] . "\n";
				}			}
			else {
				header("404 coral not found",true,404);
				echo "404 " . $item . " coral not found\n";
			}
		}
	}
	else if ($rMethod == "PUT"){
		$item = $elements[2];
		if(!array_key_exists($item,$data["corals"])) {
			#This method of getting the input from http://stackoverflow.com/questions/8945879/how-to-get-body-of-a-post-in-php
			$body = file_get_contents('php://input');
			#if no data is passed, just create
			if($body == "") {
				$data["corals"][$item]["No attributes"]="-";
			}
			else {
				#If data is added, should be at 1,3;5,7;etc
				$info = str_getcsv($body,'"');
				
				#If every attribute has a value, info should have num elements divisible by 4
				if(count($info)%4 == 1) {
					
					$index = 1;
					while($index < count($info)){
						$data["corals"][$item][$info[$index]] = $info[$index+2];
						$index = $index + 4;
					}
				}
				else{#malformed request, data cannot be oparsed
					header("400 Body could not be parsed. Are you using \" characters?",true,400);
					echo "400 The request could not be parsed. Make sure that each label has a string value, and that the labels and values are enclosed with \" characters\n";
					#too lazy to restucture program control
					exit;
				}
			}
			header("201 Successfully Added",true,201);
			echo "201: Added: " . $item . "\n";
		}
		else {
			header("409 The resource already exists",true,409);
			echo "409: " . $item . " already exists\n";
		}
		
	}
	else if ($rMethod == "DELETE") {	
		$item = $elements[2];
		if(array_key_exists($item, $data["corals"])){
			unset($data["corals"][$item]);
			header("201 Successfully deleted",true,201);
			echo "201: Deleted: " . $item . "\n";
		}
		else {
			header("409 the resource could not be deleted",true,409);
			echo "409 " . $item . " could not be deleted\n";
		}
			
	}
}
else {
	header("404 Page Not Found: cURL requests to this server must involve /corals/",true,404);
	echo "404: Requests to this server must start with /corals/\n";
}
$database = fopen("data.json","w");
fwrite($jData, json_encode($data));
fclose($jData);
?>