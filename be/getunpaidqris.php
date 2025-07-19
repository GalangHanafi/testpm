<?php
include('connection.php');

// Ambil data QRIS terakhir yang sudah dibayar dan belum masuk
$queryUnpaidQris = "SELECT id, kode_tagihan, id_tagihan, bill_number, rrn FROM qris 
            WHERE 
                status = 'UNPAID' AND 
                time > (NOW() - INTERVAL 30 MINUTE) 
            ORDER BY 
                time DESC";
$resultUnpaidQris = mysqli_query($con, $queryUnpaidQris);
$dataUnpaidQris = mysqli_fetch_all($resultUnpaidQris, MYSQLI_ASSOC);

// QRIS tidak ditemukan
if (!$dataUnpaidQris) {
    http_response_code(404);
    echo json_encode([
        "success" => false,
        "message" => "Data Unpaid QRIS tidak ditemukan",
        "data" => null
    ]);
    exit;
}

// Berhasil
echo json_encode([
    "success" => true,
    "message" => "Data Unpaid QRIS ditemukan",
    "data" => $dataUnpaidQris,
]);

// ambil data QRIS 30 menit kebelakang
// kalau data ga ketemu exit
// kalau ketemu kirim data