---
title: "Chapter 3. Updates for 26.2.15 - Red Hat build of Keycloak 26.2 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-2-updates-for-26-2-15
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/release_notes/updates_for_26_2_15
guide: release_notes
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "This release contains several fixed issues. 3.1. Maximum length of the parameters in the OIDC token endpoint When the OIDC token endpoint request (or OAuth2 token endpoint request) is sent, a new limit exists for the maximum length of every OIDC/OAuth2 parameter. The maximum length of each parameter is 4,000 characters, which is aligned with the same limit, which already exists for the parameters …"
---

# Chapter 3. Updates for 26.2.15 - Red Hat build of Keycloak 26.2 Release Notes

Chapter 4. Updates for 26.2.15
This release contains several fixed issues.
4.1. Maximum length of the parameters in the OIDC token endpoint
When the OIDC token endpoint request (or OAuth2 token endpoint request) is sent, a new limit exists for the maximum length of every OIDC/OAuth2 parameter. The maximum length of each parameter is 4,000 characters, which is aligned with the same limit, which already exists for the parameters sent to OIDC/OAuth authentication request.
If you want to increase or lower those numbers, start the server with the option req-params-default-max-size
for the default maximum length of the OIDC/OAuth2 parameters, or you can use something such as req-params-max-size
for one specific parameter. For more details, see the login-protocol
provider configuration in the All Provider Configuration Guide.
4.2. CVE fixes
The following bug fix advisories list the fixed CVEs for the ZIP file distribution and the container image:
