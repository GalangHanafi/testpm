<?php
    define('HOST', 'localhost');
    define('USER', 'root');
    define('PASS', '');
    define('DB', 'dbduta');

    date_default_timezone_set('Asia/Makassar');

    $con = mysqli_connect(HOST,USER,PASS,DB) or die('Unable to Connect');

?>