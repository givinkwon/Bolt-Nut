-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: boltnut
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_category` varchar(45) NOT NULL,
  `project_title` varchar(45) NOT NULL,
  `project_period` varchar(45) NOT NULL,
  `project_budget` varchar(45) NOT NULL,
  `project_state` int(11) NOT NULL,
  `project_content` varchar(2000) NOT NULL,
  `project_finish` varchar(45) NOT NULL,
  `project_meeting` varchar(45) NOT NULL,
  `project_location` varchar(45) NOT NULL,
  `project_location_detail` varchar(45) NOT NULL,
  `project_start` varchar(45) NOT NULL,
  `project_experience` varchar(45) NOT NULL,
  `project_goverment` varchar(45) NOT NULL,
  `file` varchar(300) NOT NULL,
  `permit` int(11) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (91,'기구설계','412412','4124124','12421412412421',0,'421421412421','412421412','오프라인 미팅','서울','421412412','4124214124','예','예','rlqls505Get_in_the_Car_and_Go.mp3',0),(92,'기구설계','41241243','12321312','3123213214',0,'3214124214','12412','오프라인 미팅','서울','5325235235','23523523','예','예','rlqls505Get_in_the_Car_and_Go.mp3',0),(93,'기구설계','권기빈극혐','20일','100원',0,'너무','2018/11/20','오프라인 미팅','서울','안암로','2018/11/25','예','예','rlqls505[월간 진행 보고서] 일진창업지원센터 업무 현황 및 향후 추진 계획_아이오펫.docx',0),(94,'기구설계','eqwewq','ewqewqeqwewqewqe','qweqweqwe',0,'wqeqweqwe','wqeqweqw','오프라인 미팅','서울','ewqeqw','eqwewqeqw','예','예','rlqls505activity_login.xml',0),(95,'기구설계','1321321','321321321321','4213123',0,'21321312321421421322222222222222222222222222222222222222222222222222222222222222222222222222222222','3213213123','오프라인 미팅','서울','21321321','3213213213','예','예','rlqls5054.txt',0),(96,'기구설계','321321','2018-11-09','3232',0,'3213123','2018-11-22','오프라인 미팅','서울','32131232','2018-11-08','예','예','rlqls505libegl.dll',0),(97,'기구설계','흡입식 반려동물 배변 청소기','30일','700만원',1,'＜프로젝트 진행 방식＞\r\n\r\n아이디어만 있기 때문에 기구설계 부터 양산까지 올인원으로 진행 되었으면 좋겠습니다.\r\n기구설계,회로설계 과정을 의뢰합니다.\r\n중간중간 미팅과 카톡으로 진행하려 합니다.                                         \r\n                                                                                    ＜프로젝트의 현재 상황＞\r\n\r\n지금은 디자인은 나왔지만 기구설계는 안되어있기 때문에 외관 디자인만 있다고 보시면 될 것 같습니다.\r\n                                          \r\n                                                                                    ＜상세한 업무 내용＞\r\n \r\n 1. 소모품                                         \r\n배변 청소이다 보니 제품의 소모품이 있고 그 소모품은 종이로 진행할 예정입니다. 아무래도 종이라 유체흐름이 빠져나갈 수 있어 이과정에서 해결이 가능하도록 개발이 진행되어야 할 것 같습니다.\r\n 2. 전지\r\n전지는 리튬이온전지 3.6V 5개입니다.\r\n 3. 회로\r\n배변의 무게를 들어 올릴 수 있을 정도의 흡입력을 토대로 개발해 주시면 될 것 같고, 재생될 때 LED빛이 나와 on상태를 알려주었으면 합니다.\r\n 4. 외관\r\n디자인을 해치지 않는 범위 내에서 진행해 주세요.\r\n \r\n                                                                                    ＜참고자료 / 유의사항＞\r\n','2018-11-30','오프라인 미팅','서울','강일동','2018-12-10','무','유','rlqls505chrome.exe.sig',1),(98,'기구설계','2','2','2',0,'＜프로젝트 진행 방식＞\r\n                                          \r\n                                                                                    ＜프로젝트의 현재 상황＞\r\n                                          \r\n                                                                                    ＜상세한 업무 내용＞\r\n                                          \r\n                                                                                    ＜참고자료 / 유의사항＞','222222-02-22','오프라인 미팅','서울','강일동','222222-02-22','유','유','rlqls505chrome_100_percent.pak',0);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_class` varchar(45) NOT NULL,
  `user_email` varchar(45) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `user_password` varchar(45) NOT NULL,
  `user_phone` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'0','rlqls505','rlqls505','ajumsee12#','01041126637'),(2,'1','rlqls505@naver.com','rlqls5051','ajumsee12#','01041126637'),(4,'1','xyz4966@naver.com','xyz4966','Chlwlsdud6!!','01048542760'),(5,'0','rlqls505@naver.com','312321','312312312','312312321');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-24 13:26:51
