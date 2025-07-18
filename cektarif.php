<?php
require 'connect.php'; // Ensure this file establishes $con and handles database connection errors

date_default_timezone_set('Asia/Jakarta');

$now = date('Y-m-d H:i:s');

header('Content-type: application/json');

$response = array(
    'status' => 400, // Default to Bad Request
    'kode' => null,  // Will be the vehicle's name
    'tarif' => null, // Will be jampertama/jamberikutnya
    'waktu' => null, // Placeholder, can be used for 'jampertama' or 'jamberikutnya' if needed
    'denda' => null, // Added 'denda' based on your table
    'message' => 'Invalid Request'
);

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['jenisk'])) {
    $jenisk = $_POST['jenisk']; // Get jenisk from POST data

    $jenisk = mysqli_real_escape_string($con, $jenisk);

    $sql = "SELECT substr(concat(curdate()+0,time_to_sec(curtime()),'2'),4) as kode, nama, jampertama, jamberikutnya, maksimal, denda FROM kendaraan WHERE nama = '$jenisk' LIMIT 1";
    $query = mysqli_query($con, $sql);

    if ($query) {
        if (mysqli_num_rows($query) > 0) {
            $output = mysqli_fetch_assoc($query);

            $response['status'] = 200; // Success
            $response['message'] = 'Data retrieved successfully';
            $response['kode'] = $output['kode'];
            $response['tarif'] = $output['jampertama']; // Assuming 'tarif' refers to 'jampertama'
            $response['waktu'] = $now;
            $response['denda'] = $output['denda']; // Add denda
            $response['maksimal'] = $output['maksimal']; // Add maksimal
        } else {
            $response['status'] = 404; // Not Found
            $response['message'] = 'Vehicle type not found';
        }
    } else {
        $response['status'] = 500; // Internal Server Error
        $response['message'] = 'Database query failed: ' . mysqli_error($con);
        error_log("Database query failed in jenisk.php: " . mysqli_error($con));
    }
} else {
    // If 'jenisk' is not provided or not a POST request
    $response['status'] = 400;
    $response['message'] = 'Missing jenisk parameter or invalid request method.';
}

// Close the database connection
mysqli_close($con);

// Encode and echo the JSON response
echo json_encode($response);
