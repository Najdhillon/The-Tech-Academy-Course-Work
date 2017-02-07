
Select *
FROM [Grant]


SELECT *
FROM [Grant]
WHERE GrantName like '%@%'
AND GrantName NOT LIKE '% %'

SELECT *
FROM CurrentProducts
WHERE ProductName LIKE '%x%'

SELECT *
FROM CurrentProducts
WHERE RetailPrice > 1100

SELECT ProductName, RetailPrice, Category 
FROM CurrentProducts
WHERE ProductName LIKE '[A-C]%'

SELECT *
FROM [Grant]
WHERE Amount BETWEEN 7500 and 20000

SELECT *
FROM [Grant]
WHERE GrantName LIKE '%_%'
AND GrantName NOT LIKE '%@%'
AND EmpID NOT LIKE 'NULL'
AND EmpID NOT LIKE '4'


SELECT *
FROM Employee
WHERE FirstName LIKE 'David'
OR FirstName like 'James'

SELECT *
FROM [Grant]
where GrantName like '_%O%'
AND Amount > 18000

SELECT *
FROM Employee
WHERE Status = 'Has Tenure'