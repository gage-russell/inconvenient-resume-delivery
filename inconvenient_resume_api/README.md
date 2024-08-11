# inconvenient-resume/inconvenient-resume-app

## Description
This is a fastapi API that supports:
* authentication via OAuth2
* retrieving user details
* retrieving PDF resume (hardcoded my resume, but easily updated to support per user resume with remote storage)
* database migrations managed via alembic

## Deployment
See [Dockerfile](./Dockerfile).
Follow instructions from [main README](../README.md) to start kind cluster and local container registry then:
1. docker build -t inconvenient-resume-api:latest ./inconvenient_resume_api
2. docker tag inconvenient-resume-api:latest localhost:5001/inconvenient-resume-api:latest
3. docker push localhost:5001/inconvenient-resume-api:latest

## Debugging
VS Code launch instructions for debugging are included in [.vscode](./.vscode).
