---
title: "Chapter 8. Visualizing activities in dashboards - Red Hat build of Keycloak 26.6 Observability Guide"
type: reference
domain: keycloak
slug: rhbk-26-6-grafana-dashboards
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/observability_guide/grafana-dashboards-
guide: observability_guide
version: 26.6
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Install the Red Hat build of Keycloak Grafana dashboards to visualize the metrics that capture the status and activities of your deployment. Red Hat build of Keycloak provides metrics to observe what is happening inside the deployment. To understand how metrics evolve over time, it is helpful to collect and visualize them in graphs. This guide provides instructions on how to visualize collected Re…"
---

# Chapter 8. Visualizing activities in dashboards - Red Hat build of Keycloak 26.6 Observability Guide

Chapter 8. Visualizing activities in dashboards
Install the Red Hat build of Keycloak Grafana dashboards to visualize the metrics that capture the status and activities of your deployment.
Red Hat build of Keycloak provides metrics to observe what is happening inside the deployment. To understand how metrics evolve over time, it is helpful to collect and visualize them in graphs.
This guide provides instructions on how to visualize collected Red Hat build of Keycloak metrics in a running Grafana instance.
8.1. Prerequisites
- Red Hat build of Keycloak metrics are enabled. Follow Gaining insights with metrics chapter for more details.
- Grafana instance is running and Red Hat build of Keycloak metrics are collected into a Prometheus instance.
-
For the HTTP request latency heatmaps to work, enable histograms for HTTP metrics by setting
http-metrics-histograms-enabled
totrue
.
8.2. Red Hat build of Keycloak Grafana dashboards
Grafana dashboards are distributed in the form of a JSON file that is imported into a Grafana instance. JSON definitions of Red Hat build of Keycloak Grafana dashboards are available in the keycloak/keycloak-grafana-dashboard GitHub repository.
Follow these steps to download JSON file definitions.
Identify the branch from
keycloak-grafana-dashboards
to use from the following table.Expand Red Hat build of Keycloak version keycloak-grafana-dashboards
branch/tag26.1 - 26.2
26.2.0
>= 26.3
main
Clone the GitHub repository
git clone -b BRANCH_FROM_STEP_1 https://github.com/keycloak/keycloak-grafana-dashboard.git
-
The dashboards are available in the directory
keycloak-grafana-dashboard/dashboards
.
The following sections describe the purpose of each dashboard.
8.2.1. Red Hat build of Keycloak troubleshooting dashboard
This dashboard is available in the JSON file: keycloak-troubleshooting-dashboard.json
.
On the top of the dashboard, graphs display the service level indicators as defined in Monitoring performance with Service Level Indicators. This dashboard can be also used while troubleshooting a Red Hat build of Keycloak deployment following the Troubleshooting using metrics chapter, for example, when SLI graphs do not show expected results.
Figure 8.1. Troubleshooting dashboard
8.2.2. Keycloak capacity planning dashboard
This dashboard is available in the JSON file: keycloak-capacity-planning-dashboard.json
.
This dashboard shows metrics that are important when estimating the load handled by a Red Hat build of Keycloak deployment. For example, it shows the number of password validations or login flows performed by Red Hat build of Keycloak. For more detail on these metrics, see the chapter Self-provided metrics.
Red Hat build of Keycloak event metrics must be enabled for this dashboard to work correctly. To enable them, see the chapter Monitoring user activities with event metrics.
Figure 8.2. Capacity planning dashboard
8.3. Import a dashboard
- Open the dashboard page from the left Grafana menu.
- Click New and Import.
- Click Upload dashboard JSON file and select the JSON file of the dashboard you want to import.
- Pick your Prometheus datasource.
- Click Import.
The Grafana dashboards have labels inserted by Kubernetes. It is possible to use the dashboards with bare-metal deployments by adding the missing labels in the Prometheus configuration file, as shown below.
Prometheus Scrape Configuration
scrape_configs:
# The job name is added as a label `job=<job_name>` to any time series scraped from this config.
- job_name: "keycloak-service"
static_configs:
- targets: ["localhost:9000", "localhost:9001", "localhost:9002"]
labels:
namespace: 'keycloak'
container: 'keycloak'
relabel_configs:
- source_labels: [__address__]
target_label: pod
8.4. Export a dashboard
Exporting a dashboard to JSON format may be useful. For example, you may want to suggest a change in our dashboard repository.
- Open a dashboard you would like to export.
- Click share in the top left corner next to the dashboard name.
- Click the Export tab.
- Enable Export for sharing externally.
- Click either Save to file or View JSON and Copy to Clipboard according to where you want to store the resulting JSON.
8.5. Further reading
Continue reading on how to connect traces to dashboard in the Analyzing outliers and errors with exemplars chapter.
