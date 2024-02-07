-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema petcodepy1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema petcodepy1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `petcodepy1` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `petcodepy1` ;

-- -----------------------------------------------------
-- Table `petcodepy1`.`clientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `petcodepy1`.`clientes` ;

CREATE TABLE IF NOT EXISTS `petcodepy1`.`clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `dni` BIGINT NULL DEFAULT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `domicilio` VARCHAR(255) NOT NULL,
  `mascota` VARCHAR(100) NOT NULL,
  `especie` VARCHAR(255) NOT NULL,
  `edad` INT NOT NULL,
  `telefono` BIGINT NOT NULL,
  `turno` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `petcodepy1`.`productos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `petcodepy1`.`productos` ;

CREATE TABLE IF NOT EXISTS `petcodepy1`.`productos` (
  `id_productos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`id_productos`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;