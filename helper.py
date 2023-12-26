# helper.py

from google.cloud import storage

class GCP_helper:
    def __init__(self, project_id, bucket_name):
        self.project_id = project_id
        self.bucket_name = bucket_name
        self.client = storage.Client(project=project_id)

    def download_FILE_CLOUDSTORAGE(self, source_blob_name, destination_file_name):
        """Downloads a blob from the bucket."""
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)

        print(f"File {source_blob_name} downloaded to {destination_file_name}.")

    def upload_File_Cloud_Storage(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Example usage:
# gcp_helper = GCP_helper("your-project-id", "your-bucket-name")
# gcp_helper.download_FILE_CLOUDSTORAGE("source_blob_name", "destination_file_name")
# gcp_helper.upload_File_Cloud_Storage("source_file_name", "destination_blob_name")
