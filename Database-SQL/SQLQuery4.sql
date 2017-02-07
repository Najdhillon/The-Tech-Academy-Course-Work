Select FirstName, LastName, City, State
FROM Employee LEFT OUTER JOIN Location
ON Employee.LocationID = Location.LocationID

Select FirstName, LastName, City, State
FROM Employee RIGHT OUTER JOIN Location
ON Employee.LocationID = Location.LocationID

Select FirstName, LastName, City, State
FROM Employee FULL OUTER JOIN Location
ON Employee.LocationID = Location.LocationID

Select FirstName, LastName, GrantName, Amount
FROM Employee Right OUTER JOIN [Grant]
ON Employee.EmpID = [Grant].EmpID

Select * FROM Employee
Select * FROM [Grant]

Select FirstName, LastName, GrantName, Amount
FROM Employee Left OUTER JOIN [Grant]
ON Employee.EmpID = [Grant].EmpID

