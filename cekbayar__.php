<?php
include('connection.php');

date_default_timezone_set('Asia/Jakarta');

// get masuk
$dataMasuk = "SELECT * FROM masuk ORDER BY waktu DESC LIMIT 1";
$dataMasuk = mysqli_query($con, $dataMasuk);
$dataMasuk = mysqli_fetch_assoc($dataMasuk);
$kodeQris = $dataMasuk['kode'];

if($dataMasuk['is_in'] == 1){
    http_response_code(403);
    echo json_encode([
        "success" => false,
        "message" => "KENDARAAN SUDAH MASUK",
    ]);
    exit;
}

// get qris
$dataQris = "SELECT * FROM qris where kode_tagihan = '$kodeQris'";
$dataQris = mysqli_query($con, $dataQris);
$dataQris = mysqli_fetch_assoc($dataQris);

// KALAU BELUM PAID
if ($dataQris['status'] != 'PAID') {
    http_response_code(403);
    echo json_encode([
        "success" => false,
        "message" => "Pembayaran belum dilakukan",
        "data" => null
    ]);
    exit;
}

// update masuk
$updateMasuk = "UPDATE masuk SET is_in = 1 WHERE kode = '$dataQris[kode_tagihan]'";
$updateMasuk = mysqli_query($con, $updateMasuk);

echo json_encode([
    "success" => true,
    "message" => "Pembayaran sudah dilakukan",
    "data" => [
        "kode" => $datamasuk['kode'],
        "amount" => $dataQris['amount'],
        "waktu" => $datamasuk['waktu'],
    ]
]);