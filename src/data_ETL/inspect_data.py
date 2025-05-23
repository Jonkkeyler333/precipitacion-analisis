import sys
sys.path.insert(0, '/home/hadoop/myenv/lib/python3.12/site-packages')

from pyspark.sql import SparkSession, functions
from pyspark.errors.exceptions.captured import AnalysisException

def inspect_data(spark,city,txt_output=None):
    hdfs_path=f'hdfs:///user/hadoop/data_project/{city}/'
    print(f"Reading data from: {hdfs_path} for city: {city}")
    df=spark.read.parquet(hdfs_path)
    print("Schema:")
    df.printSchema()
    print("Sample rows:")
    df.show(10)
    print("Count of records per month:")
    df.groupBy("month").count().orderBy("month").show()
    total_count=df.count()
    print(f"Total records: {total_count}")
    
if __name__ == "__main__":
    spark=SparkSession.builder.appName("Inspect Data").getOrCreate()
    capitales_departamentos = [
        'ARAUCA',        
        'SOLEDAD', 
        'CARTAGENA DE INDIAS',  
        'SOGAMOSO',          
        'MANIZALES',      
        'FLORENCIA',      
        'YOPAL',         
        'POPAYÁN',        
        'VALLEDUPAR',     
        'QUIBDÓ',         
        'MONTERÍA',       
        'BOGOTA D.C',    
        'NEIVA',          
        'RIOHACHA',       
        'SANTA MARTA',    
        'VILLAVICENCIO',  
        'PASTO',          
        'CÚCUTA',        
        'MOCOA',          
        'ARMENIA',        
        'PEREIRA',        
        'SAN ANDRÉS',     
        'SINCELEJO',      
        'IBAGUÉ',         
        'CALI',           
        'MITÚ',         
        'CUMARIBO',
        'SAN JOSÉ DEL GUAVIARE', 
        'BUCARAMANGA',
        'MEDELLÍN',
        'INÍRIDA' 
    ]
    for city in capitales_departamentos:
        try:
            print(f"Processing data for {city}")
            inspect_data(spark,city)
        except AnalysisException as e:
            print(f"The data not exists {city}: {e}")
    spark.stop()
    print("Data inspection completed.")
