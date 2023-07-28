WITH FIRST AS (
    SELECT
        SITETRET,
        SPELDUR,
        DISDATE
    FROM 
        dars_nic_484452_h8s1l.hes_apc_2223_dars_nic_484452_h8s1l
    WHERE 
        -- This is based on the official HES publication methodology - see readme for details
        CLASSPAT IN ('1', '5') AND EPISTAT='3'
),

SECOND AS (
    SELECT 
        SITETRET, 
        month(DISDATE) AS discharge_month,
        year(DISDATE) AS discharge_month,
        avg(SPELDUR) AS length_of_stay,
        round(count(*), -1) AS n_records
    FROM
        FIRST
    GROUP BY   
        SITETRET,
        year(DISDATE),
        month(DISDATE)
)

SELECT  
    *
FROM    
    SECOND
WHERE   
    n_records > 100
