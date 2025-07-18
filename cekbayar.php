<?php
include('connection.php');

date_default_timezone_set('Asia/Jakarta');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(
        [
            "success" => false,
            "message" => "Method not allowed",
        ]
    );
    exit();
}

if (!isset($_POST['jenis']) || !isset($_POST['qris_id'])) {
    http_response_code(400);
    echo json_encode(
        [
            "success" => false,
            "message" => "jenis dan qris_id harus diisi",
        ]
    );
    exit();
}

$jenis = $_POST['jenis'];
$qris_id = $_POST['qris_id'];
$code = generateBarcode();
$now = date('Y-m-d H:i:s');

// CEK PEMBAYARAN
$query = "SELECT id, status, is_in FROM qris ORDER BY time DESC LIMIT 1";

$result = mysqli_query($con, $query);
$qris = $result->fetch_assoc();

if ($qris['status'] == "UNPAID") {
    http_response_code(403);
    echo json_encode(
        [
            "success" => false,
            "message" => "Pembayaran belum dilakukan",
            "data" => $qris
        ]
    );
    exit();
}

if ($qris && $qris['is_in']) {
    http_response_code(404);
    echo json_encode(
        [
            "success" => false,
            "message" => "Kendaraan sudah masuk",
            "data" => $qris
        ]
    );
    exit();
}

// UPDATE IS_IN di qris
$set = "UPDATE qris SET is_in = 1";
$set = mysqli_query($con, $set);

// INSERT INTO TABEL masuk
$query = "INSERT INTO masuk (kode, waktu, jenis, foto, qris_id) 
    VALUES ('$code', '$now', $jenis, null, '$qris_id')
";
$query = mysqli_query($con, $query);

echo json_encode(
    [
        "success" => true,
        "message" => "Pembayaran Sudah dilakukan, data masuk berhasil ditambahkan",
        "data" => [
            "kode" => $code,
            "waktu" => $now,
            "jenis" => $jenis,
            "amount" => $qris['amount'],
            "foto" => null,
            "qris_id" => $qris_id
        ]
    ]
);

// 
// =================================================================================
// 

// 
// HELPERS
// 

function generateBarcode()
{
    // Buat 12 digit acak
    $code = '';
    for ($i = 0; $i < 12; $i++) {
        $code .= rand(0, 9);
    }

    // Hitung check digit ke-13 (EAN-13 checksum)
    $sum = 0;
    for ($i = 0; $i < 12; $i++) {
        $digit = (int) $code[$i];
        $sum += ($i % 2 === 0) ? $digit : $digit * 3;
    }

    $checksum = (10 - ($sum % 10)) % 10;

    return $code . $checksum;
}
