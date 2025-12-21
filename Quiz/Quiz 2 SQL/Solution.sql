--Q1
SELECT 
    c.CustomerID,
    c.Name AS CustomerName,
    SUM(so.TotalAmount) AS TotalSpent
FROM customer c
JOIN salesorder so 
    ON c.CustomerID = so.CustomerID
GROUP BY 
    c.CustomerID, c.Name
ORDER BY 
    TotalSpent DESC;


--Q2

SELECT 
    s.SupplierID,
    s.Name AS SupplierName,
    COUNT(p.ProductID) AS ProductCount
FROM supplier s
JOIN product p
    ON s.SupplierID = p.ManufacturerID
GROUP BY 
    s.SupplierID, s.Name
HAVING 
    COUNT(p.ProductID) > 10;


--Q3

SELECT 
    p.ProductID,
    p.Name AS ProductName,
    SUM(sod.Quantity) AS TotalOrderQuantity
FROM salesorderdetail sod
JOIN product p 
    ON sod.ProductID = p.ProductID
LEFT JOIN returndetail rd
    ON sod.ProductID = rd.ProductID
WHERE rd.ProductID IS NULL
GROUP BY 
    p.ProductID, p.Name;


--Q4
SELECT 
    c.CategoryID,
    c.Name AS CategoryName,
    p.Name AS ProductName,
    p.Price
FROM product p
JOIN category c 
    ON p.CategoryID = c.CategoryID
WHERE p.Price = (
    SELECT MAX(p2.Price)
    FROM product p2
    WHERE p2.CategoryID = p.CategoryID
);


--Q5
SELECT 
    so.OrderID,
    c.Name AS CustomerName,
    p.Name AS ProductName,
    cat.Name AS CategoryName,
    s.Name AS SupplierName,
    sod.Quantity
FROM salesorder so
JOIN customer c
    ON so.CustomerID = c.CustomerID
JOIN salesorderdetail sod
    ON so.OrderID = sod.OrderID
JOIN product p
    ON sod.ProductID = p.ProductID
JOIN category cat
    ON p.CategoryID = cat.CategoryID
JOIN supplier s
    ON p.ManufacturerID = s.SupplierID
ORDER BY so.OrderID;


--Q6

SELECT 
    sh.ShipmentID,
    w.Name AS WarehouseName,
    m.Name AS ManagerName,
    p.Name AS ProductName,
    sd.Quantity AS QuantityShipped,
    sh.TrackingNumber
FROM shipment sh
JOIN warehouse w
    ON sh.WarehouseID = w.WarehouseID
JOIN manager m
    ON w.ManagerID = m.ManagerID
JOIN shipmentdetail sd
    ON sh.ShipmentID = sd.ShipmentID
JOIN product p
    ON sd.ProductID = p.ProductID
ORDER BY sh.ShipmentID;


--Q7

SELECT
    CustomerID,
    CustomerName,
    OrderID,
    TotalAmount
FROM (
    SELECT
        c.CustomerID,
        c.Name AS CustomerName,
        so.OrderID,
        so.TotalAmount,
        RANK() OVER (
            PARTITION BY c.CustomerID
            ORDER BY so.TotalAmount DESC
        ) AS order_rank
    FROM salesorder so
    JOIN customer c
        ON so.CustomerID = c.CustomerID
) ranked_orders
WHERE order_rank <= 3
ORDER BY CustomerID, order_rank;


--Q8
SELECT
    sod.ProductID,
    p.Name AS ProductName,
    so.OrderID,
    so.OrderDate,
    sod.Quantity,
    LAG(sod.Quantity) OVER (
        PARTITION BY sod.ProductID
        ORDER BY so.OrderDate
    ) AS PrevQuantity,
    LEAD(sod.Quantity) OVER (
        PARTITION BY sod.ProductID
        ORDER BY so.OrderDate
    ) AS NextQuantity
FROM salesorderdetail sod
JOIN salesorder so
    ON sod.OrderID = so.OrderID
JOIN product p
    ON sod.ProductID = p.ProductID
ORDER BY sod.ProductID, so.OrderDate;


--Q9

CREATE VIEW vw_CustomerOrderSummary AS
SELECT
    c.CustomerID,
    c.Name AS CustomerName,
    COUNT(so.OrderID) AS TotalOrders,
    COALESCE(SUM(so.TotalAmount), 0) AS TotalAmountSpent,
    MAX(so.OrderDate) AS LastOrderDate
FROM customer c
LEFT JOIN salesorder so
    ON c.CustomerID = so.CustomerID
GROUP BY
    c.CustomerID,
    c.Name;

SELECT * FROM vw_CustomerOrderSummary;

--Q10

CREATE PROCEDURE sp_GetSupplierSales
    @SupplierID INT
AS
BEGIN
    SELECT
        s.SupplierID,
        SUM(sod.TotalAmount) AS TotalSalesAmount
    FROM supplier s
    JOIN product p
        ON p.ManufacturerID = s.SupplierID
    JOIN salesorderdetail sod
        ON sod.ProductID = p.ProductID
    JOIN salesorder so
        ON so.OrderID = sod.OrderID
    WHERE s.SupplierID = @SupplierID
    GROUP BY s.SupplierID;
END;


EXEC sp_GetSupplierSales @SupplierID = 1;

