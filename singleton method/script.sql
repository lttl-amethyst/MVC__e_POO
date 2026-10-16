CREATE DATABASE loja_singleton;
USE loja_singleton;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);
INSERT INTO produtos (nome, preco) VALUES
('Teclado Mecânico', 150.00),
('Mouse', 80.00),
('Headset', 200.00);