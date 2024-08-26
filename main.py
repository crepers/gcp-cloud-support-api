import argparse
from gcp_support.cloudsupport_api import CloudSupportAPI
    
def main():
    # 커맨드 라인 인자 처리
    parser = argparse.ArgumentParser(
        description='Google Cloud Support API를 사용하여 지원 케이스 정보를 가져옵니다.',
        epilog='''
        사용 예시:
        * 모든 지원 케이스 목록 가져오기: python cloudsupport.py -p my-project-id
        * 특정 지원 케이스 상세 정보 및 관련 정보 가져오기: python cloudsupport.py -p my-project-id -c 12345678
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter  # epilog 서식 유지
    )

    # project_id 설정
    parser.add_argument('-p', '--project_id', help='프로젝트 ID') 

    # case_id 설정 
    parser.add_argument('-c', '--case_id', help='케이스 ID (옵션)') 
    args = parser.parse_args()

    # project_id 매개변수 없이 실행 시 도움말 출력
    if not args.project_id:
        print(parser.format_help())
        return
    
    api = CloudSupportAPI(args.project_id)

    if args.case_id:
        # 특정 지원 케이스 상세 정보 가져오기
        case = api.cases.get_case(args.case_id)
        if case:
            print("## 지원 케이스 상세 정보 ##")
            print(case)

        # 지원 케이스의 Comments 가져오기
        comments = api.comments.list_comments(args.case_id)
        if comments:
            print("\n## 지원 케이스 댓글 ##")
            print(comments)
        
        # 지원 케이스의 첨부파일 가져오기
        attachments = api.attachments.list_attachments(args.case_id)
        if attachments:
            print("\n## 지원 케이스 첨부 파일 ##")
            print(attachments)

    else:
        # 지원 케이스 목록 가져오기
        cases = api.cases.list_cases()
        if cases:
            print("## 지원 케이스 목록 ##")
            print(cases)


if __name__ == "__main__":
    main()