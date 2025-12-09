<?php
$servername="localhost:7164";
$username="joel";
$userpassword="isujel83929";
$mydatabase ="isuecha";

mysql_connect($servername,$username,$userpassword) or die ("Unable to connect server");
mysql_select_db($mydatabase);

$mypcname=php_uname('n');

$qrysemdid = mysql_query("Select * from essyuse");
$resultsemid = mysql_fetch_assoc($qrysemdid);
$usesemid = $resultsemid['ESYearIns'];

?>
