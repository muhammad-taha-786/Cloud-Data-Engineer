-- Basic Procedures
-- Parameters 
-- Variables 

DECLARE @product_name AS VARCHAR(255);
SET @product_name = 'Electra Townie Original 7D - 2015/2016';

SELECT * FROM [production].[products]
WHERE product_name = @product_name;

CREATE PROCEDURE sp_products(@min_price AS DECIMAL)
AS
BEGIN 
	SELECT 
	product_name, 
	list_price
FROM 
	production.products
	WHERE 
	list_price > @min_price
ORDER BY 
	product_name;

END;

EXEC sp_products 10000.00;


DROP PROCEDURE sp_products;


ALTER PROCEDURE sp_product1(@min_price AS DECIMAL, @max_price AS DECIMAL, @row_count)
AS
BEGIN
DECLARE @product_name AS VARCHAR(255)
SET @product_name = 'Electra Townie Original 7D - 2015/2016';

DECLARE @model_year AS SMALLINT
SET @model_year = 2018;

SELECT 
	product_name, 
	model_year
	list_price
FROM 
	production.products
	WHERE 
	list_price > @min_price AND list_price <@max_price
	AND product_name = @product_name
	AND model_year = @model_year
ORDER BY 
	product_name;

END;

SELECT * FROM production.products;



EXEC sp_product1 @min_price=10000.00, @max_price=120000.00;



--------
CREATE PROCEDURE uspFindProductByModel (
    @model_year SMALLINT,
    @product_count INT OUTPUT
) AS
BEGIN
    SELECT 
        product_name,
        list_price
    FROM
        production.products
    WHERE
        model_year = @model_year;

    SELECT @product_count = @@ROWCOUNT;
END;



DECLARE @count INT;

EXEC uspFindProductByModel
    @model_year = 2018,
    @product_count = @count OUTPUT;

SELECT @count AS 'Number of products found';




-------------------------

SELECT * FROM [sales].[customers];

Alter PROCEDURE year_sale (
    @state AS VARCHAR(255),
	@city AS VARCHAR(255),
    @state_count INT OUTPUT
) AS
BEGIN
    SELECT 
        state
    FROM
        [sales].[customers]
    WHERE
        state = @state;

    SELECT @state_count = @@ROWCOUNT;
END;


DECLARE @count INT;

EXEC year_sale
    @state = 'NY',
	@city = 'Buffalo',
    @state_count = @count OUTPUT;

SELECT @count AS 'Total New Year ';



---------
ALTER PROCEDURE sp_product1(@min_price AS DECIMAL, @max_price AS DECIMAL)
AS
BEGIN

SELECT 
	product_name, 
	list_price
FROM 
	production.products
	WHERE 
	list_price > @min_price AND list_price <@max_price
ORDER BY 
	product_name;

	DECLARE @count AS SMALLINT;
	SET @count = @@ROWCOUNT;

	IF @count = 156
	BEGIN 
		PRINT 'Count is an expected';
	END
	ELSE
	BEGIN
		PRINT 'Count is not an expected';
	END

END;

SELECT * FROM production.products;



EXEC sp_product1 @min_price=10000.00, @max_price=120000.00;







---------WHILE-----------

DECLARE @counter INT = 1;

WHILE @counter <=5
	BEGIN
		PRINT @counter;
		SET @counter = @counter+1
	END


CREATE PROCEDURE result
AS 
BEGIN 
DECLARE @counter INT = 1;

WHILE @counter <=5
	BEGIN
		PRINT @counter;
		SET @counter = @counter+1
	END
END;

EXEC result;




-------CURSOR--------

DECLARE @product_name AS VARCHAR(255);
DECLARE @list_price AS DECIMAL ;

DECLARE product_cursor CURSOR
FOR SELECT 
        product_name, 
        list_price
    FROM 
        production.products;

OPEN product_cursor;

FETCH NEXT FROM product_cursor INTO 
@product_name, @list_price;

SELECT @@FETCH_STATUS;

CLOSE product_cursor;
DEALLOCATE product_cursor;