.PHONY: lint_app,task_1,task_2,task_3,task_4,task_5

lint_app: ## Lint whole python app
	@echo "Run linters for the app and tests folders"
	flake8 .
	mypy .
	isort .
	black .
	@echo "Done"

task_1: ## Run Task 1
	@echo "Start executing Task 1"
	python scrapping_task/task1.py
	@echo "Task 1 finished"

task_2: ## Run Task 2
	@echo "Start executing Task 2"
	python scrapping_task/task2.py
	@echo "Task 2 finished"

task_3: ## Run Task 3
	@echo "Start executing Task 3"
	python scrapping_task/task3.py
	@echo "Task 3 finished"

task_4: ## Run Task 4
	@echo "Start executing Task 4"
	python scrapping_task/task4.py
	@echo "Task 4 finished"

task_5: ## Run Task 5
	@echo "Start executing Task 5"
	python scrapping_task/task5.py
	@echo "Task 5 finished"