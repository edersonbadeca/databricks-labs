# Databricks notebook source
install.packages("mice")

# COMMAND ----------

library(mice)

# COMMAND ----------

# DBTITLE 1,O datagrame nhanes é um dataframe de dados de saude que contém valores ausentes
data(nhanes)

# COMMAND ----------

head>(nhanes)

# COMMAND ----------

# DBTITLE 1,Imputa valores faltantes utilizando a técnica de matching preditivo de médias. É uma escolha comum para variáveis contínuas.
imputed_method <- "pmm" # Imputa valores faltantes utilizando a técnica de matching preditivo de médias. É uma escolha comum para variáveis contínuas.


# COMMAND ----------

nhanes_imputed <- mice(nhanes, method=imputed_method)
completed_data <- complete(nhanes_imputed)
print(completed_data)
