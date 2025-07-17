-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2025 at 05:55 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbduta`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `waktu` datetime DEFAULT NULL,
  `idmember` int(10) DEFAULT NULL,
  `rfid` char(10) DEFAULT NULL,
  `nopol` char(10) DEFAULT NULL,
  `paket` char(30) DEFAULT NULL,
  `tarif` decimal(10,0) DEFAULT NULL,
  `masaberlaku` date DEFAULT NULL,
  `trx` char(10) DEFAULT NULL,
  `petugas` char(30) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `waktu` datetime DEFAULT NULL,
  `mac` char(50) DEFAULT NULL,
  `judul` char(50) DEFAULT NULL,
  `alamat` char(50) DEFAULT NULL,
  `foot1` char(50) DEFAULT NULL,
  `foot2` char(50) DEFAULT NULL,
  `foot3` char(50) DEFAULT NULL,
  `foot4` char(50) DEFAULT NULL,
  `ipserver` char(20) DEFAULT NULL,
  `ipcamera` char(20) DEFAULT NULL,
  `jenisk` char(20) DEFAULT NULL,
  `namapintu` char(20) DEFAULT NULL,
  `kodepintu` int(3) DEFAULT NULL,
  `aktivasi` datetime DEFAULT NULL,
  `kategori` char(10) DEFAULT 'MASUK',
  `menitfree` int(7) DEFAULT 0,
  `waktupertama` int(7) DEFAULT NULL,
  `waktukedua` int(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `batal`
--

CREATE TABLE `batal` (
  `kode` char(13) NOT NULL,
  `waktu` datetime DEFAULT NULL,
  `pintu` varchar(50) DEFAULT NULL,
  `jenis` char(10) DEFAULT NULL,
  `rfid` char(30) NOT NULL,
  `keterangan` char(50) NOT NULL DEFAULT '0',
  `wktbatal` datetime DEFAULT NULL,
  `petugas` char(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bayar`
--

CREATE TABLE `bayar` (
  `kode` char(100) DEFAULT NULL,
  `masuk` datetime DEFAULT NULL,
  `keluar` datetime DEFAULT NULL,
  `durasi` char(100) DEFAULT NULL,
  `tarif` int(10) DEFAULT NULL,
  `tkartu` char(100) DEFAULT NULL,
  `nokartu` char(100) DEFAULT NULL,
  `saldo` int(10) DEFAULT NULL,
  `saldoawal` int(10) DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `hitung` int(10) DEFAULT NULL,
  `respon` text DEFAULT NULL,
  `mid` char(100) DEFAULT NULL,
  `tid` char(100) DEFAULT NULL,
  `setel` char(100) DEFAULT '0',
  `bat` char(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `ID` int(10) NOT NULL,
  `key` longtext DEFAULT NULL,
  `secret` longtext DEFAULT NULL,
  `Private` longtext DEFAULT NULL,
  `partner` longtext DEFAULT NULL,
  `channel` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`ID`, `key`, `secret`, `Private`, `partner`, `channel`) VALUES
(1, 'ZKppnfV0kGBXDZVMHzSilA1m27hDGENj', 'ahtkm3Diu9T73pO2f5IitcbjelPta714', 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDJ9gD32PHDed+i5xSh+2TIG5xf09UfU9NBqmbdaQ5HYm2inJoIkllfi9QomhLqlM6N2S9fBT3Og4LcmVNeHQAbepuhKVgPj9TYQ0hK+EhZ7qJ8VwgicsQJdQWrvAYTH6JacXTEufQfEIvpHN6e55luPZ7OZmNjdRzBTIlYlf+Q1yGSBighGMLiUWxUMjRX4EHY9ZTSc63GvUKP2k1ouSax3gAzYbyiLBq+/Y9OH2c26rRF52xBX8kQQYcSozlltaUiAM+sjvP8ZLNXi7OcMtyD63rzZXvPKnHlmVQRqUz7+HpDtWBxCaIndkVfeCbH4436/n9C6WRmnuEv+nxBss+7AgMBAAECggEALEKL6sUyEpdScfZ3eJpJ92rJpdycL83kldb8zRgZZ36ELWdpgGhmSsCvoahGbf9nlwGaVpYk+e2rT6IQeaccX2lK0xJm+J4aVLzGCpwH6yGXnW1LXJVPLg1lzUGbCTTdFToZD4X7IJW1O8S2axexcc3yUCRzMpg3UYtu7CmPRRPky0mwxSDevaXzORRFANZet8XwGhJkKWonchGlZSz3k6rh5a6MkNOUO4PPzzUr5MwIMh0qfMS1CDN803EsCG81Xc+U+HziHgZQWNzgmckBuLIigpeT82H/4VS8cqgl48k1zUg5KCwXZivHNUO4wKgODfDFmkMLB3dM+SCfLzFHZQKBgQDajNlDcSucoBUPG4q/YGg4ip3COR000Dl5NF82DQ7UlcPPoXL5wCbcWf8VboevitJ6QbGDOGpNi7l/Gy1UceTGoe4FaMdiZQd/PG6yk3UJ9NpzzIEjZI0wb4bXJdog+eLMEVkNsldHZg67kr8NyJarAViVgjoQXKkOx3GJXPo8lwKBgQDskW8pomnCvvUK/SXvmGEKyrMe0u/RnXNYohb5L1SAbG2B/WVL8brcwHwfOB3p/ZICtJMVn5Z004uxidLtnPIES9BT234oa9avxqPzoKDiggWSfQ+81GtqIVDr0PbdlTZ1JECZSTjPX+BO6q2HiUNWh477Q6wbFyc2vfSp7KvWfQKBgBE0Ozoi44L92wqIaYCtLyccSlTquBDbP1r6M3CG0J8Ndw+WLv3YEXcRIpJmVAoOjIkROM8SltOp5x1JX2UhXhgA0ULdv6xQNanfcPtfvjvdaYDqHVRS6wZgESZIlYY5BZB44SDB5Dr7nrdHUwDbxHiLr5R9XuLA2JIQQzDD//LbAoGBAJd5K89h0gxDTw2hN+gpDoHldjmXYL077r5i0wjs2FN+mcOw52pwNnDgwtkOioDnvtUCoGcpDyJwzbJ5CFjitEgx7wuysB3bptRYAWSehkVicYTxlOEYtkp3WKQV4evRfdQVyVMdAkYuIqcFNuVg63/9Pnz+QLX75jzz9jPTedfVAoGAfiGIpN6cgLcMtd5vuDCLNPtJNHrY/YYMQ6ZRmD/S7TlViPUlZLTBPLcp2gPy479JcRmvuBvWkiAy0jL0RX0oL3MnkjCeEaWxHOWj/FC4dUNgsoRLodXpLFaSZ4F4ijim1WCHdSC8DKPFHMcN8F9lI9ED6andnHs9ySVj388BU2s=', 'f9455620-488c-47ae-8e2f-a150890d465f', '6014');

-- --------------------------------------------------------

--
-- Table structure for table `detail_auth`
--

CREATE TABLE `detail_auth` (
  `id` int(11) NOT NULL,
  `Date` timestamp NULL DEFAULT NULL,
  `sign` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detail_auth`
--

INSERT INTO `detail_auth` (`id`, `Date`, `sign`) VALUES
(1, '2025-02-18 01:01:39', 'mk25FYdurw8EAH2NDeiNRhXQsVkj5OozM6S6RkN6XK7fJ42dujjp+5Co3u9GhLQng1EAbxPFxaPRIRz4nW9kFWyHUKN9tskJkMn0DA9PlEJVSR8AQSKoWib8pmo3vnAilzmPaDJhWJZcN+PYN8LwC0aWDFs4l2U6U8T/4M0C53qO9UnhzRFsISCiSdw7yYl9hugAv2+FTJc+vfA/wMJkgCQPyMsD9xwrKE+kWmt3gAZppg5B33mbyIgOqsFijAGsp4eYgK4H0uPk35o6IYRD2LIukpBdGgawk488QpbMMr2vuKDtwqMffBiKFBAYzXR82Bpk5OMfz0YZRhOQMOWz6w=='),
(2, '2025-02-18 01:37:19', 'CJiqRQhAlSiYnbXV/P2WAnoZIhIOU5yaMjf1Ji9jcbU0t0GVf7KdH6voeFYjJs+lmCKLXTwXGjYs6Bwmr5OHjSXUiD9BwPFrRnaJRYatzHL0uBoKBEPBku4jAQjXAlhy175U3YOgNmmG4aighgllQCMh+MLn44W2UHIr0A9IPYYqlQSQ/emccLwTzi23kaC4FzNwUspyGVLf49pMlZ51/mPZs1w/MrC9Qsu1N6rWmgHAeU3pjUdRoT4XRe+3FKNbcxYbMm0NxYn+72T2SWzxf1Ku+b8yMiWj43e8GhYdgVgb+aNeiYtV/yakteP8Ct91VCigQYuAKAh0u7W/FaI8bg=='),
(3, '2025-02-18 03:14:11', 'MY0vA6cb5rLxOq9Ji8ZMnD0qY9cZ08dsSm2r1cRjaMkXkUmAldeohnF92Nhq+ROISmG1RrXeBqth+KcquEoj7T6tfsqdtKWf3cireENaaVPoiqo2S6xTeOiDYYGBRxTZMNZFy2L/WLcT76OHtJhMAB7/NLYq4kVGTtQn20P5uRcKA+8PMMcpzYA6vxGz67jIIXt9ZAA5Z9RLCJ9w1lVt5VQ4GHzx6wkifRHRT4tKK37A77yx0i2jt36txrvoQ4vZuE0sSark1Ct2iVwCEI+A+Ol+PC84PuyttOwWZsCEiGxijt5F9IAX3LGZkIwBDXSjkgllc3744RX2/4BUlpsrow==');

-- --------------------------------------------------------

--
-- Table structure for table `detail_b2b`
--

CREATE TABLE `detail_b2b` (
  `id` int(10) NOT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `token` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detail_b2b`
--

INSERT INTO `detail_b2b` (`id`, `date`, `time`, `token`) VALUES
(1, '2025-02-18', '09:04:18', 'eyJleHBpcmUiOiIyMDI1MDIxODEyMDUyMiJ9'),
(2, '2025-02-18', '09:37:21', 'eyJleHBpcmUiOiIyMDI1MDIxODEyMzgyNCJ9'),
(3, '2025-02-18', '11:14:12', 'eyJleHBpcmUiOiIyMDI1MDIxODE0MTUxNSJ9'),
(4, '2025-02-18', '11:29:19', 'eyJleHBpcmUiOiIyMDI1MDIxODE0MzAyMiJ9');

-- --------------------------------------------------------

--
-- Table structure for table `device_client`
--

CREATE TABLE `device_client` (
  `mac` char(20) DEFAULT NULL,
  `ip` char(20) DEFAULT NULL,
  `ipserver` char(20) DEFAULT NULL,
  `ipcamera` char(20) DEFAULT NULL,
  `namapintu` char(20) DEFAULT NULL,
  `kategori` char(10) DEFAULT NULL,
  `status` int(1) DEFAULT 0,
  `grop` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `grop`
--

CREATE TABLE `grop` (
  `id` int(11) NOT NULL,
  `nama` char(20) DEFAULT NULL,
  `pintu` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `hakuser`
--

CREATE TABLE `hakuser` (
  `id` int(11) NOT NULL,
  `nik` char(20) DEFAULT NULL,
  `tr1` int(1) DEFAULT NULL,
  `tr2` int(1) DEFAULT NULL,
  `tr3` int(1) DEFAULT NULL,
  `tr4` int(1) DEFAULT NULL,
  `tr5` int(1) DEFAULT NULL,
  `tr6` int(1) DEFAULT NULL,
  `lp1` int(1) DEFAULT NULL,
  `lp2` int(1) DEFAULT NULL,
  `lp3` int(1) DEFAULT NULL,
  `lp4` int(1) DEFAULT NULL,
  `lp5` int(1) DEFAULT NULL,
  `lp6` int(1) DEFAULT NULL,
  `lp7` int(1) DEFAULT NULL,
  `lp8` int(1) DEFAULT NULL,
  `lp9` int(1) DEFAULT NULL,
  `lp10` int(1) DEFAULT NULL,
  `lp11` int(1) DEFAULT NULL,
  `dm1` int(1) DEFAULT NULL,
  `dm2` int(1) DEFAULT NULL,
  `dm3` int(1) DEFAULT NULL,
  `dm4` int(1) DEFAULT NULL,
  `dm5` int(1) DEFAULT NULL,
  `dm6` int(1) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `jurnal`
--

CREATE TABLE `jurnal` (
  `id` int(16) NOT NULL,
  `id_member` char(15) DEFAULT NULL,
  `norfid` char(20) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `jenisk` varchar(255) DEFAULT NULL,
  `nopol` varchar(255) DEFAULT NULL,
  `nopol2` char(20) NOT NULL,
  `awal` date DEFAULT NULL,
  `akhir` date DEFAULT NULL,
  `paket` varchar(255) DEFAULT NULL,
  `tipe` varchar(255) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `petugas` varchar(255) DEFAULT NULL,
  `harga` int(10) DEFAULT 0,
  `time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `keluar`
--

CREATE TABLE `keluar` (
  `kode` char(15) NOT NULL,
  `nopol` char(15) DEFAULT NULL,
  `masuk` datetime DEFAULT NULL,
  `keluar` datetime DEFAULT NULL,
  `durasi` char(20) DEFAULT NULL,
  `pintum` char(20) DEFAULT NULL,
  `pintuk` char(20) DEFAULT NULL,
  `jenisk` char(30) DEFAULT NULL,
  `tarif` int(6) DEFAULT NULL,
  `parkir` int(6) DEFAULT NULL,
  `inap` int(6) DEFAULT NULL,
  `denda` int(6) DEFAULT NULL,
  `tiketmasalah` int(6) NOT NULL DEFAULT 0,
  `paket` char(15) DEFAULT NULL,
  `kadaluarsa` date DEFAULT NULL,
  `tkartu` char(2) DEFAULT NULL,
  `rfid` char(50) DEFAULT NULL,
  `petugas` char(15) DEFAULT NULL,
  `shif` char(7) DEFAULT NULL,
  `wktlogin` datetime DEFAULT NULL,
  `wktlogout` datetime DEFAULT NULL,
  `tipe` char(15) DEFAULT NULL,
  `fotom` char(10) DEFAULT '1',
  `fotok` char(10) DEFAULT '1',
  `tbayar` char(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `kendaraan`
--

CREATE TABLE `kendaraan` (
  `nama` char(20) DEFAULT NULL,
  `jampertama` int(7) DEFAULT NULL,
  `jamberikutnya` int(7) DEFAULT NULL,
  `maksimal` int(7) DEFAULT NULL,
  `denda` int(7) DEFAULT NULL,
  `grop` char(10) DEFAULT NULL,
  `inap` int(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `kendaraan`
--

INSERT INTO `kendaraan` (`nama`, `jampertama`, `jamberikutnya`, `maksimal`, `denda`, `grop`, `inap`) VALUES
('RODA 4', 1000, 1000, 1000, 1000, NULL, NULL),
('CRANE /ALATBERAT BAN', 5000, 5000, 5000, 5000, NULL, NULL),
('ALAT BERAT BAN RANTA', 7000, 7000, 7000, 7000, NULL, NULL),
('TRUK TRAILER', 3000, 3000, 3000, 3000, NULL, NULL),
('RODA 6/LEBIH', 2000, 2000, 2000, 2000, NULL, NULL),
('FORKLIFT', 4000, 4000, 4000, 4000, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `id` int(6) NOT NULL,
  `nama` char(25) DEFAULT NULL,
  `keterangan` char(50) DEFAULT NULL,
  `pelaku` char(25) DEFAULT NULL,
  `time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `loggate`
--

CREATE TABLE `loggate` (
  `waktu` datetime DEFAULT NULL,
  `mid` char(20) DEFAULT NULL,
  `tid` char(20) DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `nokartu` char(20) DEFAULT NULL,
  `gate` int(1) DEFAULT 0
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `masuk`
--

CREATE TABLE `masuk` (
  `kode` char(13) NOT NULL,
  `waktu` datetime DEFAULT NULL,
  `pintu` varchar(50) DEFAULT NULL,
  `jenis` char(10) DEFAULT NULL,
  `rfid` char(30) DEFAULT NULL,
  `cetak` int(1) DEFAULT 0,
  `foto` char(10) DEFAULT '1',
  `bcd` char(30) DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `id` int(6) NOT NULL,
  `member_id` char(15) NOT NULL,
  `norfid` char(10) NOT NULL,
  `nama` char(30) DEFAULT NULL,
  `jenisk` char(10) DEFAULT NULL,
  `paket` char(20) DEFAULT NULL,
  `nopol` char(15) DEFAULT NULL,
  `nopol2` char(20) NOT NULL,
  `awal` date DEFAULT NULL,
  `akhir` date DEFAULT NULL,
  `blokir` int(1) DEFAULT 0 COMMENT '0 plataja, 1rfid,3catatan',
  `tipe` char(10) DEFAULT 'KARTU',
  `catatan` char(50) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `member_copy`
--

CREATE TABLE `member_copy` (
  `id` int(6) NOT NULL,
  `norfid` char(10) NOT NULL,
  `nama` char(30) DEFAULT NULL,
  `jenisk` char(10) DEFAULT NULL,
  `paket` char(20) DEFAULT NULL,
  `nopol` char(15) DEFAULT NULL,
  `nopol2` char(20) NOT NULL,
  `awal` date DEFAULT NULL,
  `akhir` date DEFAULT NULL,
  `blokir` int(1) DEFAULT 0 COMMENT '0 plataja, 1rfid,3catatan',
  `tipe` char(10) DEFAULT 'KARTU',
  `catatan` char(50) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `pemakai`
--

CREATE TABLE `pemakai` (
  `ID_Operator` int(11) NOT NULL,
  `nik` varchar(20) DEFAULT NULL,
  `kunci` varchar(225) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `posisi` varchar(35) DEFAULT 'KELUAR',
  `hak` varchar(35) DEFAULT NULL,
  `lastlogin` datetime DEFAULT NULL,
  `shif` char(10) DEFAULT NULL,
  `pintu` char(20) DEFAULT NULL,
  `nokartu` char(30) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pemakai`
--

INSERT INTO `pemakai` (`ID_Operator`, `nik`, `kunci`, `nama`, `alamat`, `posisi`, `hak`, `lastlogin`, `shif`, `pintu`, `nokartu`) VALUES
(1219, 'admin', 'admin ', 'admin', NULL, 'KELUAR', 'ADMIN', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pintu`
--

CREATE TABLE `pintu` (
  `mid` char(100) DEFAULT NULL,
  `tid` char(100) DEFAULT NULL,
  `last_setel` datetime DEFAULT NULL,
  `jenisk` char(10) DEFAULT NULL,
  `namapintu` char(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pk`
--

CREATE TABLE `pk` (
  `kode` char(13) DEFAULT NULL,
  `masuk` datetime DEFAULT NULL,
  `keluar` datetime DEFAULT NULL,
  `pm` char(10) DEFAULT NULL,
  `pk` char(10) DEFAULT NULL,
  `tarif` int(10) DEFAULT NULL,
  `saldoawal` int(10) DEFAULT NULL,
  `saldoakir` int(10) DEFAULT NULL,
  `tid` char(8) DEFAULT NULL,
  `mid` char(16) DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `counter` int(10) DEFAULT NULL,
  `paket` char(10) DEFAULT NULL,
  `kadaluarsa` datetime DEFAULT NULL,
  `respon` char(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `produk`
--

CREATE TABLE `produk` (
  `id` int(7) NOT NULL,
  `kdproduk` char(20) DEFAULT NULL,
  `durasi` int(7) DEFAULT NULL,
  `jenisk` char(15) DEFAULT NULL,
  `tipe` char(15) DEFAULT 'KARTU',
  `tarif` int(7) DEFAULT NULL,
  `baru` int(7) DEFAULT NULL,
  `ganti` int(7) DEFAULT 0,
  `ubahnopol` int(7) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `qris`
--

CREATE TABLE `qris` (
  `id` int(10) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `kode_tagihan` varchar(100) DEFAULT NULL,
  `id_tagihan` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `valid_period` datetime DEFAULT NULL,
  `qrcode` text DEFAULT NULL,
  `bill_number` varchar(100) DEFAULT NULL,
  `rrn` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `qris`
--

INSERT INTO `qris` (`id`, `time`, `kode_tagihan`, `id_tagihan`, `amount`, `status`, `valid_period`, `qrcode`, `bill_number`, `rrn`) VALUES
(2, '2025-02-18 03:32:37', '2147483647', '2147483647', '10000', 'UNPAID', '0000-00-00 00:00:00', '', NULL, NULL),
(3, '2025-02-18 03:34:22', '2147483647', '2147483647', '10000', 'UNPAID', '0000-00-00 00:00:00', '', NULL, NULL),
(4, '2025-02-18 03:37:22', '2147483647', '2147483647', '10000', 'UNPAID', '2025-02-14 22:31:50', '00020101021226690023ID.CO.BANKALTIMTARA.WWW011893600124024091802802092409180280303URE51440014ID.CO.QRIS.WWW0215ID20243452761720303URE5204752353033605405100005802ID5944(TEST) RETRIBUSI PARKIR PELABUHAN BULUMINUNG6015PENAJAM PASER U610576141622501121122334455340705479056304F16E', NULL, NULL),
(5, '2025-02-18 03:38:49', '1122334455342', '202502180004', '10000', 'UNPAID', '2025-02-14 22:33:16', '00020101021226690023ID.CO.BANKALTIMTARA.WWW011893600124024091802802092409180280303URE51440014ID.CO.QRIS.WWW0215ID20243452761720303URE5204752353033605405100005802ID5944(TEST) RETRIBUSI PARKIR PELABUHAN BULUMINUNG6015PENAJAM PASER U6105761416226011311223344553420705479056304BE84', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reader`
--

CREATE TABLE `reader` (
  `no` int(10) NOT NULL,
  `perintah` char(10) DEFAULT NULL,
  `kodetrx` char(13) DEFAULT NULL,
  `waktu` datetime DEFAULT NULL,
  `mid` char(20) DEFAULT NULL,
  `tid` char(20) DEFAULT NULL,
  `tkartu` char(2) DEFAULT NULL,
  `nokartu` char(16) DEFAULT NULL,
  `amount` int(10) DEFAULT 0,
  `saldo` int(10) DEFAULT NULL,
  `wktunik` char(14) DEFAULT NULL,
  `cmd` char(200) DEFAULT NULL,
  `respon` char(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `readerin`
--

CREATE TABLE `readerin` (
  `no` int(10) NOT NULL,
  `mid` char(16) DEFAULT NULL,
  `kode` char(13) DEFAULT NULL,
  `perintah` char(10) DEFAULT NULL,
  `cmd` char(200) DEFAULT NULL,
  `waktu` datetime DEFAULT NULL,
  `wktunik` char(14) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `readerout`
--

CREATE TABLE `readerout` (
  `no` int(10) NOT NULL,
  `kode` char(13) DEFAULT NULL,
  `cmd` char(10) DEFAULT NULL,
  `wktkirim` datetime DEFAULT NULL,
  `wktrespon` datetime DEFAULT NULL,
  `perintah` char(100) DEFAULT NULL,
  `respon` char(200) DEFAULT NULL,
  `wktunik` char(14) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `rekap`
--

CREATE TABLE `rekap` (
  `id` int(10) NOT NULL,
  `wktlaporan` datetime DEFAULT NULL,
  `wktlogin` datetime DEFAULT NULL,
  `wktlogout` datetime DEFAULT NULL,
  `jenisk` char(30) DEFAULT NULL,
  `parkir` decimal(10,0) DEFAULT NULL,
  `inap` decimal(10,0) DEFAULT NULL,
  `denda` decimal(10,0) DEFAULT NULL,
  `jumlah` int(5) DEFAULT NULL,
  `setor` decimal(14,0) DEFAULT NULL,
  `pendapatan` decimal(14,0) DEFAULT NULL,
  `petugas` char(20) DEFAULT NULL,
  `pintu` char(10) DEFAULT NULL,
  `shif` char(10) DEFAULT NULL,
  `masalah` decimal(10,0) DEFAULT 0,
  `admin` char(15) DEFAULT NULL,
  `paket` char(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `respontrx`
--

CREATE TABLE `respontrx` (
  `id` int(10) NOT NULL,
  `waktu` datetime DEFAULT NULL,
  `trx` char(10) DEFAULT NULL,
  `nokartu` char(100) DEFAULT NULL,
  `kodetrx` char(30) DEFAULT NULL,
  `tid` char(50) DEFAULT NULL,
  `respon` text DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `sale_id` bigint(20) UNSIGNED NOT NULL,
  `total` double(8,2) UNSIGNED NOT NULL,
  `rfc` varchar(191) NOT NULL,
  `id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `created` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `setel`
--

CREATE TABLE `setel` (
  `tanggal` date DEFAULT NULL,
  `wktsetel` char(50) DEFAULT NULL,
  `mid` char(100) DEFAULT NULL,
  `tid` char(100) DEFAULT NULL,
  `versi` char(100) DEFAULT NULL,
  `bat` char(250) DEFAULT NULL,
  `tutupbuku` int(1) DEFAULT 0,
  `trxcount` int(10) DEFAULT NULL,
  `trxamount` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `setoran`
--

CREATE TABLE `setoran` (
  `id` int(10) NOT NULL,
  `kode` char(20) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `mobil` int(8) DEFAULT NULL,
  `motor` int(8) DEFAULT NULL,
  `denda` int(8) DEFAULT NULL,
  `vmobil` int(8) DEFAULT NULL,
  `vmotor` int(8) DEFAULT NULL,
  `wktbuat` datetime DEFAULT NULL,
  `lastupdate` datetime DEFAULT NULL,
  `admin` char(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `setorandetail`
--

CREATE TABLE `setorandetail` (
  `kode` int(20) DEFAULT NULL,
  `nama` char(20) DEFAULT NULL,
  `pintu` char(20) DEFAULT NULL,
  `shif` char(20) DEFAULT NULL,
  `mobil` int(8) DEFAULT NULL,
  `motor` int(8) DEFAULT NULL,
  `denda` int(8) DEFAULT NULL,
  `vmobil` int(8) DEFAULT NULL,
  `vmotor` int(8) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `shif`
--

CREATE TABLE `shif` (
  `kode` char(10) NOT NULL,
  `nama` char(10) DEFAULT NULL,
  `awal` time DEFAULT NULL,
  `akhir` time DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `struk`
--

CREATE TABLE `struk` (
  `kode` char(15) DEFAULT NULL,
  `nopol` char(15) DEFAULT NULL,
  `masuk` datetime DEFAULT NULL,
  `keluar` datetime DEFAULT NULL,
  `durasi` char(20) DEFAULT NULL,
  `pintum` char(20) DEFAULT NULL,
  `pintuk` char(20) DEFAULT NULL,
  `jenisk` char(15) DEFAULT NULL,
  `tarif` int(6) DEFAULT NULL,
  `parkir` int(6) DEFAULT NULL,
  `inap` int(6) DEFAULT 0,
  `denda` int(6) DEFAULT NULL,
  `tiketmasalah` int(6) DEFAULT 0,
  `paket` char(15) DEFAULT NULL,
  `kadaluarsa` date DEFAULT '2000-01-01',
  `rfid` char(15) DEFAULT NULL,
  `petugas` char(15) DEFAULT NULL,
  `shif` char(7) DEFAULT NULL,
  `wktlogin` datetime DEFAULT NULL,
  `wktlogout` datetime DEFAULT NULL,
  `tipe` char(15) DEFAULT NULL,
  `fotom` char(10) DEFAULT NULL,
  `fotok` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id` int(16) NOT NULL,
  `id_member` char(15) DEFAULT NULL,
  `norfid` char(20) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `jenisk` varchar(255) DEFAULT NULL,
  `nopol` varchar(255) DEFAULT NULL,
  `nopol2` char(20) NOT NULL,
  `awal` date DEFAULT NULL,
  `akhir` date DEFAULT NULL,
  `paket` varchar(255) DEFAULT NULL,
  `tipe` varchar(255) DEFAULT NULL,
  `petugas` varchar(255) DEFAULT NULL,
  `harga` int(10) DEFAULT 0,
  `time` datetime DEFAULT NULL,
  `durasi` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(191) NOT NULL,
  `email` varchar(191) NOT NULL,
  `phone` varchar(191) DEFAULT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(191) NOT NULL,
  `administrator` tinyint(1) NOT NULL DEFAULT 0,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `batal`
--
ALTER TABLE `batal`
  ADD PRIMARY KEY (`kode`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `detail_auth`
--
ALTER TABLE `detail_auth`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `detail_b2b`
--
ALTER TABLE `detail_b2b`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `grop`
--
ALTER TABLE `grop`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hakuser`
--
ALTER TABLE `hakuser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jurnal`
--
ALTER TABLE `jurnal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `keluar`
--
ALTER TABLE `keluar`
  ADD PRIMARY KEY (`kode`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `masuk`
--
ALTER TABLE `masuk`
  ADD PRIMARY KEY (`kode`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`,`member_id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `member_copy`
--
ALTER TABLE `member_copy`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `pemakai`
--
ALTER TABLE `pemakai`
  ADD PRIMARY KEY (`ID_Operator`);

--
-- Indexes for table `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qris`
--
ALTER TABLE `qris`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `readerin`
--
ALTER TABLE `readerin`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `readerout`
--
ALTER TABLE `readerout`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `rekap`
--
ALTER TABLE `rekap`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `respontrx`
--
ALTER TABLE `respontrx`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`sale_id`),
  ADD KEY `sales_id_foreign` (`id`),
  ADD KEY `sales_rfc_foreign` (`rfc`);

--
-- Indexes for table `setoran`
--
ALTER TABLE `setoran`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shif`
--
ALTER TABLE `shif`
  ADD PRIMARY KEY (`kode`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `detail_auth`
--
ALTER TABLE `detail_auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `detail_b2b`
--
ALTER TABLE `detail_b2b`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `grop`
--
ALTER TABLE `grop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hakuser`
--
ALTER TABLE `hakuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `jurnal`
--
ALTER TABLE `jurnal`
  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `member_copy`
--
ALTER TABLE `member_copy`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pemakai`
--
ALTER TABLE `pemakai`
  MODIFY `ID_Operator` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1220;

--
-- AUTO_INCREMENT for table `produk`
--
ALTER TABLE `produk`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `qris`
--
ALTER TABLE `qris`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `reader`
--
ALTER TABLE `reader`
  MODIFY `no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `readerin`
--
ALTER TABLE `readerin`
  MODIFY `no` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `readerout`
--
ALTER TABLE `readerout`
  MODIFY `no` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rekap`
--
ALTER TABLE `rekap`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1787;

--
-- AUTO_INCREMENT for table `respontrx`
--
ALTER TABLE `respontrx`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `setoran`
--
ALTER TABLE `setoran`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
