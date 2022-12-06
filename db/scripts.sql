

CREATE OR REPLACE FUNCTION get_departamentos()
RETURNS TABLE(j json)
LANGUAGE plpgsql
AS
$$
BEGIN
    RETURN QUERY
    SELECT COALESCE(ARRAY_TO_JSON(ARRAY_AGG(departamentos)) ,'[]'::json) AS data FROM (SELECT d.id,
                   d.nombre
            FROM departamento AS d
            ORDER BY d.nombre
    ) AS departamentos;
END;
$$;

CREATE OR REPLACE FUNCTION get_clases_by_departamento(pk int)
RETURNS TABLE(j json)
LANGUAGE plpgsql
AS
$$
BEGIN
    RETURN QUERY
    SELECT COALESCE(array_to_json(array_agg(clases)), '[]'::json) as data FROM
    (SELECT
        c.id,
        c.nombre
    FROM clase AS c
    WHERE c.departamento_id = pk
    ORDER BY c.nombre) AS clases;
END
$$;

CREATE OR REPLACE FUNCTION get_familias_by_clase(pk int)
RETURNS TABLE(j json)
LANGUAGE plpgsql
AS
$$
BEGIN
    RETURN QUERY
    SELECT COALESCE(array_to_json(array_agg(familias)),'[]'::JSON) FROM (SELECT
        f.id,
        f.nombre
    FROM familia AS f
    WHERE f.clase_id = pk
    ORDER BY f.nombre) AS familias;
END;
$$;

CREATE OR REPLACE FUNCTION get_articulo(pk INT)
RETURNS TABLE(j json)
LANGUAGE plpgsql
AS
$$
BEGIN
    RETURN QUERY
    SELECT array_to_json(ARRAY_AGG(articulo)) AS data FROM (SELECT
        a.sku,
        a.nombre,
        a.marca,
        a.modelo,
        a.departamento_id,
        a.clase_id,
        a.familia_id,
        a.fecha_alta,
        a.fecha_baja,
        a.stock,
        a.cantidad,
        a.descontinuado
    FROM articulo AS a
    WHERE a.sku = pk and a.estatus = 1) AS articulo;
END
$$;

CREATE OR REPLACE FUNCTION update_articulo(
    a_sku smallint,
    a_nombre varchar,
    a_marca varchar,
    a_modelo varchar,
    a_cantidad smallint,
    a_stock smallint,
    a_departamento bigint,
    a_clase bigint,
    a_familia bigint,
    a_descontinuado smallint
)
returns varchar
language plpgsql
AS
$$
    DECLARE
        log_res varchar;
BEGIN
     log_res = 'error';
     update articulo set nombre = a_nombre, marca = a_marca, modelo = a_modelo,
                         stock = a_stock, cantidad = a_cantidad, descontinuado = a_descontinuado,
                         clase_id = a_clase, departamento_id = a_departamento, familia_id = a_familia
                         WHERE sku = a_sku and estatus > 0;
     update articulo set fecha_baja = NOW() WHERE sku = a_sku and estatus > 0 and descontinuado = 1;
    log_res = 'ok';
    RETURN log_res;
END
$$;

CREATE OR REPLACE FUNCTION delete_articulo(
a_sku smallint
)
returns varchar
language plpgsql
AS
$$
    DECLARE
        log_res varchar;
BEGIN
     log_res = 'error';
     update articulo set estatus = 0 WHERE sku = a_sku and estatus > 0;
    log_res = 'ok';
    RETURN log_res;
END
$$;

