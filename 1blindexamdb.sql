-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 13, 2024 at 08:07 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1blindexamdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `questb`
--

CREATE TABLE `questb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Question` varchar(500) NOT NULL,
  `OptionA` varchar(500) NOT NULL,
  `OptionB` varchar(500) NOT NULL,
  `OptionC` varchar(500) NOT NULL,
  `OptionD` varchar(500) NOT NULL,
  `Answer` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `questb`
--

INSERT INTO `questb` (`id`, `Question`, `OptionA`, `OptionB`, `OptionC`, `OptionD`, `Answer`) VALUES
(2, 'Question', 'A', 'B', 'C', 'D', 'Option A'),
(3, 'Question 2', 'A', 'B', 'C', 'D', 'Option D'),
(4, 'Question 3', 'A', 'B', 'C', 'D', 'Option B');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'san', '7904902206', 'sangeeth5535@gmail.com', 'No 16 samnath plaza, melapudur  trichy\r\n', 'san', 'san'),
(2, 'san', '7904902206', 'sangeeth5535@gmail.com', 'No 16 samnath plaza, melapudur  trichy\r\n', 'san1', 'san1'),
(3, 'sangeeth', '7904902206', 'sangeeth5535@gmail.com', 'No 16 samnath plaza, melapudur  trichy\r\nNo 16 samnath plaza, melapudur, trichy', 'sangeeth', 'sangeeth');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `id` int(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `temptb`
--

INSERT INTO `temptb` (`id`, `UserName`) VALUES
(1, 'sangeeth');
