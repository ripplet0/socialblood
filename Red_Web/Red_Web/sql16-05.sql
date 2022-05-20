/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - red_app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`red_app` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `red_app`;

/*Table structure for table `blood_bank` */

DROP TABLE IF EXISTS `blood_bank`;

CREATE TABLE `blood_bank` (
  `bank_id` int(11) DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  `place` varchar(250) DEFAULT NULL,
  `pin` varchar(250) DEFAULT NULL,
  `Phone` varchar(250) DEFAULT NULL,
  `email` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `blood_bank` */

insert  into `blood_bank`(`bank_id`,`name`,`place`,`pin`,`Phone`,`email`) values (20,'tony','payyavoor','4546435','9876543210','anandke369@gmail.com'),(NULL,'ee','ee','ee','ee','ee');

/*Table structure for table `camp` */

DROP TABLE IF EXISTS `camp`;

CREATE TABLE `camp` (
  `camp_id` int(11) NOT NULL AUTO_INCREMENT,
  `blood_bank_id` int(11) DEFAULT NULL,
  `details` varchar(200) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`camp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `camp` */

/*Table structure for table `donor` */

DROP TABLE IF EXISTS `donor`;

CREATE TABLE `donor` (
  `donor_id` int(11) DEFAULT NULL,
  `donor_name` varchar(100) DEFAULT NULL,
  `blood_group` varchar(100) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `donor` */

insert  into `donor`(`donor_id`,`donor_name`,`blood_group`,`phone`,`place`,`post`,`pin`,`district`,`state`,`email`) values (2,'rahul','b+',0,'gduasgdua',NULL,NULL,NULL,NULL,'abc@gmail.com'),(4,'eewrw',NULL,543545,'ret',NULL,NULL,NULL,NULL,'dasd@mail'),(6,'Athira','B+',2147483647,'kannur','kannur',670592,'Kannur','kerala','rob@gmail.com');

/*Table structure for table `donor_request` */

DROP TABLE IF EXISTS `donor_request`;

CREATE TABLE `donor_request` (
  `donor_request_id` int(11) DEFAULT NULL,
  `donor_id` int(11) DEFAULT NULL,
  `donor_request_details` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `donor_request` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedbacks` varchar(200) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `feedback_date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedbacks`,`user_id`,`feedback_date`) values (2,'Wow this  is awsome',1,'0002-02-22'),(3,'hi this is very nice',6,'2022-04-05'),(5,'dd',36,'2022-04-05'),(6,'e',36,'2022-04-05'),(7,'e',36,'2022-04-05'),(8,'e',36,'2022-04-05'),(9,'hai',36,'2022-04-05'),(10,'juijj ',4,'2022-04-05'),(11,'uugk',2,'2022-04-05'),(12,'Hi,\r\n Buddys how are you?\r\n....',2,'2022-04-11'),(13,'<h3>hai</h3>\r\n<script>alert(\"hacked\")</script>',1,'2022-04-14'),(14,'so good',1,'2022-05-01'),(15,'mmm',3,'2022-05-17');

/*Table structure for table `forgot` */

DROP TABLE IF EXISTS `forgot`;

CREATE TABLE `forgot` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `ur_id` int(11) DEFAULT NULL,
  `br_id` int(11) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `forgot` */

insert  into `forgot`(`f_id`,`ur_id`,`br_id`,`email`) values (1,3,20,'t@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_Id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_Id`,`username`,`password`,`usertype`) values (1,'rob@gmail.com','123456','user'),(2,'f','f','bank'),(3,'admin','123456','user'),(4,'t@gmail.com','apple123','pending'),(6,'hf','098','user'),(20,'b','b','bank');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `blood_bank_id` int(11) DEFAULT NULL,
  `blood_group` varchar(100) DEFAULT NULL,
  `unit` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`stock_id`,`blood_bank_id`,`blood_group`,`unit`) values (1,23,'A+','67'),(2,23,'B+','12'),(3,6,'A+','3'),(4,7,'A+','11'),(5,7,'AB+','52'),(6,24,'A+','50'),(7,24,'B+','2'),(8,35,'B+','d'),(9,35,'A+','109'),(10,56,'A+','2'),(11,56,'B+','2'),(12,10,'A+','20'),(13,3,'B+','60'),(14,20,'A+','24');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `blood_group` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`username`,`gender`,`phone`,`place`,`post`,`pin`,`state`,`district`,`email`,`blood_group`) values (6,'Athira','male','9198976445','kannur','kannur',670592,'kerala','kannur','rob@gmail.com','B+'),(1,'qq',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `user_request` */

DROP TABLE IF EXISTS `user_request`;

CREATE TABLE `user_request` (
  `user_request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `blood_bank_id` int(11) DEFAULT NULL,
  `unit` int(11) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `rblood_group` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user_request` */

insert  into `user_request`(`user_request_id`,`user_id`,`date`,`blood_bank_id`,`unit`,`status`,`rblood_group`) values (1,2,'2022-04-11',3,2,'accepted','AB-'),(2,2,'2022-04-11',3,3,'rejected','B-'),(3,1,'2022-04-13',20,0,'user','A+'),(5,1,'2022-04-29',5,555,'pending','555-555-0199@example.com'),(6,1,'2022-04-29',0,555,'pending','555-555-0199@example.com'),(7,3,'2022-05-17',20,5,'pending','AB+');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
