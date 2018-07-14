<?php

require_once('Sms.php');
require_once('Sms/Interface.php');
require_once('Sms/Dummy.php');

$pin = 1234;

$serial = new Sms_Dummy;

if (Sms::factory($serial)->insertPin($pin)
                ->sendSMS(09264668713, "test Hi")) {
    echo "SMS sent\n";
} else {
    echo "SMS not Sent\n";
}
