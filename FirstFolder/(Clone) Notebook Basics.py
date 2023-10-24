# Databricks notebook source
# MAGIC %python
# MAGIC print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "This is from New Cell" myCol

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # This is test
# MAGIC ## Another Test
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **This is Bold**
# MAGIC *Italic* now

# COMMAND ----------

# MAGIC %md
# MAGIC pick
# MAGIC 1. First
# MAGIC 1. Second
# MAGIC 1. Third

# COMMAND ----------

# MAGIC %run ../Includes/Setup

# COMMAND ----------

print(Name)

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

dbutils.help()

# COMMAND ----------

display(dbutils.fs)

# COMMAND ----------

files = dbutils.fs.ls('.')
display(files)

# COMMAND ----------

type(files)

# COMMAND ----------


