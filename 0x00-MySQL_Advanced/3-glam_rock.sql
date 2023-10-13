-- get longlived Gram lock style bands

SELECT DISTINCT band_name, IFNULL(2020, 'split') - formed AS lifespan 
	FROM metal_bands
	WHERE FIND_IN_SET('Glam rock', style)
	ORDER BY lifespan DESC;
