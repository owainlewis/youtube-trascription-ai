env:
	@if [ ! -d ".env" ]; then \
		echo "Creating virtual environment"; \
		python3 -m venv .env; \
	fi
	@echo "Activating virtual environment"
	@. .env/bin/activate && pip install -r requirements.txt

clean:
	@rm -rf .env
	@echo "Cleaned virtual environment"

.PHONY: env clean
