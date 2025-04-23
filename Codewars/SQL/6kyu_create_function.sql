CREATE FUNCTION agecalculator (age DATE)
RETURNS INT
LANGUAGE plpgsql
AS
$$
DECLARE actage INT;
BEGIN
  actage = (DATE_PART('year', CURRENT_DATE::date) - DATE_PART('year', age::date)) * 12 +
  (DATE_PART('month', CURRENT_DATE::date) - DATE_PART('month', age::date));
  RETURN actage/12;
  
END;
$$


CREATE FUNCTION agecalculator(age DATE) RETURNS INTEGER AS $$
BEGIN
    return date_part('year', AGE(age));
END 
$$ LANGUAGE plpgsql;