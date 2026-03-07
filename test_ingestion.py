from rag.ingestion import DataIngestion

pipeline = DataIngestion("data/uploads/sample.pdf")

pipeline.run_pipeline()

print("Ingestion Completed")