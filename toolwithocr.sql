-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 09, 2023 at 08:28 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `toolwithocr`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `id` int(11) NOT NULL,
  `user_name` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`id`, `user_name`, `password`, `last_update`) VALUES
(1, 'admin', 'admin', '2019-11-07 08:49:32'),
(2, 'admin2', 'admin', '2019-11-07 08:51:20');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(11) NOT NULL,
  `user` text NOT NULL,
  `location` text NOT NULL,
  `payment` text NOT NULL,
  `vehicle` text NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `user`, `location`, `payment`, `vehicle`, `status`) VALUES
(1, 'test1@email.com', 'Haridwar', '800', 'AP15CD5678', ''),
(2, 'test1@email.com', 'Haridwar', '800', 'CH17GH6589', 'Completed'),
(3, 'test1@email.com', 'Haridwar', '800', 'AP15CD5678', 'Completed'),
(4, 'test2@email.com', 'Haridwar', '800', 'UP14AB1234', 'Completed'),
(5, 'up16user@email.com', 'Haridwar', '800', 'UP16AD3456', 'Completed'),
(6, 'up16user@email.com', 'Haridwar', '800', 'UP16AD3456', 'Completed'),
(7, 'test2@email.com', 'Haridwar', '100', 'UP14AB1234', 'Completed'),
(8, 'up16user@email.com', 'Haridwar', '100', 'UP12DL1234', 'Canceled'),
(9, 'test1@email.com', 'Haridwar', '100', '21BH2345AA', 'Booked'),
(10, 'userabc@email.com', 'Haridwar', '100', 'HR26DK8337', 'Completed');

-- --------------------------------------------------------

--
-- Table structure for table `challans`
--

CREATE TABLE `challans` (
  `id` int(11) NOT NULL,
  `reg_no` text NOT NULL,
  `driver` text NOT NULL,
  `user_phone` text NOT NULL,
  `description` text NOT NULL,
  `amount` text NOT NULL,
  `location` text NOT NULL,
  `date_and_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `paid` text NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `challans`
--

INSERT INTO `challans` (`id`, `reg_no`, `driver`, `user_phone`, `description`, `amount`, `location`, `date_and_time`, `paid`) VALUES
(1, 'regt', 'testdriver', 'test90910', 'Description test ', '800', 'Meerut', '2021-04-24 13:07:03', 'PAID'),
(2, 'werd', 'qwewqe', 'qweq', ' sdfqwera', 'fdfsdf', 'saferewqw', '2021-04-24 13:23:05', 'PAID'),
(3, 'DL13EB3210', 'qwrwer', 'erwr', ' wqerwq', 'wrwer', 'werwr', '2021-04-25 02:43:24', ''),
(4, '1234', 'dasas', 'dasdas', ' asdasd', 'asdasds', 'dasdasd', '2021-04-25 02:57:21', ''),
(5, 'DL13EB3210', 'Driver', 'jdkladj', 'slsadj ', '89', 'alkdj', '2021-04-25 04:52:41', '');

-- --------------------------------------------------------

--
-- Table structure for table `feedbacks`
--

CREATE TABLE `feedbacks` (
  `id` int(11) NOT NULL,
  `user_name` text NOT NULL,
  `user_email` text NOT NULL,
  `fedback` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedbacks`
--

INSERT INTO `feedbacks` (`id`, `user_name`, `user_email`, `fedback`) VALUES
(1, 'Hardeep', 'hardeep@email.com', 'Hello this is test feed back'),
(2, 'Hardeep', 'hardeep@email.com', 'this is second feedback thank you.');

-- --------------------------------------------------------

--
-- Table structure for table `officers`
--

CREATE TABLE `officers` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `officers`
--

INSERT INTO `officers` (`id`, `name`, `phone`, `password`) VALUES
(3, 'Officer 1', '9876987612', 'pass');

-- --------------------------------------------------------

--
-- Table structure for table `tolls`
--

CREATE TABLE `tolls` (
  `id` int(11) NOT NULL,
  `location` text NOT NULL,
  `highway` text NOT NULL,
  `amount` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tolls`
--

INSERT INTO `tolls` (`id`, `location`, `highway`, `amount`) VALUES
(2, 'Haridwar', 'NH24', '100');

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone` varchar(14) NOT NULL,
  `email` varchar(30) NOT NULL,
  `pass` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_login`
--

INSERT INTO `user_login` (`id`, `name`, `phone`, `email`, `pass`) VALUES
(1, 'Test One', '9090909', 'test1@email.com', 'pass'),
(2, 'Test2', '12345', 'test2@email.com', 'pass'),
(3, 'up16user', '161616', 'up16user@email.com', 'pass'),
(4, 'userabc', 'pass', 'userabc@email.com', 'pass'),
(5, 'test4', '1234567812', 'test4@email.com', 'pass');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_registrations`
--

CREATE TABLE `vehicle_registrations` (
  `id` int(11) NOT NULL,
  `reg_number` text NOT NULL,
  `eng_no` text NOT NULL,
  `chesis_no` text NOT NULL,
  `owner_phone` text NOT NULL,
  `owner_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_registrations`
--

INSERT INTO `vehicle_registrations` (`id`, `reg_number`, `eng_no`, `chesis_no`, `owner_phone`, `owner_name`) VALUES
(3, 'UP14AB1234', '342423523523', '86757123421423', '1234567890', 'Ram Kishan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `challans`
--
ALTER TABLE `challans`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedbacks`
--
ALTER TABLE `feedbacks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `officers`
--
ALTER TABLE `officers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tolls`
--
ALTER TABLE `tolls`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_login`
--
ALTER TABLE `user_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle_registrations`
--
ALTER TABLE `vehicle_registrations`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_login`
--
ALTER TABLE `admin_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `challans`
--
ALTER TABLE `challans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `feedbacks`
--
ALTER TABLE `feedbacks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `officers`
--
ALTER TABLE `officers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tolls`
--
ALTER TABLE `tolls`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_login`
--
ALTER TABLE `user_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vehicle_registrations`
--
ALTER TABLE `vehicle_registrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
