from enum import Enum

class FileUploadSessionTransport(str, Enum):
    HTTP_CHUNKED = "http-chunked"
    PRESIGNED_MULTIPART = "presigned-multipart"
    PRESIGNED_PUT = "presigned-put"

    def __str__(self) -> str:
        return str(self.value)
