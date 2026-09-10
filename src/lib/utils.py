import json
from pyspark.sql.types import StructType

def table_exists(spark, catalog, database, tablename):
    count = (spark.sql(f"show tables from {catalog}.{database}")
                  .filter(f'database = "{database}" and tableName = "{tablename}"')
                  .count())
    return count == 1

def import_schema(tablename):
    with open(f"../schemas/{tablename}.json", "r") as f:
        schema_json = json.load(f)
    return StructType.fromJson(schema_json)