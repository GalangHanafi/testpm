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

if (!isset($_POST['kode']) || !isset($_POST['waktu']) || !isset($_POST['jenis']) || !isset($_POST['bcd'])) {
    http_response_code(400);
    echo json_encode(
        [
            "success" => false,
            "message" => "kode, waktu, jenis, dan bcd harus diisi",
        ]
    );
    exit();
}

$kode = $_POST['kode'];
$waktu = $_POST['waktu'];
$jenis = $_POST['jenis'];
$bcd = $_POST['bcd'];

// $query = "INSERT INTO masuk (kode, waktu, jenis, bcd) 
//     VALUES ('$kode', '$waktu', $jenis, '$bcd')
// ";

// $query = mysqli_query($con, $query);

$stmt = $con->prepare("INSERT INTO masuk (kode, waktu, jenis, bcd) VALUES (?, ?, ?, ?)");
$stmt->bind_param("ssis", $kode, $waktu, $jenis, $bcd);
$stmt->execute();

echo json_encode([
    "success" => true,
    "message" => "Data masuk berhasil ditambahkan",
    "data" => [
        "kode" => $kode,
        "waktu" => $waktu,
        "jenis" => $jenis,
        "bcd" => $bcd
    ]
]);
