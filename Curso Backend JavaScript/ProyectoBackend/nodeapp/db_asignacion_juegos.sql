-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-05-2024 a las 18:57:04
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_asignacion_juegos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `cod_genero` varchar(6) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `cod_grupo` int(11) NOT NULL,
  `Juego` varchar(10) NOT NULL,
  `genero` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juegos`
--

CREATE TABLE `juegos` (
  `cod_juego` varchar(10) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `region` varchar(40) NOT NULL,
  `plataforma` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `juegos`
--

INSERT INTO `juegos` (`cod_juego`, `nombre`, `region`, `plataforma`) VALUES
('1', 'The Legend of Zelda', 'North America', 'Nintendo Switch'),
('10', 'God of War', 'Europe', 'PlayStation 4'),
('11', 'Halo Infinite', 'Asia', 'Xbox Series X'),
('12', 'Animal Crossing: New Horizons', 'South America', 'Nintendo Switch'),
('123', 'Need For Speed Most Wanted', 'US, EU', 'PS2, XBOX 360, PC'),
('13', 'Final Fantasy VII Remake', 'North America', 'PlayStation 4'),
('14', 'Genshin Impact', 'Europe', 'PC'),
('15', 'Among Us', 'Asia', 'Mobile'),
('16', 'The Elder Scrolls V: Skyrim', 'South America', 'PC'),
('17', 'Dark Souls III', 'North America', 'PlayStation 4'),
('18', 'Overwatch', 'Europe', 'PC'),
('19', 'League of Legends', 'Asia', 'PC'),
('2', 'Super Mario Odyssey', 'Europe', 'Nintendo Switch'),
('20', 'Horizon Zero Dawn', 'South America', 'PlayStation 4'),
('241526', 'Call Of Duty', 'US, FRA, ALE, EU', 'PS4, XBOX One, XBOX 360, PS3, PC'),
('3', 'Minecraft', 'Asia', 'PC'),
('3425', 'Need For Speed Pro Street', 'US, EU, COLOMBIA', 'PS2, XBOX 360, PC, PS3'),
('4', 'Fortnite', 'South America', 'PC'),
('5', 'Red Dead Redemption 2', 'North America', 'PlayStation 4'),
('6', 'The Witcher 3: Wild Hunt', 'Europe', 'PlayStation 4'),
('7', 'Apex Legends', 'Asia', 'Xbox One'),
('8', 'Call of Duty: Modern Warfare', 'South America', 'Xbox One'),
('9', 'Cyberpunk 2077', 'North America', 'PC');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`cod_genero`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`cod_grupo`),
  ADD KEY `asignatura` (`Juego`,`genero`),
  ADD KEY `empresa` (`genero`);

--
-- Indices de la tabla `juegos`
--
ALTER TABLE `juegos`
  ADD PRIMARY KEY (`cod_juego`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `grupo`
--
ALTER TABLE `grupo`
  MODIFY `cod_grupo` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`Juego`) REFERENCES `juegos` (`cod_juego`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `grupo_ibfk_2` FOREIGN KEY (`genero`) REFERENCES `genero` (`cod_genero`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
