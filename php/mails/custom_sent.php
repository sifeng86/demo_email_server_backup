<?php

require("class.phpmailer.php");
$email=stripslashes(trim($_POST['email']));
$message=stripslashes(trim($_POST['message']));
$key=stripslashes(trim($_POST['key']));
$json_file = file_get_contents('config.json');
$json = json_decode($json_file);
$api_key = $json->{'cachigo_key'};

if($key!=$api_key){
    exit();
}

if($email==''){
  exit();
}

$to=$email;
$subject="This is Terminal 1 assessment from Secondary Email Server:Cachigo";


$cont=
'
<body>
<strong>'.$message.'</strong>

</body>

</html>
';

$mail = new PHPMailer();
$mail->Body ='
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Messages sent from Secondary Email Server</title>

</head>
';


$mail->Body .= $cont;
$mail->IsSmtp();
$mail->Host     = $json->{'email_host'}; 
$mail->SMTPAuth = true;
$mail->Username = $json->{'email_username'};
$mail->Password = $json->{'email_password'};;
$mail->IsHTML(true);


$mail->From     = $json->{'email_username'};
$mail->FromName = 'Terminal 1 Assessment';
$mail->WordWrap = 72;
$mail->CharSet  = "utf-8";
$mail->AddAddress($to);
$mail->Subject  = $subject;
$mail->Send();

?>



