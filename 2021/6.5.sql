CREATE OR REPLACE TABLE jednostki_z_krajami(id_gracza INT, lok_x INT, lok_y INT, kraj TINYTEXT);
INSERT INTO jednostki_z_krajami SELECT id_gracza, lok_x, lok_y, kraj FROM jednostki NATURAL JOIN gracze;
CREATE OR REPLACE VIEW miejsca AS SELECT id_gracza, lok_x, lok_y FROM jednostki_z_krajami GROUP BY lok_x, lok_y;
SELECT COUNT(*) FROM miejsca WHERE (SELECT COUNT(*) FROM jednostki_z_krajami WHERE lok_x = miejsca.lok_x AND lok_y = miejsca.lok_y AND id_gracza != miejsca.id_gracza) > 0;
CREATE OR REPLACE VIEW miejsca AS SELECT id_gracza, lok_x, lok_y FROM jednostki_z_krajami WHERE kraj = "Polska" GROUP BY lok_x, lok_y;
SELECT COUNT(*) FROM miejsca WHERE (SELECT COUNT(*) FROM jednostki_z_krajami WHERE lok_x = miejsca.lok_x AND lok_y = miejsca.lok_y AND id_gracza != miejsca.id_gracza) > 0;