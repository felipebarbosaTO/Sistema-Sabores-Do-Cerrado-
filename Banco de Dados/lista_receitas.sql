-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: lista_receitas
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `avaliacao`
--

DROP TABLE IF EXISTS `avaliacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avaliacao` (
  `id_avaliacao` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_receita` int NOT NULL,
  `nota` int NOT NULL,
  `comentario` text,
  PRIMARY KEY (`id_avaliacao`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_receita` (`id_receita`),
  CONSTRAINT `avaliacao_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `avaliacao_ibfk_2` FOREIGN KEY (`id_receita`) REFERENCES `receita` (`id_receita`),
  CONSTRAINT `avaliacao_chk_1` CHECK ((`nota` between 1 and 5))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avaliacao`
--

LOCK TABLES `avaliacao` WRITE;
/*!40000 ALTER TABLE `avaliacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `avaliacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cardapio`
--

DROP TABLE IF EXISTS `cardapio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardapio` (
  `id_cardapio` int NOT NULL AUTO_INCREMENT,
  `id_receita` int NOT NULL,
  `data_cardapio` date NOT NULL,
  `tipo_refeicao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_cardapio`),
  KEY `id_receita` (`id_receita`),
  CONSTRAINT `cardapio_ibfk_1` FOREIGN KEY (`id_receita`) REFERENCES `receita` (`id_receita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardapio`
--

LOCK TABLES `cardapio` WRITE;
/*!40000 ALTER TABLE `cardapio` DISABLE KEYS */;
/*!40000 ALTER TABLE `cardapio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorito`
--

DROP TABLE IF EXISTS `favorito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorito` (
  `id_favorito` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_receita` int NOT NULL,
  PRIMARY KEY (`id_favorito`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_receita` (`id_receita`),
  CONSTRAINT `favorito_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `favorito_ibfk_2` FOREIGN KEY (`id_receita`) REFERENCES `receita` (`id_receita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorito`
--

LOCK TABLES `favorito` WRITE;
/*!40000 ALTER TABLE `favorito` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico`
--

DROP TABLE IF EXISTS `historico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico` (
  `id_historico` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_receita` int NOT NULL,
  `data_visualizacao` datetime NOT NULL,
  PRIMARY KEY (`id_historico`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_receita` (`id_receita`),
  CONSTRAINT `historico_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `historico_ibfk_2` FOREIGN KEY (`id_receita`) REFERENCES `receita` (`id_receita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico`
--

LOCK TABLES `historico` WRITE;
/*!40000 ALTER TABLE `historico` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receita`
--

DROP TABLE IF EXISTS `receita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receita` (
  `id_receita` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `ingredientes` text NOT NULL,
  `modo_preparo` text NOT NULL,
  `link_imagem` varchar(255) DEFAULT NULL,
  `link_video` varchar(255) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `dificuldade` enum('Facil, Medio, Dificil') DEFAULT NULL,
  PRIMARY KEY (`id_receita`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receita`
--

LOCK TABLES `receita` WRITE;
/*!40000 ALTER TABLE `receita` DISABLE KEYS */;
/*!40000 ALTER TABLE `receita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipo_usuario` enum('admin','usuario') NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-31 15:58:08


--- --------------------------------------- ---
--- Alterações importantes feitas no Banco  ---
-- use lista_receitas;

INSERT INTO usuario (nome, email, senha, tipo_usuario)
VALUES 
('admin', 'admin@sabores.com', '123', 'admin'),
('joao', 'joao@email.com', 'abc', 'usuario'),
('maria', 'maria@email.com', 'xyz', 'usuario');

ALTER TABLE receita
CHANGE dificuldade dificuldade enum('Facil', 'Medio', 'Dificil') DEFAULT NULL;

INSERT INTO receita (nome, ingredientes, modo_preparo, categoria, dificuldade)
VALUES
('Espaguete à Bolonhesa', '500g de espaguete, 300g de carne moída, 2 dentes de alho picados, 1 cebola picada, 2 xícaras de molho de tomate', 'Cozinhe o espaguete em água e sal até ficar al dente. Refogue o alho e a cebola, adicione a carne moída e cozinhe até dourar. Acrescente o molho de tomate, sal e pimenta, e cozinhe por 15 minutos. Sirva o molho sobre o macarrão.','Massas','Facil'),
('Frango ao Curry com Arroz', '500g de peito de frango em cubos, 1 cebola picada, 1 colher de sopa de curry, 1 lata de creme de leite, 1 colher de sopa de azeite, Sal a gosto', 'Em uma panela, aqueça o azeite e refogue a cebola. Adicione o frango e doure bem. Acrescente o curry e o sal. Quando o frango estiver cozido, adicione o creme de leite e cozinhe por mais 5 minutos. Sirva com arroz branco.', 'Prato principal','Medio'),
('Salada Tropical', '1 alface americana picada, 1 manga em cubos, 1 cenoura ralada, 100g de peito de peru fatiado, 2 colheres de sopa de molho de iogurte', 'Em uma tigela, misture todos os ingredientes e regue com o molho de iogurte. Sirva gelada.','Saladas','Facil'),
('Bolo de Cenoura com Cobertura de Chocolate', '3 cenouras médias picadas, 3 ovos, 2 xícaras de açúcar, 2 e 1/2 xícaras de farinha de trigo, 1 colher de sopa de fermento, 1 xícara de óleo, Cobertura: 3 colheres de chocolate em pó, 2 colheres de manteiga e 1/2 xícara de leite', 'Bata no liquidificador a cenoura, os ovos e o óleo. Em uma tigela, misture o açúcar, a farinha e o fermento, e junte com a mistura batida. Asse por 40 minutos em forno médio. Ferva os ingredientes da cobertura e despeje sobre o bolo.','Sobremesa','Medio'),
('Pão de Queijo Mineiro', '500g de polvilho azedo, 3 ovos, 200ml de leite, 100ml de óleo, 250g de queijo minas ralado, Sal a gosto; queijo minas', 'Ferva o leite com o óleo e despeje sobre o polvilho, mexendo bem. Adicione os ovos e o queijo. Modele bolinhas e asse em forno pré-aquecido a 180°C até dourar.','Lanches','Medio');


-- Fim das alterações importantes feitas no Banco  ---