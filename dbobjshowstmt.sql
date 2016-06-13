SELECT TRIM(TableName)||'.'||
	CASE WHEN tablekind = 'm' THEN 'mac'
		WHEN tablekind = 't' THEN 'tab'
		WHEN tablekind = 'v' THEN 'vw'
		WHEN tablekind = 'p' THEN 'proc' 
	END AS filename
	,'SHOW ' || 
	CASE WHEN tablekind = 'm' THEN 'MACRO' 
		WHEN tablekind = 't' THEN 'TABLE' 
		WHEN tablekind = 'v' THEN 'VIEW' 
		WHEN tablekind = 'p' THEN 'PROCEDURE'
	END 
	|| ' ' || TRIM(databasename) || '.' || TRIM(tablename) || ';' AS showstmt
FROM dbc.tables 
WHERE tablekind IN ('T','V','M','P')
	AND databasename = ?;

