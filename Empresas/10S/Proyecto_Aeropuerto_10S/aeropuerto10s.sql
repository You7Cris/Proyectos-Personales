-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-09-2022 a las 12:09:43
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `aeropuerto10s`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_arrivals`
--

CREATE TABLE `arrivals_departures_arrivals` (
  `id` bigint(20) NOT NULL,
  `time` time(6) NOT NULL,
  `flight_no` varchar(6) NOT NULL,
  `expected_time` time(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `update_at` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_arrivals`
--

INSERT INTO `arrivals_departures_arrivals` (`id`, `time`, `flight_no`, `expected_time`, `created_at`, `update_at`, `user_id`) VALUES
(1, '19:35:00.000000', 'LY4488', NULL, '2022-09-17 00:05:40.119158', '2022-09-16', 1),
(2, '19:40:00.000000', 'TK7252', NULL, '2022-09-17 00:06:34.063285', '2022-09-16', 1),
(3, '19:45:00.000000', 'LV2317', NULL, '2022-09-17 07:29:37.450219', '2022-09-17', 1),
(4, '19:55:00.000000', 'HV3323', '20:02:00.000000', '2022-09-17 07:30:19.553277', '2022-09-17', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_arrivals_lugar`
--

CREATE TABLE `arrivals_departures_arrivals_lugar` (
  `id` bigint(20) NOT NULL,
  `arrivals_id` bigint(20) NOT NULL,
  `ciudad_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_arrivals_lugar`
--

INSERT INTO `arrivals_departures_arrivals_lugar` (`id`, `arrivals_id`, `ciudad_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_arrivals_remarks`
--

CREATE TABLE `arrivals_departures_arrivals_remarks` (
  `id` bigint(20) NOT NULL,
  `arrivals_id` bigint(20) NOT NULL,
  `remarks_arrivals_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_arrivals_remarks`
--

INSERT INTO `arrivals_departures_arrivals_remarks` (`id`, `arrivals_id`, `remarks_arrivals_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_ciudad`
--

CREATE TABLE `arrivals_departures_ciudad` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_ciudad`
--

INSERT INTO `arrivals_departures_ciudad` (`id`, `name`, `created_at`) VALUES
(1, 'Glasgow', '2022-09-16 23:00:06.968392'),
(2, 'Rome', '2022-09-16 23:00:13.344477'),
(3, 'San Francisco', '2022-09-16 23:00:21.519136'),
(4, 'Los Angeles', '2022-09-16 23:00:39.576190'),
(5, 'Frankfurt', '2022-09-16 23:00:48.704172'),
(6, 'Toronto', '2022-09-16 23:00:55.834628'),
(7, 'London', '2022-09-16 23:01:00.099719'),
(8, 'New York', '2022-09-17 07:29:59.985399');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_departures`
--

CREATE TABLE `arrivals_departures_departures` (
  `id` bigint(20) NOT NULL,
  `time` time(6) NOT NULL,
  `flight_no` varchar(6) NOT NULL,
  `expected_time` time(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `update_at` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_departures`
--

INSERT INTO `arrivals_departures_departures` (`id`, `time`, `flight_no`, `expected_time`, `created_at`, `update_at`, `user_id`) VALUES
(1, '07:35:00.000000', 'TH3946', NULL, '2022-09-17 00:12:05.599631', '2022-09-16', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_departures_gate`
--

CREATE TABLE `arrivals_departures_departures_gate` (
  `id` bigint(20) NOT NULL,
  `departures_id` bigint(20) NOT NULL,
  `gate_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_departures_gate`
--

INSERT INTO `arrivals_departures_departures_gate` (`id`, `departures_id`, `gate_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_departures_lugar`
--

CREATE TABLE `arrivals_departures_departures_lugar` (
  `id` bigint(20) NOT NULL,
  `departures_id` bigint(20) NOT NULL,
  `ciudad_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_departures_lugar`
--

INSERT INTO `arrivals_departures_departures_lugar` (`id`, `departures_id`, `ciudad_id`) VALUES
(1, 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_departures_remarks`
--

CREATE TABLE `arrivals_departures_departures_remarks` (
  `id` bigint(20) NOT NULL,
  `departures_id` bigint(20) NOT NULL,
  `remarks_departures_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_departures_remarks`
--

INSERT INTO `arrivals_departures_departures_remarks` (`id`, `departures_id`, `remarks_departures_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_gate`
--

CREATE TABLE `arrivals_departures_gate` (
  `id` bigint(20) NOT NULL,
  `name` varchar(3) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_gate`
--

INSERT INTO `arrivals_departures_gate` (`id`, `name`, `created_at`) VALUES
(1, 'A1', '2022-09-16 23:03:01.993047'),
(2, 'A2', '2022-09-16 23:03:06.129600'),
(3, 'A3', '2022-09-16 23:03:09.669069'),
(4, 'A4', '2022-09-16 23:03:13.343100'),
(5, 'A5', '2022-09-16 23:03:17.351748'),
(6, 'A6', '2022-09-16 23:03:21.126482'),
(7, 'B1', '2022-09-16 23:03:38.761440'),
(8, 'B2', '2022-09-16 23:03:42.246842'),
(9, 'B3', '2022-09-16 23:03:45.888639'),
(10, 'B4', '2022-09-16 23:03:49.474539'),
(11, 'B5', '2022-09-16 23:03:52.702301'),
(12, 'B6', '2022-09-16 23:03:56.861365'),
(13, 'C1', '2022-09-16 23:04:03.997559'),
(14, 'C2', '2022-09-16 23:04:06.800894'),
(15, 'C3', '2022-09-16 23:04:10.038091'),
(16, 'C4', '2022-09-16 23:04:13.240470'),
(17, 'C5', '2022-09-16 23:04:17.065692'),
(18, 'C6', '2022-09-16 23:04:20.241088');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_remarks_arrivals`
--

CREATE TABLE `arrivals_departures_remarks_arrivals` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_remarks_arrivals`
--

INSERT INTO `arrivals_departures_remarks_arrivals` (`id`, `name`, `created_at`) VALUES
(1, 'BAGS DELIVERED', '2022-09-16 23:01:17.776002'),
(2, 'BAGS ARRIVING', '2022-09-16 23:01:29.193682'),
(4, 'LANDED', '2022-09-16 23:02:04.990351'),
(5, 'EXPECTED', '2022-09-16 23:02:25.609569');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `arrivals_departures_remarks_departures`
--

CREATE TABLE `arrivals_departures_remarks_departures` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `arrivals_departures_remarks_departures`
--

INSERT INTO `arrivals_departures_remarks_departures` (`id`, `name`, `created_at`) VALUES
(1, 'ON TIME', '2022-09-16 23:02:36.118897'),
(2, 'DELAYED', '2022-09-16 23:02:42.797504'),
(3, 'CANCELLED', '2022-09-16 23:02:52.537675');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Ciudad', 7, 'add_ciudad'),
(26, 'Can change Ciudad', 7, 'change_ciudad'),
(27, 'Can delete Ciudad', 7, 'delete_ciudad'),
(28, 'Can view Ciudad', 7, 'view_ciudad'),
(29, 'Can add Porton', 8, 'add_gate'),
(30, 'Can change Porton', 8, 'change_gate'),
(31, 'Can delete Porton', 8, 'delete_gate'),
(32, 'Can view Porton', 8, 'view_gate'),
(33, 'Can add Comentario', 9, 'add_remarks_arrivals'),
(34, 'Can change Comentario', 9, 'change_remarks_arrivals'),
(35, 'Can delete Comentario', 9, 'delete_remarks_arrivals'),
(36, 'Can view Comentario', 9, 'view_remarks_arrivals'),
(37, 'Can add Comentario', 10, 'add_remarks_departures'),
(38, 'Can change Comentario', 10, 'change_remarks_departures'),
(39, 'Can delete Comentario', 10, 'delete_remarks_departures'),
(40, 'Can view Comentario', 10, 'view_remarks_departures'),
(41, 'Can add Llegada', 11, 'add_departures'),
(42, 'Can change Llegada', 11, 'change_departures'),
(43, 'Can delete Llegada', 11, 'delete_departures'),
(44, 'Can view Llegada', 11, 'view_departures'),
(45, 'Can add Llegada', 12, 'add_arrivals'),
(46, 'Can change Llegada', 12, 'change_arrivals'),
(47, 'Can delete Llegada', 12, 'delete_arrivals'),
(48, 'Can view Llegada', 12, 'view_arrivals');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$rMRESxWUznEnU59GdAsfu2$qz75XYvtVuUC8ti8jL5InAneeXGuqEpNe+0rpuu9kG0=', '2022-09-17 09:49:20.414136', 1, 'cristian', 'Cristian', 'Gonzalez', 'cristian@gmail.com', 1, 1, '2022-09-16 21:59:16.000000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-09-16 23:00:07.005847', '1', 'Glasgow', 1, '[{\"added\": {}}]', 7, 1),
(2, '2022-09-16 23:00:13.366931', '2', 'Rome', 1, '[{\"added\": {}}]', 7, 1),
(3, '2022-09-16 23:00:21.599190', '3', 'San Francisco', 1, '[{\"added\": {}}]', 7, 1),
(4, '2022-09-16 23:00:39.577188', '4', 'Los Angeles', 1, '[{\"added\": {}}]', 7, 1),
(5, '2022-09-16 23:00:48.766029', '5', 'Frankfurt', 1, '[{\"added\": {}}]', 7, 1),
(6, '2022-09-16 23:00:55.899465', '6', 'Toronto', 1, '[{\"added\": {}}]', 7, 1),
(7, '2022-09-16 23:01:00.099719', '7', 'London', 1, '[{\"added\": {}}]', 7, 1),
(8, '2022-09-16 23:01:17.817614', '1', 'BAGS DELIVERED', 1, '[{\"added\": {}}]', 9, 1),
(9, '2022-09-16 23:01:29.296998', '2', 'BAGS ARRIVING', 1, '[{\"added\": {}}]', 9, 1),
(10, '2022-09-16 23:01:49.432075', '3', 'LANDED', 1, '[{\"added\": {}}]', 9, 1),
(11, '2022-09-16 23:02:05.065001', '4', 'LANDED', 1, '[{\"added\": {}}]', 9, 1),
(12, '2022-09-16 23:02:18.563891', '3', 'LANDED', 3, '', 9, 1),
(13, '2022-09-16 23:02:25.638500', '5', 'EXPECTED', 1, '[{\"added\": {}}]', 9, 1),
(14, '2022-09-16 23:02:36.166218', '1', 'ON TIME', 1, '[{\"added\": {}}]', 10, 1),
(15, '2022-09-16 23:02:42.838688', '2', 'DELAYED', 1, '[{\"added\": {}}]', 10, 1),
(16, '2022-09-16 23:02:52.583801', '3', 'CANCELLED', 1, '[{\"added\": {}}]', 10, 1),
(17, '2022-09-16 23:03:01.998099', '1', 'A1', 1, '[{\"added\": {}}]', 8, 1),
(18, '2022-09-16 23:03:06.168501', '2', 'A2', 1, '[{\"added\": {}}]', 8, 1),
(19, '2022-09-16 23:03:09.696955', '3', 'A3', 1, '[{\"added\": {}}]', 8, 1),
(20, '2022-09-16 23:03:13.385612', '4', 'A4', 1, '[{\"added\": {}}]', 8, 1),
(21, '2022-09-16 23:03:17.396960', '5', 'A5', 1, '[{\"added\": {}}]', 8, 1),
(22, '2022-09-16 23:03:21.127487', '6', 'A6', 1, '[{\"added\": {}}]', 8, 1),
(23, '2022-09-16 23:03:38.814338', '7', 'B1', 1, '[{\"added\": {}}]', 8, 1),
(24, '2022-09-16 23:03:42.307038', '8', 'B2', 1, '[{\"added\": {}}]', 8, 1),
(25, '2022-09-16 23:03:45.914799', '9', 'B3', 1, '[{\"added\": {}}]', 8, 1),
(26, '2022-09-16 23:03:49.516498', '10', 'B4', 1, '[{\"added\": {}}]', 8, 1),
(27, '2022-09-16 23:03:52.729103', '11', 'B5', 1, '[{\"added\": {}}]', 8, 1),
(28, '2022-09-16 23:03:56.997351', '12', 'B6', 1, '[{\"added\": {}}]', 8, 1),
(29, '2022-09-16 23:04:04.071516', '13', 'C1', 1, '[{\"added\": {}}]', 8, 1),
(30, '2022-09-16 23:04:06.944546', '14', 'C2', 1, '[{\"added\": {}}]', 8, 1),
(31, '2022-09-16 23:04:10.108892', '15', 'C3', 1, '[{\"added\": {}}]', 8, 1),
(32, '2022-09-16 23:04:13.269242', '16', 'C4', 1, '[{\"added\": {}}]', 8, 1),
(33, '2022-09-16 23:04:17.102419', '17', 'C5', 1, '[{\"added\": {}}]', 8, 1),
(34, '2022-09-16 23:04:20.268071', '18', 'C6', 1, '[{\"added\": {}}]', 8, 1),
(35, '2022-09-17 00:05:40.190187', '1', 'LY4488', 1, '[{\"added\": {}}]', 12, 1),
(36, '2022-09-17 00:06:34.319189', '2', 'TK7252', 1, '[{\"added\": {}}]', 12, 1),
(37, '2022-09-17 00:12:05.856091', '1', 'TH3946', 1, '[{\"added\": {}}]', 11, 1),
(38, '2022-09-17 06:14:00.202792', '1', 'cristian', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1),
(39, '2022-09-17 07:29:37.594318', '3', 'LV2317', 1, '[{\"added\": {}}]', 12, 1),
(40, '2022-09-17 07:30:00.020605', '8', 'New York', 1, '[{\"added\": {}}]', 7, 1),
(41, '2022-09-17 07:30:19.588216', '4', 'HV3323', 1, '[{\"added\": {}}]', 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(12, 'arrivals_departures', 'arrivals'),
(7, 'arrivals_departures', 'ciudad'),
(11, 'arrivals_departures', 'departures'),
(8, 'arrivals_departures', 'gate'),
(9, 'arrivals_departures', 'remarks_arrivals'),
(10, 'arrivals_departures', 'remarks_departures'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-09-16 21:56:10.481953'),
(2, 'auth', '0001_initial', '2022-09-16 21:56:19.890968'),
(3, 'admin', '0001_initial', '2022-09-16 21:56:22.197887'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-09-16 21:56:22.267385'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-09-16 21:56:22.328773'),
(6, 'arrivals_departures', '0001_initial', '2022-09-16 21:56:43.900596'),
(7, 'contenttypes', '0002_remove_content_type_name', '2022-09-16 21:56:45.258792'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-09-16 21:56:46.090952'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-09-16 21:56:46.373246'),
(10, 'auth', '0004_alter_user_username_opts', '2022-09-16 21:56:46.450024'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-09-16 21:56:47.265941'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-09-16 21:56:47.306832'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-09-16 21:56:47.395292'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-09-16 21:56:47.544096'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-09-16 21:56:47.743569'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-09-16 21:56:47.901879'),
(17, 'auth', '0011_update_proxy_permissions', '2022-09-16 21:56:47.971286'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-09-16 21:56:48.163123'),
(19, 'sessions', '0001_initial', '2022-09-16 21:56:48.823971'),
(20, 'arrivals_departures', '0002_alter_departures_options_and_more', '2022-09-16 23:05:32.697696'),
(21, 'arrivals_departures', '0003_alter_arrivals_expected_time', '2022-09-16 23:13:11.151997'),
(22, 'arrivals_departures', '0004_alter_arrivals_expected_time_and_more', '2022-09-16 23:32:42.045847'),
(23, 'arrivals_departures', '0005_alter_arrivals_expected_time_and_more', '2022-09-16 23:37:45.233949');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('06bbbjlqqqcv178i8aj5ltawqxyoujn3', 'e30:1oZShc:dvSuwVpPffjiPsK92coZtfTizJ5DN9wcCniM0Xw17aw', '2022-10-01 07:57:28.757659');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `arrivals_departures_arrivals`
--
ALTER TABLE `arrivals_departures_arrivals`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `flight_no` (`flight_no`),
  ADD KEY `arrivals_departures_arrivals_user_id_34351ab1_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `arrivals_departures_arrivals_lugar`
--
ALTER TABLE `arrivals_departures_arrivals_lugar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `arrivals_departures_arri_arrivals_id_ciudad_id_91db8bc6_uniq` (`arrivals_id`,`ciudad_id`),
  ADD KEY `arrivals_departures__ciudad_id_d418f0d6_fk_arrivals_` (`ciudad_id`);

--
-- Indices de la tabla `arrivals_departures_arrivals_remarks`
--
ALTER TABLE `arrivals_departures_arrivals_remarks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `arrivals_departures_arri_arrivals_id_remarks_arri_6cb6002c_uniq` (`arrivals_id`,`remarks_arrivals_id`),
  ADD KEY `arrivals_departures__remarks_arrivals_id_08c954e5_fk_arrivals_` (`remarks_arrivals_id`);

--
-- Indices de la tabla `arrivals_departures_ciudad`
--
ALTER TABLE `arrivals_departures_ciudad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `arrivals_departures_departures`
--
ALTER TABLE `arrivals_departures_departures`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `flight_no` (`flight_no`),
  ADD KEY `arrivals_departures_departures_user_id_f0a00e11_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `arrivals_departures_departures_gate`
--
ALTER TABLE `arrivals_departures_departures_gate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `arrivals_departures_depa_departures_id_gate_id_5f94c5a0_uniq` (`departures_id`,`gate_id`),
  ADD KEY `arrivals_departures__gate_id_af9369df_fk_arrivals_` (`gate_id`);

--
-- Indices de la tabla `arrivals_departures_departures_lugar`
--
ALTER TABLE `arrivals_departures_departures_lugar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `arrivals_departures_depa_departures_id_ciudad_id_e4a53de2_uniq` (`departures_id`,`ciudad_id`),
  ADD KEY `arrivals_departures__ciudad_id_997829db_fk_arrivals_` (`ciudad_id`);

--
-- Indices de la tabla `arrivals_departures_departures_remarks`
--
ALTER TABLE `arrivals_departures_departures_remarks`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `arrivals_departures_depa_departures_id_remarks_de_f4ee1407_uniq` (`departures_id`,`remarks_departures_id`),
  ADD KEY `arrivals_departures__remarks_departures_i_31ba4714_fk_arrivals_` (`remarks_departures_id`);

--
-- Indices de la tabla `arrivals_departures_gate`
--
ALTER TABLE `arrivals_departures_gate`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `arrivals_departures_remarks_arrivals`
--
ALTER TABLE `arrivals_departures_remarks_arrivals`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `arrivals_departures_remarks_departures`
--
ALTER TABLE `arrivals_departures_remarks_departures`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_arrivals`
--
ALTER TABLE `arrivals_departures_arrivals`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_arrivals_lugar`
--
ALTER TABLE `arrivals_departures_arrivals_lugar`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_arrivals_remarks`
--
ALTER TABLE `arrivals_departures_arrivals_remarks`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_ciudad`
--
ALTER TABLE `arrivals_departures_ciudad`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_departures`
--
ALTER TABLE `arrivals_departures_departures`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_departures_gate`
--
ALTER TABLE `arrivals_departures_departures_gate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_departures_lugar`
--
ALTER TABLE `arrivals_departures_departures_lugar`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_departures_remarks`
--
ALTER TABLE `arrivals_departures_departures_remarks`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_gate`
--
ALTER TABLE `arrivals_departures_gate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_remarks_arrivals`
--
ALTER TABLE `arrivals_departures_remarks_arrivals`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `arrivals_departures_remarks_departures`
--
ALTER TABLE `arrivals_departures_remarks_departures`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `arrivals_departures_arrivals`
--
ALTER TABLE `arrivals_departures_arrivals`
  ADD CONSTRAINT `arrivals_departures_arrivals_user_id_34351ab1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `arrivals_departures_arrivals_lugar`
--
ALTER TABLE `arrivals_departures_arrivals_lugar`
  ADD CONSTRAINT `arrivals_departures__arrivals_id_94f38c8a_fk_arrivals_` FOREIGN KEY (`arrivals_id`) REFERENCES `arrivals_departures_arrivals` (`id`),
  ADD CONSTRAINT `arrivals_departures__ciudad_id_d418f0d6_fk_arrivals_` FOREIGN KEY (`ciudad_id`) REFERENCES `arrivals_departures_ciudad` (`id`);

--
-- Filtros para la tabla `arrivals_departures_arrivals_remarks`
--
ALTER TABLE `arrivals_departures_arrivals_remarks`
  ADD CONSTRAINT `arrivals_departures__arrivals_id_5cdb8f33_fk_arrivals_` FOREIGN KEY (`arrivals_id`) REFERENCES `arrivals_departures_arrivals` (`id`),
  ADD CONSTRAINT `arrivals_departures__remarks_arrivals_id_08c954e5_fk_arrivals_` FOREIGN KEY (`remarks_arrivals_id`) REFERENCES `arrivals_departures_remarks_arrivals` (`id`);

--
-- Filtros para la tabla `arrivals_departures_departures`
--
ALTER TABLE `arrivals_departures_departures`
  ADD CONSTRAINT `arrivals_departures_departures_user_id_f0a00e11_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `arrivals_departures_departures_gate`
--
ALTER TABLE `arrivals_departures_departures_gate`
  ADD CONSTRAINT `arrivals_departures__departures_id_31a7aff6_fk_arrivals_` FOREIGN KEY (`departures_id`) REFERENCES `arrivals_departures_departures` (`id`),
  ADD CONSTRAINT `arrivals_departures__gate_id_af9369df_fk_arrivals_` FOREIGN KEY (`gate_id`) REFERENCES `arrivals_departures_gate` (`id`);

--
-- Filtros para la tabla `arrivals_departures_departures_lugar`
--
ALTER TABLE `arrivals_departures_departures_lugar`
  ADD CONSTRAINT `arrivals_departures__ciudad_id_997829db_fk_arrivals_` FOREIGN KEY (`ciudad_id`) REFERENCES `arrivals_departures_ciudad` (`id`),
  ADD CONSTRAINT `arrivals_departures__departures_id_7546ac8f_fk_arrivals_` FOREIGN KEY (`departures_id`) REFERENCES `arrivals_departures_departures` (`id`);

--
-- Filtros para la tabla `arrivals_departures_departures_remarks`
--
ALTER TABLE `arrivals_departures_departures_remarks`
  ADD CONSTRAINT `arrivals_departures__departures_id_592172fa_fk_arrivals_` FOREIGN KEY (`departures_id`) REFERENCES `arrivals_departures_departures` (`id`),
  ADD CONSTRAINT `arrivals_departures__remarks_departures_i_31ba4714_fk_arrivals_` FOREIGN KEY (`remarks_departures_id`) REFERENCES `arrivals_departures_remarks_departures` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
