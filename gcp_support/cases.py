import googleapiclient.discovery
from googleapiclient.errors import HttpError
from .utils import handle_api_error

class CaseAPI:
    def __init__(self, client):
        self.client = client  # CloudSupportClient 인스턴스를 받아옴

    def list_cases(self):
        """프로젝트의 모든 지원 케이스 목록을 가져옵니다."""

        try:
            parent = f"projects/{self.client.project_id}"
            request = self.client.service.cases().list(parent=parent)
            response = request.execute()

            # 필요한 경우 응답 데이터를 가공하여 반환
            return response.get('cases', [])

        except HttpError as e:
            handle_api_error(e)

    def get_case(self, case_id):
        """특정 지원 케이스의 상세 정보를 가져옵니다."""

        try:
            name = f"projects/{self.client.project_id}/cases/{case_id}"
            request = self.client.service.cases().get(name=name)
            response = request.execute()

            # 필요한 경우 응답 데이터를 가공하여 반환
            return response

        except HttpError as e:
            handle_api_error(e)