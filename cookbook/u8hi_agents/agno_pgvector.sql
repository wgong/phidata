select * from pdf_agent;

select * from zinets;

select content, length(content), meta_data from zinets limit 1;


-- check pgvector version 
SELECT extversion 
FROM pg_extension 
WHERE extname = 'vector';

SELECT * FROM pg_available_extensions WHERE name = 'vector';

-- not working
SELECT pg_typeof(embedding), vector_dim(embedding)
FROM zinets
LIMIT 1;

-- check embedding dimensions
SELECT 
    a.attname AS column_name,
    format_type(a.atttypid, a.atttypmod) AS data_type
FROM 
    pg_attribute a
JOIN 
    pg_class t ON a.attrelid = t.oid
WHERE 
    a.attname = 'embedding' 
    AND t.relname = 'zinets'
    AND a.attnum > 0 
    AND NOT a.attisdropped;