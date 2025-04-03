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
        valor - LAG(valor) OVER (PARTITION BY variable ORDER BY año) AS diferencia
        FROM parquet_scan(?) AS datos
        WHERE variable = 'ed_sup_completa' OR variable = 'sin_ed_sup'
        ORDER BY variable, año
    """,
    "calificacion_ocupacion": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable = 'alta_calificacion' OR variable = 'calificacion_media_baja'
        ORDER BY variable, año
    """,
    "ed_sup_calificacion_ocupacion": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable = 'ed_sup_competencia_alta' OR variable = 'ed_sup_competencia_media_baja'
        ORDER BY variable, año
    """,
    "sector_publico": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable = 'sector_publico' OR variable = 'no_sector_publico'
        ORDER BY variable, año
    """,
    "nacionalidad": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable = 'nacionalidad_chilena' OR variable = 'nacionalidad_extranjera'
        ORDER BY variable, año
    """,
    "sexo": """
        SELECT 
        año,
        variable,
        valor,
        FROM parquet_scan(?) AS datos
        WHERE variable = 'hombre' OR variable = 'mujer'
        ORDER BY variable, año
    """
}