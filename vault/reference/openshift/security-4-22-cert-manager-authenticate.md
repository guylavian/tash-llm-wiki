---
title: "Authenticating the {cert-manager-operator}"
type: reference
domain: openshift
slug: security-4-22-cert-manager-authenticate
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/cert-manager-authenticate
version: 4.22
family: security
documentKind: "Documentation"
---

# Authenticating the {cert-manager-operator}

[id="cert-manager-authenticate"]
= Authenticating the {cert-manager-operator}

[role="_abstract"]
To enable the operator to manage components on your cloud provider, authenticate the {cert-manager-operator} by configuring cloud credentials. You can grant the Operator access to external services required for certificate issuance, such as DNS providers.

//  on AWS
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-authenticate.adoc

[id="cert-manager-configure-cloud-credentials-aws-non-sts_{context}"]
= Authenticating on AWS

[role="_abstract"]
To securely access AWS resources from your applications, authenticate your workloads on AWS by using the {cert-manager-operator}.

.Prerequisites

* You have installed version 1.11.1 or later of the {cert-manager-operator}.
* You have configured the Cloud Credential Operator to operate in _mint_ or _passthrough_ mode.

.Procedure

. Create a `CredentialsRequest` resource YAML file, for example, `sample-credential-request.yaml`, as follows:
+
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: cert-manager
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - action:
      - "route53:GetChange"
      effect: Allow
      resource: "arn:aws:route53:::change/*"
    - action:
      - "route53:ChangeResourceRecordSets"
      - "route53:ListResourceRecordSets"
      effect: Allow
      resource: "arn:aws:route53:::hostedzone/*"
    - action:
      - "route53:ListHostedZonesByName"
      effect: Allow
      resource: "*"
  secretRef:
    name: aws-creds
    namespace: cert-manager
  serviceAccountNames:
  - cert-manager
----

. Create a `CredentialsRequest` resource by running the following command:
+
[source,terminal]
----
$ oc create -f sample-credential-request.yaml
----

. Update the subscription object for {cert-manager-operator} by running the following command:
+
[source,terminal]
----
$ oc -n cert-manager-operator patch subscription openshift-cert-manager-operator --type=merge -p '{"spec":{"config":{"env":[{"name":"CLOUD_CREDENTIALS_SECRET_NAME","value":"aws-creds"}]}}}'
----

.Verification

. Get the name of the redeployed cert-manager controller pod by running the following command:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                          READY   STATUS    RESTARTS   AGE
cert-manager-bd7fbb9fc-wvbbt  1/1     Running   0          15m39s
----

. Verify that the cert-manager controller pod is updated with AWS credential volumes that are mounted under the path specified in `mountPath` by running the following command:
+
[source,terminal]
----
$ oc get -n cert-manager pod/<cert-manager_controller_pod_name> -o yaml
----
+
.Example output
[source,terminal]
----
...
spec:
  containers:
  - args:
    ...
    - mountPath: /.aws
      name: cloud-credentials
  ...
  volumes:
  ...
  - name: cloud-credentials
    secret:
      ...
      secretName: aws-creds
----

// with AWS Security Token Service
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-authenticate.adoc

[id="cert-manager-configure-cloud-credentials-aws-sts_{context}"]
= Authenticating with AWS Security Token Service

[role="_abstract"]
To securely access AWS resources from your applications without managing long-lived keys, authenticate your workloads by using the AWS Security Token Service (STS).

.Prerequisites

* You have extracted and prepared the `ccoctl` binary.
* You have configured an OpenShift Container Platform cluster with AWS STS by using the Cloud Credential Operator in manual mode.

.Procedure

. Create a directory to store a `CredentialsRequest` resource YAML file by running the following command:
+
[source,terminal]
----
$ mkdir credentials-request
----

. Create a `CredentialsRequest` resource YAML file under the `credentials-request` directory, such as, `sample-credential-request.yaml`, by applying the following yaml:
+
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: cert-manager
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AWSProviderSpec
    statementEntries:
    - action:
      - "route53:GetChange"
      effect: Allow
      resource: "arn:aws:route53:::change/*"
    - action:
      - "route53:ChangeResourceRecordSets"
      - "route53:ListResourceRecordSets"
      effect: Allow
      resource: "arn:aws:route53:::hostedzone/*"
    - action:
      - "route53:ListHostedZonesByName"
      effect: Allow
      resource: "*"
  secretRef:
    name: aws-creds
    namespace: cert-manager
  serviceAccountNames:
  - cert-manager
----

. Use the `ccoctl` tool to process `CredentialsRequest` objects by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-iam-roles \
    --name <user_defined_name> --region=<aws_region> \
    --credentials-requests-dir=<path_to_credrequests_dir> \
    --identity-provider-arn <oidc_provider_arn> --output-dir=<path_to_output_dir>
----
+
.Example output
[source,terminal]
----
2023/05/15 18:10:34 Role arn:aws:iam::XXXXXXXXXXXX:role/<user_defined_name>-cert-manager-aws-creds created
2023/05/15 18:10:34 Saved credentials configuration to: <path_to_output_dir>/manifests/cert-manager-aws-creds-credentials.yaml
2023/05/15 18:10:35 Updated Role policy for Role <user_defined_name>-cert-manager-aws-creds
----
+
Copy the `<aws_role_arn>` from the output to use in the next step. For example, `"arn:aws:iam::XXXXXXXXXXXX:role/<user_defined_name>-cert-manager-aws-creds"`

. Add the `eks.amazonaws.com/role-arn="<aws_role_arn>"` annotation to the service account by running the following command:
+
[source,terminal]
----
$ oc -n cert-manager annotate serviceaccount cert-manager eks.amazonaws.com/role-arn="<aws_role_arn>"
----

. To create a new pod, delete the existing cert-manager controller pod by running the following command:
+
[source,terminal]
----
$ oc delete pods -l app.kubernetes.io/name=cert-manager -n cert-manager
----
+
The AWS credentials are applied to a new cert-manager controller pod within a minute.

.Verification

. Get the name of the updated cert-manager controller pod by running the following command:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                          READY   STATUS    RESTARTS   AGE
cert-manager-bd7fbb9fc-wvbbt  1/1     Running   0          39s
----

. Verify that AWS credentials are updated by running the following command:
+
[source,terminal]
----
$ oc set env -n cert-manager po/<cert_manager_controller_pod_name> --list
----
+
.Example output
[source,terminal]
----
# pods/cert-manager-57f9555c54-vbcpg, container cert-manager-controller
# POD_NAMESPACE from field path metadata.namespace
AWS_ROLE_ARN=XXXXXXXXXXXX
AWS_WEB_IDENTITY_TOKEN_FILE=/var/run/secrets/eks.amazonaws.com/serviceaccount/token
----

[role="_additional-resources"]
[id="additional-resources_cert-manager-authenticate-gcp"]
.Additional resources

* Configuring the Cloud Credential Operator utility

// on GCP
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-authenticate.adoc

[id="cert-manager-configure-cloud-credentials-gcp-non-sts_{context}"]
= Authenticating on {gcp-short}

[role="_abstract"]
To securely access {gcp-first} resources, authenticate your workloads on {gcp-short} by using the {cert-manager-operator}.

.Prerequisites

* You have installed version 1.11.1 or later of the {cert-manager-operator}.
* You have configured the Cloud Credential Operator to operate in _mint_ or _passthrough_ mode.

.Procedure

. Create a `CredentialsRequest` resource YAML file, such as, `sample-credential-request.yaml` by applying the following yaml:
+
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: cert-manager
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: GCPProviderSpec
    predefinedRoles:
    - roles/dns.admin
  secretRef:
    name: gcp-credentials
    namespace: cert-manager
  serviceAccountNames:
  - cert-manager
----
+
[NOTE]
====
The `dns.admin` role provides admin privileges to the service account for managing {gcp-full} DNS resources. To ensure that the cert-manager runs with the service account that has the least privilege, you can create a custom role with the following permissions:

* `dns.resourceRecordSets.*`
* `dns.changes.*`
* `dns.managedZones.list`
====

. Create a `CredentialsRequest` resource by running the following command:
+
[source,terminal]
----
$ oc create -f sample-credential-request.yaml
----

. Update the subscription object for {cert-manager-operator} by running the following command:
+
[source,terminal]
----
$ oc -n cert-manager-operator patch subscription openshift-cert-manager-operator --type=merge -p '{"spec":{"config":{"env":[{"name":"CLOUD_CREDENTIALS_SECRET_NAME","value":"gcp-credentials"}]}}}'
----

.Verification

. Get the name of the redeployed cert-manager controller pod by running the following command:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-bd7fbb9fc-wvbbt               1/1     Running   0          15m39s
----

. Verify that the cert-manager controller pod is updated with {gcp-short} credential volumes that are mounted under the path specified in `mountPath` by running the following command:
+
[source,terminal]
----
$ oc get -n cert-manager pod/<cert-manager_controller_pod_name> -o yaml
----
+
.Example output
[source,terminal]
----
spec:
  containers:
  - args:
    ...
    volumeMounts:
    ...
    - mountPath: /.config/gcloud
      name: cloud-credentials
    ....
  volumes:
  ...
  - name: cloud-credentials
    secret:
      ...
      items:
      - key: service_account.json
        path: application_default_credentials.json
      secretName: gcp-credentials
----

// with GCP Workload Identity
// Module included in the following assemblies:
//
// * security/cert_manager_operator/cert-manager-authenticate.adoc

[id="cert-manager-configure-cloud-credentials-gcp-sts_{context}"]
= Authenticating with {gcp-short} Workload Identity

[role="_abstract"]
To securely access {gcp-first} resources from your applications without managing long-lived keys, authenticate your workloads by using {gcp-short} Workload Identity.

.Prerequisites

* You extracted and prepared the `ccoctl` binary.
* You have installed version 1.11.1 or later of the {cert-manager-operator}.
* You have configured an OpenShift Container Platform cluster with {gcp-short} Workload Identity by using the Cloud Credential Operator in a manual mode.

.Procedure

. Create a directory to store a `CredentialsRequest` resource YAML file by running the following command:
+
[source,terminal]
----
$ mkdir credentials-request
----

. In the `credentials-request` directory, create a YAML file that contains the following `CredentialsRequest` manifest:
+
[source,yaml]
----
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: cert-manager
  namespace: openshift-cloud-credential-operator
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: GCPProviderSpec
    predefinedRoles:
    - roles/dns.admin
  secretRef:
    name: gcp-credentials
    namespace: cert-manager
  serviceAccountNames:
  - cert-manager
----
+
[NOTE]
====
The `dns.admin` role provides admin privileges to the service account for managing {gcp-full} DNS resources. To ensure that the cert-manager runs with the service account that has the least privilege, you can create a custom role with the following permissions:

* `dns.resourceRecordSets.*`
* `dns.changes.*`
* `dns.managedZones.list`
====

. Use the `ccoctl` tool to process `CredentialsRequest` objects by running the following command:
+
[source,terminal]
----
$ ccoctl gcp create-service-accounts \
    --name <user_defined_name> --output-dir=<path_to_output_dir> \
    --credentials-requests-dir=<path_to_credrequests_dir> \
    --workload-identity-pool <workload_identity_pool> \
    --workload-identity-provider <workload_identity_provider> \
    --project <gcp_project_id>
----
+
.Example command
[source,terminal]
----
$ ccoctl gcp create-service-accounts \
    --name abcde-20230525-4bac2781 --output-dir=/home/outputdir \
    --credentials-requests-dir=/home/credentials-requests \
    --workload-identity-pool abcde-20230525-4bac2781 \
    --workload-identity-provider abcde-20230525-4bac2781 \
    --project openshift-gcp-devel
----

. Apply the secrets generated in the manifests directory of your cluster by running the following command:
+
[source,terminal]
----
$ ls <path_to_output_dir>/manifests/*-credentials.yaml | xargs -I{} oc apply -f {}
----

. Update the subscription object for {cert-manager-operator} by running the following command:
+
[source,terminal]
----
$ oc -n cert-manager-operator patch subscription openshift-cert-manager-operator --type=merge -p '{"spec":{"config":{"env":[{"name":"CLOUD_CREDENTIALS_SECRET_NAME","value":"gcp-credentials"}]}}}'
----

.Verification

. Get the name of the redeployed cert-manager controller pod by running the following command:
+
[source,terminal]
----
$ oc get pods -l app.kubernetes.io/name=cert-manager -n cert-manager
----
+
.Example output
[source,terminal]
----
NAME                          READY   STATUS    RESTARTS   AGE
cert-manager-bd7fbb9fc-wvbbt  1/1     Running   0          15m39s
----

. Verify that the cert-manager controller pod is updated with {gcp-short} workload identity credential volumes that are mounted under the path specified in `mountPath` by running the following command:
+
[source,terminal]
----
$ oc get -n cert-manager pod/<cert-manager_controller_pod_name> -o yaml
----
+
.Example output
[source,terminal]
----
spec:
  containers:
  - args:
    ...
    volumeMounts:
    - mountPath: /var/run/secrets/openshift/serviceaccount
      name: bound-sa-token
      ...
    - mountPath: /.config/gcloud
      name: cloud-credentials
  ...
  volumes:
  - name: bound-sa-token
    projected:
      ...
      sources:
      - serviceAccountToken:
          audience: openshift
          ...
          path: token
  - name: cloud-credentials
    secret:
      ...
      items:
      - key: service_account.json
        path: application_default_credentials.json
      secretName: gcp-credentials
----

[role="_additional-resources"]
[id="additional-resources_cert-manager-authenticate-gcp-workload-identity"]
.Additional resources

* Configuring the Cloud Credential Operator utility

* Manual mode with short-term credentials for components

* Default behavior of the Cloud Credential Operator
