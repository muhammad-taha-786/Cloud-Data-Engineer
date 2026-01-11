--scalar function

CREATE FUNCTION sales.fn_NetSales(
	@quantity SMALLINT,
	@listPrice DECIMAL(10, 2),
	@discount DECIMAL(10, 2)

)
RETURNS DECIMAL(10,2)
AS
BEGIN 
	RETURN @quantity * @listPrice * (1 - @discount);
END;


SELECT sales.fn_NetSales(10,10,0.1) AS NetPrice;


CREATE FUNCTION sales.fn_sum(
	@a SMALLINT, 
	@b DECIMAL(10,2),
	@c DECIMAL(10,2)
)
RETURNS DECIMAL(10,2)
AS 
	BEGIN
		RETURN (@a + @b + @C) 
	END

SELECT sales.fn_sum(10,20,20) AS SumValue;


CREATE FUNCTION udfProductInYear (
    @model_year INT
)
RETURNS TABLE
AS
RETURN
    SELECT 
        product_name,
        model_year,
        list_price
    FROM
        production.products
    WHERE
        model_year = @model_year;

SELECT * FROM udfProductInYear(2017);



SELECT * FROM production.products;
--SQL Server Table Variables
DECLARE @product_table TABLE (
    product_name VARCHAR(MAX) NOT NULL,
    brand_id INT NOT NULL,
    list_price DEC(11,2) NOT NULL
);

INSERT INTO @product_table
SELECT
    product_name,
    brand_id,
    list_price
FROM
    production.products
WHERE
    category_id = 1;

SELECT
    *
FROM
    @product_table;
GO


SELECT * FROM [sales].[order_items];

DECLARE @sales_order TABLE (
    item_id INT NOT NULL, 
    product_id INT NOT NULL,
    list_price INT NOT NULL
);

INSERT INTO @sales_order
SELECT 
    item_id,
    product_id,
    list_price
FROM sales.order_items
WHERE order_id = 7;

SELECT * FROM @sales_order;
