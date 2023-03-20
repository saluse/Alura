-- Usaando a Condição HAVING
SELECT 
    Estado,
    SUM(Limite_de_Credito) AS Soma_Limite
FROM Tabela_de_Clientes
GROUP BY Estado
HAVING SUM(Limite_de_Credito) > 900000;

SELECT
    Embalagem,
    MAX(Preco_de_Lista) AS Maior_Preco,
    MIN(Preco_de_Lista) AS Menor_Preco
FROM Tabela_de_Produtos
GROUP BY Embalagem
HAVING SUM(Preco_de_Lista) <= 80;

SELECT
    Embalagem,
    MAX(Preco_de_Lista) AS Maior_Preco,
    MIN(Preco_de_Lista) AS Menor_Preco
FROM Tabela_de_Produtos
GROUP BY Embalagem
HAVING SUM(Preco_de_Lista) <= 80 AND MAX(Preco_de_Lista) >=5

-- Cláusula CASE
SELECT
    Nome_do_Produto,
    Preco_de_Lista
    CASE
        WHEN Preco_de_Lista >= 12 THEN "Produto Caro"
        WHEN Preco_de_Lista >= 7 AND < 12 THEN "Produto em Conta"
        ELSE "Produto Barato"
END AS Status_Preco,
AVG(Preco_de_Lista) AS Preco_Medio
FROM Tabela_de_Produtos
WHERE Sabor = "Manga"
GROUP BY Embalagem
    CASE
        WHEN Preco_de_Lista >= 12 THEN "Produto Caro"
        WHEN Preco_de_Lista >= 7 AND < 12 THEN "Produto em Conta"
        ELSE "Produto Barato"
    END AS Status_Preco,

-- JOINs

SELECT * FROM Tabela_de_Clientes
SELECT * FROM Tabela_Notas_Fiscais

SELECT * FROM Tabela_de_Clientes a
SELECT * FROM Tabela_Notas_Fiscais b 
ON a.Numero = b.Numero

SELECT * FROM Tabela_de_Clientes A
INNER JOIN Tabela_Notas_Fiscais B 
ON A.Matricula = B.Matricula

SELECT
    a.Matricula,
    a.Nome,
    COUNT(*)
FROM Tabela_de_Clientes A
INNER JOIN Tabela_Notas_Fiscais B 
ON A.Matricula = B.Matricula
GROUP BY A.Matricula,
         A.Nome
         