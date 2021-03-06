
#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# cloud_upload.py
#
# Cloud Providers Storage API
#
#-------------------------------------------------------------------------------

import requests, os
from google.cloud import storage
from azure.storage.blob import BlockBlobService
import boto3

def upload_gcp(gcp_bucket, filename):
    print("[COMAE] Uploading to GCP bucket " + gcp_bucket)
    blobpath = os.path.basename(filename)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(gcp_bucket)
    blob = bucket.blob(blobpath)
    blob.upload_from_filename(filename)

def upload_az(az_account_name, az_account_key, az_container, filename):
    print("[COMAE] Uploading to Azure container " + az_container)
    blobpath = os.path.basename(filename)
    block_blob_service = BlockBlobService(account_name=az_account_name, account_key=az_account_key)
    block_blob_service.create_container(az_container)
    block_blob_service.create_blob_from_path(az_container, blobpath, filename)

def upload_s3(s3_access_id, s3_access_secret, bucket, filename):
    print("[COMAE] Uploading to S3 bucket " + bucket)
    blobpath = os.path.basename(filename)
    s3 = boto3.client('s3', aws_access_key_id=s3_access_id, aws_secret_access_key=s3_access_secret)
    s3.upload_file(filename, bucket, blobpath)