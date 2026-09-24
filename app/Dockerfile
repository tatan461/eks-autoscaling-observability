FROM python:3.11-slim AS builder

WORKDIR /app

# Crear virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Stage final: imagen mínima sin herramientas de build
FROM python:3.11-slim

WORKDIR /app

# Copiar solo el venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /opt/venv /opt/venv

# Eliminar pip, setuptools y wheel del runtime
RUN pip uninstall -y pip setuptools wheel

# Copiar código de la aplicación
COPY src/ .

# Usuario no privilegiado
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]