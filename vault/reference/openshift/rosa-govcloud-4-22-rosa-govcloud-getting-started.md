---
title: "Getting started with {product-title} in AWS GovCloud"
type: reference
domain: openshift
slug: rosa-govcloud-4-22-rosa-govcloud-getting-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_govcloud/rosa-govcloud-getting-started
version: 4.22
family: rosa_govcloud
documentKind: "Documentation"
---

# Getting started with {product-title} in AWS GovCloud

[id="rosa-govcloud-getting-started"]
= Getting started with OpenShift Container Platform in AWS GovCloud

//I'm not sure what I meant by <Govcloud statement>, but there was likely a request for making a statement about the access or similar to it. I'll see what I can find
//[NOTE]
//====
//<Govcloud statement>
//====

// old definitition as no blocking anymore based on verification
//Federal and government agencies can be granted access to the OpenShift Container Platform in AWS GovCloud environment without further verification. However, commercial organizations and Federal Information Security Modernization Act (FISMA) R&D Universities must provide documentation to show that they are supporting a government contract or in the process of bidding on a government contract such as a request for proposal (RFP) or request for information (RFI) pre-bid stage. The customers who are in the government support verification process can review a subset of the FedRAMP Authority to Operate (ATO) documentation, but cannot gain access to the OpenShift Container Platform in AWS GovCloud environment until verification is complete.

[role="_abstract"]
This service is for use by federal and government agencies, or by commercial organizations and Federal Information Security Modernization Act (FISMA) research and development universities supporting a government contract or in the process of bidding on a government contract such as a request for proposal (RFP) or request for information (RFI) pre-bid stage.

//Snippet for accessing ROSA in AWS GovCloud

// Module included in the following assemblies:
//
// * rosa_govcloud/rosa-create-govcloud-cluster.adoc

[id="rosa-govcloud-fedramp-signup_{context}"]
= Signing up for a Red Hat FedRAMP account

[role="_abstract"]
To access OpenShift Container Platform in AWS GovCloud, you must sign up for a Red{nbsp}Hat FedRAMP account.

.Procedure
. Navigate to the ROSA GovCloud access request form.
. Complete the access request form.
. Click *Submit* to sign up. You receive a _Submission confirmation_.
+
Red{nbsp}Hat's confirmed stateside support team contacts you through email for the following information:
+
* *Admin details* to include your _organization name_, _administrator first and surname_ and _administrator email_.
* *User authentication* option to the FedRAMP {hybrid-console-second} from one of the following two options:
** _Local group in a Red{nbsp}Hat managed Keycloak instance_, where users will be required to setup multifactor authentication (MFA) with an approved device.
+
[NOTE]
====
Only device YubiKEY 5C NFC FIPS currently accepted.
====
+
** _Customer managed Identity Provider (IdP), integrated via OpenID Connect (OIDC)_, where you will need to provide the following:
*** *Discovery Endpoint:* The IdP's OIDC discovery URL (typically ending in _/.well-known/openid-configuration_). This allows Keycloak to automatically fetch most of the IdP's settings.
*** *Client ID and secret:* Credentials that allow Keycloak to authenticate with the customer's IdP.
*** *Email domain(s):* A list of approved email domains. Only users with an email address from one of these domains will be allowed to log in.
*** *Essential claim:* A specific key-value pair (e.g., _"rh-approved": "true"_) that must be present in a user's token from the IdP to grant them access. In this configuration, the customer takes on the responsibility for implementing FIPS 140-2 validated MFA.

// Following process with a sign up button will not be available until https://issues.redhat.com/browse/CRCPLAN-397 is complete.
//. Navigate to https://console.openshiftusgov.com/openshift/token.
//. Click *Sign up* to sign up for a OpenShift Container Platform FedRAMP account.
//+
//* The *Sign up* link is located below the *Log in* button.
//+
//. Enter the required information and click the *Sign up* button.
//. Once you receive an email with a code for you to confirm, enter the token and click *Confirm account*.
//+
//You will be directed to a screen with your login token.
