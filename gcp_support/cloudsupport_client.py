import googleapiclient.discovery

class CloudSupportClient:
    def __init__(self, project_id):
        self.project_id = project_id
        self.service = self._build_service()

    def _build_service(self):
        """Google Cloud Support API 서비스 객체를 생성합니다."""
        return googleapiclient.discovery.build('cloudsupport', 'v2')