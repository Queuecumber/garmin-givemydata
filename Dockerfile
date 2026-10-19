FROM python:3.12-slim

# Chromium is here so the selenium-based login/sync can run headless in-pod
# (one-off or CronJob). The MCP server itself never touches the browser.
RUN apt-get update && apt-get install -y --no-install-recommends \
      chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir /app \
 && pip install --no-cache-dir 'mcp[cli]>=1.8,<2'

RUN mkdir -p /data

ENV GARMIN_DATA_DIR=/data \
    MCP_TRANSPORT=streamable-http \
    MCP_HOST=0.0.0.0 \
    MCP_PORT=8000 \
    PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["python", "run_mcp_http.py"]
