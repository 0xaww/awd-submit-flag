<?php
$token = $_POST['token'];
$flag = $_POST['flag'];
//print_r($username);
if($flag == "flag{123123}")
{
echo "ÄúµÄtoken: $token <br>\n";
echo "ÄúµÄflag£º $flag <br>\n";
echo "¹¥»÷×´Ì¬: success <br>\n";
}
else
{
echo "ÄúµÄtoken: $token <br>\n";
echo "ÄúµÄflag£º $flag <br>\n";
echo "¹¥»÷×´Ì¬: failed <br>\n";
}
#print_r($_POST)
//echo "aaaa";
?>
</PRE>
</p>
