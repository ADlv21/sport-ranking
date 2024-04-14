.PHONY: build-client build-server build-service start-client start-server start-service stop-client stop-server stop-service clean-client clean-server clean-service

# Set the names and directories for each application
CLIENT_NAME = my-client-app
CLIENT_DIR = ./client
SERVER_NAME = my-server-app
SERVER_DIR = ./server
SERVICE_NAME = my-service-app
SERVICE_DIR = ./service

# Set the environment variables for each application
export CLIENT_ENV = production
export SERVER_ENV = production
export SERVICE_ENV = production
export CLIENT_PORT = 3000
export SERVER_PORT = 5000
export SERVICE_PORT = 5001

build-client:
	cd $(CLIENT_DIR) && npm install
	cd $(CLIENT_DIR) && npm run build

build-server:
	cd $(SERVER_DIR) && pip install -r requirements.txt

build-service:
	cd $(SERVICE_DIR) && pip install -r requirements.txt

start-client:
	cd $(CLIENT_DIR) && npm start

start-server:
	cd $(SERVER_DIR) && python app.py

start-service:
	cd $(SERVICE_DIR) && python app.py

stop-client:
	@if [ -f $(CLIENT_DIR)/app.pid ]; then \
		kill `cat $(CLIENT_DIR)/app.pid`; \
		rm $(CLIENT_DIR)/app.pid; \
	else \
		echo "$(CLIENT_NAME) is not running."; \
	fi

stop-server:
	@if [ -f $(SERVER_DIR)/app.pid ]; then \
		kill `cat $(SERVER_DIR)/app.pid`; \
		rm $(SERVER_DIR)/app.pid; \
	else \
		echo "$(SERVER_NAME) is not running."; \
	fi

stop-service:
	@if [ -f $(SERVICE_DIR)/app.pid ]; then \
		kill `cat $(SERVICE_DIR)/app.pid`; \
		rm $(SERVICE_DIR)/app.pid; \
	else \
		echo "$(SERVICE_NAME) is not running."; \
	fi

clean-client:
	cd $(CLIENT_DIR) && rm -rf node_modules
	cd $(CLIENT_DIR) && rm -rf .next

clean-server:
	cd $(SERVER_DIR) && rm -rf venv

clean-service:
	cd $(SERVICE_DIR) && rm -rf venv