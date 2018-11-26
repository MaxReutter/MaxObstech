-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 25, 2018 at 08:10 PM
-- Server version: 5.6.41-84.1
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `obstecho_test`
--

-- --------------------------------------------------------

--
-- Table structure for table `weather_calib`
--

CREATE TABLE `weather_calib` (
  `id` int(11) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `temperature_internal` float DEFAULT NULL,
  `temperature_external` float DEFAULT NULL,
  `temperature_sky` float DEFAULT NULL,
  `dewpoint` float DEFAULT NULL,
  `wind_dir` float DEFAULT NULL,
  `windspeed` float DEFAULT NULL,
  `windspeed_2mn_average` float DEFAULT NULL,
  `windgust` float DEFAULT NULL,
  `windgust_dir` float DEFAULT NULL,
  `rain` float DEFAULT NULL,
  `dailyrain` float DEFAULT NULL,
  `condensation` int(11) DEFAULT NULL,
  `sqm` float DEFAULT NULL,
  `vsm` float DEFAULT NULL,
  `weatherstatus` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `temperature_AAGexternal` float NOT NULL,
  `temperature_AAGsky` float NOT NULL,
  `temperature_AAGdiff` float NOT NULL,
  `rainfreq_AAG` float NOT NULL,
  `voltage_AAG` float NOT NULL,
  `light_AAG` float NOT NULL,
  `temperature_AAGrainsensor` float NOT NULL,
  `windspeed_AAG` float NOT NULL,
  `SiderealTime` text COLLATE utf8_unicode_ci NOT NULL,
  `MoonPhase` float NOT NULL,
  `MoonElevation` float NOT NULL,
  `SunElevation` float NOT NULL,
  `UTC` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `weather_calib`
--

INSERT INTO `weather_calib` (`id`, `UTC`, `sqm`) VALUES
(633000, '', 22.1),
(633956, '', 7.28),
(659623, '', 21.34),
(662629, '', 21.49),
(702209, '', 21.04);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `weather_calib`
--
ALTER TABLE `weather_calib`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `weather_calib`
--
ALTER TABLE `weather_calib`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=737563;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
