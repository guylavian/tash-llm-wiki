---
title: "Chapter 10. Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-deploy-keycloak-kubernetes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/deploy-keycloak-kubernetes-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 10. Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 10. Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator
This guide describes advanced Red Hat build of Keycloak configurations for Kubernetes which are load tested and will recover from single Pod failures.
These instructions are intended for use with the setup described in the Concepts for multi-site deployments chapter. Use it together with the other building blocks outlined in the Building blocks multi-site deployments chapter.
10.1. Prerequisites
- OpenShift or Kubernetes cluster running.
- Understanding of a Basic Red Hat build of Keycloak deployment of Red Hat build of Keycloak with the Red Hat build of Keycloak Operator.
- Aurora AWS database deployed using the Deploy AWS Aurora in multiple availability zones chapter.
- Data Grid server deployed using the Deploy Data Grid for HA with the Data Grid Operator chapter.
10.2. Procedure
- Determine the sizing of the deployment using the Concepts for sizing CPU and memory resources chapter.
- Install the Red Hat build of Keycloak Operator as described in the Red Hat build of Keycloak Operator installation chapter.
- Notice the configuration file below contains options relevant for connecting to the Aurora database from Deploy AWS Aurora in multiple availability zones
- Notice the configuration file below options relevant for connecting to the Data Grid server from Deploy Data Grid for HA with the Data Grid Operator
- Build a custom Red Hat build of Keycloak image which is prepared for usage with the Amazon Aurora PostgreSQL database.
Deploy the Red Hat build of Keycloak CR with the following values with the resource requests and limits calculated in the first step:
apiVersion: k8s.keycloak.org/v2alpha1 kind: Keycloak metadata: labels: app: keycloak name: keycloak namespace: keycloak spec: hostname: hostname: <KEYCLOAK_URL_HERE> resources: requests: cpu: "2" memory: "1250M" limits: cpu: "6" memory: "2250M" db: vendor: postgres url: jdbc:aws-wrapper:postgresql://<AWS_AURORA_URL_HERE>:5432/keycloak poolMinSize: 30
1 poolInitialSize: 30 poolMaxSize: 30 usernameSecret: name: keycloak-db-secret key: username passwordSecret: name: keycloak-db-secret key: password image: <KEYCLOAK_IMAGE_HERE>
2 startOptimized: false
3 features: enabled: - multi-site
4 transaction: xaEnabled: false
5 additionalOptions: - name: http-max-queued-requests value: "1000" - name: log-console-output value: json - name: metrics-enabled
6 value: 'true' - name: http-pool-max-threads
7 value: "66" - name: cache-remote-host value: "infinispan.keycloak.svc" - name: cache-remote-port value: "11222" - name: cache-remote-username secret: name: remote-store-secret key: username - name: cache-remote-password secret: name: remote-store-secret key: password - name: spi-connections-infinispan-quarkus-site-name value: keycloak - name: db-driver value: software.amazon.jdbc.Driver http: tlsSecret: keycloak-tls-secret instances: 3
- 1
- The database connection pool initial, max and min size should be identical to allow statement caching for the database. Adjust this number to meet the needs of your system. As most requests will not touch the database due to the Red Hat build of Keycloak embedded cache, this change can server several hundreds of requests per second. See the Concepts for database connection pools chapter for details.
- 2 3
- Specify the URL to your custom Red Hat build of Keycloak image. If your image is optimized, set the
startOptimized
flag totrue
. - 4
- Enable additional features for multi-site support like the loadbalancer probe
/lb-check
. - 5
- XA transactions are not supported by the Amazon Web Services JDBC Driver.
- 6
- To be able to analyze the system under load, enable the metrics endpoint. The disadvantage of the setting is that the metrics will be available at the external Red Hat build of Keycloak endpoint, so you must add a filter so that the endpoint is not available from the outside. Use a reverse proxy in front of Red Hat build of Keycloak to filter out those URLs.
- 7
- You might consider limiting the number of Red Hat build of Keycloak threads further because multiple concurrent threads will lead to throttling by Kubernetes once the requested CPU limit is reached. See the Concepts for configuring thread pools chapter for details.
10.3. Verifying the deployment
Confirm that the Red Hat build of Keycloak deployment is ready.
oc wait --for=condition=Ready keycloaks.k8s.keycloak.org/keycloak
oc wait --for=condition=RollingUpdate=False keycloaks.k8s.keycloak.org/keycloak
10.4. Optional: Load shedding
To enable load shedding, limit the number of queued requests.
Load shedding with max queued http requests
spec:
additionalOptions:
- name: http-max-queued-requests
value: "1000"
All exceeding requests are served with an HTTP 503. See the Concepts for configuring thread pools chapter about load shedding for details.
10.5. Optional: Disable sticky sessions
When running on OpenShift and the default passthrough Ingress setup as provided by the Red Hat build of Keycloak Operator, the load balancing done by HAProxy is done by using sticky sessions based on the IP address of the source. When running load tests, or when having a reverse proxy in front of HAProxy, you might want to disable this setup to avoid receiving all requests on a single Red Hat build of Keycloak Pod.
Add the following supplementary configuration under the spec
in the Red Hat build of Keycloak Custom Resource to disable sticky sessions.
spec:
ingress:
enabled: true
annotations:
# When running load tests, disable sticky sessions on the OpenShift HAProxy router
# to avoid receiving all requests on a single Red Hat build of Keycloak Pod.
haproxy.router.openshift.io/balance: roundrobin
haproxy.router.openshift.io/disable_cookies: 'true'
