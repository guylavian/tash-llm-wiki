---
title: "Configuring advanced direct authentication fields"
type: reference
domain: openshift
slug: authentication-4-22-structured-auth-config-fields
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/structured-auth-config-fields
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring advanced direct authentication fields

[id="structured-auth-config-fields"]
= Configuring advanced direct authentication fields

[role="_abstract"]
You can configure advanced direct authentication fields in the `authentications.config.openshift.io` custom resource definition (CRD) to enable enhanced OIDC configurations, security enforcement, and flexible token validation for standalone and hosted control plane (HCP) clusters.

// About advanced direct authentication fields
// Module included in the following assemblies:
//
// * authentication/structured-auth-config-fields.adoc

[id="structured-auth-config-about_{context}"]
= About advanced direct authentication fields

[role="_abstract"]
Advanced direct authentication fields provide flexibility and security for OIDC-based authentication in OpenShift Container Platform. You can configure advanced OIDC settings, implement custom token validation logic, and enforce security policies on usernames and groups.

The following capabilities are available:

Custom OIDC discovery URL::
Specify a custom OIDC discovery endpoint when your identity provider does not use the standard discovery URL format. Useful for complex networking setups or non-standard identity providers.

CEL-based claim mapping::
Use Common Expression Language (CEL) expressions to construct usernames and groups from JWT token claims with fallback logic. This addresses scenarios where different user types require varying claim mappings.

Claim validation rules::
Use CEL expressions to implement advanced token validation logic, such as enforcing maximum token lifetimes, validating multiple claims, or implementing custom security policies.

User validation rules::
Enforce security policies on usernames and groups extracted from tokens to prevent privilege escalation by blocking reserved system usernames and group prefixes.

These fields extend the base OIDC authentication configuration introduced in OpenShift Container Platform 4.14. You must first configure an external OIDC identity provider before using these advanced fields.

These fields require the `TechPreviewNoUpgrade` feature set to be enabled. They are available on standalone OpenShift Container Platform clusters and hosted control plane (HCP) environments.

[IMPORTANT]
====
These advanced authentication fields are available as a Technology Preview feature. Ensure you have a backup authentication method, such as a certificate-based kubeconfig file, before configuring these fields.
====

// Configuring a custom OIDC discovery URL
// Module included in the following assemblies:
//
// * authentication/structured-auth-config-fields.adoc

[id="structured-auth-config-discovery-url_{context}"]
= Configuring a custom OIDC discovery URL

[role="_abstract"]
Configure a custom OIDC discovery URL when your identity provider does not follow the standard discovery endpoint format.

.Prerequisites

* You have configured an external OIDC identity provider for direct authentication.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.

.Procedure

. Create a YAML file named `authentication-discovery-url.yaml` with your custom discovery URL configuration:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  type: OIDC
  oidcProviders:
  - name: my-oidc-provider
    issuer:
      issuerURL: https://idp.example.com
      discoveryURL: https://custom-discovery.example.com/.well-known/openid-configuration
      audiences:
      - my-audience
    claimMappings:
      username:
        claim: email
----
+
where:
+
`issuerURL`:: Specifies the issuer URL displayed in JWT token `iss` claim.
`discoveryURL`:: Specifies the custom OIDC discovery endpoint URL. Must differ from `issuerURL`, use HTTPS, and must not contain query parameters, fragments, or user info. Maximum length: 2048 characters.
+
[NOTE]
====
Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `https://custom-discovery.example.com/.well-known/openid-configuration`, `my-audience`) with your actual OIDC provider configuration.
====

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f authentication-discovery-url.yaml
----

.Verification

* Monitor the cluster authentication Operator status to ensure the configuration is applied successfully:
+
[source,terminal]
----
$ oc get clusteroperator authentication
----
+
The Operator should report `Available=True` and `Degraded=False`.

* Check the cluster authentication Operator logs for any errors:
+
[source,terminal]
----
$ oc logs -n openshift-authentication-operator deployments/authentication-operator
----

* Verify the kube-apiserver is using the custom discovery URL by checking the authentication configuration:
+
[source,terminal]
----
$ oc get configmap kube-apiserver-to-kubelet-client-ca -n openshift-kube-apiserver -o yaml
----
+
[source,terminal]
----
$ oc get authentication.config.openshift.io/cluster -o jsonpath='{.spec.oidcProviders[0].issuer.discoveryURL}'
----
+
The output should display your custom discovery URL.

// Configuring CEL expressions for username and groups claim mapping
// Module included in the following assemblies:
//
// * authentication/structured-auth-config-fields.adoc

[id="structured-auth-config-cel-claim-mapping_{context}"]
= Configuring CEL expressions for username and groups claim mapping

[role="_abstract"]
You can use Common Expression Language (CEL) expressions to construct usernames and groups from JWT token claims. This provides flexible claim mapping, including fallback logic when specific claims are not present.

.Prerequisites

* You have configured an external OIDC identity provider for direct authentication.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.
* You are familiar with CEL expression syntax.

.Procedure

. Create a YAML file named `authentication-cel-mapping.yaml` with your CEL expression configuration:
+
[IMPORTANT]
====
When using `expression`, do not set the `claim` field. You must use either `claim` or `expression`, but not both. Setting both will result in a validation error. Additionally, when using `expression`, do not set `prefixPolicy` to `Prefix`. Prefix policies are only compatible with `claim`-based mappings.
====
+
[NOTE]
====
When using the `email` claim in CEL expressions, you must also validate `email_verified` to ensure the email address has been verified by the identity provider.
====
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  type: OIDC
  oidcProviders:
  - name: my-oidc-provider
    issuer:
      issuerURL: https://idp.example.com
      audiences:
      - my-audience
    claimMappings:
      username:
        expression: 'claims.?upn.orValue(claims.?oid.orValue(claims.sub))'
      groups:
        expression: 'claims.?groups.orValue([])'
# ...
----
+
where:
+
`username.expression`:: Specifies the fallback logic for username: `upn` if present, else `oid`, else `sub`.
`groups.expression`:: Specifies that the `groups` claim is used if present, else an empty array.
+
[NOTE]
====
Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `my-audience`) with your actual OIDC provider configuration.
====

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f authentication-cel-mapping.yaml
----

.Verification

* Verify that the authentication configuration is applied successfully:
+
[source,terminal]
----
$ oc get authentication.config.openshift.io/cluster -o yaml
----

* Authenticate with a user account and verify the username is constructed correctly:
+
[source,terminal]
----
$ oc whoami
----

* Monitor the cluster authentication Operator status:
+
[source,terminal]
----
$ oc get clusteroperator authentication
----
+
The Operator should report `Available=True` and `Degraded=False`.

[NOTE]
====
CEL expressions have access to standard CEL string functions (`lowerAscii()`, `upperAscii()`, `contains()`, `startsWith()`, `endsWith()`, `matches()`, `split()`), operators (`+`, `?`, `has()`, ternary `? :`), and the `orValue()` method for optional chaining. See the CEL specification link in Additional resources for the complete function reference.
====

You can use the following CEL expression patterns for claim mapping:

Use the optional chaining Operator `?` to safely access claims that might not exist::
+
[source,yaml]
----
username:
  expression: 'claims.email_verified ? claims.email : claims.sub'
----
+
Uses `email` if verified, otherwise `sub`. When using the `email` claim, you must also check `email_verified`.

Concatenate multiple claims::
+
[source,yaml]
----
username:
  expression: 'claims.givenname + "." + claims.surname'
----
+
Combines given name and surname claims.

Transform claim values::
+
[source,yaml]
----
username:
  expression: 'claims.email.lowerAscii()'
----
+
Converts email to lowercase.

Conditional logic for different user types::
+
[source,yaml]
----
username:
  expression: 'has(claims.upn) ? claims.upn : claims.oid'
----
+
Uses `upn` for regular users, `oid` for service principals.

Extract domain from email::
+
[source,yaml]
----
groups:
  expression: 'claims.?email.orValue("").split("@").size() > 1 ? [claims.email.split("@")[1]] : []'
----
+
Safely extracts domain from email address for group assignment, returning an empty array if email is missing or malformed.

Combine group sources::
+
[source,yaml]
----
groups:
  expression: 'claims.?groups.orValue([]) + claims.?roles.orValue([])'
----
+
Combines `groups` and `roles` claims.

// Configuring claim validation rules
// Module included in the following assemblies:
//
// * authentication/structured-auth-config-fields.adoc

[id="structured-auth-config-claim-validation_{context}"]
= Configuring claim validation rules

[role="_abstract"]
Use Common Expression Language (CEL) expressions to define custom validation rules for JWT token claims and enforce advanced security policies such as maximum token lifetimes.

[WARNING]
====
All claim validation rules must pass for authentication to succeed. Incorrectly configured validation rules can lock all users out of the cluster. Ensure you complete the following tasks:

* Have a backup authentication method, such as a certificate-based kubeconfig file, before applying these rules
* Test validation rules in a non-production environment first
* Verify your CEL expressions are correct to avoid blocking valid users from accessing the cluster
====

.Prerequisites

* You have configured an external OIDC identity provider for direct authentication.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.
* You are familiar with CEL expression syntax.

.Procedure

. Create a YAML file named `authentication-claim-validation.yaml` with your claim validation rules:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  type: OIDC
  oidcProviders:
  - name: my-oidc-provider
    issuer:
      issuerURL: https://idp.example.com
      audiences:
      - my-audience
    claimMappings:
      username:
        claim: email
    claimValidationRules:
    - type: CEL
      cel:
        expression: 'claims.exp - claims.nbf <= 86400'
        message: 'Total token lifetime must not exceed 24 hours'
    - type: CEL
      cel:
        expression: 'has(claims.email) && claims.email_verified && claims.email.contains("@example.com")'
        message: 'Email claim must be verified and from example.com domain'
----
+
where:
+
`claimValidationRules`:: Specifies an array of validation rules. All must pass for authentication.
`type`:: Specifies the validation type. Set to `CEL` for CEL-based validation.
`cel.expression`:: Specifies the CEL expression that must evaluate to `true`.
`cel.message`:: Specifies the error message displayed when validation fails.
+
[NOTE]
====
Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `my-audience`, `@example.com`) with your actual OIDC provider configuration and validation requirements.
====

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f authentication-claim-validation.yaml
----

.Verification

* Verify that the authentication configuration is applied successfully:
+
[source,terminal]
----
$ oc get authentication.config.openshift.io/cluster -o yaml
----

* Authenticate with a token that matches your validation rules to confirm they are enforced correctly.

* Check the cluster authentication Operator logs for validation errors:
+
[source,terminal]
----
$ oc logs -n openshift-authentication-operator deployments/authentication-operator
----

When writing CEL expressions for claim validation:

* Access claims using `claims` variable (for example, `claims.sub` or `claims.foo.bar` for nested claims)
* Expressions must evaluate to boolean values
* Use `has()` to check claim existence
* Standard CEL operators and functions available: `&&`, `||`, `!`, `contains()`, `startsWith()`, `endsWith()`

Common use cases include:

Enforce maximum token lifetime::
+
[source,yaml]
----
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.exp - claims.nbf <= 86400'
    message: 'Token lifetime must not exceed 24 hours'
----

Require specific claim values::
+
[source,yaml]
----
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.tenant == "production"'
    message: 'Only production tenant tokens are allowed'
----

Validate email domain::
+
[source,yaml]
----
claimValidationRules:
- type: CEL
  cel:
    expression: 'has(claims.email) && claims.email_verified && claims.email.endsWith("@trusted-domain.com")'
    message: 'Email must be verified and from trusted-domain.com'
----
+
When using the `email` claim, you must also check `email_verified` to ensure the email address has been verified by the identity provider.

Combine conditions::
+
[source,yaml]
----
claimValidationRules:
- type: CEL
  cel:
    expression: 'has(claims.role) && (claims.role == "admin" || claims.role == "developer")'
    message: 'User must have admin or developer role'
----

.Troubleshooting

If authentication fails after the configuration is applied::
+
Even if your claim validation rules pass the configuration validation gates, runtime authentication errors can occur. Check the kube-apiserver logs for detailed error messages explaining why authentication failed:
+
[source,terminal]
----
$ oc logs -n openshift-kube-apiserver -l app=openshift-kube-apiserver | grep -i auth
----
+
These log messages will indicate which validation rule failed and include the custom `message` you specified in the CEL expression.

If you incorrectly configure validation rules and lock users out of the cluster::
+
. Use your certificate-based kubeconfig to authenticate as `cluster-admin`.
+
. Edit the Authentication custom resource to remove or fix invalid rules:
+
[source,terminal]
----
$ oc edit authentication.config.openshift.io/cluster
----
+
. Monitor the cluster authentication Operator to confirm it returns to `Available` status:
+
[source,terminal]
----
$ oc get clusteroperator authentication
----

// Configuring user validation rules
// Module included in the following assemblies:
//
// * authentication/structured-auth-config-fields.adoc

[id="structured-auth-config-user-validation_{context}"]
= Configuring user validation rules

[role="_abstract"]
You can define validation rules to enforce security policies on the user object created from an authenticated token. This helps prevent privilege escalation by blocking reserved usernames and group prefixes.

[NOTE]
====
User validation rules are evaluated after claim mapping is complete, including all prefix transformations. Your CEL expressions must validate the final username and group names as they will appear in RBAC policies, not the raw claim values from the JWT token.
====

[WARNING]
====
All user validation rules must pass for authentication to succeed. Incorrectly configured validation rules can lock all users out of the cluster. Ensure you:

* Have a backup authentication method, such as a certificate-based kubeconfig file, before applying these rules
* Test validation rules in a non-production environment first
* Verify your CEL expressions correctly validate the final username and groups to avoid blocking valid users or allowing unauthorized access
====

.Prerequisites

* You have configured an external OIDC identity provider for direct authentication.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.
* You are familiar with CEL expression syntax.

.Procedure

. Create a YAML file named `authentication-user-validation.yaml` with your user validation rules:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  type: OIDC
  oidcProviders:
  - name: my-oidc-provider
    issuer:
      issuerURL: https://idp.example.com
      audiences:
      - my-audience
    claimMappings:
      username:
        claim: email
      groups:
        claim: groups
    userValidationRules:
    - expression: "!user.username.startsWith('system:')"
      message: 'Username cannot use reserved system: prefix'
    - expression: "!user.groups.exists(g, g.startsWith('system:'))"
      message: 'Groups cannot use reserved system: prefix'
----
+
where:
+
`userValidationRules`:: Specifies an array of validation rules. All must pass for authentication.
`expression`:: Specifies the CEL expression that must evaluate to `true`.
`message`:: Specifies the error message displayed when validation fails.
+
[NOTE]
====
Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `my-audience`) with your actual OIDC provider configuration.
====

. Apply the configuration:
+
[source,terminal]
----
$ oc apply -f authentication-user-validation.yaml
----

.Verification

* Verify that the authentication configuration is applied successfully:
+
[source,terminal]
----
$ oc get authentication.config.openshift.io/cluster -o yaml
----

* Authenticate with credentials that would create a user matching your validation rules to confirm they are enforced correctly.

* Check the cluster authentication Operator logs for validation errors:
+
[source,terminal]
----
$ oc logs -n openshift-authentication-operator deployments/authentication-operator
----

When writing CEL expressions for user validation:

* Access user fields: `user.username`, `user.groups` (array), `user.uid`, `user.extra` (map)
* Expressions must evaluate to boolean values
* Use `startsWith()`, `endsWith()`, `contains()` for string matching
* Use `exists()` for array checks (for example, `user.groups.exists(g, g == "admin")`)

Common use cases include:

Prevent reserved username prefixes::
+
[source,yaml]
----
userValidationRules:
- expression: "!user.username.startsWith('system:')"
  message: 'Username cannot use reserved system: prefix'
----

Prevent reserved group prefixes::
+
[source,yaml]
----
userValidationRules:
- expression: "!user.groups.exists(g, g.startsWith('system:'))"
  message: 'Groups cannot use reserved system: prefix'
----

Require username format::
+
[source,yaml]
----
userValidationRules:
- expression: "user.username.matches('^[a-z0-9]([-a-z0-9]*[a-z0-9])?$')"
  message: 'Username must be a valid DNS subdomain'
----

Validate group membership::
+
[source,yaml]
----
userValidationRules:
- expression: "user.groups.exists(g, g == 'verified-users')"
  message: 'User must be a member of verified-users group'
----

Combine conditions::
+
[source,yaml]
----
userValidationRules:
- expression: "!user.username.startsWith('system:') && !user.username.startsWith('kube:')"
  message: 'Username cannot use reserved system: or kube: prefixes'
----

.Troubleshooting

If you incorrectly configure validation rules and lock users out of the cluster:

. Use your certificate-based kubeconfig to authenticate as `cluster-admin`.

. Edit the Authentication custom resource to remove or fix invalid rules:
+
[source,terminal]
----
$ oc edit authentication.config.openshift.io/cluster
----

. Monitor the cluster authentication Operator to confirm it returns to `Available` status:
+
[source,terminal]
----
$ oc get clusteroperator authentication
----

// Advanced authentication field reference
// Module included in the following assemblies:
//
// * authentication/structured-auth-config-fields.adoc

[id="structured-auth-config-fields-reference_{context}"]
= Advanced authentication field reference

[role="_abstract"]
The following table describes the advanced authentication configuration fields available as Technology Preview in OpenShift Container Platform.

.Advanced `oidcProviders` configuration fields
[cols="1,2",options="header"]
|===
|Parameter
|Description

|`issuer.discoveryURL`
a|Optional parameter. Custom OIDC discovery endpoint URL for retrieving identity provider metadata from a non-standard location.

Requirements:

* Must be a valid HTTPS URL
* Must differ from `issuer.issuerURL`

When not specified, OpenShift Container Platform constructs the discovery URL by using the standard OIDC format: `{issuerURL}/.well-known/openid-configuration`.

*Example:*

[source,yaml]
----
issuer:
  issuerURL: https://idp.example.com
  discoveryURL: https://custom-discovery.example.com/.well-known/openid-configuration
----

|`claimValidationRules`
a|Optional parameter. Array of validation rules for JWT token claims using Common Expression Language (CEL) expressions. All rules must evaluate to `true` for authentication to succeed (AND operation).

Each rule has:

* `type`: Set to `CEL` for CEL-based validation
* `cel`: Object with `expression` (must evaluate to `true`) and `message` (error text)

CEL expressions access claims by using `claims` variable (for example, `claims.sub`).

*Example:*

[source,yaml]
----
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.exp - claims.nbf <= 86400'
    message: 'Total token lifetime must not exceed 24 hours'
- type: CEL
  cel:
    expression: 'has(claims.email) && claims.email.contains("@example.com")'
    message: 'Email claim must be present and from example.com domain'
----

|`claimValidationRules[].type`
a|Required. Validation rule type. Set to `CEL` for CEL-based validation. Requires `cel` field.

|`claimValidationRules[].cel`
a|Required when `type` is `CEL`. Contains `expression` (CEL expression to evaluate) and `message` (error text).

|`claimValidationRules[].cel.expression`
a|Required. CEL expression that validates token claims. Must evaluate to `true` for authentication to succeed.

Constraints: 1-1024 characters, must evaluate to boolean.

Access claims by using `claims` variable: `claims.sub`, `claims.foo.bar` (nested), `has(claims.email)` (existence check).

[NOTE]
====
When using the `email` claim in CEL expressions, you must also validate the `email_verified` claim to ensure the email address has been verified by the identity provider. For example: `claims.email_verified && claims.email.endsWith("@example.com")`.
====

|`claimValidationRules[].cel.message`
a|Required. Error message displayed when validation fails. Constraints: 1-256 characters.

|`userValidationRules`
a|Optional parameter. Array of validation rules for user objects by using CEL expressions. All rules must evaluate to `true` for authentication to succeed (AND operation).

Each rule has `expression` (must evaluate to `true`) and `message` (error text).

CEL expressions access user object by using `user` variable: `user.username` (string), `user.groups` (array), `user.uid` (string), `user.extra` (map).

*Example:*

[source,yaml]
----
userValidationRules:
- expression: "!user.username.startsWith('system:')"
  message: 'Username cannot use reserved system: prefix'
- expression: "!user.groups.exists(g, g.startsWith('system:'))"
  message: 'Groups cannot use reserved system: prefix'
----

|`userValidationRules[].expression`
a|Required. CEL expression that validates the user object. Must evaluate to `true` for authentication to succeed.

Constraints: 1-1024 characters, must evaluate to boolean.

Access user fields: `user.username.startsWith('system:')`, `user.groups.exists(g, g == "admin")`, `user.extra["example.com/role"]`.

|`userValidationRules[].message`
a|Required. Error message displayed when validation fails. Must not be empty.

|===

[role="_additional-resources"]
.Additional resources

* Enabling direct authentication with an external OIDC identity provider
* Common Expression Language (CEL) specification
* Common Expression Language in Kubernetes
