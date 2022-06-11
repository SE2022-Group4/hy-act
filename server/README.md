
# HY-ACT-SERVER

Backend API Server for HY-ACT Service

Backed with Python3, Django 4

## Deployment

### Using Docker (Recommended)

HY-ACT-SERVER는 Docker를 기반으로 배포 환경이 최적화되었습니다.

도커 설치 후 해당 스크립트를 수행하여 서버를 실행할 수 있습니다.

```
$ docker build -t hy_act_server .
$ docker run -p 8080:8080 hy_act_server    
```

도커 컨테이너 실행시 서비스 사용에 필요한 데이터베이스 테이블 추가와 테스트를 위한 Fixture Data를 설정합니다.

이때 API 테스트를 위한 기본 사용자 계정 3개도 함께 추가됩니다.

기본 생성되는 사용자명은 `student_1`, `lecturer_1`, `admin_1` 이며 공통 비밀번호는 `Qoswlfdlsnrn` 입니다.  

## API Testing

API의 문서화는 `drf-spectacular` 라이브러리를 통해 Swagger 형식으로 자동 생성됩니다.

API Documentation은 서버 실행 후 해당 경로로 접속해 확인할 수 있습니다.

http://localhost:8000/api/v1/schema/swagger-ui/

## API Usage Guide

### Authentication

거의 모든 API의 사용을 위해서는 User Authentication이 필요합니다.

사용자 인증에는 Token Authentication 방식을 사용합니다.

사용자 토큰을 얻어오는 방식은 다음과 같습니다.

http://localhost:8000/api/v1/schema/swagger-ui/#/user/user_signin_create

Signin API를 통해 

## Contribution Guide
