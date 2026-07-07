---
title: "Content Security Policy (CSP)"
type: reference
domain: openshift
slug: web-console-4-22-content-security-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/content-security-policy
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Content Security Policy (CSP)

[id="content-security-policy_{context}"]
= Content Security Policy (CSP)

[role="_abstract"]
You can specify Content Security Policy (CSP) directives for your dynamic plugin using the `contentSecurityPolicy` field in the `ConsolePluginSpec` file. This field helps mitigate potential security risks by specifying which sources are allowed for fetching content like scripts, styles, images, and fonts. For dynamic plugins that require loading resources from external sources, defining custom CSP rules ensures secure integration into the OpenShift Container Platform console.

[IMPORTANT]
====
The console currently uses the `Content-Security-Policy-Report-Only` response header, so the browser will only warn about CSP violations in the web console and enforcement of CSP policies will be limited. CSP violations will be logged in the browser console, but the associated CSP directives will not be enforced. This feature is behind a `feature-gate`, so you will need to manually enable it.

For more information, see Enabling feature sets using the web console.
====

// Module included in the following assemblies:
//
// * web_console/dynamic-plugin/content-security-policy.adoc

[id="content-security-policy-overview_{context}"]
= Key features of Content Security Policy (CSP)

[role="_abstract"]
A Content Security Policy (CSP) is delivered to the browser in the `Content-Security-Policy-Report-Only` response header. The policy is specified as a series of directives and values. Each directive type serves a different purpose, and each directive can have a list of values representing allowed sources.

[id="content-security-policy-directive-types_{context}"]
== Directive Types
The supported directive types include `DefaultSrc`, `ScriptSrc`, `StyleSrc`, `ImgSrc`, and `FontSrc`. These directives allow you to specify valid sources for loading different types of content for your plugin. Each directive type serves a different purpose. For example, `ScriptSrc` defines valid JavaScript sources, while `ImgSrc` controls where images can be loaded from.

//backporting the ConnectSrc directive, but that is tbd - openshift/console#14701 and https://github.com/openshift/api/pull/2164
[id="content-security-policy-values_{context}"]
== Values
Each directive can have a list of values representing allowed sources. For example, `ScriptSrc` can specify multiple external scripts. These values are restricted to 1024 characters and cannot include whitespace, commas, or semicolons. Additionally, single-quoted strings and wildcard characters (`*`) are disallowed.

[id="content-security-policy-unified-policy_{context}"]
== Unified Policy
The OpenShift Container Platform web console aggregates the CSP directives across all enabled `ConsolePlugin` custom resources (CRs) and merges them with its own default policy. The combined policy is then applied with the `Content-Security-Policy-Report-Only` HTTP response header.

[id="content-security-policy-validation-rules_{context}"]
== Validation Rules
* Each directive can have up to 16 unique values.
* The total size of all values across directives must not exceed 8192 bytes (8KB).
* Each value must be unique, and additional validation rules are in place to ensure no quotes, spaces, commas, or wildcard symbols are used.

[role="_additional-resources"]
[id="content-security-policy_additional-resources"]
== Additional resources

* Content Security Policy (CSP)
