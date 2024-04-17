SELECT kod_u `Kod urządzenia`, nazwa_u `Nazwa urządzenia`, COUNT(DISTINCT kod_k) `Liczba krajów` FROM instalacje NATURAL JOIN urzadzenia WHERE typ_u = "Tablet" GROUP BY kod_u ORDER BY `Liczba krajów` DESC LIMIT 1;