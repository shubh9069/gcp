# app.py

from helper import GCP_helper

def upload_file_cloudStorage(filename, bucket_name):
    project_id = "your-project-id"
    gcp_helper = GCP_helper(project_id, bucket_name)
    destination_blob_name = filename  # You can modify this based on your requirements
    gcp_helper.upload_File_Cloud_Storage(filename, destination_blob_name)

def download_file_cloudStorage(filename, bucket_name):
    project_id = "your-project-id"
    gcp_helper = GCP_helper(project_id, bucket_name)
    source_blob_name = filename  # You can modify this based on your requirements
    destination_file_name = f"downloaded_{filename}"  # You can modify this based on your requirements
    gcp_helper.download_FILE_CLOUDSTORAGE(source_blob_name, destination_file_name)

if __name__ == "__main__":
    # Replace these with the actual values
    argfilename = "example.txt"
    argbucketName = "bkt-26dec-shubham-v2"

    upload_file_cloudStorage(argfilename, argbucketName)
    download_file_cloudStorage(argfilename, argbucketName)
