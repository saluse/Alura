-- Usaando a Condição HAVING
SELECT 
    Estado,
    SUM(Limite_de_Credito) AS Soma_Limite
FROM Tabela_de_Clientes
GROUP BY Estado
HAVING SUM(Limite_de_Credito) > 900000;
