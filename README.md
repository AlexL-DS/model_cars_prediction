# model_cars_prediction
This is a project for a Docker, including files with learning model (pipeline), making prediction (predict), DAG-file (hw_dag), and directory data
This model made to using in Docker/Airflow, but possible local using. The model train on traindata, search the best model (LR, RFC, SVC), and make a predict for testdata to dataframe in 'data/predict'
If you wanna learning model on your data, you schould reload your file as file 'homework' in directory 'data/train'. The content of file must be strongly correspond by columns
If you wanna receive a predict for your data, you should add files in directory 'data/test'. Files must be single-row, filenames you need add or replace in code 'predict', variable 'test_files'
