--SQL Server TRY CATCH

CREATE PROC usp_divide(
    @a decimal,
    @b decimal,
    @c decimal output
) AS
BEGIN
    BEGIN TRY
        SET @c = @a / @b;
    END TRY
    BEGIN CATCH
        SELECT  
            ERROR_NUMBER() AS ErrorNumber  
            ,ERROR_SEVERITY() AS ErrorSeverity  
            ,ERROR_STATE() AS ErrorState  
            ,ERROR_PROCEDURE() AS ErrorProcedure  
            ,ERROR_LINE() AS ErrorLine  
            ,ERROR_MESSAGE() AS ErrorMessage;  
    END CATCH
END;
GO


DECLARE @r decimal;
EXEC usp_divide 20, 0, @r output;
PRINT @r;


CREATE PROCEDURE usp_add(
	@a DECIMAL,
	@b DECIMAL,
	@c DECIMAL OUTPUT

)AS 
BEGIN 
	BEGIN TRY 
		SET @c = @a + @b;
	END TRY 

	BEGIN CATCH
        SELECT  
            ERROR_NUMBER() AS ErrorNumber  
            ,ERROR_SEVERITY() AS ErrorSeverity  
            ,ERROR_STATE() AS ErrorState  
            ,ERROR_PROCEDURE() AS ErrorProcedure  
            ,ERROR_LINE() AS ErrorLine  
            ,ERROR_MESSAGE() AS ErrorMessage;  
    END CATCH

END; 
GO 

DECLARE @r DECIMAL;
EXEC usp_add 10,20, @r OUTPUT 
PRINT @r;

ALTER PROCEDURE sp_sub(
	@a DECIMAL,
	@b DECIMAL
) AS

BEGIN 
	BEGIN TRY
	DECLARE @c DECIMAL;
	SET @c = @a - @b;
	END TRY 

	BEGIN CATCH 
	SELECT  
            ERROR_NUMBER() AS ErrorNumber  
            ,ERROR_SEVERITY() AS ErrorSeverity  
            ,ERROR_STATE() AS ErrorState  
            ,ERROR_PROCEDURE() AS ErrorProcedure  
            ,ERROR_LINE() AS ErrorLine  
            ,ERROR_MESSAGE() AS ErrorMessage;  
	END CATCH 
END;
GO 


EXEC sp_sub 10,10;

