
<?php
    require 'connect.php';
    $brcd = '';
    $wktmasuk = '';
	$jenisk = '';
	$pintu = '';
	$nopol = '';
	$tipe = '';

    $brcd = trim(isset($_POST['brcd'])) ? $_POST['brcd'] : '';
    $wktmasuk = trim(isset($_POST['wktmasuk'])) ? $_POST['wktmasuk'] : '';
	$jenisk = trim(isset($_POST['jenisk'])) ? $_POST['jenisk'] : '';
	$pintu = trim(isset($_POST['pintu'])) ? $_POST['pintu'] : '';
	$nopol = trim(isset($_POST['nopol'])) ? $_POST['nopol'] : '';
	$tipe = trim(isset($_POST['tipe'])) ? $_POST['tipe'] : '';
    
    if ($wktmasuk != ''){
		$nupdate = "update masuk set waktu = '$wktmasuk' where kode='$brcd'";
		$nupdate = mysqli_query($con, $nupdate);

	}
	
	if ($tipe == 'KARTU'){
		$selectmasuk = "SELECT masuk.*,DATEDIFF(CURRENT_DATE(), waktu) AS jmlinap,TIMEDIFF(NOW(),waktu) AS lamawaktu,hour(TIMEDIFF(NOW(),waktu)) AS lamajam,minute(TIMEDIFF(NOW(),waktu)) AS lamamenit, now() as waktuk, DAYNAME(NOW()) as namahari FROM masuk where rfid='$brcd' LIMIT 1";
        $perintahmasuk = mysqli_query($con, $selectmasuk);
        $countmasuk = mysqli_num_rows($perintahmasuk);

	}else {
        $selectmasuk = "SELECT masuk.*,DATEDIFF(CURRENT_DATE(), waktu) AS jmlinap,TIMEDIFF(NOW(),waktu) AS lamawaktu,hour(TIMEDIFF(NOW(),waktu)) AS lamajam,minute(TIMEDIFF(NOW(),waktu)) AS lamamenit, now() as waktuk, DAYNAME(NOW()) as namahari FROM masuk where kode='$brcd' LIMIT 1";
        $perintahmasuk = mysqli_query($con, $selectmasuk);
        $countmasuk = mysqli_num_rows($perintahmasuk);
	} 
        if($countmasuk > 0){
            foreach($perintahmasuk as $i){
                $lamawaktu =  $i['lamawaktu'];
				$namahari =  $i['namahari'];
				$kode = $i['kode'];
				$masuk = $i['waktu'];
				$keluar = $i['waktuk'];
				$pintum = $i['pintu'];
				$lamajam = $i['lamajam'];
				$lamamenit = $i['lamamenit'];
				$rfid = $i['rfid'];
				$foto = $i['foto'];
				$jmlinap = $i['jmlinap'];
			}

			$starif = "SELECT * from kendaraan where nama='$jenisk'";
			$qtarif = mysqli_query($con, $starif);
			foreach($qtarif as $i){
				$nama = $i['nama'];
				$jampertama = $i['jampertama'];
				$jamberikutnya = $i['jamberikutnya'];
				$maksimal = $i['maksimal'];
				$denda = $i['denda'];
			 	$inap = $i['inap'];
			}

			$tarifinap = $inap * $jmlinap;
	
		if ($tipe=='KARTU'){
			$selectmember = "SELECT * from member where norfid='$brcd' and date(akhir) >= date(now()) and (nopol='$nopol' or nopol2='$nopol') LIMIT 1";
			$perintahmember = mysqli_query($con, $selectmember);
			$countmember = mysqli_num_rows($perintahmember);

		}else{
			
			$selectmember = "SELECT * from member where date(akhir) >= date(now()) and (nopol='$nopol' or nopol2='$nopol') LIMIT 1";
			$perintahmember = mysqli_query($con, $selectmember);
			$countmember = mysqli_num_rows($perintahmember);
		}	
			if($countmember > 0){
				foreach($perintahmember as $i){
					$paket = $i['paket'];
					$tglakhir = $i['akhir'];
				}
				if ($tipe != 'HILANG'){
					$jampertama = 0;
					$jamberikutnya = 0;
					$maksimal = 0;
					$denda = 0;
				}
			}else{
				$paket = 'UMUM';
				$tglakhir = '';
			}

			$selectuser = "SELECT * from pemakai where pintu='$pintu' and posisi='MASUK'";
			$perintahuser = mysqli_query($con, $selectuser);
			foreach($perintahuser as $i){
				$nik = $i['nik'];
				$lastlogin = $i['lastlogin'];
				$shif = $i['shif'];

			}
			$hapus = "delete from struk where pintuk='$pintu'";
			$nhapus = mysqli_query($con, $hapus);

			$isi = "INSERT INTO struk(kode,masuk,keluar,pintum,pintuk,petugas,shif,wktlogin,wktlogout,jenisk,nopol,rfid,paket,durasi) 
			values('$kode','$masuk','$keluar','$pintum','$pintu','$nik','$shif','$lastlogin','$lastlogin','$jenisk','$nopol','$rfid','$paket','$lamawaktu')";
			

			
			$nsimpan = mysqli_query($con, $isi);
			
			//$isi = "INSERT INTO KELUAR(kode,masuk,keluar,pintum,pintuk,tarif,parkir,inap,denda,paket,kadaluarsa,rfid,petugas,shif,wktlogin,wktlogout) 
			$hapus = "delete from keluar where kode='$kode'";
			$nhapus = mysqli_query($con, $hapus);
			$aa = date("Y/m/d");

			$isi = "INSERT INTO keluar(kode,masuk,keluar,pintum,pintuk,petugas,shif,wktlogin,wktlogout,jenisk,nopol,rfid,paket,durasi,tipe, fotom,fotok) 
			values('$kode','$masuk','$keluar','$pintum','$pintu','$nik','$shif','$lastlogin','$lastlogin','$jenisk','$nopol','$rfid','$paket','$lamawaktu','$tipe', '$foto','$aa')";
			$nsimpan = mysqli_query($con, $isi);

            $response = array(
				"status"  => "200",
				"kode" => $kode,
				"masuk" => $masuk,
                "lamawaktu" => $lamawaktu,
				"namahari" => $namahari,
				"lamajam" => $lamajam,
				"lamamenit" => $lamamenit,
				"jenisk" => $nama,
				"jampertama" => $jampertama,
				"jamberikutnya" => $jamberikutnya,
				"maksimal" => $maksimal,
				"denda" => $denda,
				"tipe" => $tipe,
				"fotom" => $foto,
				"fotok" => $aa,
				"jmlinap" => $jmlinap,
				"inap" => $inap,
				"tarifinap" => $tarifinap
                );
    
			echo json_encode($response);
			
        }else{
            $response = array(
                "status"  => "400",
                "pesan" => 'Data Masuk Kosong'
                );
    
            echo json_encode($response);
        }
 ?>
