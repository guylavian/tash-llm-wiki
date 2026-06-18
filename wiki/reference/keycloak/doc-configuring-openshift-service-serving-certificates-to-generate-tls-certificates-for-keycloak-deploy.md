---
title: "Appendix A. Configuring OpenShift service serving certificates to generate TLS certificates for Keycloak - Red Hat Trusted Artifact Signer 1.1 Deployment Guide"
type: reference
domain: keycloak
slug: doc-configuring-openshift-service-serving-certificates-to-generate-tls-certificates-for-keycloak-deploy
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_trusted_artifact_signer/1.1/html/deployment_guide/configuring-openshift-service-serving-certificates-to-generate-tls-certificates-for-keycloak_deploy
guide: deployment_guide
documentKind: "Documentation"
---

# Appendix A. Configuring OpenShift service serving certificates to generate TLS certificates for Keycloak - Red Hat Trusted Artifact Signer 1.1 Deployment Guide

Appendix A. Configuring OpenShift service serving certificates to generate TLS certificates for Keycloak
OpenShift’s service serving certificate can automate the generation and management of Transport Layer Security (TLS) certificates for use by Keycloak. Infrastructure components, such as the Ingress Controller, within an OpenShift cluster will trust these TLS certificates.
Prerequisites
- Red Hat OpenShift Container Platform version 4.13 or later.
- Installation of the RHBK operator.
-
Access to the OpenShift web console with the
cluster-admin
role.
Procedure
- In OpenShift web console, from the Administrator perspective, expand Home from the navigation menu, and click Projects.
-
Search for
keycloak
, and select thekeycloak-system
namespace. Create a new service.
- Click the + icon.
In the Import YAML text box, copy the example, and paste it into the text box.
Example
apiVersion: v1 kind: Service metadata: annotations: service.beta.openshift.io/serving-cert-secret-name: keycloak-tls labels: app: keycloak app.kubernetes.io/instance: keycloak name: keycloak-service-trusted namespace: keycloak-system spec: internalTrafficPolicy: Cluster ipFamilies: - IPv4 ipFamilyPolicy: SingleStack ports: - name: https port: 8443 selector: app: keycloak app.kubernetes.io/instance: keycloak
- Click the Create button.
- Expand Operators from the navigation menu, click Installed Operators, and click Keycloak Operator.
In the YAML view of the
Keycloak
resource, under thespec
section, add theingress
property:Example
spec: ... ingress: annotations: route.openshift.io/destination-ca-certificate-secret: keycloak-tls route.openshift.io/termination: reencrypt ...
By default, the Keycloak operator creates Ingress resources instead of routes. OpenShift automatically creates a route based on the Ingress definition.
Specify the name of the secret containing the TLS certificate, under the
spec
section:Example
spec: ... http: tlsSecret: keycloak-tls ...
Once Keycloak starts, OpenShift’s service serving certificate starts generating TLS certificates for Keycloak.
