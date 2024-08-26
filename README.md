This project contains sample code for retrieving a list of support cases using the GCP Support API. To successfully use the API, the following prerequisites must be met:

### 1. Verify your GCP Support Plan

* The GCP Support API is only available with Enhanced Support or Premium Support plans. Verify your current plan and upgrade if necessary.

### 2. Enable the Cloud Support API

* In the GCP Console, navigate to APIs & Services > Library, search for "Cloud Support API" and enable it.

### 3. Set up IAM Permissions

* Grant the `roles/cloudsupport.viewer` role or higher to the user or service account that will be making API calls. If needed, you can also grant the `roles/cloudsupport.user` role for additional permissions to create and modify support cases.

### 4. Set up a Python Virtual Environment

* Create and activate a Python virtual environment using the following commands:

   ```bash
   python3 -m venv .venv 
   source .venv/bin/activate
   ```

### 5. Install Required Libraries

* Install the necessary libraries in the activated virtual environment:

   ```bash
   pip3 install google-api-python-client
   ```

### 6. Configure your Cloud Shell Environment (Optional)

* If you are working in Cloud Shell, ensure that it is running in the correct project and change the project if necessary.

### 7. Start Using the API

* Once the prerequisites are met, you can use the provided sample code to retrieve a list of support cases using the GCP Support API.

   ```bash
    > python3 cloudsupport.py
    usage: cloudsupport.py [-h] [-p PROJECT_ID] [-c CASE_ID]

    Google Cloud Support API를 사용하여 지원 케이스 정보를 가져옵니다.

    options:
        -h, --help            show this help message and exit
        -p PROJECT_ID, --project_id PROJECT_ID
                                    프로젝트 ID
        -c CASE_ID, --case_id CASE_ID
                                케이스 ID (옵션)

            사용 예시:
            * 모든 지원 케이스 목록 가져오기: python cloudsupport.py -p my-project-id
            * 특정 지원 케이스 상세 정보 및 관련 정보 가져오기: python cloudsupport.py -p my-project-id -c 12345678
   ```
