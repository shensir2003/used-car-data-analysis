-- 查询五年的保值率并输出最大值
SELECT brand, five_year_rate
FROM mean_value_df
WHERE five_year_rate IS NOT NULL
ORDER BY five_year_rate DESC
LIMIT 1;
-- 查询十年的保值率并输出最大值
SELECT brand, ten_year_rate
FROM mean_value_df
WHERE ten_year_rate IS NOT NULL
ORDER BY ten_year_rate DESC
LIMIT 1;
