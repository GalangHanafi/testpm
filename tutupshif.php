<?php
    //require 'connect.php';
    include_once 'config.php';
	$nik = '';
	$pintu = '';

	$nik = trim(isset($_POST['nik'])) ? $_POST['nik'] : '';
	$pintu = trim(isset($_POST['pintu'])) ? $_POST['pintu'] : '';

    $belumkeluar = 0;

    $selectuser = "SELECT count(*) as jumlahmasuk FROM masuk";
    $perintahuser = mysql_query( $selectuser);
    $countuser = mysql_num_rows($perintahuser);
    if($countuser > 0){
        while($i = mysql_fetch_array($perintahuser))
        {
			$belumkeluar =  $i['jumlahmasuk'];
        }

    }

	$selectuser = "SELECT nama, lastlogin, now() as wktlogout, shif FROM pemakai where nik='$nik' and pintu='$pintu'";
    $perintahuser = mysql_query( $selectuser);
    $countuser = mysql_num_rows($perintahuser);
        
    if($countuser > 0){
        $responsistem = array();
		$responsistem["data"] = array();
        $responsistem["data2"] = array();
        $data2['status'] = 200;
        $data2['belumkeluar'] = $belumkeluar;
        
        while($i = mysql_fetch_array($perintahuser))
        {
			$nama =  $i['nama'];
			$wktlogout =  $i['wktlogout'];
            $lastlogin =  $i['lastlogin'];
            $shif =  $i['shif'];

            $data2['nama'] = $nama;
            $data2['login'] = $lastlogin;
            $data2['logout'] = $wktlogout;
            $data2['shif'] = $shif;
            $data2['pintu'] = $pintu;
        }
        
        array_push($responsistem["data2"], $data2);

        $selectkeluar = "SELECT pintuk, shif, jenisk,SUM(tarif) AS tarif,SUM(parkir) AS parkir, SUM(inap) AS inap, SUM(denda) AS denda, SUM(tiketmasalah) AS tiketmasalah, paket, COUNT(*) AS jumlah from keluar where wktlogin='$lastlogin' and pintuk='$pintu' and wktlogin=wktlogout and petugas='$nik' group by pintuk, shif, jenisk, paket";
        $perintahkeluar = mysql_query( $selectkeluar);
        $countkeluar = mysql_num_rows($perintahkeluar);

        if($countkeluar < 1){
            $data['status'] = 300;
            array_push($responsistem["data"], $data);
        }

        if($countkeluar > 0){
            $data['status'] = 200;
            while($k = mysql_fetch_array($perintahkeluar))
                {

                $data['jenisk'] = $k['jenisk'];
                $data['tarif'] = $k['tarif'];
                $data['jumlah'] = $k['jumlah'];
                $data['paket'] = $k['paket'];


                array_push($responsistem["data"], $data);

                $pintuk = $k['pintuk'];
                $shif = $k['shif'];
                $jenisk = $k['jenisk'];
                $tarif = $k['tarif'];
                $parkir = $k['parkir'];
                $inap = $k['inap'];
                $denda = $k['denda'];
                $tiketmasalah = $k['tiketmasalah'];
                $jumlah = $k['jumlah'];
                $paket = $k['paket'];

                $isi = "INSERT INTO rekap(wktlaporan, wktlogin, wktlogout, jenisk, parkir, inap, denda, jumlah, setor, pendapatan, petugas, pintu, shif, masalah, admin, paket) 
                values('$wktlogout','$lastlogin','$wktlogout','$jenisk','$parkir','$inap','$denda','$jumlah',0,'$tarif','$nik','$pintuk','$shif','$tiketmasalah','','$paket')";
                $nsimpan = mysql_query( $isi);
            }
        }

        echo json_encode($responsistem);

        $ubah = "update keluar set wktlogout='$wktlogout' where pintuk='$pintu' and wktlogin='$lastlogin' and wktlogin=wktlogout and petugas='$nik' ";
        $nsimpan = mysql_query( $ubah);

        $ubah = "update pemakai set posisi='KELUAR' WHERE nik='$nik' and pintu='$pintu'";
        $nsimpan = mysql_query( $ubah);
	}
	

 ?>