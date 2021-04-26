-- Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:


Select FirstName, LastName, City, State
From Person  
left Join Address
on Person.PersonId = Address.PersonId