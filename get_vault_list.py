import boto3

from data import data

# Boto3 클라이언트 생성
client = boto3.client('glacier', region_name=data.region_name)

# 아카이브 조회
response = client.list_vaults()

print("response:", response)

# 조회 결과 출력
for vault in response['VaultList']:
    print('Vault Name:', vault['VaultName'])
    print('Number of Archives:', vault['NumberOfArchives'])
    print('Creation Date:', vault['CreationDate'])
    print('ARN:', vault['VaultARN'])
    print('---')
