from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] - %(message)s')
logger = logging.getLogger(__name__)

# Database configurations
target_db_username = "postgres"
target_db_password = "database-new"
target_db_host = "database-new.chcw6o82icob.us-east-2.rds.amazonaws.com"
target_db_name = "database-new"

# Create SQLAlchemy engine for the target database
target_engine = create_engine(f'postgresql+psycopg2://{target_db_username}:{target_db_password}@{target_db_host}/{target_db_name}?connect_timeout=600')

# Create metadata object for the target database
target_metadata = MetaData()

# Reflect existing tables in the target database
target_metadata.reflect(bind=target_engine)

# Table reference for the target table
target_table = target_metadata.tables['finmodeling_financial_ratios_new']

try:
    # Open a session for the target database
    with sessionmaker(bind=target_engine)() as target_session:
        print("Session opened successfully.")

        print("Retrieving all data from the target table...")

        # Retrieve all data from the target table
        query = select(target_table)
        result = target_session.execute(query)

        '''print("Printing the retrieved data:")
        for row in result:
            print(row)'''

        logger.info("Data retrieval completed successfully.")

except SQLAlchemyError as e:
    logger.error(f"An error occurred during data retrieval: {str(e)}")
    print("An error occurred during data retrieval.")

finally:
    print("Closing the database connection...")
    # Close the database connection
    target_engine.dispose()
    print("Database connection closed.")

query = "SELECT * FROM finmodeling_financial_ratios_new"
db_url = "postgresql://postgres:crossvalidation@database-1.c0rz9kyyn4jp.us-east-2.rds.amazonaws.com:5432/database-1"
engine = create_engine(db_url)
df = pd.read_sql_query(query, engine)
df.head(10)
df.to_csv('data.csv', index=False)




