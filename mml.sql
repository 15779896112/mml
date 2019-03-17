-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: mml
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_comment`
--

DROP TABLE IF EXISTS `app_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` datetime(6) NOT NULL,
  `comment` longtext NOT NULL,
  `time` datetime(6) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_comment_goods_id_1c80d8d1_fk_mml_goods_id` (`goods_id`),
  KEY `app_comment_user_id_693f46cc_fk_mml_user_id` (`user_id`),
  CONSTRAINT `app_comment_goods_id_1c80d8d1_fk_mml_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `mml_goods` (`id`),
  CONSTRAINT `app_comment_user_id_693f46cc_fk_mml_user_id` FOREIGN KEY (`user_id`) REFERENCES `mml_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_comment`
--

LOCK TABLES `app_comment` WRITE;
/*!40000 ALTER TABLE `app_comment` DISABLE KEYS */;
INSERT INTO `app_comment` VALUES (1,'2019-03-17 03:21:49.792154','哈哈','2019-03-17 03:21:49.792263',1,3),(2,'2019-03-17 03:36:05.674221','宝贝收到了，棒棒的','2019-03-17 03:36:05.674717',12,3);
/*!40000 ALTER TABLE `app_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_order`
--

DROP TABLE IF EXISTS `app_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createtime` datetime(6) NOT NULL,
  `updatetime` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `identifier` varchar(256) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_order_user_id_f25a9fc4_fk_mml_user_id` (`user_id`),
  CONSTRAINT `app_order_user_id_f25a9fc4_fk_mml_user_id` FOREIGN KEY (`user_id`) REFERENCES `mml_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_order`
--

LOCK TABLES `app_order` WRITE;
/*!40000 ALTER TABLE `app_order` DISABLE KEYS */;
INSERT INTO `app_order` VALUES (1,'2019-03-16 12:05:32.937534','2019-03-16 12:05:32.937683',3,'15527379323611',3),(2,'2019-03-16 12:06:07.789920','2019-03-16 12:06:07.789965',3,'15527379677172',3),(3,'2019-03-16 12:09:38.192927','2019-03-16 12:09:38.192976',3,'15527381783110',3),(4,'2019-03-16 12:17:42.857644','2019-03-16 12:17:42.857693',3,'15527386626395',3),(5,'2019-03-16 12:26:25.445602','2019-03-16 12:26:25.445647',3,'15527391853621',3),(6,'2019-03-16 12:29:33.211898','2019-03-16 12:29:33.211945',3,'15527393731536',3),(7,'2019-03-16 12:30:36.311754','2019-03-16 12:30:36.311945',3,'15527394369826',3),(8,'2019-03-16 12:35:00.974806','2019-03-16 12:35:00.974851',0,'15527397002728',3),(9,'2019-03-16 12:43:48.105611','2019-03-16 12:43:48.105683',0,'15527402284360',3),(10,'2019-03-16 12:45:11.875599','2019-03-16 12:45:11.875652',3,'15527403112250',3),(11,'2019-03-16 12:46:17.632673','2019-03-16 12:46:17.632728',3,'15527403775647',3),(12,'2019-03-16 12:50:03.812304','2019-03-16 12:50:03.812352',2,'15527406032719',3),(13,'2019-03-16 12:54:40.976845','2019-03-16 12:54:40.976888',2,'15527408808407',3),(14,'2019-03-16 12:56:40.497431','2019-03-16 12:56:40.497624',3,'15527410001105',3),(15,'2019-03-16 12:59:57.560887','2019-03-16 12:59:57.561563',2,'15527411975071',3),(16,'2019-03-16 13:03:40.578846','2019-03-16 13:03:40.578890',3,'15527414201955',3),(17,'2019-03-16 13:05:22.940915','2019-03-16 13:05:22.940966',1,'15527415225318',3),(18,'2019-03-16 13:12:46.706610','2019-03-16 13:12:46.706783',2,'15527419669422',3),(19,'2019-03-16 13:29:55.281762','2019-03-16 13:29:55.281809',3,'15527429955639',3),(20,'2019-03-17 00:23:33.551490','2019-03-17 00:23:33.551585',2,'15527822137018',3),(21,'2019-03-17 00:54:24.990971','2019-03-17 00:54:24.991032',1,'15527840643835',3),(22,'2019-03-17 03:34:43.172833','2019-03-17 03:34:43.172898',3,'15527936831514',3),(23,'2019-03-17 03:54:33.682072','2019-03-17 03:54:33.682151',0,'15527948738011',7);
/*!40000 ALTER TABLE `app_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_ordergoods`
--

DROP TABLE IF EXISTS `app_ordergoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_ordergoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_ordergoods_goods_id_b3c19f94_fk_mml_goods_id` (`goods_id`),
  KEY `app_ordergoods_order_id_ef926487_fk_app_order_id` (`order_id`),
  CONSTRAINT `app_ordergoods_goods_id_b3c19f94_fk_mml_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `mml_goods` (`id`),
  CONSTRAINT `app_ordergoods_order_id_ef926487_fk_app_order_id` FOREIGN KEY (`order_id`) REFERENCES `app_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_ordergoods`
--

LOCK TABLES `app_ordergoods` WRITE;
/*!40000 ALTER TABLE `app_ordergoods` DISABLE KEYS */;
INSERT INTO `app_ordergoods` VALUES (7,3,1,7,14697),(8,1,12,8,129),(9,3,12,9,387),(10,1,2,9,2889),(11,1,3,9,5999),(12,2,3,10,11998),(13,1,2,10,2889),(14,1,2,11,2889),(15,1,2,12,2889),(16,1,12,12,129),(17,2,1,13,9798),(18,1,4,13,4899),(19,3,12,13,387),(20,1,11,13,2099),(21,2,11,14,4198),(22,1,2,14,2889),(23,2,2,15,5778),(24,2,3,15,11998),(25,1,1,16,4899),(26,1,12,16,129),(27,2,12,17,258),(28,1,11,17,2099),(29,1,1,18,4899),(30,1,2,19,2889),(31,1,1,20,4899),(32,1,1,20,4899),(33,3,3,20,17997),(34,1,2,20,2889),(35,1,1,21,4899),(36,1,6,21,3799),(37,1,12,22,129),(38,1,12,23,129);
/*!40000 ALTER TABLE `app_ordergoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add wheel',7,'add_wheel'),(20,'Can change wheel',7,'change_wheel'),(21,'Can delete wheel',7,'delete_wheel'),(22,'Can add classify',8,'add_classify'),(23,'Can change classify',8,'change_classify'),(24,'Can delete classify',8,'delete_classify'),(25,'Can add goods',9,'add_goods'),(26,'Can change goods',9,'change_goods'),(27,'Can delete goods',9,'delete_goods'),(28,'Can add user',10,'add_user'),(29,'Can change user',10,'change_user'),(30,'Can delete user',10,'delete_user'),(31,'Can add cart',11,'add_cart'),(32,'Can change cart',11,'change_cart'),(33,'Can delete cart',11,'delete_cart'),(34,'Can add order',12,'add_order'),(35,'Can change order',12,'change_order'),(36,'Can delete order',12,'delete_order'),(37,'Can add order goods',13,'add_ordergoods'),(38,'Can change order goods',13,'change_ordergoods'),(39,'Can delete order goods',13,'delete_ordergoods'),(40,'Can add comment',14,'add_comment'),(41,'Can change comment',14,'change_comment'),(42,'Can delete comment',14,'delete_comment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(11,'app','cart'),(8,'app','classify'),(14,'app','comment'),(9,'app','goods'),(12,'app','order'),(13,'app','ordergoods'),(10,'app','user'),(7,'app','wheel'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-14 10:08:14.681237'),(2,'auth','0001_initial','2019-03-14 10:08:15.681513'),(3,'admin','0001_initial','2019-03-14 10:08:15.860311'),(4,'admin','0002_logentry_remove_auto_add','2019-03-14 10:08:15.958577'),(5,'app','0001_initial','2019-03-14 10:08:16.058078'),(6,'contenttypes','0002_remove_content_type_name','2019-03-14 10:08:16.182363'),(7,'auth','0002_alter_permission_name_max_length','2019-03-14 10:08:16.229549'),(8,'auth','0003_alter_user_email_max_length','2019-03-14 10:08:16.333291'),(9,'auth','0004_alter_user_username_opts','2019-03-14 10:08:16.351297'),(10,'auth','0005_alter_user_last_login_null','2019-03-14 10:08:16.422981'),(11,'auth','0006_require_contenttypes_0002','2019-03-14 10:08:16.427866'),(12,'auth','0007_alter_validators_add_error_messages','2019-03-14 10:08:16.441379'),(13,'auth','0008_alter_user_username_max_length','2019-03-14 10:08:16.512660'),(14,'sessions','0001_initial','2019-03-14 10:08:16.555113'),(15,'app','0002_classify','2019-03-15 01:56:46.446078'),(16,'app','0003_goods','2019-03-15 06:34:19.402979'),(17,'app','0004_goods_fatherid','2019-03-15 06:38:14.742830'),(18,'app','0005_user','2019-03-15 12:02:36.995149'),(19,'app','0006_auto_20190315_1213','2019-03-15 12:13:27.539171'),(20,'app','0007_auto_20190315_1240','2019-03-15 12:40:54.577431'),(21,'app','0008_auto_20190316_0452','2019-03-16 04:52:35.164279'),(22,'app','0009_cart_total','2019-03-16 06:57:13.542734'),(23,'app','0010_auto_20190316_0703','2019-03-16 07:03:58.206189'),(24,'app','0011_order_ordergoods','2019-03-16 11:55:52.947356'),(25,'app','0012_ordergoods_total','2019-03-16 12:23:42.734849'),(26,'app','0013_comment','2019-03-17 03:17:46.252695');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2ro8gd7r8nsy4dgzcc3v7mlln4niga9n','MGI0Nzg5ZWViYzljNDUxMDg3Njg0YzBhZjAzODFmYWI3YTRiMjlhYTp7InRva2VuIjoiZThjZjE5MTFiZWM4NWNhY2Q4MWIxZmNiZWJkNDVkOGIifQ==','2019-03-31 03:53:58.450762'),('pl1hktd9racf0d1o0psu1vnnz1qqgixq','YmMwNjc3OWZkNjFlODU1ODA0YWNkNzUxM2E2YWUwNTY5YzAwNzJjZjp7InRva2VuIjoiZDhkNzQ1YzQ3NjMyOTE5YzM1ZjM4YTA2YWQyMzAxMzAifQ==','2019-03-31 03:50:39.252777');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mml_cart`
--

DROP TABLE IF EXISTS `mml_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mml_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `isselect` tinyint(1) NOT NULL,
  `isdelete` tinyint(1) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mml_cart_goods_id_a878acc0_fk_mml_goods_id` (`goods_id`),
  KEY `mml_cart_user_id_565614aa_fk_mml_user_id` (`user_id`),
  CONSTRAINT `mml_cart_goods_id_a878acc0_fk_mml_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `mml_goods` (`id`),
  CONSTRAINT `mml_cart_user_id_565614aa_fk_mml_user_id` FOREIGN KEY (`user_id`) REFERENCES `mml_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mml_cart`
--

LOCK TABLES `mml_cart` WRITE;
/*!40000 ALTER TABLE `mml_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `mml_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mml_goods`
--

DROP TABLE IF EXISTS `mml_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mml_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lrp` varchar(20) NOT NULL,
  `price` varchar(20) NOT NULL,
  `img` varchar(100) NOT NULL,
  `bigimg` varchar(100) NOT NULL,
  `title` varchar(255) NOT NULL,
  `intro` varchar(255) NOT NULL,
  `fatherid` varchar(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mml_goods`
--

LOCK TABLES `mml_goods` WRITE;
/*!40000 ALTER TABLE `mml_goods` DISABLE KEYS */;
INSERT INTO `mml_goods` VALUES (1,'¥5299.00','¥4899.00','img/04540869910713027_sm.jpg','img/1_05248483506833146_360.jpg','惠普（HP）24-g038cn 23.8英寸一体机电脑（i3-6100U 8G DDR4 7200转1T GT920A 2G独显 IPS FHD Win10）白色','','00000','惠普电脑'),(2,'¥3200.00','¥2889.00','img/04540859619208219_sm.gif','img/1_05248474005377295_360.jpg','联想（Lenovo）扬天S4105-00 21.5英寸商务一体机电脑 黑色/E1-7010/2G/500G/集显','','00000','联想s4105'),(3,'¥6200.00','¥5999.00','img/web-601-197-1-1.jpg','img/1_05248464323660863_360.jpg','联想（Lenovo）扬天T4900c 台式电脑 (I7-4790 8G 1T 2GB DVDRW WIN7)20英寸','','00000','联想4900'),(4,'¥5299.00','¥4899.00','img/04540869910713027_sm.jpg','img/1_05248483506833146_360.jpg','惠普（HP）24-g038cn 23.8英寸一体机电脑（i3-6100U 8G DDR4 7200转1T GT920A 2G独显 IPS FHD Win10）白色','','00000','惠普24-g038cn'),(5,'¥7500.00','¥6999.00','img/04540870544944460_sm.jpg','img/1_05248502805011216_360.jpg','戴尔(DELL)Ins14PR-4748B 14英寸高清游戏笔记本电脑(i7-4720HQ 8G 1T GTX 950M 4G独显?DVD Win10)黑','','00001','戴尔Ins14PR-4748B'),(6,'¥4399.00','¥3799.00','img/web-603-210-1-6.jpg','img/1_05017007060390084_360.jpg','【电脑节】12月10日 华硕 AS F554L 5200U/5AG5/4G/US笔记本（i5-5200U 4G内存 500G硬盘 AMD Radeon R5 M320 2G显存）黑色','欢乐12月 疯狂电脑节','00001','华硕 AS F554L'),(7,'¥7500.00','¥6999.00','img/04540870544944460_sm.jpg','img/1_05248502805011216_360.jpg','戴尔(DELL)Ins14PR-4748B 14英寸高清游戏笔记本电脑(i7-4720HQ 8G 1T GTX 950M 4G独显?DVD Win10)黑','','00001','戴尔(DELL)Ins14PR'),(8,'¥9000.00','¥7988.00','img/web-601-197-1-2.png','img/1_05267320084587504_360.jpg','预定苹果Apple iPhone 7Plus 银色 256G','','00100','iPhone 7Plus'),(9,'¥9000.00','¥7988.00','img/web-601-197-1-2.png','img/1_05267320084587504_360.jpg','预定苹果Apple iPhone 8Plus 银色 256G','','00100','iPhone 8Plus'),(10,'¥9000.00','¥7988.00','img/web-601-197-1-2.png','img/1_05267320084587504_360.jpg','预定苹果Apple iPhone 6Plus 银色 256G','','00100','iPhone 6Plus'),(11,'¥3599.00','¥2099.00','img/web-603-210-1-5.jpg','img/180_05005781594356422_360.jpeg','小米（MI）小米Note (16G ROM)版 双卡双待 白色 白色 标准版','','00101','小米Note'),(12,'¥154.79','¥129.00','img/05192199780569025_sm.png','img/1_04584019370211928_360.png','诺基亚（NOKIA）1050 GSM手机 直板功能手机 第二备用手机（红色）','第二备用手机，超长待机，经久耐用，特价特价！！！','00101','NOKIA');
/*!40000 ALTER TABLE `mml_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mml_types`
--

DROP TABLE IF EXISTS `mml_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mml_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` varchar(10) NOT NULL,
  `typename` varchar(100) NOT NULL,
  `childtypenames` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mml_types`
--

LOCK TABLES `mml_types` WRITE;
/*!40000 ALTER TABLE `mml_types` DISABLE KEYS */;
INSERT INTO `mml_types` VALUES (1,'000','电脑','全部分类:0#台式:00000#笔记本:00001'),(2,'001','手机','全部分类:0#苹果:00100#其他:00101'),(3,'002','生活','全部分类:0#母婴:00200#零食:00201#办公:00202#生活用品:00203');
/*!40000 ALTER TABLE `mml_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mml_user`
--

DROP TABLE IF EXISTS `mml_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mml_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `freindword` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mml_user_username_3102a44a_uniq` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mml_user`
--

LOCK TABLES `mml_user` WRITE;
/*!40000 ALTER TABLE `mml_user` DISABLE KEYS */;
INSERT INTO `mml_user` VALUES (1,'15779896112','e10adc3949ba59abbe56e057f20f883e',''),(2,'www','e10adc3949ba59abbe56e057f20f883e',''),(3,'wzh','fb44d1e84d3b35fa844945b29a496bc0',''),(4,'w','e10adc3949ba59abbe56e057f20f883e',''),(5,'wan','202cb962ac59075b964b07152d234b70',''),(6,'AAAA','202cb962ac59075b964b07152d234b70',''),(7,'晓峰残月','202cb962ac59075b964b07152d234b70','');
/*!40000 ALTER TABLE `mml_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mml_wheel`
--

DROP TABLE IF EXISTS `mml_wheel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mml_wheel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bg` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mml_wheel`
--

LOCK TABLES `mml_wheel` WRITE;
/*!40000 ALTER TABLE `mml_wheel` DISABLE KEYS */;
INSERT INTO `mml_wheel` VALUES (1,'rgb(60, 1, 253)','img/web-101-101-1.png','手机特卖199'),(2,'rgb(236, 215, 170)','img/web-101-101-5.jpg','为揽阅M2 803L'),(5,'rgb(237, 235, 246)','img/web-101-101-2.jpg','iPhone SE');
/*!40000 ALTER TABLE `mml_wheel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-16 21:08:17
