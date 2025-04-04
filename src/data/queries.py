queries = {
    "ocupados": """
        SELECT datos.*
        FROM parquet_scan(?) AS datos
        WHERE variable = 'ocupados'
        ORDER BY año
    """,
    "informalidad": """
        SELECT año, variable, valor
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'formal', 'informal') AND año >= 2018
        ORDER BY variable, año
    """,
    "tpi": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'tpi', 'no_tpi')
        ORDER BY variable, año
    """,
    "ed_sup": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'ed_sup_completa', 'sin_ed_sup')
        ORDER BY variable, año
    """,
    "calificacion_ocupacion": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'alta_calificacion', 'calificacion_media_baja')
        ORDER BY variable, año
    """,
    "ed_sup_calificacion_ocupacion": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'ed_sup_competencia_alta', 'ed_sup_competencia_media_baja')
        ORDER BY variable, año
    """,
    "edu_calificacion_ocupacion": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados','sin_ed_sup', 'ed_sup_competencia_alta', 'ed_sup_competencia_media_baja')
        ORDER BY variable, año
    """,
    "sector_publico": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'sector_publico', 'no_sector_publico')
        ORDER BY variable, año
    """,
    "nacionalidad": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'nacionalidad_chilena', 'nacionalidad_extranjera')
        ORDER BY variable, año
    """,
    "sexo": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable IN ('ocupados', 'hombre', 'mujer')
        ORDER BY variable, año
    """
}