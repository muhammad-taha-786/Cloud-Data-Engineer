--DDL Trigger


CREATE TABLE index_logs (
    log_id INT IDENTITY PRIMARY KEY,
    event_data XML NOT NULL,
    changed_by SYSNAME NOT NULL
);
GO


SELECT * FROM index_logs;

CREATE TRIGGER trg_index_log 
ON DATABASE 
FOR 
	CREATE_INDEX,
	ALTER_INDEX,
	DROP_INDEX 
AS
	BEGIN 
		INSERT INTO index_logs(
		event_data, 
		changed_by
		) 
		VALUES(
			EVENTDATA(),
			USER
		);
END

CREATE NONCLUSTERED INDEX ind_fname
ON [sales].[customers](first_name);


-- FOR VIEW 


CREATE TABLE index_log_details (
    log_id INT IDENTITY PRIMARY KEY,
    event_data XML NOT NULL,
    changed_by SYSNAME NOT NULL
);
GO

CREATE TRIGGER trg_index_log_details
ON DATABASE 
FOR 
	CREATE_VIEW, 
	ALTER_VIEW,
	DROP_VIEW
AS 
	BEGIN 
		INSERT INTO index_log_details(
		event_data, 
		changed_by
		) 
		VALUES(
			EVENTDATA(),
			USER
		);
	END

CREATE VIEW vw_customers
AS SELECT * FROM [sales].[customers];

SELECT * FROM index_log_details;

--DISABLE TRIGGER

DISABLE TRIGGER trg_index_log
ON DATABASE;

DISABLE TRIGGER index_log_details 
ON DATABASE;

ENABLE TRIGGER trg_index_log
ON DATABASE;

CREATE VIEW vw_orders
AS SELECT * FROM [sales].[orders];

CREATE VIEW vw_staff 
AS SELECT * FROM [sales].[staffs];


--View Trigger Definition

SELECT definition FROM sys.sql_modules 
WHERE object_id = OBJECT_ID('[production].[trg_product_audit]'); 

SELECT * FROM sys.triggers;

SELECT * FROM sys.triggers 