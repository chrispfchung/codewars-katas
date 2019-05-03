#https://www.hackerrank.com/challenges/weather-observation-station-14/problem


SELECT TRUNCATE(MAX(LAT_N),4) FROM STATION
WHERE LAT_N < 137.2345

#Query highest latitude number less than 137.2345 to 4 decimal places.
