## Simple python scripts to fetch and push csv files from and to S3

This project is for an assignment that required accessing csv files that are stored in an Amazon S3 bucket for a data pipeline.

### Requirements

- Python 3.7+
- AWS S3-capable User

### Instructions

1.  Create a bucket named `company-pipeline-bucket` on your AWS account and set up a user with the right permissions to read and write to the bucket. You may need to contact your administrator for this.

2.  Proceed to clone the repo locally and open the root directory in a terminal window that has access to your python installation.

3.  Set the following environment variables for your operating system

    ```
    AWS_ACCESS_KEY_ID =
    AWS_SECRET_KEY_ID =
    ```

4.  Run `python -m pip install -r requirements.txt` to install the project dependencies. You may want to create and activate a python virtual environment to isolate the dependencies.

5.  You can now run either of the scripts:

    - For the push script (`push_s3.py`), you need to create a directory named `data` in the project root. Each company must have a seperate directory inside the `data` directory, and then CSV files relating to the company are placed inside that company's directory. Once all the data is organized, run the script with

      ```
      python push_s3.py
      ```

      It should print a success message on completion.

    - The fetch script does not require any directory setups. Simply run the script with

      ```
      python fetch_s3.py
      ```

      On success, it should also print a message.

### Disclaimer

The scripts are not general purpose for fetching and pushing files to S3. They are very project specific, and hence the structure and configurations of the project dependencies are very specific. You may adapt the code to suit your needs but do not use this project as a drop-in solution for to your problem unless your requirements perfectly match those of the project it was created for.
