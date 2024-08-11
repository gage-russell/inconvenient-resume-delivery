start-cluster:
	@echo "Starting kind cluster and local container registry"
	sh ./kind-with-registry.sh
	@echo "Ready to use kind cluster"

setup-ingress:
	@echo "Setting up ingress controller"
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	kubectl wait --namespace ingress-nginx \
	--for=condition=ready pod \
	--selector=app.kubernetes.io/component=controller \
	--timeout=90s
	@echo "Ingress controller setup"

build-api:
	@echo "Building API image"
	docker build -t inconvenient-resume-api:latest ./inconvenient_resume_api
	@echo "Tagging API image"
	docker tag inconvenient-resume-api:latest localhost:5001/inconvenient-resume-api:latest
	@echo "Pushing API image to local registry"
	docker push localhost:5001/inconvenient-resume-api:latest
	@echo "API image built and pushed"

build-app:
	@echo "Building APP image"
	docker build -t inconvenient-resume-app:latest ./inconvenient_resume_app
	@echo "Tagging APP image"
	docker tag inconvenient-resume-app:latest localhost:5001/inconvenient-resume-app:latest
	@echo "Pushing APP image to local registry"
	docker push localhost:5001/inconvenient-resume-app:latest
	@echo "APP image built and pushed"

deploy-umbrella-chart:
	@echo "Updating helm deps"
	cd ./charts/umbrella && helm dependency update
	@echo "Building helm deps"
	cd ./charts/umbrella && helm dependency build
	@echo "Deploying umbrella chart"
	cd ./charts/umbrella && helm upgrade --install umbrella . -f values.yaml

start-all: start-cluster build-api build-app deploy-umbrella-chart
	@echo "All services started"

destroy:
	@echo "Destroying kind cluster"
	kind delete cluster
	@echo "Kind cluster destroyed"
