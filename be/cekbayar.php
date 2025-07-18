<?php
include('connection.php');
header('Content-Type: application/json');

// Ambil data QRIS terakhir yang sudah dibayar dan belum masuk
$queryQris = "SELECT * FROM qris WHERE status = 'PAID' AND is_in = 0 ORDER BY time DESC LIMIT 1";
$resultQris = mysqli_query($con, $queryQris);
$dataQris = mysqli_fetch_assoc($resultQris);

// QRIS tidak ditemukan
if (!$dataQris) {
    http_response_code(404);
    echo json_encode([
        "success" => false,
        "message" => "Pembayaran belum dilakukan",
        "data" => null
    ]);
    exit;
}

// Cek jika kendaraan sudah ditandai masuk
if ($dataQris['is_in'] == 1) {
    http_response_code(403);
    echo json_encode([
        "success" => false,
        "message" => "KENDARAAN SUDAH MASUK",
        "data" => null
    ]);
    exit;
}

// Ambil data masuk berdasarkan kode tagihan
$kode = mysqli_real_escape_string($con, $dataQris['kode_tagihan']);
$queryMasuk = "SELECT * FROM masuk WHERE kode = '$kode'";
$resultMasuk = mysqli_query($con, $queryMasuk);
$dataMasuk = mysqli_fetch_assoc($resultMasuk);

// Jika data masuk tidak ditemukan
if (!$dataMasuk) {
    http_response_code(404);
    echo json_encode([
        "success" => false,
        "message" => "Data kendaraan tidak ditemukan",
        "data" => null
    ]);
    exit;
}

// Update status is_in di tabel masuk
$updateMasuk = mysqli_query($con, "UPDATE masuk SET is_in = 1 WHERE kode = '$kode'");

// Update status is_in di tabel qris
$updateQris = mysqli_query($con, "UPDATE qris SET is_in = 1 WHERE kode_tagihan = '$kode'");

// Berhasil
echo json_encode([
    "success" => true,
    "message" => "Pembayaran sudah dilakukan",
    "data" => [
        "kode" => $dataMasuk['kode'],
        "amount" => $dataQris['amount'],
        "jenisk" => $dataMasuk['jenisk'],
        "waktu" => $dataMasuk['waktu'],
    ]
]);
