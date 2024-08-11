# inconvenient-resume/inconvenient-resume-app

## Description
This is a streamlit app with:
* login page:
    * authenticates through API using username and password
    * stores JWT token in session_state
* user page:
    * fetches and displays user details
    * supports logging out via logout button
* resume page:
    * fetches and displays PDF resume

## Deployment
See [Dockerfile](./Dockerfile).
Follow instructions from [main README](../README.md) to start kind cluster and local container registry then:
1. docker build -t inconvenient-resume-app:latest ./inconvenient_resume_app
2. docker tag inconvenient-resume-app:latest localhost:5001/inconvenient-resume-app:latest
3. docker push localhost:5001/inconvenient-resume-app:latest

## Debugging
VS Code launch instructions for debugging are included in [.vscode](./.vscode).
