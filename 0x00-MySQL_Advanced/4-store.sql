-- A script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Trigger implimentation
DELIMITER //

CREATE TRIGGER update_items_after_order
AFTER INSERT ON orders
FOR EACH ROW 
BEGIN 
    UPDATE items 
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;