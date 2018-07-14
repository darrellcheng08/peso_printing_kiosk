<?php
include "connection.php";
include "smsGateway.php";

if(isset($_POST['btnprint']))
{
	$filename = $_FILES["txtfilename"]["name"];
	$pages = $_POST['txtpages'];
	$numcopy = $_POST['txtnumcopy'];
	$color = $_POST['txtcolor'];
	$credits = $_POST['txtcredits'];
	move_uploaded_file($_FILES["txtfilename"]['tmp_name'], "file/" . $filename);
	// shell_exec('python /home/pi/printingkiosk/coin.py ' . $filename . ' ' . $pages . ' ' . $numcopy);
	$total = $numcopy * $pages;
	$q = mysqli_query($con, "SELECT * FROM papertbl limit 1");
	$rows = mysqli_fetch_array($q);
	$nopaper = $rows['numberpaper'];

	if($total >= $nopaper)
	{
		$smsGateway = new SmsGateway('cheng.darrell12@gmail.com', 'basacheng');
		$deviceID = 46481;
		$number = '+639150025592';
		$mess = 'Empty Paper.';
		$smsGateway->sendMessageToNumber($number, $mess, $deviceID);
		?><script> alert("Empty Paper."); window.location = "flashdrive.php"; </script><?php
	}
	else
	{
		if($credits >= $total)
		{
			require_once('PrintIpp/PrintIPP.php');
			$ipp = new PrintIPP();
			$ipp->setHost("localhost");
			$ipp->getPrinters();
			$uri = $ipp->available_printers[0];
			$ipp->setPrinterURI($uri);#"/printers/epson"
			$ipp->setCopies($numcopy);
			$ipp->setData("file/".$filename);
			$ipp->getPrinterAttributes();
			/* Cups defines an attribute "printer -type" */
			if ($color == 'print-black')
			{
				$ipp->setAttribute($ipp->printer_attributes->printer_type->_value2, "print-black");
			}else{
				$ipp->setAttribute($ipp->printer_attributes->printer_type->_value3, "print-color");
			}
			$ipp->printJob();

			mysqli_query($con, "INSERT INTO salestbl(filename,credits,dateprint)VALUES('$filename','$credits','"+date("M d, Y")+"')");
			$totapaper = $nopaper - $total; 
			mysqli_query($con, "UPDATE papertbl SET numberpaper='$totapaper'");
			?><script> alert("Successfully print."); window.location = "flashdrive.php"; </script><?php

		}else{
			?><script> alert("Kulang ang pera mu."); window.location = "flashdrive.php"; </script><?php
		}
	}
}

if(isset($_POST['btnupdatepaper']))
{
	$nopaper = $_POST["numberpaper"];
	mysqli_query($con, "UPDATE papertbl SET numberpaper='$nopaper'");
	header("location: admin.php");
}

if(isset($_POST['btnpreview']))
{
	$filename = $_FILES["txtfilename"]["name"];
	move_uploaded_file($_FILES["txtfilename"]['tmp_name'], "file/" . $filename);
	//shell_exec('python3 preview.py '. $filename);
	//shell_exec('libreoffice --show /var/www/html/printingkiosk/file/'. $filename);
	header("Content-type: application/pdf");
	header("Content-Disposition: inline; filename=file/" . $filename);
	header("Content-Transfer-Encoding: binary");
	@readfile("file/" . $filename);
	//header("location: flashdrive.php");
}

if(isset($_POST['getCredits']))
{
	$count = shell_exec('python D:\Desktop\printingkiosk\coin.py');
	echo $count;
}

if(isset($_POST['makediscoverable']))
{
	shell_exec('python3 /var/www/html/printingkiosk/connectbluetooth.py');
}
?>