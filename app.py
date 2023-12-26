# app.py

import argparse
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

def main():
    parser = argparse.ArgumentParser(description="Upload and download files from Google Cloud Storage")
    parser.add_argument("filename", help="Name of the file to upload/download")
    parser.add_argument("bucket_name", help="Name of the Google Cloud Storage bucket")
    parser.add_argument("action", choices=["upload", "download"], help="Action to perform: upload or download")

    args = parser.parse_args()

    if args.action == "upload":
        upload_file_cloudStorage(args.filename, args.bucket_name)
    elif args.action == "download":
        download_file_cloudStorage(args.filename, args.bucket_name)

if __name__ == "__main__":
    main()
