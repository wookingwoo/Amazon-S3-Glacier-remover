import json


def parse_archive_ids_from_json(file_path):
    # 파일 열기
    with open(file_path, 'r') as file:
        # JSON 데이터 로드
        data = json.load(file)

        # ArchiveId 추출
        archive_ids = [job['ArchiveId'] for job in data['ArchiveList']]

    return archive_ids


def get_archive_id_list(file_path):
    archive_ids = parse_archive_ids_from_json(file_path)
    print(archive_ids)
    return archive_ids


if __name__ == "__main__":
    file_path = './data/output_json/output01.json'
    get_archive_id_list(file_path)
