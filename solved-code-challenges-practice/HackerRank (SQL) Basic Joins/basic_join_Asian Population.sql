#https://www.hackerrank.com/challenges/asian-population/problem

#Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

SELECT SUM(City.Population) FROM City JOIN Country 
ON City.Countrycode = Country.Code
WHERE COUNTRY.CONTINENT = 'Asia';
