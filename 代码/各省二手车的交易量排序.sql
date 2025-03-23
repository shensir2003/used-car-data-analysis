-- 查询各省份二手车交易总数排名，按降序排列
SELECT province_name, count
FROM province_rank_df
ORDER BY count DESC;
