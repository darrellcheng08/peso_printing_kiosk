<?php 
$filename = $_FILES["file"]["name"];
move_uploaded_file($_FILES["file"]['tmp_name'], $filename);
shell_exec('libreoffice --convert-to pdf /var/www/html/printingkiosk/file/' . $filename);
$count = shell_exec('python countpages.py ' . $filename);
echo $count;
?>