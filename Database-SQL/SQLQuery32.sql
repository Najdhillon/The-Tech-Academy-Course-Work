Select *
FROM PayRates

Select *
FROM Employee

Select *
FROM Employee INNER JOIN PayRates
ON Employee.EmpID = Payrates.EmpID

Select *
FROM Employee

Select *
FROM Employee

Select *
FROM Location

Select *
FROM Employee INNER JOIN Location
ON Employee.LocationID = Location.LocationID

Select FirstName, LastName, City, State
FROM Employee INNER JOIN Location
ON Employee.LocationID = Location.LocationID

Select * FROM  [Grant]

Select FirstName,LastName,GrantName, Amount
FROM Employee INNER JOIN [Grant]
ON Employee.EmpID = [Grant].EmpID

Select [date],Item,Price,CustomerName
FROM PurchaseActivity INNER JOIN Customer
ON PurchaseActivity.CustomerID = Customer.CustomerID