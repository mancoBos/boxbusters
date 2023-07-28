WITH hes_data AS (
    SELECT
        epikey,
        sitetret,
        sex,
        startage_calc,
        admimeth,
        ethnos,
        lsoa11,
        speldur,
        tretspef,
        diag_count,
        diag_3_concat,
        diag_4_concat,
        opertn_3_concat,
        opertn_4_concat,
        opertn_count
    FROM 
        dars_nic_484452_h8s1l.hes_apc_2223_dars_nic_484452_h8s1l
    WHERE 
        -- This is based on the official HES publication methodology - see readme for details
        classpat IN ('1', '5') AND epistat='3' AND speldur IS NOT NULL
),

add_imd AS (
    SELECT
        *
    FROM
        hes_data
    LEFT JOIN (
        SELECT  
            lsoa_code_2011,
            index_of_multiple_deprivation_imd_score
        FROM    
            dhsc_byod.imd_lsoa_lookup_file_7___all_iod2019_scores__ranks__deciles_and_population_denominators_3
    ) AS imd
    ON 
        hes_data.lsoa11 = imd.lsoa_code_2011
),

SELECT 
    epikey,
    sitetret,
    admimeth,
    sex,
    startage_calc,
    ethnos,
    index_of_multiple_deprivation_imd_score,
    diag_count,
    opertn_count,
    tretspef,
    speldur
FROM    
    add_imd
