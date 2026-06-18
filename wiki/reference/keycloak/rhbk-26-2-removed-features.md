---
title: "Chapter 18. Removed features - Red Hat build of Keycloak 26.2 Release Notes"
type: reference
domain: keycloak
slug: rhbk-26-2-removed-features
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/release_notes/removed_features
guide: release_notes
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "In previous sections, some features have already been mentioned as removed. The following sections provide details on other removed features. 18.1. OpenShift v3 identity brokering Because OpenShift v3 reached end-of-life, support for identity brokering with OpenShift v3 has been removed from Red Hat build of Keycloak. 18.2. robots.txt file The robots.txt file, previously included by default, is no…"
---

# Chapter 18. Removed features - Red Hat build of Keycloak 26.2 Release Notes

Chapter 19. Removed features
In previous sections, some features have already been mentioned as removed. The following sections provide details on other removed features.
19.1. OpenShift v3 identity brokering
Because OpenShift v3 reached end-of-life, support for identity brokering with OpenShift v3 has been removed from Red Hat build of Keycloak.
19.2. robots.txt file
The robots.txt
file, previously included by default, is now removed. The default robots.txt
file blocked all crawling, which prevented the noindex
/nofollow
directives from being followed. The desired default behavior is for Red Hat build of Keycloak pages to not show up in search engine results and this is accomplished by the existing X-Robots-Tag
header, which is set to none
by default. The value of this header can be overridden per-realm if a different behavior is needed.
If you previously added a rule in your reverse proxy configuration for this situation, you can now remove it.
19.3. X-XSS-Protection header
Because the X-XSS-Protection
header is no longer supported by any user agents that are supported by Red Hat build of Keycloak, it has been removed. This header was a feature of Internet Explorer, Chrome, and Safari that stopped pages from loading when they detected reflected cross-site scripting (XSS) attacks.
We don’t expect that this will impact any deployments due to the lack of support in user agents, as well as this feature being supplanted by Content Security Policy (CSP).
