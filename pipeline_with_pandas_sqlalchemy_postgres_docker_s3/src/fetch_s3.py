import os
from os import path
import boto3

s3 = boto3.client("s3", aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_KEY_ID'))

data_dir = path.dirname(path.dirname(path.abspath(__file__)))+"/data/"
bucket_name = "company-pipeline-bucket"

response = s3.list_objects(Bucket=bucket_name)

files = [obj["Key"] for obj in response["Contents"]]

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


printProgressBar(0, len(files), prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, file in enumerate(files):
    parts = file.split("/")
    if len(parts) == 2:
        os.makedirs(path.join(data_dir, parts[0]))
        with open(path.join(data_dir, file), 'wb') as f:
            s3.download_fileobj(bucket_name, file, f)
    printProgressBar(i + 1, len(files), prefix = 'Progress:', suffix = 'Complete', length = 50)


print("S3 Download Completed")
