-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 20 nov. 2020 à 08:43
-- Version du serveur :  5.7.21
-- Version de PHP :  5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `ipssi_casino_g2`
--

-- --------------------------------------------------------

--
-- Structure de la table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
CREATE TABLE IF NOT EXISTS `joueur` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(250) DEFAULT NULL,
  `argent` double(10,2) DEFAULT NULL,
  `creation` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `joueur`
--

INSERT INTO `joueur` (`id`, `pseudo`, `argent`, `creation`) VALUES
(2, 'Louis', 41.00, '2020-11-17 16:01:23'),
(3, 'Micka', 0.00, '2020-11-17 16:13:00'),
(4, 'test', 10.00, '2020-11-17 16:34:32'),
(5, 'William', 10.00, '2020-11-17 17:24:00'),
(6, 'Loui', 20.00, '2020-11-17 17:26:24'),
(7, 'Maxime', 20.00, '2020-11-17 17:46:20'),
(8, 'Sarah', 0.00, '2020-11-17 17:56:20'),
(9, 'Bernard', 0.00, '2020-11-17 19:24:05'),
(10, 'Jr', 3.00, '2020-11-18 12:06:10'),
(11, 'Myriam', 10.00, '2020-11-18 15:12:46'),
(12, 'Eva', 10.00, '2020-11-18 15:40:54'),
(13, '55555', 10.00, '2020-11-18 16:30:56'),
(14, 'Valerie', 10.00, '2020-11-18 19:41:38'),
(15, 'Alex', 10.00, '2020-11-19 09:31:38'),
(16, '5', 10.00, '2020-11-19 15:27:07');

-- --------------------------------------------------------

--
-- Structure de la table `resultat`
--

DROP TABLE IF EXISTS `resultat`;
CREATE TABLE IF NOT EXISTS `resultat` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_joueur` int(10) NOT NULL,
  `niveau` int(10) DEFAULT NULL,
  `victoire` tinyint(1) DEFAULT NULL,
  `nb_coup` int(10) DEFAULT NULL,
  `mise` double(10,2) DEFAULT NULL,
  `gain` double(10,2) DEFAULT NULL,
  `creation` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_joueur` (`id_joueur`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `resultat`
--

INSERT INTO `resultat` (`id`, `id_joueur`, `niveau`, `victoire`, `nb_coup`, `mise`, `gain`, `creation`) VALUES
(1, 3, 3, 1, 5, 10.00, 10.00, '2020-11-17 17:09:33'),
(2, 3, 1, 1, 2, 10.00, 10.00, '2020-11-17 17:10:55'),
(3, 3, 2, 1, 5, 10.00, 5.00, '2020-11-17 17:12:43'),
(4, 3, 3, 1, 3, 5.00, 10.00, '2020-11-17 17:15:36'),
(5, 3, 3, 1, 4, 10.00, 10.00, '2020-11-17 17:16:38'),
(6, 3, 3, 1, 5, 10.00, 10.00, '2020-11-17 17:17:10'),
(7, 3, 3, 1, 5, 10.00, 10.00, '2020-11-17 17:17:47'),
(8, 3, 3, 1, 5, 10.00, 10.00, '2020-11-17 17:18:22'),
(9, 5, 3, 1, 4, 10.00, 10.00, '2020-11-17 17:24:18'),
(10, 6, 3, 1, 3, 10.00, 20.00, '2020-11-17 17:26:38'),
(11, 2, 1, 1, 3, 10.00, 5.00, '2020-11-17 17:37:07'),
(12, 2, 2, 1, 4, 5.00, 5.00, '2020-11-17 17:40:16'),
(13, 2, 3, 1, 4, 5.00, 5.00, '2020-11-17 17:41:03'),
(14, 2, 3, 0, 7, 5.00, 0.00, '2020-11-17 17:42:23'),
(15, 7, 1, 1, 1, 10.00, 20.00, '2020-11-17 17:47:30'),
(16, 7, 2, 1, 3, 20.00, 20.00, '2020-11-17 17:49:35'),
(17, 8, 1, 0, 3, 10.00, 0.00, '2020-11-17 17:58:28'),
(18, 9, 1, 0, 3, 10.00, 0.00, '2020-11-17 19:24:51'),
(19, 3, 1, 1, 1, 5.00, 10.00, '2020-11-18 10:55:14'),
(20, 3, 1, 1, 3, 5.00, 3.00, '2020-11-18 10:57:09'),
(21, 3, 1, 1, 2, 5.00, 5.00, '2020-11-18 10:58:54'),
(22, 3, 1, 0, 3, 5.00, 0.00, '2020-11-18 11:01:08'),
(23, 3, 1, 0, 3, 5.00, 0.00, '2020-11-18 11:01:24'),
(24, 2, 1, 0, 3, 40.00, 0.00, '2020-11-18 11:06:06'),
(25, 2, 3, 1, 2, 40.00, 80.00, '2020-11-18 11:06:42'),
(26, 2, 3, 1, 3, 40.00, 80.00, '2020-11-18 12:00:45'),
(27, 2, 1, 0, 3, 40.00, 0.00, '2020-11-18 12:03:38'),
(28, 2, 1, 1, 3, 5.00, 3.00, '2020-11-18 12:05:13'),
(29, 10, 1, 1, 3, 5.00, 3.00, '2020-11-18 12:06:23'),
(30, 10, 1, 0, 3, 5.00, 0.00, '2020-11-18 12:07:10'),
(31, 3, 3, 1, 5, 3.00, 3.00, '2020-11-18 12:16:08'),
(32, 2, 3, 1, 6, 70.00, 70.00, '2020-11-18 17:55:25'),
(33, 2, 1, 0, 3, 5.00, 0.00, '2020-11-18 18:11:52'),
(34, 2, 1, 0, 3, 1.00, 0.00, '2020-11-18 18:13:26'),
(35, 3, 1, 0, 3, 3.00, 0.00, '2020-11-19 14:42:21'),
(36, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 14:51:08'),
(37, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:09:24'),
(38, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:10:05'),
(39, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:38:20'),
(40, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:39:16'),
(41, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:45:26'),
(42, 2, 1, 1, 3, 1.00, 1.00, '2020-11-19 15:46:03'),
(43, 2, 1, 0, 3, 12.00, 0.00, '2020-11-19 15:46:56'),
(44, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:48:07'),
(45, 2, 2, 0, 5, 5.00, 0.00, '2020-11-19 15:49:38'),
(46, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:54:41'),
(47, 2, 1, 0, 3, 1.00, 0.00, '2020-11-19 15:56:44'),
(48, 2, 1, 1, 2, 5.00, 5.00, '2020-11-19 16:08:28'),
(49, 2, 3, 1, 5, 5.00, 5.00, '2020-11-19 16:08:56'),
(50, 2, 1, 0, 3, 5.00, 0.00, '2020-11-20 09:04:58');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `resultat`
--
ALTER TABLE `resultat`
  ADD CONSTRAINT `resultat_ibfk_1` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
