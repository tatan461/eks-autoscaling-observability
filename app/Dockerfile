FROM python:3.11-slim AS builder

WORKDIR /app

# Crear virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias de la app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Stage final: imagen mínima
FROM python:3.11-slim

WORKDIR /app

# Usar solo el venv creado, sin site-packages global
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /opt/venv /opt/venv

# Copiar solo el código de la aplicación
COPY src/ .

# Usuario no privilegiado
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]