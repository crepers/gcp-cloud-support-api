from .cases import CaseAPI
from .comments import CommentAPI
from .attachments import AttachmentAPI
from .cloudsupport_client import CloudSupportClient

class CloudSupportAPI:
    def __init__(self, project_id):
        self.client = CloudSupportClient(project_id)
        self.cases = CaseAPI(self.client)
        self.comments = CommentAPI(self.client)
        self.attachments = AttachmentAPI(self.client)