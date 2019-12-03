<?php
$token = $_POST['token'];
$flag = $_POST['flag'];
//print_r($username);
if($_COOKIE["team"] == "team1")
{
   if($flag == "flag{123123}")
    {
    echo "提交的token: $token <br>\n";
    echo "提交的flag: $flag <br>\n";
    echo "attack status: success <br>\n";
    }
    else
    {
    echo "提交的token: $token <br>\n";
    echo "提交的flag: $flag <br>\n";
    echo "attack status: failed <br>\n";
    } 
}
else
{
    echo "你的team cookies有问题";
}
?>
</PRE>
</p>
