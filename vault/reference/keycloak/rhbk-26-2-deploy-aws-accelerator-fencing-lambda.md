---
title: "Chapter 12. Deploying an AWS Lambda to disable a non-responding site - Red Hat build of Keycloak 26.2 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-deploy-aws-accelerator-fencing-lambda
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/deploy-aws-accelerator-fencing-lambda-
guide: high_availability_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Deploy an AWS Lambda as part of the load-balancer building block in a multi-site deployment. This chapter explains how to resolve split-brain scenarios between two sites in a multi-site deployment. It also disables replication if one site fails, so the other site can continue to serve requests. This deployment is intended to be used with the setup described in the Concepts for multi-site deploymen…"
---

# Chapter 12. Deploying an AWS Lambda to disable a non-responding site - Red Hat build of Keycloak 26.2 High Availability Guide

Chapter 12. Deploying an AWS Lambda to disable a non-responding site
Deploy an AWS Lambda as part of the load-balancer building block in a multi-site deployment.
This chapter explains how to resolve split-brain scenarios between two sites in a multi-site deployment. It also disables replication if one site fails, so the other site can continue to serve requests.
This deployment is intended to be used with the setup described in the Concepts for multi-site deployments chapter. Use this deployment with the other building blocks outlined in the Building blocks multi-site deployments chapter.
We provide these blueprints to show a minimal functionally complete example with a good baseline performance for regular installations. You would still need to adapt it to your environment and your organization’s standards and security best practices.
12.1. Architecture
In the event of a network communication failure between sites in a multi-site deployment, it is no longer possible for the two sites to continue to replicate the data between them. The Data Grid is configured with a FAIL
failure policy, which ensures consistency over availability. Consequently, all user requests are served with an error message until the failure is resolved, either by restoring the network connection or by disabling cross-site replication.
In such scenarios, a quorum is commonly used to determine which sites are marked as online or offline. However, as multi-site deployments only consist of two sites, this is not possible. Instead, we leverage “fencing” to ensure that when one of the sites is unable to connect to the other site, only one site remains in the load balancer configuration, and hence only this site is able to serve subsequent users requests.
In addition to the load balancer configuration, the fencing procedure disables replication between the two Data Grid clusters to allow serving user requests from the site that remains in the load balancer configuration. As a result, the sites will be out-of-sync once the replication has been disabled.
To recover from the out-of-sync state, a manual re-sync is necessary as described in Synchronizing sites. This is why a site which is removed via fencing will not be re-added automatically when the network communication failure is resolved. The remove site should only be re-added once the two sites have been synchronized using the outlined procedure Bringing a site online.
In this chapter we describe how to implement fencing using a combination of Prometheus Alerts and AWS Lambda functions. A Prometheus Alert is triggered when split-brain is detected by the Data Grid server metrics, which results in the Prometheus AlertManager calling the AWS Lambda based webhook. The triggered Lambda function inspects the current Global Accelerator configuration and removes the site reported to be offline.
In a true split-brain scenario, where both sites are still up but network communication is down, it is possible that both sites will trigger the webhook simultaneously. We guard against this by ensuring that only a single Lambda instance can be executed at a given time. The logic in the AWS Lambda ensures that always one site entry remains in the load balancer configuration.
12.2. Prerequisites
- ROSA HCP based multi-site Keycloak deployment
- AWS CLI Installed
- AWS Global Accelerator load balancer
-
jq
tool installed
12.3. Procedure
Enable Openshift user alert routing
Command:
oc apply -f - << EOF apiVersion: v1 kind: ConfigMap metadata: name: user-workload-monitoring-config namespace: openshift-user-workload-monitoring data: config.yaml: | alertmanager: enabled: true enableAlertmanagerConfig: true EOF oc -n openshift-user-workload-monitoring rollout status --watch statefulset.apps/alertmanager-user-workload
Decide upon a username/password combination which will be used to authenticate the Lambda webhook and create an AWS Secret storing the password
Command:
aws secretsmanager create-secret \ --name webhook-password \
1 --secret-string changeme \
2 --region eu-west-1
3 Create the Role used to execute the Lambda.
Command:
FUNCTION_NAME=
1 ROLE_ARN=$(aws iam create-role \ --role-name ${FUNCTION_NAME} \ --assume-role-policy-document \ '{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }' \ --query 'Role.Arn' \ --region eu-west-1 \
2 --output text )
Create and attach the 'LambdaSecretManager' Policy so that the Lambda can access AWS Secrets
Command:
POLICY_ARN=$(aws iam create-policy \ --policy-name LambdaSecretManager \ --policy-document \ '{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "secretsmanager:GetSecretValue" ], "Resource": "*" } ] }' \ --query 'Policy.Arn' \ --output text ) aws iam attach-role-policy \ --role-name ${FUNCTION_NAME} \ --policy-arn ${POLICY_ARN}
Attach the
ElasticLoadBalancingReadOnly
policy so that the Lambda can query the provisioned Network Load BalancersCommand:
aws iam attach-role-policy \ --role-name ${FUNCTION_NAME} \ --policy-arn arn:aws:iam::aws:policy/ElasticLoadBalancingReadOnly
Attach the
GlobalAcceleratorFullAccess
policy so that the Lambda can update the Global Accelerator EndpointGroupCommand:
aws iam attach-role-policy \ --role-name ${FUNCTION_NAME} \ --policy-arn arn:aws:iam::aws:policy/GlobalAcceleratorFullAccess
Create a Lambda ZIP file containing the required fencing logic
Command:
LAMBDA_ZIP=/tmp/lambda.zip cat << EOF > /tmp/lambda.py from urllib.error import HTTPError import boto3 import jmespath import json import os import urllib3 from base64 import b64decode from urllib.parse import unquote # Prevent unverified HTTPS connection warning urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) class MissingEnvironmentVariable(Exception): pass class MissingSiteUrl(Exception): pass def env(name): if name in os.environ: return os.environ[name] raise MissingEnvironmentVariable(f"Environment Variable '{name}' must be set") def handle_site_offline(labels): a_client = boto3.client('globalaccelerator', region_name='us-west-2') acceleratorDNS = labels['accelerator'] accelerator = jmespath.search(f"Accelerators[?(DnsName=='{acceleratorDNS}'|| DualStackDnsName=='{acceleratorDNS}')]", a_client.list_accelerators()) if not accelerator: print(f"Ignoring SiteOffline alert as accelerator with DnsName '{acceleratorDNS}' not found") return accelerator_arn = accelerator[0]['AcceleratorArn'] listener_arn = a_client.list_listeners(AcceleratorArn=accelerator_arn)['Listeners'][0]['ListenerArn'] endpoint_group = a_client.list_endpoint_groups(ListenerArn=listener_arn)['EndpointGroups'][0] endpoints = endpoint_group['EndpointDescriptions'] # Only update accelerator endpoints if two entries exist if len(endpoints) > 1: # If the reporter endpoint is not healthy then do nothing for now # A Lambda will eventually be triggered by the other offline site for this reporter reporter = labels['reporter'] reporter_endpoint = [e for e in endpoints if endpoint_belongs_to_site(e, reporter)][0] if reporter_endpoint['HealthState'] == 'UNHEALTHY': print(f"Ignoring SiteOffline alert as reporter '{reporter}' endpoint is marked UNHEALTHY") return offline_site = labels['site'] endpoints = [e for e in endpoints if not endpoint_belongs_to_site(e, offline_site)] del reporter_endpoint['HealthState'] a_client.update_endpoint_group( EndpointGroupArn=endpoint_group['EndpointGroupArn'], EndpointConfigurations=endpoints ) print(f"Removed site={offline_site} from Accelerator EndpointGroup") take_infinispan_site_offline(reporter, offline_site) print(f"Backup site={offline_site} caches taken offline") else: print("Ignoring SiteOffline alert only one Endpoint defined in the EndpointGroup") def endpoint_belongs_to_site(endpoint, site): lb_arn = endpoint['EndpointId'] region = lb_arn.split(':')[3] client = boto3.client('elbv2', region_name=region) tags = client.describe_tags(ResourceArns=[lb_arn])['TagDescriptions'][0]['Tags'] for tag in tags: if tag['Key'] == 'site': return tag['Value'] == site return false def take_infinispan_site_offline(reporter, offlinesite): endpoints = json.loads(INFINISPAN_SITE_ENDPOINTS) if reporter not in endpoints: raise MissingSiteUrl(f"Missing URL for site '{reporter}' in 'INFINISPAN_SITE_ENDPOINTS' json") endpoint = endpoints[reporter] password = get_secret(INFINISPAN_USER_SECRET) url = f"https://{endpoint}/rest/v2/container/x-site/backups/{offlinesite}?action=take-offline" http = urllib3.PoolManager(cert_reqs='CERT_NONE') headers = urllib3.make_headers(basic_auth=f"{INFINISPAN_USER}:{password}") try: rsp = http.request("POST", url, headers=headers) if rsp.status >= 400: raise HTTPError(f"Unexpected response status '%d' when taking site offline", rsp.status) rsp.release_conn() except HTTPError as e: print(f"HTTP error encountered: {e}") def get_secret(secret_name): session = boto3.session.Session() client = session.client( service_name='secretsmanager', region_name=SECRETS_REGION ) return client.get_secret_value(SecretId=secret_name)['SecretString'] def decode_basic_auth_header(encoded_str): split = encoded_str.strip().split(' ') if len(split) == 2: if split[0].strip().lower() == 'basic': try: username, password = b64decode(split[1]).decode().split(':', 1) except: raise DecodeError else: raise DecodeError else: raise DecodeError return unquote(username), unquote(password) def handler(event, context): print(json.dumps(event)) authorization = event['headers'].get('authorization') if authorization is None: print("'Authorization' header missing from request") return { "statusCode": 401 } expectedPass = get_secret(WEBHOOK_USER_SECRET) username, password = decode_basic_auth_header(authorization) if username != WEBHOOK_USER and password != expectedPass: print('Invalid username/password combination') return { "statusCode": 403 } body = event.get('body') if body is None: raise Exception('Empty request body') body = json.loads(body) print(json.dumps(body)) if body['status'] != 'firing': print("Ignoring alert as status is not 'firing', status was: '%s'" % body['status']) return { "statusCode": 204 } for alert in body['alerts']: labels = alert['labels'] if labels['alertname'] == 'SiteOffline': handle_site_offline(labels) return { "statusCode": 204 } INFINISPAN_USER = env('INFINISPAN_USER') INFINISPAN_USER_SECRET = env('INFINISPAN_USER_SECRET') INFINISPAN_SITE_ENDPOINTS = env('INFINISPAN_SITE_ENDPOINTS') SECRETS_REGION = env('SECRETS_REGION') WEBHOOK_USER = env('WEBHOOK_USER') WEBHOOK_USER_SECRET = env('WEBHOOK_USER_SECRET') EOF zip -FS --junk-paths ${LAMBDA_ZIP} /tmp/lambda.py
Create the Lambda function.
Command:
aws lambda create-function \ --function-name ${FUNCTION_NAME} \ --zip-file fileb://${LAMBDA_ZIP} \ --handler lambda.handler \ --runtime python3.12 \ --role ${ROLE_ARN} \ --region eu-west-1
1 - 1
- The AWS Region hosting your Kubernetes clusters
Expose a Function URL so the Lambda can be triggered as webhook
Command:
aws lambda create-function-url-config \ --function-name ${FUNCTION_NAME} \ --auth-type NONE \ --region eu-west-1
1 - 1
- The AWS Region hosting your Kubernetes clusters
Allow public invocations of the Function URL
Command:
aws lambda add-permission \ --action "lambda:InvokeFunctionUrl" \ --function-name ${FUNCTION_NAME} \ --principal "*" \ --statement-id FunctionURLAllowPublicAccess \ --function-url-auth-type NONE \ --region eu-west-1
1 - 1
- The AWS Region hosting your Kubernetes clusters
Configure the Lambda’s Environment variables:
In each Kubernetes cluster, retrieve the exposed Data Grid URL endpoint:
oc -n ${NAMESPACE} get route infinispan-external -o jsonpath='{.status.ingress[].host}'
1 - 1
- Replace
${NAMESPACE}
with the namespace containing your Data Grid server
Upload the desired Environment variables
ACCELERATOR_NAME=
1 LAMBDA_REGION=
2 CLUSTER_1_NAME=
3 CLUSTER_1_ISPN_ENDPOINT=
4 CLUSTER_2_NAME=
5 CLUSTER_2_ISPN_ENDPOINT=
6 INFINISPAN_USER=
7 INFINISPAN_USER_SECRET=
8 WEBHOOK_USER=
9 WEBHOOK_USER_SECRET=
10 INFINISPAN_SITE_ENDPOINTS=$(echo "{\"${CLUSTER_NAME_1}\":\"${CLUSTER_1_ISPN_ENDPOINT}\",\"${CLUSTER_2_NAME}\":\"${CLUSTER_2_ISPN_ENDPOINT\"}" | jq tostring) aws lambda update-function-configuration \ --function-name ${ACCELERATOR_NAME} \ --region ${LAMBDA_REGION} \ --environment "{ \"Variables\": { \"INFINISPAN_USER\" : \"${INFINISPAN_USER}\", \"INFINISPAN_USER_SECRET\" : \"${INFINISPAN_USER_SECRET}\", \"INFINISPAN_SITE_ENDPOINTS\" : ${INFINISPAN_SITE_ENDPOINTS}, \"WEBHOOK_USER\" : \"${WEBHOOK_USER}\", \"WEBHOOK_USER_SECRET\" : \"${WEBHOOK_USER_SECERT}\", \"SECRETS_REGION\" : \"eu-central-1\" } }"
- 1
- The name of the AWS Global Accelerator used by your deployment
- 2
- The AWS Region hosting your Kubernetes cluster and Lambda function
- 3
- The name of one of your Data Grid sites as defined in Deploying Data Grid for HA with the Data Grid Operator
- 4
- The Data Grid endpoint URL associated with the CLUSER_1_NAME site
- 5
- The name of the second Data Grid site
- 6
- The Data Grid endpoint URL associated with the CLUSER_2_NAME site
- 7
- The username of a Data Grid user which has sufficient privileges to perform REST requests on the server
- 8
- The name of the AWS secret containing the password associated with the Data Grid user
- 9
- The username used to authenticate requests to the Lambda Function
- 10
- The name of the AWS secret containing the password used to authenticate requests to the Lambda function
Retrieve the Lambda Function URL
Command:
aws lambda get-function-url-config \ --function-name ${FUNCTION_NAME} \ --query "FunctionUrl" \ --region eu-west-1 \
1 --output text
- 1
- The AWS region where the Lambda was created
Output:
https://tjqr2vgc664b6noj6vugprakoq0oausj.lambda-url.eu-west-1.on.aws
In each Kubernetes cluster, configure a Prometheus Alert routing to trigger the Lambda on split-brain
Command:
NAMESPACE= # The namespace containing your deployments oc apply -n ${NAMESPACE} -f - << EOF apiVersion: v1 kind: Secret type: kubernetes.io/basic-auth metadata: name: webhook-credentials stringData: username: 'keycloak'
1 password: 'changme'
2 --- apiVersion: monitoring.coreos.com/v1beta1 kind: AlertmanagerConfig metadata: name: example-routing spec: route: receiver: default groupBy: - accelerator groupInterval: 90s groupWait: 60s matchers: - matchType: = name: alertname value: SiteOffline receivers: - name: default webhookConfigs: - url: 'https://tjqr2vgc664b6noj6vugprakoq0oausj.lambda-url.eu-west-1.on.aws/'
3 httpConfig: basicAuth: username: key: username name: webhook-credentials password: key: password name: webhook-credentials tlsConfig: insecureSkipVerify: true --- apiVersion: monitoring.coreos.com/v1 kind: PrometheusRule metadata: name: xsite-status spec: groups: - name: xsite-status rules: - alert: SiteOffline expr: 'min by (namespace, site) (vendor_jgroups_site_view_status{namespace="default",site="site-b"}) == 0'
4 labels: severity: critical reporter: site-a
5 accelerator: a3da6a6cbd4e27b02.awsglobalaccelerator.com
6 - 1
- The username required to authenticate Lambda requests
- 2
- The password required to authenticate Lambda requests
- 3
- The Lambda Function URL
- 4
- The namespace value should be the namespace hosting the Infinispan CR and the site should be the remote site defined by
spec.service.sites.locations[0].name
in your Infinispan CR - 5
- The name of your local site defined by
spec.service.sites.local.name
in your Infinispan CR - 6
- The DNS of your Global Accelerator
12.4. Verify
To test that the Prometheus alert triggers the webhook as expected, perform the following steps to simulate a split-brain:
In each of your clusters execute the following:
Command:
oc -n openshift-operators scale --replicas=0 deployment/infinispan-operator-controller-manager
1 oc -n openshift-operators rollout status -w deployment/infinispan-operator-controller-manager oc -n ${NAMESPACE} scale --replicas=0 deployment/infinispan-router
2 oc -n ${NAMESPACE} rollout status -w deployment/infinispan-router
-
Verify the
SiteOffline
event has been fired on a cluster by inspecting the ObserveAlerting menu in the Openshift console - Inspect the Global Accelerator EndpointGroup in the AWS console and there should only be a single endpoint present
Scale up the Data Grid Operator and Gossip Router to re-establish a connection between sites:
Command:
oc -n openshift-operators scale --replicas=1 deployment/infinispan-operator-controller-manager oc -n openshift-operators rollout status -w deployment/infinispan-operator-controller-manager oc -n ${NAMESPACE} scale --replicas=1 deployment/infinispan-router
1 oc -n ${NAMESPACE} rollout status -w deployment/infinispan-router
- 1
- Replace
${NAMESPACE}
with the namespace containing your Data Grid server
-
Inspect the
vendor_jgroups_site_view_status
metric in each site. A value of1
indicates that the site is reachable. - Update the Accelerator EndpointGroup to contain both Endpoints. See the Bringing a site online chapter for details.
