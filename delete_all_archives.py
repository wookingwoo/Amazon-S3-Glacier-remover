import boto3
from data import data


def delete_all_archives(vault_name, region_name, archive_ids):
    client = boto3.client('glacier', region_name=region_name)

    for archive_id in archive_ids:
        try:
            response = client.delete_archive(
                vaultName=vault_name,
                archiveId=archive_id
            )
            print(f"Deleted archive {archive_id}")
        except Exception as e:
            print(f"Failed to delete archive {archive_id}. Reason: {str(e)}")


# List of your archive ids. You need to fill this.
archive_ids = data.archive_ids1  # 예: ["your_archive_id_1", "your_archive_id_2", "your_archive_id_3"]

vault_name = data.vault_name1
region_name = data.region_name  # 예: 'us-west-2'

# Call the function
delete_all_archives(vault_name, region_name, archive_ids)
