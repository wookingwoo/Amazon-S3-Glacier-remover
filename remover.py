import boto3

from data import data


def delete_all_archives(vault_name, region_name):
    glacier = boto3.client('glacier', region_name=region_name)

    try:
        response = glacier.list_jobs(vaultName=vault_name)
        print("response:", response)
        jobs = response['JobList']
        print("jobs:", jobs)

        for job in jobs:
            if job['StatusCode'] == 'InProgress':
                print("There is an ongoing job. Please wait for it to complete.")
                return

        response = glacier.list_multipart_uploads(vaultName=vault_name)
        uploads = response['UploadsList']

        if uploads:
            print("There are ongoing multipart uploads. Please wait for them to complete.")
            return

        response = glacier.list_parts(vaultName=vault_name)
        parts = response['Parts']

        if parts:
            print("There are ongoing incomplete multipart upload parts. Please wait for them to complete.")
            return

        response = glacier.list_jobs(vaultName=vault_name, completed=True)
        completed_jobs = response['JobList']

        for job in completed_jobs:
            if job['Action'] != 'ArchiveRetrieval':
                print("There are completed jobs other than ArchiveRetrieval. Please make sure all jobs are cleared.")
                return

            response = glacier.delete_archive(vaultName=vault_name, archiveId=job['ArchiveId'])
            print(f"Deleting archive: {job['ArchiveId']}")

        print("All archives have been deleted.")

    except glacier.exceptions.ResourceNotFoundException:
        print("Vault not found.")
    except Exception as e:
        print("An error occurred: ", str(e))


# Vault를 비울 Glacier Vault의 이름과 리전을 지정합니다.
vault_name = data.vault_name2
region_name = data.region_name  # 예: 'us-west-2'

delete_all_archives(vault_name, region_name)
