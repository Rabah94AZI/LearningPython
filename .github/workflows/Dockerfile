
FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir pytest pytest-cov numpy

COPY trick/ ./trick/

CMD ["python", "-m", "pytest", "trick/tests", "--cov=trick", "--cov-report=term-missing"]
