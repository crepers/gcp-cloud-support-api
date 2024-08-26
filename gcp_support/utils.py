def handle_api_error(error):
    """Google API 호출 중 발생한 오류를 처리하고 메시지를 출력합니다."""

    error_details = error.content.decode('utf-8')
    print(f"API 호출 중 오류 발생: {error_details}")