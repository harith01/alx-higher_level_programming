-- Convert db `hbtn_0c_0` to utf8mb4, collate utf8mb_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER SET = utf8mb4 COLLATE = utf8mb_unicode_ci
ALTER TABLE second_table CHANGE name VARCHAR(256) COLLATE = utf8mb_unicode_ci  
