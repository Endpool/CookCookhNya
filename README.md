# Server Configuration Branch

Welcome to the `server` branch of the CookCookhNya repository! This branch is specifically designed to store configuration files for deploying and managing **production** and **stage** environments on the server. Using Docker Compose, these configurations orchestrate services like databases, backend, frontend, and monitoring tools to ensure smooth operation of the application.

---

## 📂 Directory Structure

The branch is organized into two primary directories:

- **`prod`**: Configuration files for the **production environment**, including advanced monitoring and logging setups.
- **`stage`**: Configuration files for the **stage environment**, a lightweight setup for testing and development.

Here's the breakdown:

```bash
.
├── prod
│   ├── compose-prod.yaml       # Docker Compose for production
│   ├── prometheus.yml          # Prometheus configuration
│   ├── promtail-config.yaml    # Promtail configuration for log scraping
│   └── .env                    # Environment variables for production
└── stage
    ├── compose-stage.yaml      # Docker Compose for stage
    └── .env                    # Environment variables for stage
```

---

## 🌐 Production Environment (`prod`)

The production environment is fully equipped with a robust set of services for running the application including monitoring and logging tools.

### Files

- **`compose-prod.yaml`**  
  Defines the production services:
  - **db**: PostgreSQL database (v17) with persistent storage in the `db-data` volume.
  - **backend**: The CookCookhNya backend service, exposed on port `5018`.
  - **frontend**: The CookCookhNya frontend service, exposed on port `8443`, with **webhook support** (see [Webhook Configuration](#webhook-configuration-in-production)).
  - **loki**: Log aggregation service for centralized logging.
  - **promtail**: Collects container logs and sends them to Loki.
  - **prometheus**: Metrics monitoring service, exposed on port `9090`.
  - **cadvisor**: Container performance monitoring, exposed on port `8082`.
  - **postgres-exporter**: Exports PostgreSQL metrics to Prometheus.
  - **grafana**: Visualization dashboard for logs and metrics, accessible at `http://home.pasha1st.ru:5011`.

- **`promtail-config.yaml`**  
  Configures Promtail to scrape logs from `frontend`, `backend`, and `db` services using Docker service discovery. It processes logs with regex and JSON pipelines and forwards them to Loki.

- **`prometheus.yml`**  
  Configuration for Prometheus to scrape metrics from services `cadvisor`, `postgres-exporter`, and also from backend hanlder /metrics, that exposes custom metrics.

- **`.env`**  
  Stores environment variables such as image tags, bot token, database credentials, and webhook settings.

---

## 🛠️ Stage Environment (`stage`)

The stage environment is a simplified setup for testing and development, omitting the monitoring and logging stack present in production.

### Files

- **`compose-stage.yaml`**  
  Defines the stage services:
  - **db**: PostgreSQL database (v17) with persistent storage in the `db-data-stage` volume.
  - **backend**: The CookCookhNya backend service, exposed on port `8081`.
  - **frontend**: The CookCookhNya frontend service, running without webhook support.

- **`.env`**  
  Contains stage-specific environment variables, similar to production but tailored for testing.

---

## 🌟 Webhook Configuration in Production

A key feature of the production environment is the **webhook integration** in the `frontend` service, which is absent in the stage setup. This enables notifications about users actions from Telegram api to our frontend service, without the need to check for updates manually constantly:
  
User interacts with bot -> Telegram notificates our frontend service -> We process the update.

### Details

- **Configuration**: In `compose-prod.yaml`, the `frontend` service uses the `--webhook` command.
- **Environment Variables** (set in `.env`):
  - `WEBHOOK_PORT`: Port for the webhook (default: `8443`).
  - `WEBHOOK_HOST`: Our webhook endpoint on production server
  - `WEBHOOK_SECRET`: Secret key for securing webhook requests.

---

