import boto3
from tqdm import tqdm

import parsing_archiveid
from data import config


def delete_all_archives(vault_name, region_name, archive_ids):
    client = boto3.client('glacier', region_name=region_name)

    with tqdm(total=len(archive_ids), desc="Deleting archives") as pbar:
        for archive_id in archive_ids:
            try:
                response = client.delete_archive(
                    vaultName=vault_name,
                    archiveId=archive_id
                )
                pbar.set_postfix({"Deleted": archive_id})
            except Exception as e:
                pbar.set_postfix({"Failed": archive_id})
                pbar.write(f"Failed to delete archive {archive_id}. Reason: {str(e)}")
            finally:
                pbar.update(1)


# List of your archive ids. You need to fill this.
archive_ids = parsing_archiveid.get_archive_id_list(
    './data/output_json/output1.json')  # 예: ["your_archive_id_1", "your_archive_id_2", "your_archive_id_3"]

vault_name = config.vault_name1
region_name = config.region_name  # 예: 'us-west-2'

# Call the function
delete_all_archives(vault_name, region_name, archive_ids)
