#!/bin/bash

# Step 1: Data Preprocessing
echo "Starting data preprocessing..."
python src/data_preprocessing.py
if [ $? -ne 0 ]; then
    echo "Data preprocessing failed!"
    exit 1
fi
echo "Data preprocessing completed."

# Step 2: Model Training
echo "Starting model training..."
python src/model_training.py
if [ $? -ne 0 ]; then
    echo "Model training failed!"
    exit 1
fi
echo "Model training completed."

# Step 3: Model Evaluation
echo "Starting model evaluation..."
python src/model_evaluation.py
if [ $? -ne 0 ]; then
    echo "Model evaluation failed!"
    exit 1
fi
echo "Model evaluation completed."

echo "Pipeline execution completed successfully."