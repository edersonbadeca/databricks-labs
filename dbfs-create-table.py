# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Overview
# MAGIC
# MAGIC This notebook will show you how to create and query a table or DataFrame that you uploaded to DBFS. [DBFS](https://docs.databricks.com/user-guide/dbfs-databricks-file-system.html) is a Databricks File System that allows you to store data for querying inside of Databricks. This notebook assumes that you have a file already inside of DBFS that you would like to read from.
# MAGIC
# MAGIC This notebook is written in **Python** so the default cell type is Python. However, you can use different languages by using the `%LANGUAGE` syntax. Python, Scala, SQL, and R are all supported.

# COMMAND ----------

dbutils.fs.rm('/user/hive/warehouse/data_csv', recurse=True)

# Para este procedimento funcionar o arquivo data.csv deve estar carregado no DBFS no endereço especificado na variável `file_location`
file_location = '/FileStore/tables/data.csv'
file_type = 'csv'
infer_schema = 'true'
first_row_is_header = 'true'
delimiter = ';'

df = spark\
    .read\
    .format(file_type)\
    .option('inferSchema', infer_schema)\
    .option('header', first_row_is_header)\
    .option('sep', delimiter)\
    .load(file_location)

table_name = 'data_csv'

df.write.format('parquet').saveAsTable(table_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC /* Query the created temp table in a SQL cell */
# MAGIC
# MAGIC select * from `data_csv`
