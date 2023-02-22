-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart_item`
--

DROP TABLE IF EXISTS `cart_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_item` (
  `cart_item_id` varchar(100) NOT NULL,
  `quantity` int NOT NULL,
  `shopping_cart_id` varchar(100) NOT NULL,
  `product_id` varchar(100) NOT NULL,
  PRIMARY KEY (`cart_item_id`),
  KEY `shopping_cart_id` (`shopping_cart_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `cart_item_ibfk_1` FOREIGN KEY (`shopping_cart_id`) REFERENCES `shopping_cart` (`shopping_cart_id`),
  CONSTRAINT `cart_item_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_item`
--

LOCK TABLES `cart_item` WRITE;
/*!40000 ALTER TABLE `cart_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `postal_code` varchar(50) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('058d223b-df63-4ac0-a044-b355f75d7f77','Aleksandar','Petrovic','065978887','Kralja Petra 8','Smederevo','Srbija','11300','e4784914-3f9e-4bcb-b21e-01838c84b16e'),('17a859fa-45fd-4353-8109-cf58551eb7a1','Janko','Petrovic','0659878887','Kralja Petra 6','Smederevo','Srbija','11300','2b8fe473-8573-4f57-92e4-b731263dcd26'),('c8cef8b6-f5d1-4621-b19f-07a36748040d','Milica','Pekic','06245548','Karadjordjeva 6','Kragujevac','Srbija','11000','07990f40-d089-47e8-bc83-fd8e8231ba3f');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `job_title` varchar(100) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `office_id` varchar(100) NOT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `office_id` (`office_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`office_id`) REFERENCES `office` (`office_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('3e01de3f-7ae1-4be0-9484-81307b43d212','David','Pantic','0631033362','Sef','f815a998-1a24-4ea3-a63e-00a3ffc282a7','4d1049f8-6442-4268-a4cd-f5f7279a2d0c');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `office`
--

DROP TABLE IF EXISTS `office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `office` (
  `office_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `postal_code` varchar(50) NOT NULL,
  `territory` varchar(50) NOT NULL,
  PRIMARY KEY (`office_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `office`
--

LOCK TABLES `office` WRITE;
/*!40000 ALTER TABLE `office` DISABLE KEYS */;
INSERT INTO `office` VALUES ('4d1049f8-6442-4268-a4cd-f5f7279a2d0c','Pantic Auto','0631033362','16 Oktobra','Smederevo','Srbija','11300','Podunavski okrug');
/*!40000 ALTER TABLE `office` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producer`
--

DROP TABLE IF EXISTS `producer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producer` (
  `producer_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`producer_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producer`
--

LOCK TABLES `producer` WRITE;
/*!40000 ALTER TABLE `producer` DISABLE KEYS */;
INSERT INTO `producer` VALUES ('6bfa5c04-1111-444f-82fd-db9f7bda0409','Taurus','Nemacka','Najbolji proizvodi za...'),('6dd186b5-0f79-4102-9680-acf38bd45796','Castrol','Nemacka','Najbolja ulja i ostali proizvodi za...'),('be46c42c-7774-448b-863b-511fdfe6199d','BOSCH','Nemacka','Najbolji proizvodi za sve vrste automobila...'),('e54f4d4e-4122-45c8-b55e-e19790b6b865','MOMO','Nemacka','Najbolji proizvodi za sve vrste automobila, gume, felne...');
/*!40000 ALTER TABLE `producer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `code` varchar(50) NOT NULL,
  `price` float NOT NULL,
  `for_car_brand` varchar(100) DEFAULT NULL,
  `quantity_in_stock` int NOT NULL,
  `producer_id` varchar(100) NOT NULL,
  `product_category_id` varchar(100) NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `code` (`code`),
  KEY `producer_id` (`producer_id`),
  KEY `product_category_id` (`product_category_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`producer_id`) REFERENCES `producer` (`producer_id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`product_category_id`) REFERENCES `product_category` (`product_category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('20ff0e12-6ab4-4fe6-a799-d1d760781549','Akumulator','Akumulator za...','Sk9',12900,'skoda',100,'be46c42c-7774-448b-863b-511fdfe6199d','52429d53-49f1-40a9-a6a8-39d5b582601c'),('28641b2e-43c0-47e6-ab3a-8a400f42978a','Akumulator','Akumulator za...','SEAA659',12600,'seat ibiza',129,'be46c42c-7774-448b-863b-511fdfe6199d','52429d53-49f1-40a9-a6a8-39d5b582601c'),('2a815353-8704-4ceb-9d0e-3158aaea35ae','Far','Far za...','SS449',5000,'seat',60,'6bfa5c04-1111-444f-82fd-db9f7bda0409','d1d9db87-7c00-47e1-ad8e-cb337f925e8c'),('32fa06a5-223b-4970-8ef7-1be35288a684','Zimske gume','Gume za...','S666',16000,'skoda',30,'6bfa5c04-1111-444f-82fd-db9f7bda0409','3ee5bd4f-c344-42e6-b8ae-dc9b512dfab4'),('3314b4ca-c810-46df-a71f-bc49b65348b2','Akumulator','Akumulator za seat..','ASTU',12000,'seat',130,'6dd186b5-0f79-4102-9680-acf38bd45796','52429d53-49f1-40a9-a6a8-39d5b582601c'),('3dbd3d2b-0ba6-44e8-908b-200245f297f2','Zimske gume','Gume za...','SE666',16300,'seat',30,'6bfa5c04-1111-444f-82fd-db9f7bda0409','3ee5bd4f-c344-42e6-b8ae-dc9b512dfab4'),('45e2b827-edc0-4306-b9ed-d2cd4ad62902','Far','Far za...','AA449',5500,'audi',60,'6bfa5c04-1111-444f-82fd-db9f7bda0409','d1d9db87-7c00-47e1-ad8e-cb337f925e8c'),('565d5491-5443-43fb-9c90-2be8bc71d26a','Kocioni diskovi','Kocioni sistem za...','AAK101',20300,'audi a4',60,'e54f4d4e-4122-45c8-b55e-e19790b6b865','49b8a1b2-6f3a-41e7-a13b-9f95669206fb'),('56f4d1d9-effd-4cde-8f12-0b020454c4ab','Kociona sajla','Kocioni sistem za...','SETSK101',13000,'seat',60,'e54f4d4e-4122-45c8-b55e-e19790b6b865','49b8a1b2-6f3a-41e7-a13b-9f95669206fb'),('5918c007-71c8-45c3-a8d3-3e17a9424201','Far','Far za...','Sk449',5900,'skoda',100,'be46c42c-7774-448b-863b-511fdfe6199d','d1d9db87-7c00-47e1-ad8e-cb337f925e8c'),('5f166d7c-4ab7-4836-a3d8-2dfb24e1bb1a','Kocioni diskovi','Kocioni sistem za...','SK101',18300,'seat ibiza',60,'e54f4d4e-4122-45c8-b55e-e19790b6b865','49b8a1b2-6f3a-41e7-a13b-9f95669206fb'),('6cc3e546-7e24-4002-8cd4-6387ca394d3b','Motorno ulje','Motorno ulje za...','AMU526',1250,'audi',98,'6dd186b5-0f79-4102-9680-acf38bd45796','777fa6ed-d95a-4212-bdce-3b4fb4e1b84c'),('96b94911-a46c-4d70-933c-29d8450e0a93','Motorno ulje','Motorno ulje za...','SEMU26',1500,'seat',128,'6dd186b5-0f79-4102-9680-acf38bd45796','777fa6ed-d95a-4212-bdce-3b4fb4e1b84c'),('a6e3eae3-ee66-45b3-981d-1dabb9ead2eb','Akumulator','Akumulator za...','AAU3TU',14000,'audi a4',130,'be46c42c-7774-448b-863b-511fdfe6199d','52429d53-49f1-40a9-a6a8-39d5b582601c'),('aee7d621-ab93-4929-ba79-aecd05146e96','Kociona sajla','Kocioni sistem za...','ASK101',20300,'audi a4',60,'e54f4d4e-4122-45c8-b55e-e19790b6b865','49b8a1b2-6f3a-41e7-a13b-9f95669206fb'),('bde742cb-39ee-43a9-a852-523888ff452e','Zimske gume','Gume za...','AA5666',16300,'audi a1',59,'e54f4d4e-4122-45c8-b55e-e19790b6b865','3ee5bd4f-c344-42e6-b8ae-dc9b512dfab4'),('d657a62d-747e-47c8-b777-d4048d29bf7a','Motorno ulje','Motorno ulje za...','SMU526',1350,'skoda',107,'6dd186b5-0f79-4102-9680-acf38bd45796','777fa6ed-d95a-4212-bdce-3b4fb4e1b84c'),('d99192aa-4445-4b19-8f67-36227e62cffc','Zimske gume','Gume za...','A666',15000,'audi',30,'6bfa5c04-1111-444f-82fd-db9f7bda0409','3ee5bd4f-c344-42e6-b8ae-dc9b512dfab4'),('e884a4aa-184c-412b-995b-8fa106e758db','Zimske gume','Gume za...','SET5666',16300,'seat ibiza',60,'e54f4d4e-4122-45c8-b55e-e19790b6b865','3ee5bd4f-c344-42e6-b8ae-dc9b512dfab4');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_category`
--

DROP TABLE IF EXISTS `product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_category` (
  `product_category_id` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`product_category_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_category`
--

LOCK TABLES `product_category` WRITE;
/*!40000 ALTER TABLE `product_category` DISABLE KEYS */;
INSERT INTO `product_category` VALUES ('52429d53-49f1-40a9-a6a8-39d5b582601c','Akumulatori'),('d1d9db87-7c00-47e1-ad8e-cb337f925e8c','Farovi'),('3ee5bd4f-c344-42e6-b8ae-dc9b512dfab4','Gume'),('49b8a1b2-6f3a-41e7-a13b-9f95669206fb','Kocioni sistemi'),('777fa6ed-d95a-4212-bdce-3b4fb4e1b84c','Ulja');
/*!40000 ALTER TABLE `product_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_cart`
--

DROP TABLE IF EXISTS `shopping_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_cart` (
  `shopping_cart_id` varchar(100) NOT NULL,
  `total_cost` float DEFAULT NULL,
  `customer_id` varchar(100) NOT NULL,
  PRIMARY KEY (`shopping_cart_id`),
  UNIQUE KEY `customer_id` (`customer_id`),
  CONSTRAINT `shopping_cart_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_cart`
--

LOCK TABLES `shopping_cart` WRITE;
/*!40000 ALTER TABLE `shopping_cart` DISABLE KEYS */;
INSERT INTO `shopping_cart` VALUES ('289b402e-e684-41e7-b174-b32defbbaf04',0,'c8cef8b6-f5d1-4621-b19f-07a36748040d'),('4124c74e-c6c2-4e42-af67-d6ac8376f9dc',0,'17a859fa-45fd-4353-8109-cf58551eb7a1'),('c28ab3f3-1a28-4cfe-8aa9-22d86ecd9748',0,'058d223b-df63-4ac0-a044-b355f75d7f77');
/*!40000 ALTER TABLE `shopping_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_order`
--

DROP TABLE IF EXISTS `shopping_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_order` (
  `shopping_order_id` varchar(100) NOT NULL,
  `total_price` float NOT NULL,
  `shipping_cost` float NOT NULL,
  `status` int NOT NULL,
  `order_date` date NOT NULL,
  `shipped_date` date DEFAULT NULL,
  `customer_id` varchar(100) NOT NULL,
  `office_id` varchar(100) NOT NULL,
  PRIMARY KEY (`shopping_order_id`),
  KEY `customer_id` (`customer_id`),
  KEY `office_id` (`office_id`),
  CONSTRAINT `shopping_order_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `shopping_order_ibfk_2` FOREIGN KEY (`office_id`) REFERENCES `office` (`office_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_order`
--

LOCK TABLES `shopping_order` WRITE;
/*!40000 ALTER TABLE `shopping_order` DISABLE KEYS */;
INSERT INTO `shopping_order` VALUES ('012e07f0-075f-4aef-8ff3-af2d4ce9425c',14500,400,0,'2023-02-22',NULL,'c8cef8b6-f5d1-4621-b19f-07a36748040d','4d1049f8-6442-4268-a4cd-f5f7279a2d0c'),('2dd93e03-54ff-426a-98f6-5fbfcd4b9f53',19450,400,0,'2023-02-22',NULL,'17a859fa-45fd-4353-8109-cf58551eb7a1','4d1049f8-6442-4268-a4cd-f5f7279a2d0c'),('939fa448-cb3f-41e7-9f59-b14b2ce82439',1650,400,0,'2023-02-22',NULL,'058d223b-df63-4ac0-a044-b355f75d7f77','4d1049f8-6442-4268-a4cd-f5f7279a2d0c'),('a737f332-cada-4c9c-b940-5529924ee4f5',4450,400,0,'2023-02-22',NULL,'058d223b-df63-4ac0-a044-b355f75d7f77','4d1049f8-6442-4268-a4cd-f5f7279a2d0c');
/*!40000 ALTER TABLE `shopping_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_order_item`
--

DROP TABLE IF EXISTS `shopping_order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_order_item` (
  `shopping_order_item_id` varchar(100) NOT NULL,
  `quantity` int NOT NULL,
  `product_id` varchar(100) NOT NULL,
  `shopping_order_id` varchar(100) NOT NULL,
  PRIMARY KEY (`shopping_order_item_id`),
  KEY `product_id` (`product_id`),
  KEY `shopping_order_id` (`shopping_order_id`),
  CONSTRAINT `shopping_order_item_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  CONSTRAINT `shopping_order_item_ibfk_2` FOREIGN KEY (`shopping_order_id`) REFERENCES `shopping_order` (`shopping_order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_order_item`
--

LOCK TABLES `shopping_order_item` WRITE;
/*!40000 ALTER TABLE `shopping_order_item` DISABLE KEYS */;
INSERT INTO `shopping_order_item` VALUES ('064df66f-0784-4e32-9350-8659f492f2e0',1,'6cc3e546-7e24-4002-8cd4-6387ca394d3b','2dd93e03-54ff-426a-98f6-5fbfcd4b9f53'),('4b4c43e1-fc4f-47e4-aeda-b94f05bc2296',1,'96b94911-a46c-4d70-933c-29d8450e0a93','012e07f0-075f-4aef-8ff3-af2d4ce9425c'),('51e3fe68-c45a-4c71-8d82-117e907472e4',1,'28641b2e-43c0-47e6-ab3a-8a400f42978a','012e07f0-075f-4aef-8ff3-af2d4ce9425c'),('73a0a925-71cb-4f7c-a481-6ba58b2e347a',1,'96b94911-a46c-4d70-933c-29d8450e0a93','2dd93e03-54ff-426a-98f6-5fbfcd4b9f53'),('91f8dafb-1a6e-435e-b7a0-4ff5c7c4701d',1,'6cc3e546-7e24-4002-8cd4-6387ca394d3b','939fa448-cb3f-41e7-9f59-b14b2ce82439'),('c2b71904-f8b2-46f3-84c8-37d74742e708',3,'d657a62d-747e-47c8-b777-d4048d29bf7a','a737f332-cada-4c9c-b940-5529924ee4f5'),('f03d5b32-6cba-415a-9e3a-1fb7fbc56e98',1,'bde742cb-39ee-43a9-a852-523888ff452e','2dd93e03-54ff-426a-98f6-5fbfcd4b9f53');
/*!40000 ALTER TABLE `shopping_order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('07990f40-d089-47e8-bc83-fd8e8231ba3f','milica@gmail.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,0),('2b8fe473-8573-4f57-92e4-b731263dcd26','janko@gmail.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,0),('3c3cc73f-45fb-4d02-9274-88ec2d36ac7b','admin@itbc.rs','3eb3fe66b31e3b4d10fa70b5cad49c7112294af6ae4e476a1c405155d45aa121',1,1),('e4784914-3f9e-4bcb-b21e-01838c84b16e','aleksandar@gmail.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,0),('f815a998-1a24-4ea3-a63e-00a3ffc282a7','davidpantic@gmail.com','473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8',1,1);
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

-- Dump completed on 2023-02-22 18:16:29
