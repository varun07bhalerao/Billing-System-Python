-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2025 at 03:27 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `billing_python_final`
--

-- --------------------------------------------------------

--
-- Table structure for table `bills_counter2`
--

CREATE TABLE `bills_counter2` (
  `id` int(11) NOT NULL,
  `bill_no` varchar(20) DEFAULT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `items` text DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `bill_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `counter_number` int(10) NOT NULL DEFAULT 2,
  `employee_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bills_counter2`
--

INSERT INTO `bills_counter2` (`id`, `bill_no`, `customer_name`, `phone`, `address`, `items`, `total_price`, `bill_date`, `counter_number`, `employee_name`) VALUES
(5, '2514', 'aaa', '1111', 'sss', 'Zinger Burger (1 x ₹99 = ₹99)', 99.00, '2025-03-16 11:24:40', 2, '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bills_counter2`
--
ALTER TABLE `bills_counter2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bills_counter2`
--
ALTER TABLE `bills_counter2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
