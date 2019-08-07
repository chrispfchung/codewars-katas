#https://www.hackerrank.com/challenges/african-cities/problem

#Query names of all cities in Africa by joining both tables

SELECT CITY.NAME FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'AFRICA';
