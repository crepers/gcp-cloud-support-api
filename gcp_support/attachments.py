import googleapiclient.discovery
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from .utils import handle_api_error

class AttachmentAPI:
    def __init__(self, client):
        self.client = client

    def list_attachments(self, case_id):
        """지정된 지원 케이스의 첨부 파일 목록을 가져옵니다."""

        try:
            parent = f"projects/{self.client.project_id}/cases/{case_id}"
            request = self.client.service.cases().attachments().list(parent=parent)
            response = request.execute()

            # 필요한 경우 응답 데이터를 가공하여 반환
            return response.get('attachments', [])

        except HttpError as e:
            handle_api_error(e)

    def download_attachment(self, attachment_id, filename):
        """지정된 첨부 파일을 다운로드합니다."""

        try:
            name = f"projects/{self.client.project_id}/cases/attachments/{attachment_id}"
            request = self.client.service.cases().attachments().download(name=name)
            with open(filename, 'wb') as f:
                downloader = MediaIoBaseDownload(f, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()

            print(f"첨부 파일 '{filename}' 다운로드 완료")

        except HttpError as e:
            handle_api_error(e)

    def upload_attachment(self, case_id, filename):
        """지정된 지원 케이스에 첨부 파일을 업로드합니다."""

        try:
            parent = f"projects/{self.client.project_id}/cases/{case_id}"
            media = MediaFileUpload(filename, resumable=True)
            request = self.client.service.cases().attachments().upload(parent=parent, media_body=media)

            response = None
            while response is None:
                status, response = request.next_chunk()

            # 필요한 경우 응답 데이터를 가공하여 반환
            return response

        except HttpError as e:
            handle_api_error(e)