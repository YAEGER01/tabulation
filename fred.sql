/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 12.0.2-MariaDB : Database - tabulatormsanfermin
*********************************************************************
*/

/*!40101 SET NAMES utf8 */
;

/*!40101 SET SQL_MODE=''*/
;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */
;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */
;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */
;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */
;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tabulatormsanfermin` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `tabulatormsanfermin`;

/*Table structure for table `approval` */

DROP TABLE IF EXISTS `approval`;

CREATE TABLE `approval` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `approved` tinyint (1) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `approval` */

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(150) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `group_id` int(11) NOT NULL,
    `permission_id` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`, `permission_id`),
    KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
    CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
    CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `content_type_id` int(11) NOT NULL,
    `codename` varchar(100) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`, `codename`),
    CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 133 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `auth_permission` */

insert into
    `auth_permission` (
        `id`,
        `name`,
        `content_type_id`,
        `codename`
    )
values (
        1,
        'Can add log entry',
        1,
        'add_logentry'
    ),
    (
        2,
        'Can change log entry',
        1,
        'change_logentry'
    ),
    (
        3,
        'Can delete log entry',
        1,
        'delete_logentry'
    ),
    (
        4,
        'Can view log entry',
        1,
        'view_logentry'
    ),
    (
        5,
        'Can add permission',
        2,
        'add_permission'
    ),
    (
        6,
        'Can change permission',
        2,
        'change_permission'
    ),
    (
        7,
        'Can delete permission',
        2,
        'delete_permission'
    ),
    (
        8,
        'Can view permission',
        2,
        'view_permission'
    ),
    (
        9,
        'Can add group',
        3,
        'add_group'
    ),
    (
        10,
        'Can change group',
        3,
        'change_group'
    ),
    (
        11,
        'Can delete group',
        3,
        'delete_group'
    ),
    (
        12,
        'Can view group',
        3,
        'view_group'
    ),
    (
        13,
        'Can add user',
        4,
        'add_user'
    ),
    (
        14,
        'Can change user',
        4,
        'change_user'
    ),
    (
        15,
        'Can delete user',
        4,
        'delete_user'
    ),
    (
        16,
        'Can view user',
        4,
        'view_user'
    ),
    (
        17,
        'Can add content type',
        5,
        'add_contenttype'
    ),
    (
        18,
        'Can change content type',
        5,
        'change_contenttype'
    ),
    (
        19,
        'Can delete content type',
        5,
        'delete_contenttype'
    ),
    (
        20,
        'Can view content type',
        5,
        'view_contenttype'
    ),
    (
        21,
        'Can add session',
        6,
        'add_session'
    ),
    (
        22,
        'Can change session',
        6,
        'change_session'
    ),
    (
        23,
        'Can delete session',
        6,
        'delete_session'
    ),
    (
        24,
        'Can view session',
        6,
        'view_session'
    ),
    (
        25,
        'Can add approval',
        7,
        'add_approval'
    ),
    (
        26,
        'Can change approval',
        7,
        'change_approval'
    ),
    (
        27,
        'Can delete approval',
        7,
        'delete_approval'
    ),
    (
        28,
        'Can view approval',
        7,
        'view_approval'
    ),
    (
        29,
        'Can add candidate',
        8,
        'add_candidate'
    ),
    (
        30,
        'Can change candidate',
        8,
        'change_candidate'
    ),
    (
        31,
        'Can delete candidate',
        8,
        'delete_candidate'
    ),
    (
        32,
        'Can view candidate',
        8,
        'view_candidate'
    ),
    (
        33,
        'Can add criteria',
        9,
        'add_criteria'
    ),
    (
        34,
        'Can change criteria',
        9,
        'change_criteria'
    ),
    (
        35,
        'Can delete criteria',
        9,
        'delete_criteria'
    ),
    (
        36,
        'Can view criteria',
        9,
        'view_criteria'
    ),
    (
        37,
        'Can add es log user',
        10,
        'add_esloguser'
    ),
    (
        38,
        'Can change es log user',
        10,
        'change_esloguser'
    ),
    (
        39,
        'Can delete es log user',
        10,
        'delete_esloguser'
    ),
    (
        40,
        'Can view es log user',
        10,
        'view_esloguser'
    ),
    (
        41,
        'Can add event',
        11,
        'add_event'
    ),
    (
        42,
        'Can change event',
        11,
        'change_event'
    ),
    (
        43,
        'Can delete event',
        11,
        'delete_event'
    ),
    (
        44,
        'Can view event',
        11,
        'view_event'
    ),
    (
        45,
        'Can add gradinsname',
        12,
        'add_gradinsname'
    ),
    (
        46,
        'Can change gradinsname',
        12,
        'change_gradinsname'
    ),
    (
        47,
        'Can delete gradinsname',
        12,
        'delete_gradinsname'
    ),
    (
        48,
        'Can view gradinsname',
        12,
        'view_gradinsname'
    ),
    (
        49,
        'Can add gradminpas',
        13,
        'add_gradminpas'
    ),
    (
        50,
        'Can change gradminpas',
        13,
        'change_gradminpas'
    ),
    (
        51,
        'Can delete gradminpas',
        13,
        'delete_gradminpas'
    ),
    (
        52,
        'Can view gradminpas',
        13,
        'view_gradminpas'
    ),
    (
        53,
        'Can add judge',
        14,
        'add_judge'
    ),
    (
        54,
        'Can change judge',
        14,
        'change_judge'
    ),
    (
        55,
        'Can delete judge',
        14,
        'delete_judge'
    ),
    (
        56,
        'Can view judge',
        14,
        'view_judge'
    ),
    (
        57,
        'Can add judge approval',
        15,
        'add_judgeapproval'
    ),
    (
        58,
        'Can change judge approval',
        15,
        'change_judgeapproval'
    ),
    (
        59,
        'Can delete judge approval',
        15,
        'delete_judgeapproval'
    ),
    (
        60,
        'Can view judge approval',
        15,
        'view_judgeapproval'
    ),
    (
        61,
        'Can add judgecriteria',
        16,
        'add_judgecriteria'
    ),
    (
        62,
        'Can change judgecriteria',
        16,
        'change_judgecriteria'
    ),
    (
        63,
        'Can delete judgecriteria',
        16,
        'delete_judgecriteria'
    ),
    (
        64,
        'Can view judgecriteria',
        16,
        'view_judgecriteria'
    ),
    (
        65,
        'Can add judgesapproved',
        17,
        'add_judgesapproved'
    ),
    (
        66,
        'Can change judgesapproved',
        17,
        'change_judgesapproved'
    ),
    (
        67,
        'Can delete judgesapproved',
        17,
        'delete_judgesapproved'
    ),
    (
        68,
        'Can view judgesapproved',
        17,
        'view_judgesapproved'
    ),
    (
        69,
        'Can add resall',
        18,
        'add_resall'
    ),
    (
        70,
        'Can change resall',
        18,
        'change_resall'
    ),
    (
        71,
        'Can delete resall',
        18,
        'delete_resall'
    ),
    (
        72,
        'Can view resall',
        18,
        'view_resall'
    ),
    (
        73,
        'Can add rescri',
        19,
        'add_rescri'
    ),
    (
        74,
        'Can change rescri',
        19,
        'change_rescri'
    ),
    (
        75,
        'Can delete rescri',
        19,
        'delete_rescri'
    ),
    (
        76,
        'Can view rescri',
        19,
        'view_rescri'
    ),
    (
        77,
        'Can add resnoshow',
        20,
        'add_resnoshow'
    ),
    (
        78,
        'Can change resnoshow',
        20,
        'change_resnoshow'
    ),
    (
        79,
        'Can delete resnoshow',
        20,
        'delete_resnoshow'
    ),
    (
        80,
        'Can view resnoshow',
        20,
        'view_resnoshow'
    ),
    (
        81,
        'Can add s admin',
        21,
        'add_sadmin'
    ),
    (
        82,
        'Can change s admin',
        21,
        'change_sadmin'
    ),
    (
        83,
        'Can delete s admin',
        21,
        'delete_sadmin'
    ),
    (
        84,
        'Can view s admin',
        21,
        'view_sadmin'
    ),
    (
        85,
        'Can add scorevents',
        22,
        'add_scorevents'
    ),
    (
        86,
        'Can change scorevents',
        22,
        'change_scorevents'
    ),
    (
        87,
        'Can delete scorevents',
        22,
        'delete_scorevents'
    ),
    (
        88,
        'Can view scorevents',
        22,
        'view_scorevents'
    ),
    (
        89,
        'Can add score',
        23,
        'add_score'
    ),
    (
        90,
        'Can change score',
        23,
        'change_score'
    ),
    (
        91,
        'Can delete score',
        23,
        'delete_score'
    ),
    (
        92,
        'Can view score',
        23,
        'view_score'
    ),
    (
        93,
        'Can add s candidates',
        24,
        'add_scandidates'
    ),
    (
        94,
        'Can change s candidates',
        24,
        'change_scandidates'
    ),
    (
        95,
        'Can delete s candidates',
        24,
        'delete_scandidates'
    ),
    (
        96,
        'Can view s candidates',
        24,
        'view_scandidates'
    ),
    (
        97,
        'Can add scri',
        25,
        'add_scri'
    ),
    (
        98,
        'Can change scri',
        25,
        'change_scri'
    ),
    (
        99,
        'Can delete scri',
        25,
        'delete_scri'
    ),
    (
        100,
        'Can view scri',
        25,
        'view_scri'
    ),
    (
        101,
        'Can add s judge',
        26,
        'add_sjudge'
    ),
    (
        102,
        'Can change s judge',
        26,
        'change_sjudge'
    ),
    (
        103,
        'Can delete s judge',
        26,
        'delete_sjudge'
    ),
    (
        104,
        'Can view s judge',
        26,
        'view_sjudge'
    ),
    (
        105,
        'Can add sinscore',
        27,
        'add_sinscore'
    ),
    (
        106,
        'Can change sinscore',
        27,
        'change_sinscore'
    ),
    (
        107,
        'Can delete sinscore',
        27,
        'delete_sinscore'
    ),
    (
        108,
        'Can view sinscore',
        27,
        'view_sinscore'
    ),
    (
        109,
        'Can add score',
        28,
        'add_score'
    ),
    (
        110,
        'Can change score',
        28,
        'change_score'
    ),
    (
        111,
        'Can delete score',
        28,
        'delete_score'
    ),
    (
        112,
        'Can view score',
        28,
        'view_score'
    ),
    (
        113,
        'Can add candidate',
        29,
        'add_candidate'
    ),
    (
        114,
        'Can change candidate',
        29,
        'change_candidate'
    ),
    (
        115,
        'Can delete candidate',
        29,
        'delete_candidate'
    ),
    (
        116,
        'Can view candidate',
        29,
        'view_candidate'
    ),
    (
        117,
        'Can add criteria',
        30,
        'add_criteria'
    ),
    (
        118,
        'Can change criteria',
        30,
        'change_criteria'
    ),
    (
        119,
        'Can delete criteria',
        30,
        'delete_criteria'
    ),
    (
        120,
        'Can view criteria',
        30,
        'view_criteria'
    ),
    (
        121,
        'Can add event',
        31,
        'add_event'
    ),
    (
        122,
        'Can change event',
        31,
        'change_event'
    ),
    (
        123,
        'Can delete event',
        31,
        'delete_event'
    ),
    (
        124,
        'Can view event',
        31,
        'view_event'
    ),
    (
        125,
        'Can add judge',
        32,
        'add_judge'
    ),
    (
        126,
        'Can change judge',
        32,
        'change_judge'
    ),
    (
        127,
        'Can delete judge',
        32,
        'delete_judge'
    ),
    (
        128,
        'Can view judge',
        32,
        'view_judge'
    ),
    (
        129,
        'Can add judge criteria',
        33,
        'add_judgecriteria'
    ),
    (
        130,
        'Can change judge criteria',
        33,
        'change_judgecriteria'
    ),
    (
        131,
        'Can delete judge criteria',
        33,
        'delete_judgecriteria'
    ),
    (
        132,
        'Can view judge criteria',
        33,
        'view_judgecriteria'
    );

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `password` varchar(128) NOT NULL,
    `last_login` datetime(6) DEFAULT NULL,
    `is_superuser` tinyint (1) NOT NULL,
    `username` varchar(150) NOT NULL,
    `first_name` varchar(150) NOT NULL,
    `last_name` varchar(150) NOT NULL,
    `email` varchar(254) NOT NULL,
    `is_staff` tinyint (1) NOT NULL,
    `is_active` tinyint (1) NOT NULL,
    `date_joined` datetime(6) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL,
    `group_id` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`, `group_id`),
    KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
    CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
    CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL,
    `permission_id` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`, `permission_id`),
    KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
    CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
    CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `candidate` */

DROP TABLE IF EXISTS `candidate`;

CREATE TABLE `candidate` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `cano` int(11) DEFAULT NULL,
    `cname` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `candidate` */

/*Table structure for table `criteria` */

DROP TABLE IF EXISTS `criteria`;

CREATE TABLE `criteria` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `ctitle` varchar(50) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `criteria` */

/*Table structure for table `dbase_candidate` */

DROP TABLE IF EXISTS `dbase_candidate`;

CREATE TABLE `dbase_candidate` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `dbase_candidate` */

/*Table structure for table `dbase_criteria` */

DROP TABLE IF EXISTS `dbase_criteria`;

CREATE TABLE `dbase_criteria` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `dbase_criteria` */

/*Table structure for table `dbase_event` */

DROP TABLE IF EXISTS `dbase_event`;

CREATE TABLE `dbase_event` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `dbase_event` */

/*Table structure for table `dbase_judge` */

DROP TABLE IF EXISTS `dbase_judge`;

CREATE TABLE `dbase_judge` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `dbase_judge` */

/*Table structure for table `dbase_judgecriteria` */

DROP TABLE IF EXISTS `dbase_judgecriteria`;

CREATE TABLE `dbase_judgecriteria` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `criteria_id` bigint (20) NOT NULL,
    `judge_id` bigint (20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `dbase_judgecriteria_criteria_id_ad039158_fk_dbase_criteria_id` (`criteria_id`),
    KEY `dbase_judgecriteria_judge_id_bb4cf821_fk_dbase_judge_id` (`judge_id`),
    CONSTRAINT `dbase_judgecriteria_criteria_id_ad039158_fk_dbase_criteria_id` FOREIGN KEY (`criteria_id`) REFERENCES `dbase_criteria` (`id`),
    CONSTRAINT `dbase_judgecriteria_judge_id_bb4cf821_fk_dbase_judge_id` FOREIGN KEY (`judge_id`) REFERENCES `dbase_judge` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `dbase_judgecriteria` */

/*Table structure for table `dbase_score` */

DROP TABLE IF EXISTS `dbase_score`;

CREATE TABLE `dbase_score` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `value` int(11) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `dbase_score` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `action_time` datetime(6) NOT NULL,
    `object_id` longtext DEFAULT NULL,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint (5) unsigned NOT NULL CHECK (`action_flag` >= 0),
    `change_message` longtext NOT NULL,
    `content_type_id` int(11) DEFAULT NULL,
    `user_id` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
    KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
    CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
    CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `app_label` varchar(100) NOT NULL,
    `model` varchar(100) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`, `model`)
) ENGINE = InnoDB AUTO_INCREMENT = 34 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `django_content_type` */

insert into
    `django_content_type` (`id`, `app_label`, `model`)
values (1, 'admin', 'logentry'),
    (3, 'auth', 'group'),
    (2, 'auth', 'permission'),
    (4, 'auth', 'user'),
    (
        5,
        'contenttypes',
        'contenttype'
    ),
    (29, 'dbase', 'candidate'),
    (30, 'dbase', 'criteria'),
    (31, 'dbase', 'event'),
    (32, 'dbase', 'judge'),
    (33, 'dbase', 'judgecriteria'),
    (28, 'dbase', 'score'),
    (7, 'mainapp', 'approval'),
    (8, 'mainapp', 'candidate'),
    (9, 'mainapp', 'criteria'),
    (10, 'mainapp', 'esloguser'),
    (11, 'mainapp', 'event'),
    (12, 'mainapp', 'gradinsname'),
    (13, 'mainapp', 'gradminpas'),
    (14, 'mainapp', 'judge'),
    (
        15,
        'mainapp',
        'judgeapproval'
    ),
    (
        16,
        'mainapp',
        'judgecriteria'
    ),
    (
        17,
        'mainapp',
        'judgesapproved'
    ),
    (18, 'mainapp', 'resall'),
    (19, 'mainapp', 'rescri'),
    (20, 'mainapp', 'resnoshow'),
    (21, 'mainapp', 'sadmin'),
    (24, 'mainapp', 'scandidates'),
    (23, 'mainapp', 'score'),
    (22, 'mainapp', 'scorevents'),
    (25, 'mainapp', 'scri'),
    (27, 'mainapp', 'sinscore'),
    (26, 'mainapp', 'sjudge'),
    (6, 'sessions', 'session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `app` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `applied` datetime(6) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 22 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `django_migrations` */

insert into
    `django_migrations` (
        `id`,
        `app`,
        `name`,
        `applied`
    )
values (
        1,
        'contenttypes',
        '0001_initial',
        '2025-10-11 00:48:47.999553'
    ),
    (
        2,
        'auth',
        '0001_initial',
        '2025-10-11 00:48:49.250357'
    ),
    (
        3,
        'admin',
        '0001_initial',
        '2025-10-11 00:48:49.479653'
    ),
    (
        4,
        'admin',
        '0002_logentry_remove_auto_add',
        '2025-10-11 00:48:49.486701'
    ),
    (
        5,
        'admin',
        '0003_logentry_add_action_flag_choices',
        '2025-10-11 00:48:49.504055'
    ),
    (
        6,
        'contenttypes',
        '0002_remove_content_type_name',
        '2025-10-11 00:48:49.650602'
    ),
    (
        7,
        'auth',
        '0002_alter_permission_name_max_length',
        '2025-10-11 00:48:49.734279'
    ),
    (
        8,
        'auth',
        '0003_alter_user_email_max_length',
        '2025-10-11 00:48:49.792361'
    ),
    (
        9,
        'auth',
        '0004_alter_user_username_opts',
        '2025-10-11 00:48:49.802904'
    ),
    (
        10,
        'auth',
        '0005_alter_user_last_login_null',
        '2025-10-11 00:48:49.891536'
    ),
    (
        11,
        'auth',
        '0006_require_contenttypes_0002',
        '2025-10-11 00:48:49.901410'
    ),
    (
        12,
        'auth',
        '0007_alter_validators_add_error_messages',
        '2025-10-11 00:48:49.914100'
    ),
    (
        13,
        'auth',
        '0008_alter_user_username_max_length',
        '2025-10-11 00:48:49.967537'
    ),
    (
        14,
        'auth',
        '0009_alter_user_last_name_max_length',
        '2025-10-11 00:48:50.050298'
    ),
    (
        15,
        'auth',
        '0010_alter_group_name_max_length',
        '2025-10-11 00:48:50.126460'
    ),
    (
        16,
        'auth',
        '0011_update_proxy_permissions',
        '2025-10-11 00:48:50.154190'
    ),
    (
        17,
        'auth',
        '0012_alter_user_first_name_max_length',
        '2025-10-11 00:48:50.212165'
    ),
    (
        18,
        'mainapp',
        '0001_initial',
        '2025-10-11 00:48:51.820479'
    ),
    (
        19,
        'sessions',
        '0001_initial',
        '2025-10-11 00:48:51.935773'
    ),
    (
        20,
        'dbase',
        '0001_initial',
        '2025-10-11 03:27:50.703120'
    ),
    (
        21,
        'mainapp',
        '0002_judge_event_judge_uname',
        '2025-10-11 03:39:09.064601'
    );

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
    `session_key` varchar(40) NOT NULL,
    `session_data` longtext NOT NULL,
    `expire_date` datetime(6) NOT NULL,
    PRIMARY KEY (`session_key`),
    KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `django_session` */

insert into
    `django_session` (
        `session_key`,
        `session_data`,
        `expire_date`
    )
values (
        '26p3m2pakkhymc4nmun5lttf47dhwdsw',
        '.eJyrVsrJT89LzE1VslJKTMnNzEtJTSpNV9IBCRckFhejCBsaGUNkMlOUrEwNDIx0lJJLinJgvFoA9k0Yrg:1vSuid:I8ltphPff7IyiJ5-wReYl4PkDUHSIFUATFbHAw5tZD4',
        '2025-12-23 10:13:19.770598'
    ),
    (
        '58wsuyrxygrphcotj6ryh3n9h5xrywh5',
        '.eJyrVsrJT89LzE1VslJKTMnNzDMyMDJV0gGJFiQWF8NEQWyETGaKkpWpgYGhjlJySVEOjFcLAKRVF1E:1v8S2i:mh1q9h1CNthr42XKxpor3CFUWGKBbdq8734VTCcBArY',
        '2025-10-27 23:33:28.041127'
    ),
    (
        '660tbzrse6txzdf3dbrzpqc4a00zbvtl',
        '.eJyrVsrJT89LzE1VslJKTMnNzDMyMDJV0gGJFiQWF8NEQWyETGaKkpWpgYGhjlJySVEOjFcLAKRVF1E:1vDiF1:WB6E5fhXDurUDtp5UJgAU4XsmOi9Yjr4adDE8pYtEgA',
        '2025-11-11 11:51:55.926348'
    ),
    (
        '6f6d19zx6loxdtqtg3si54m4ggvbjnj8',
        '.eJyrVsoqTUlPzUxRsjIxMDTQUUpOLElNV7JSKspPysmvAEsaKQGFS4pyEIpy8tPzEnNT0ZXVAgDcMxl6:1v8VYz:5AWkX82biX9ZPz7sRrlztwRjeimkV_5B4UGqRF7ENrY',
        '2025-10-28 03:19:01.576723'
    ),
    (
        '9l4kabxsmga4tzn221a7ty72wkpdsg66',
        '.eJyrVsoqTUlPzUxRsjIxMDDWUUpOLElNV7JSKsvPUwLySopyEHI5-el5ibmpQNmU0pLUopJUpVoAgDQUIA:1v8HbC:abgO_uZmukjlKPV89qPzR84rxMVBD9wLYAaMq3Eaq_M',
        '2025-10-27 12:24:22.080816'
    ),
    (
        'a23k2ec044yno4ycq9namfa5qvgnhcri',
        '.eJyrVsrJT89LzE1VslJKTMnNzDMyMDJV0gGJFiQWF8NEQWyETGaKkpWpgYGhjlJySVEOjFcLAKRVF1E:1v8VlL:aPsH3WFaEWjaTpr1mZBkEW0IYjkmqFwhbqY8M4Tnn6Y',
        '2025-10-28 03:31:47.446883'
    ),
    (
        'al0pqz6zte1w0ntb14sqfq2xdzu145zh',
        '.eJyrVsoqTUlPzUxRsjIxMDTUUUpOLElNV7JSKspPysmvAEsaKwGFS4pyEIpy8tPzEnNT0ZXVAgDcuxl-:1v8VYo:H-1jR9ziCWWH3SXQt5ZDLk1xZYEW_fUsSpA44lmsl7I',
        '2025-10-28 03:18:50.141725'
    ),
    (
        'bro1i5tek0wrac2mskahwma2mmcl9vo9',
        '.eJyrVsrJT89LzE1VslJKTMnNzDMyMDJV0gGJFiQWF8NEQWyETGaKkpWpgYGhjlJySVEOjFcLAKRVF1E:1vDw2A:dLN5TJKhDFjAV6lprU6YVrS-FBAsn-y2BusAVXzUfD0',
        '2025-11-12 02:35:34.379433'
    ),
    (
        'cci72ixxzumuj4yyuocj3z1pneuq3zpf',
        '.eJyrVsoqTUlPzUxRsjLUUUpOLElNV7KCiBkqAQVKinKgcjn56XmJualAWS-IbC0ASHwTBA:1vDiZO:h1YU7ZwPNdrYfPj5jC8WzoUt7OvJTZ_zwA11UezWj80',
        '2025-11-11 12:12:58.314284'
    ),
    (
        'eqotuupmginobt6jzzgtxpxka8xr6bff',
        'eyJqdWRnZWlkIjo3LCJjYXRlZyI6ImpvZWwiLCJjdHJsaWQiOjcsImxvZ25hbWUiOiJKb2VsIEd1bWlyYW4ifQ:1vDwKU:7isjCuyTOSiN1U_Xfjans33psEkJHCvoYdL3fIO6Wvg',
        '2025-11-12 02:54:30.660975'
    ),
    (
        'gbhgt9l6d7zsg5f7s4sk8ad54ykd1myb',
        '.eJyrVsoqTUlPzUxRsjI00lFKTixJTVeyUspKzcurVALyS4pyYHI5-el5ibmpQFkvkKyCf1FKZl5iUWW-Ui0AG74XBw:1vSuvh:n9XHdnj-xd8mon6V16KHrL6VEj1wcoNUv3rkfCjBQ-c',
        '2025-12-23 10:26:49.992472'
    ),
    (
        'j1id8m7im81mkeftzrx3flj52zq75blq',
        '.eJyrVsoqTUlPzUxRsrLQUUpOLElNV7JSSs5ILSqqVAIKlBTlQOVy8tPzEnNTgbLOYFkF99LczKLEPKVaAP8gFp8:1vDwWJ:IhjYAFbUvnQ8jJvRwR5MSKqtQL8mJ-VFMvF9zAJ6SEg',
        '2025-11-12 03:06:43.038335'
    ),
    (
        'jlu53ucarcgn62p7yhgyp6dn43d0k6tb',
        '.eJyrVsoqTUlPzUxRsjIxMDDWUUpOLElNV7JSKsvPUwLySopyEHI5-el5ibmpQNmU0pLUopJUpVoAgDQUIA:1v8HgS:SknX4Rbv0mumaKxs9Zr4wV_zTmhn-za2wTX1OnHW0fs',
        '2025-10-27 12:29:48.245138'
    ),
    (
        'm88wb30900pq9q65vip5wk94tfrit07g',
        '.eJyrVsoqTUlPzUxRsjI01FFKTixJTVeyUkorSk1RAnJLinJgUjn56XmJualASTegZGpRZnK2gm9iSmJlYrpSLQAqExcK:1vSumo:2kcW0b2G_6iHUUcqJQ8OVS4hNNEtnOQxrw-AEIH_IKc',
        '2025-12-23 10:17:38.570768'
    ),
    (
        'ntuivh6i7kq7ep7cbesqzr82jft8kj77',
        'e30:1v8HjF:pYGSsICC1b3wwA_J3DBLIqP90LeA4T7Qr2m9AyBr6Zk',
        '2025-10-27 12:32:41.249460'
    ),
    (
        'pfo9qfdegfy7vnlgeh26yrd96ndgvtbl',
        '.eJyrVsoqTUlPzUxRsjIxMDDWUUpOLElNV7JSKsvPUwLySopyEHI5-el5ibmpQNmU0pLUopJUpVoAgDQUIA:1v8HZ6:yOlUeSPaxuxQ9QWEB0tr_sdPTYwy6ueSBLk6TVcaoAg',
        '2025-10-27 12:22:12.692236'
    ),
    (
        'r2ld6sz7su4ftp2z8kee67hpjcqcptkb',
        'e30:1vDwYa:8XYrcVfyjDetph-4wHLDb7TvKyISn2e-1JgBMUpIhlI',
        '2025-11-12 03:09:04.728381'
    ),
    (
        'rdhgqax2zlp1571qnyvps58p35xd92uu',
        '.eJyrVsoqTUlPzUxRsjLTUUpOLElNV7JSyi0CixorAYVKinKgsjn56XmJuanI8rUApeQU8A:1vDifr:jRGLOHK_1oeWsqVFbAxLqfwFiuuH3ANGMDIh7ZOHnS8',
        '2025-11-11 12:19:39.852195'
    ),
    (
        't0uwhgmq5kshbetar0vdccl8cwh1v9en',
        '.eJyrVsoqTUlPzUxRsjI01lFKTixJTVeyUspKLM7NzEtVAoqUFOXAZHPy0_MSc1OB8l4QeYWg_JLS9MQcpVoAT6EXtg:1vSuvE:wZUOemA14zf6DrlhFZbhdiqmxVsBU_g-q82ZMbL44aU',
        '2025-12-23 10:26:20.738737'
    ),
    (
        'ts3by1gqmn1uyypc0w3ugcsxo24fq3bl',
        'eyJqdWRnZWlkIjo5LCJjYXRlZyI6InZvbiIsImN0cmxpZCI6OSwibG9nbmFtZSI6IkNocmlzdG9waGVyIn0:1vDwT6:bHB0TXVEWqtwk0UFYy1IgzSKta2qnbOz5fSOqUd-qNQ',
        '2025-11-12 03:03:24.900598'
    ),
    (
        'ueclstupoeg8gsx3pdqwsqjf78r2ywiy',
        '.eJyrVsoqTUlPzUxRsjIxMDDWUUpOLElNV7JSKsvPUwLySopyEHI5-el5ibmpQNmU0pLUopJUpVoAgDQUIA:1v8Hba:5F4EhfBWgDe24xCFZjvShNnvWbdYdraqw6n5WdegiYc',
        '2025-10-27 12:24:46.084209'
    ),
    (
        'w8r969av5ujzk7j38aqscgbm7ccodwmu',
        'e30:1v8HYj:tH0_-3g3P6rVHI7eLmjoUFtVbk2poyLZKFaFMbmZfRo',
        '2025-10-27 12:21:49.066081'
    ),
    (
        'xlw0681hayptny7gosvw00pzonjklt3h',
        '.eJyrVsoqTUlPzUxRsjIxMDDWUUpOLElNV7JSKsvPUwLySopyEHI5-el5ibmpQNmU0pLUopJUpVoAgDQUIA:1v8Hq7:3QrU6MTjuz63OddZPFaZF9htimTTUbQBpghKCA9VQjQ',
        '2025-10-27 12:39:47.446595'
    ),
    (
        'xv1nd482j0fnbsad7u1uttr23a5r8e0h',
        '.eJyrVsoqTUlPzUxRsjIxMDDRUUpOLElNV7JSKkktLsnMS1cCipQU5SDkc_LT8xJzU4EqyvLz8iqVagG4dRUK:1v8QLB:v50LqBf4vxgk1rjVyitgWlnoybHTFMSsxYMHoZ7OSKU',
        '2025-10-27 21:44:25.201139'
    );

/*Table structure for table `esloguser` */

DROP TABLE IF EXISTS `esloguser`;

CREATE TABLE `esloguser` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `action` varchar(100) NOT NULL,
    `timestamp` datetime(6) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `esloguser` */

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `evdes` varchar(150) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 17 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `event` */

insert into
    `event` (`id`, `evdes`)
values (9, 'ROBLOX'),
    (10, 'LEGO'),
    (11, 'zxc123'),
    (12, 'DEBUG SIR JOEL'),
    (13, 'Miss San Fermin'),
    (14, 'Mr. San Fermin'),
    (15, 'zxc'),
    (16, 'haha');

/*Table structure for table `gradinsname` */

DROP TABLE IF EXISTS `gradinsname`;

CREATE TABLE `gradinsname` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `fname` varchar(50) NOT NULL,
    `lname` varchar(50) NOT NULL,
    `ulevel` varchar(5) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `gradinsname` */

/*Table structure for table `gradminpas` */

DROP TABLE IF EXISTS `gradminpas`;

CREATE TABLE `gradminpas` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `spassword` varchar(128) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 5 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `gradminpas` */

insert into
    `gradminpas` (`id`, `username`, `spassword`)
values (
        3,
        'admin_gradmin',
        'pass_gradmin'
    ),
    (
        4,
        'easygradmin',
        'easygradminpass'
    );

/*Table structure for table `judge` */

DROP TABLE IF EXISTS `judge`;

CREATE TABLE `judge` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `jname` varchar(100) NOT NULL,
    `event_id` bigint (20) DEFAULT NULL,
    `uname` varchar(100) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `judge_event_id_a26fbaae_fk_event_id` (`event_id`),
    CONSTRAINT `judge_event_id_a26fbaae_fk_event_id` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 23 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `judge` */

/*Table structure for table `judgeapproval` */

DROP TABLE IF EXISTS `judgeapproval`;

CREATE TABLE `judgeapproval` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `approved` tinyint (1) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `judgeapproval` */

/*Table structure for table `judgecriteria` */

DROP TABLE IF EXISTS `judgecriteria`;

CREATE TABLE `judgecriteria` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `ejid` int(11) DEFAULT NULL,
    `scri` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `judgecriteria` */

/*Table structure for table `judgesapproved` */

DROP TABLE IF EXISTS `judgesapproved`;

CREATE TABLE `judgesapproved` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `ejid` int(11) DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    `sconid` int(11) DEFAULT NULL,
    `aprem` varchar(2) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `judgesapproved` */

/*Table structure for table `resall` */

DROP TABLE IF EXISTS `resall`;

CREATE TABLE `resall` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `sconid` int(11) DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    `ejid` int(11) DEFAULT NULL,
    `scri` int(11) DEFAULT NULL,
    `inscore` varchar(6) DEFAULT NULL,
    `category` varchar(20) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `resall` */

/*Table structure for table `rescri` */

DROP TABLE IF EXISTS `rescri`;

CREATE TABLE `rescri` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `sconid` int(11) DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    `ejid` int(11) DEFAULT NULL,
    `scri` int(11) DEFAULT NULL,
    `inscore` varchar(6) DEFAULT NULL,
    `category` varchar(20) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `rescri` */

/*Table structure for table `resnoshow` */

DROP TABLE IF EXISTS `resnoshow`;

CREATE TABLE `resnoshow` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `noshow` varchar(3) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `resnoshow` */

/*Table structure for table `sadmin` */

DROP TABLE IF EXISTS `sadmin`;

CREATE TABLE `sadmin` (
    `userid` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) DEFAULT NULL,
    `userlevel` varchar(5) DEFAULT NULL,
    `uname` varchar(50) DEFAULT NULL,
    `spassword` longblob DEFAULT NULL,
    PRIMARY KEY (`userid`)
) ENGINE = InnoDB AUTO_INCREMENT = 5003 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `sadmin` */

insert into
    `sadmin` (
        `userid`,
        `username`,
        `userlevel`,
        `uname`,
        `spassword`
    )
values (
        2001,
        'admin_sadmin',
        '1',
        'Admin SAdmin',
        'pass_sadmin'
    ),
    (
        3001,
        'easyadmin',
        '1',
        'Easy Admin',
        'a75d96038b009f347978e771f49ba355'
    ),
    (
        5001,
        'admin2025',
        '1',
        'Admin 2025',
        '32a8dbf00001d9179be0ffca69e0290d'
    ),
    (
        5002,
        'admindebug',
        '1',
        'Admin Debug',
        'aca991ac0eee9dcaf58528d40d66ad72'
    );

/*Table structure for table `scandidates` */

DROP TABLE IF EXISTS `scandidates`;

CREATE TABLE `scandidates` (
    `sconid` int(11) NOT NULL AUTO_INCREMENT,
    `cano` int(11) DEFAULT NULL,
    `cname` varchar(100) DEFAULT NULL,
    `course` varchar(10) DEFAULT NULL,
    `category` varchar(20) DEFAULT NULL,
    `canstatus` varchar(2) DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    `ejid` int(11) DEFAULT NULL,
    PRIMARY KEY (`sconid`),
    KEY `scandidates_ejid_43e33722_fk_sjudge_ejid` (`ejid`),
    KEY `scandidates_evid_b6c60647_fk_scorevents_evid` (`evid`),
    CONSTRAINT `scandidates_ejid_43e33722_fk_sjudge_ejid` FOREIGN KEY (`ejid`) REFERENCES `sjudge` (`ejid`),
    CONSTRAINT `scandidates_evid_b6c60647_fk_scorevents_evid` FOREIGN KEY (`evid`) REFERENCES `scorevents` (`evid`)
) ENGINE = InnoDB AUTO_INCREMENT = 9 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `scandidates` */

insert into
    `scandidates` (
        `sconid`,
        `cano`,
        `cname`,
        `course`,
        `category`,
        `canstatus`,
        `evid`,
        `ejid`
    )
values (
        6,
        1,
        'Roblox1',
        'none1',
        'Mr.',
        '1',
        9,
        NULL
    ),
    (
        7,
        2,
        'Roblox2',
        'none',
        'Mr.',
        '1',
        9,
        NULL
    ),
    (
        8,
        3,
        'Roblox3',
        'none',
        'Mr.',
        '1',
        9,
        NULL
    );

/*Table structure for table `score` */

DROP TABLE IF EXISTS `score`;

CREATE TABLE `score` (
    `id` bigint (20) NOT NULL AUTO_INCREMENT,
    `value` double NOT NULL,
    `candidate_id` bigint (20) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `score_candidate_id_457544f8_fk_candidate_id` (`candidate_id`),
    CONSTRAINT `score_candidate_id_457544f8_fk_candidate_id` FOREIGN KEY (`candidate_id`) REFERENCES `candidate` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `score` */

/*Table structure for table `scorevents` */

DROP TABLE IF EXISTS `scorevents`;

CREATE TABLE `scorevents` (
    `evid` int(11) NOT NULL AUTO_INCREMENT,
    `evdes` varchar(150) DEFAULT NULL,
    PRIMARY KEY (`evid`)
) ENGINE = InnoDB AUTO_INCREMENT = 11 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `scorevents` */

insert into
    `scorevents` (`evid`, `evdes`)
values (9, '123'),
    (10, 'miss123');

/*Table structure for table `scri` */

DROP TABLE IF EXISTS `scri`;

CREATE TABLE `scri` (
    `scri` int(11) NOT NULL AUTO_INCREMENT,
    `ctitle` varchar(50) DEFAULT NULL,
    `cper` int(11) DEFAULT NULL,
    `category` varchar(20) DEFAULT NULL,
    `status` varchar(2) DEFAULT NULL,
    `minrate` varchar(4) DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    PRIMARY KEY (`scri`),
    KEY `scri_evid_d237dab2_fk_scorevents_evid` (`evid`),
    CONSTRAINT `scri_evid_d237dab2_fk_scorevents_evid` FOREIGN KEY (`evid`) REFERENCES `scorevents` (`evid`)
) ENGINE = InnoDB AUTO_INCREMENT = 11 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `scri` */

insert into
    `scri` (
        `scri`,
        `ctitle`,
        `cper`,
        `category`,
        `status`,
        `minrate`,
        `evid`
    )
values (
        6,
        'Debug1',
        25,
        '0',
        '1',
        '1',
        9
    ),
    (
        7,
        'Debug2',
        15,
        '0',
        '1',
        '1',
        9
    ),
    (
        8,
        'Debug3',
        15,
        '0',
        '1',
        '1',
        9
    ),
    (
        9,
        'Debug4',
        20,
        '0',
        '1',
        '1',
        9
    ),
    (
        10,
        'Debug5',
        30,
        '0',
        '1',
        '1',
        9
    );

/*Table structure for table `sinscore` */

DROP TABLE IF EXISTS `sinscore`;

CREATE TABLE `sinscore` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `inscore` varchar(6) DEFAULT NULL,
    `category` varchar(20) DEFAULT NULL,
    `subdon` varchar(2) DEFAULT NULL,
    `cristat` varchar(2) DEFAULT NULL,
    `rankscore` smallint (6) DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    `sconid` int(11) DEFAULT NULL,
    `scri` int(11) DEFAULT NULL,
    `ejid` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `sinscore_evid_7c25c83f_fk_scorevents_evid` (`evid`),
    KEY `sinscore_sconid_fdce9ebb_fk_scandidates_sconid` (`sconid`),
    KEY `sinscore_scri_5dc5ddcf_fk_scri_scri` (`scri`),
    KEY `sinscore_ejid_a9444b70_fk_sjudge_ejid` (`ejid`),
    CONSTRAINT `sinscore_ejid_a9444b70_fk_sjudge_ejid` FOREIGN KEY (`ejid`) REFERENCES `sjudge` (`ejid`),
    CONSTRAINT `sinscore_evid_7c25c83f_fk_scorevents_evid` FOREIGN KEY (`evid`) REFERENCES `scorevents` (`evid`),
    CONSTRAINT `sinscore_sconid_fdce9ebb_fk_scandidates_sconid` FOREIGN KEY (`sconid`) REFERENCES `scandidates` (`sconid`),
    CONSTRAINT `sinscore_scri_5dc5ddcf_fk_scri_scri` FOREIGN KEY (`scri`) REFERENCES `scri` (`scri`)
) ENGINE = InnoDB AUTO_INCREMENT = 67 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `sinscore` */

insert into
    `sinscore` (
        `id`,
        `inscore`,
        `category`,
        `subdon`,
        `cristat`,
        `rankscore`,
        `evid`,
        `sconid`,
        `scri`,
        `ejid`
    )
values (
        22,
        '13',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        6,
        11
    ),
    (
        23,
        '23',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        6,
        12
    ),
    (
        24,
        '21',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        6,
        12
    ),
    (
        25,
        '14',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        6,
        12
    ),
    (
        26,
        '17',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        6,
        13
    ),
    (
        27,
        '19',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        6,
        13
    ),
    (
        28,
        '24',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        6,
        13
    ),
    (
        29,
        '12',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        6,
        11
    ),
    (
        30,
        '18',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        6,
        11
    ),
    (
        31,
        '13',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        7,
        13
    ),
    (
        32,
        '9',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        7,
        13
    ),
    (
        33,
        '12',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        7,
        13
    ),
    (
        34,
        '13',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        7,
        12
    ),
    (
        35,
        '11',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        7,
        12
    ),
    (
        36,
        '10',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        7,
        12
    ),
    (
        37,
        '13',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        7,
        11
    ),
    (
        38,
        '15',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        7,
        11
    ),
    (
        39,
        '11',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        7,
        11
    ),
    (
        40,
        '9.7',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        8,
        12
    ),
    (
        41,
        '11.5',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        8,
        12
    ),
    (
        42,
        '9.1',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        8,
        12
    ),
    (
        43,
        '11',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        8,
        11
    ),
    (
        44,
        '10',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        8,
        11
    ),
    (
        45,
        '10.5',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        8,
        11
    ),
    (
        46,
        '14.5',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        8,
        13
    ),
    (
        47,
        '13.7',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        8,
        13
    ),
    (
        48,
        '11.2',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        8,
        13
    ),
    (
        49,
        '15.11',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        9,
        11
    ),
    (
        50,
        '11.2',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        9,
        11
    ),
    (
        51,
        '10.8',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        9,
        11
    ),
    (
        52,
        '14',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        9,
        12
    ),
    (
        53,
        '5',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        9,
        12
    ),
    (
        54,
        '8',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        9,
        12
    ),
    (
        55,
        '13',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        9,
        13
    ),
    (
        56,
        '7',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        9,
        13
    ),
    (
        57,
        '17',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        9,
        13
    ),
    (
        58,
        '26',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        10,
        11
    ),
    (
        59,
        '21',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        10,
        11
    ),
    (
        60,
        '27',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        10,
        11
    ),
    (
        61,
        '25.1',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        10,
        13
    ),
    (
        62,
        '22',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        10,
        13
    ),
    (
        63,
        '19',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        10,
        13
    ),
    (
        64,
        '27',
        NULL,
        'y',
        NULL,
        0,
        9,
        6,
        10,
        12
    ),
    (
        65,
        '28',
        NULL,
        'y',
        NULL,
        0,
        9,
        7,
        10,
        12
    ),
    (
        66,
        '26',
        NULL,
        'y',
        NULL,
        0,
        9,
        8,
        10,
        12
    );

/*Table structure for table `sjudge` */

DROP TABLE IF EXISTS `sjudge`;

CREATE TABLE `sjudge` (
    `ejid` int(11) NOT NULL AUTO_INCREMENT,
    `jname` varchar(100) DEFAULT NULL,
    `uname` varchar(30) DEFAULT NULL,
    `category` varchar(20) DEFAULT NULL,
    `spassword` longblob DEFAULT NULL,
    `evid` int(11) DEFAULT NULL,
    PRIMARY KEY (`ejid`),
    KEY `sjudge_evid_67a3b185_fk_scorevents_evid` (`evid`),
    CONSTRAINT `sjudge_evid_67a3b185_fk_scorevents_evid` FOREIGN KEY (`evid`) REFERENCES `scorevents` (`evid`)
) ENGINE = InnoDB AUTO_INCREMENT = 14 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*Data for the table `sjudge` */

insert into
    `sjudge` (
        `ejid`,
        `jname`,
        `uname`,
        `category`,
        `spassword`,
        `evid`
    )
values (
        10,
        'Admin Debug',
        'admindebug',
        NULL,
        '��������(�\rf�r',
        NULL
    ),
    (
        11,
        'Frederick Madayag',
        'fred',
        NULL,
        '77064f5bd13e417f564e7d880dc7a536',
        9
    ),
    (
        12,
        'Jenny Ordinaryo',
        'jenny',
        NULL,
        '067fccb09c1d91f4f0c5d6d21d5355d9',
        9
    ),
    (
        13,
        'Jasmine Rotugal',
        'jasmine',
        NULL,
        'e3586b257e1b0d9300d2432b55deb8c3',
        9
    );

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */
;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */
;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */
;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */
;