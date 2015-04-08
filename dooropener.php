<html>
<head>
<link rel="apple-touch-icon" href="door-icon.png">
</head>
Oeffne Tuer...
<?php
$result = exec("sudo /usr/lib/cgi-bin/dooropener.py", $output);
?>
<br/>Tuer geoeffnet.
</html>
