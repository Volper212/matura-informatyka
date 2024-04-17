ALTER TABLE gracze ADD COLUMN IF NOT EXISTS kategoria VARCHAR(15);
UPDATE gracze SET kategoria = CASE
	WHEN wiek <= 19 THEN "juniorzy"
    WHEN wiek BETWEEN 20 AND 49 THEN "seniorzy"
    ELSE "weterani"
END;

CREATE OR REPLACE VIEW maksima AS SELECT kategoria, MAX(liczba_ocen) maksimum FROM (SELECT gracze.kategoria, COUNT(*) liczba_ocen FROM oceny JOIN gracze ON oceny.id_gracza = gracze.id_gracza GROUP BY oceny.id_gry, gracze.kategoria) liczby_ocen GROUP BY kategoria;

SELECT liczby_ocen.kategoria, nazwa, liczba_ocen FROM (
    SELECT gracze.kategoria, id_gry, COUNT(*) liczba_ocen FROM oceny JOIN gracze ON oceny.id_gracza = gracze.id_gracza GROUP BY id_gry, gracze.kategoria
) liczby_ocen
JOIN gry ON liczby_ocen.id_gry = gry.id_gry
WHERE liczba_ocen IN (SELECT maksimum FROM maksima WHERE maksima.kategoria = liczby_ocen.kategoria) ORDER BY liczby_ocen.kategoria;