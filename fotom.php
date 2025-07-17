<?php

$ip = '';
$nama ='';
$ip = trim(isset($_POST['ip'])) ? $_POST['ip'] : '';
$nama = trim(isset($_POST['nama'])) ? $_POST['nama'] : '';


  $url = "http://admin:Admin123@".$ip."/ISAPI/Streaming/channels/1/picture";
 
  //$url = "http://admin:Admin123@192.168.1.112/ISAPI/Streaming/channels/1/picture";

  if ($url) {

    $aa = date("Y/m/d");
    $direktori = "../server_parkir/images/masuk/";
    $structure = $direktori;
    if(!file_exists($structure)) {
      if (!mkdir($structure, 0, true)) {
      die('Gagal membuat folder...');
      }
    }

      header("Content-type: image/jpeg");
      $image= file_get_contents($url);
	    file_put_contents($structure.'/m_'. $nama.'.jpg',$image);
  }
?>