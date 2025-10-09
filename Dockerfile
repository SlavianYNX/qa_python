FROM python:3.13
COPY requirements.txt .
COPY tests.py .
COPY main.py .
RUN mkdir allure-results allure-report
RUN pip install allure-pytest
RUN pip install pytest
RUN pip install -r requirements.txt
CMD ["pytest", "tests.py", "--alluredir=allure-results"]