SELECT imie, nazwisko, SUM(DATEDIFF(data_wyjazdu, data_przyjazdu)) `Liczba noclegów` FROM noclegi NATURAL JOIN klienci GROUP BY nr_dowodu ORDER BY `Liczba noclegów` DESC;