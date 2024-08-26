import googleapiclient.discovery
from googleapiclient.errors import HttpError
from .utils import handle_api_error

class CommentAPI:
    def __init__(self, client):
        self.client = client

    def list_comments(self, case_id):
        """지정된 지원 케이스의 댓글 목록을 가져옵니다."""

        try:
            parent = f"projects/{self.client.project_id}/cases/{case_id}"
            request = self.client.service.cases().comments().list(parent=parent)
            response = request.execute()

            # 필요한 경우 응답 데이터를 가공하여 반환
            return response.get('comments', [])

        except HttpError as e:
            handle_api_error(e)

    def create_comment(self, case_id, body):
        """지정된 지원 케이스에 새 댓글을 작성합니다."""

        try:
            parent = f"projects/{self.client.project_id}/cases/{case_id}"
            comment = {
                'body': body
            }
            request = self.client.service.cases().comments().create(parent=parent, body=comment)
            response = request.execute()

            # 필요한 경우 응답 데이터를 가공하여 반환
            return response

        except HttpError as e:
            handle_api_error(e)