import boto3

from data import config

# Boto3 클라이언트 생성
client = boto3.client('glacier', region_name=config.region_name)

# 아카이브 삭제
client.delete_archive(
    vaultName='your_vault_name',
    archiveId='your_archive_id'
)
