SELECT * FROM 
    tabela_de_vendedores A
INNER JOIN notas_fiscais B
ON A.MATRICULA = B.MATRICULA;

SELECT 
    A.MATRICULA, 
    A.NOME, COUNT(*) 
FROM tabela_de_vendedores A
INNER JOIN notas_fiscais B
ON A.MATRICULA = B.MATRICULA
GROUP BY A.MATRICULA, A.NOME;

SELECT 
    DISTINCT A.CPF, 
    A.NOME, 
    B.CPF 
FROM tabela_de_clientes A
LEFT JOIN notas_fiscais B 
    ON A.CPF = B.CPF
    
