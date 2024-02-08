# Aplicación de Gestión de Torneo de Fútbol

Esta aplicación Python permite gestionar un torneo de fútbol con dos cuadrangulares y una fase preliminar y una final.

## Instalación

1. Asegúrate de tener Python y XAMPP instalados en tu sistema.
2. Crea una base de datos en MySQL a través de phpMyAdmin.
3. Clona este repositorio en tu máquina local.

## Configuración

1. Configura la conexión a la base de datos en `conexion_db.py`.
2. Define la estructura de tu base de datos y crea las tablas necesarias.
3. Ejecuta el script `main.py` para iniciar la aplicación.

## Funcionalidades

- Crear equipos y registrar partidos.
- Visualizar los cuadrangulares y la tabla de posiciones.
- Realizar simulaciones de partidos y actualizar los resultados.


## Base de Datos

-- Crear la base de datos
CREATE DATABASE cuadrangular;

-- Usar la base de datos
USE cuadrangular;

-- Crear la tabla para los equipos
CREATE TABLE equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    puntos_cuadrangular_1 INT DEFAULT 0,
    puntos_cuadrangular_2 INT DEFAULT 0
);

-- Crear la tabla para los partidos (opcional)
CREATE TABLE partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo1_id INT,
    equipo2_id INT,
    marcador_equipo1 INT,
    marcador_equipo2 INT,
    FOREIGN KEY (equipo1_id) REFERENCES equipos(id),
    FOREIGN KEY (equipo2_id) REFERENCES equipos(id)
);


