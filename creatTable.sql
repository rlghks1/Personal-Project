CREATE TABLE googleprotein (
    productId VARCHAR(255) NOT NULL,
    productName VARCHAR(255),
    price INTEGER, 
    productDetails VARCHAR(255), 
    description VARCHAR(255), 
    merchantName VARCHAR(255),
    brand VARCHAR(255),
    PRIMARY KEY (productId)
);

UPDATE googleprotein
SET price = (SELECT SUBSTRING_INDEX(price, ' +', 1)*1.1)
where price like '%+%';
