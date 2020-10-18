<?php
$token = $_POST['token'];
$flag = $_POST['flag'];
//print_r($username);
if($flag == "flag{123123}" || $flag == "flag{223223}")
{
echo "your token: $token <br>\n";
echo "your flag: $flag <br>\n";
echo "attack status: success <br>\n";
}
else
{
echo "your token: $token <br>\n";
echo "your flag: $flag <br>\n";
echo "attack status: failed <br>\n";
}
#print_r($_POST)
//echo "aaaa";
?>
</PRE>
</p>
