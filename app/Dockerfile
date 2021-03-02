# Python image
FROM python:3.9.1-buster

# Install runtime libraries for Postgres connection
RUN apt-get update && apt-get install -y libpq-dev netcat

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy Pipfile[.lock]
COPY ./Pipfile* ./

# Copy scripts dir
COPY ./scripts/ ./scripts

# Install pipenv and packages
RUN pip install pipenv && \
    pipenv install --system --deploy --dev

# Copy everything else
COPY app .

# Run service
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
