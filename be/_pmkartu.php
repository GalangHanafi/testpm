<?php 
//require 'config.php';
include_once 'config.php';

	if ($_SERVER['REQUEST_METHOD']=="POST") {
			$pintu = '';
            $kodePintu = '';
            $jenisk = '';
            $kartu = '';
			
			$pintu = trim(isset($_POST['pintu'])) ? $_POST['pintu'] : '';
            $kodePintu = trim(isset($_POST['kodepintu'])) ? $_POST['kodepintu'] : '';
            $jenisk = trim(isset($_POST['jenisk'])) ? $_POST['jenisk'] : '';
            $kartu = trim(isset($_POST['kartu'])) ? $_POST['kartu'] : '';
            
            $penomeren = "SELECT substr(concat(curdate()+0,time_to_sec(curtime()),'$kodePintu'),4) as kode, now() as waktu FROM pemakai LIMIT 1";
            $perintahPenomeran = mysql_query( $penomeren);
            $jumPenomeran = mysql_num_rows($perintahPenomeran);

                while($i = mysql_fetch_array($perintahPenomeran))
            {
                $kode =  $i['kode'];
                $waktu = $i['waktu'];
            }

            $digits= "".sprintf("%012s",$kode);

            $even_sum = $digits{1} + $digits{3} + $digits{5} + $digits{7} + $digits{9} + $digits{11};
            $even_sum_three = $even_sum * 3;
            $odd_sum = $digits{0} + $digits{2} + $digits{4} + $digits{6} + $digits{8} + $digits{10};
            $total_sum = $even_sum_three + $odd_sum;
            $next_ten = (ceil($total_sum/10))*10;
            $check_digit = $next_ten - $total_sum;
            $brcd = $digits . $check_digit;

            $selectmasuk = "SELECT * FROM masuk where rfid='$kartu'";
            $perintahmasuk = mysql_query( $selectmasuk);
            $countmasuk = mysql_num_rows($perintahmasuk);
          
            if ($countmasuk == 0){

                $selectmember = "SELECT * from rfid where norfid='$kartu' and awal <= date(now()) and akhir >= date(now())";
                $perintahmember = mysql_query( $selectmember);
                $countmember = mysql_num_rows($perintahmember);

                if($countmember > 0){
                    $aa = date("Y/m/d");
                    $simpan = "insert into masuk(kode,waktu,pintu,jenis,rfid) values('$brcd','$waktu','$pintu','$jenisk','$kartu')";
                    $nsimpan = mysql_query( $simpan);
    
                    $response = array(
                        "status"  => "200",
                        "kode" => $brcd,
                        "waktu" => $waktu,
                        "pintu" => $pintu
                        );
                    echo json_encode($response);
                }else{
                    $response = array(
                        "status"  => "400",
                        "Pesan" => "Kartu Tidak Terdaftar"
                        );
                    echo json_encode($response);

                }
            }else{
                $response = array(
                    "status"  => "300",
                    "Pesan" => "Kendaraan sudah masuk sebelumnya"
                    );
                echo json_encode($response);
            }
    }
           
 ?>