---
title: "Responsive restarts and security certificates"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-responsive-restarts-cas
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-responsive-restarts-cas
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Responsive restarts and security certificates

[id="microshift-responsive-restarts-cas"]
= Responsive restarts and security certificates

[role="_abstract"]
{microshift-short} automatically restarts when system configuration changes are detected. These changes include IP address updates, clock adjustments, and security certificate expiration.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-responsive-restarts-cas.adoc

[id="microshift-ip-address-clock-changes_{context}"]
= IP address changes or clock adjustments

[role="_abstract"]
{microshift-short} depends on device IP addresses and system-wide clock settings to remain consistent during its runtime. However, these settings might occasionally change on edge devices.

For example, DHCP or Network Time Protocol (NTP) updates can change times. When these changes occur, some {microshift-short} components might stop functioning properly. To mitigate this situation, {microshift-short} monitors the IP address and system time and restarts if either setting changes.

The threshold for a clock-driven restart is a time change of greater than 10 seconds in either direction. Small drifts during regular NTP service adjustments do not trigger a restart.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-responsive-restarts-cas.adoc

[id="microshift-certificate-lifetime_{context}"]
= Security certificate lifetime

[role="_abstract"]
{microshift-short} certificates are digital certificates that secure communication with communication protocols such as HTTPS. They fall into two basic categories:

Short-lived certificates:: Valid for one year. Most server or leaf certificates are short-lived.
Long-lived certificates:: Valid for 10 years. For example, the client certificate for `system:admin` user authentication, or the `kube-apiserver` external serving certificate signer.

{microshift-short} restarts automatically depending on certificate age.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-responsive-restarts-cas.adoc

[id="microshift-certificate-rotation_{context}"]
= Certificate rotation

[role="_abstract"]
Certificates that are expired or close to their expiration dates must be rotated to ensure continued {microshift-short} operation. Certificate rotation can occur automatically.

When {microshift-short} restarts for any reason, certificates that are close to expiring are rotated. A certificate that expires soon, or has already expired, can also cause an automatic {microshift-short} restart to perform a rotation.

[IMPORTANT]
====
If the rotated certificate is a {microshift-short} certificate authority (CA), all signed certificates are also rotated. If you created custom CAs, you must rotate them manually.
====

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-responsive-restarts-cas.adoc

[id="microshift-short-term-certificate-rotation_{context}"]
= Short-term-certificate rotation

[role="_abstract"]
Short-term certificates that are expired or close to their expiration dates must be rotated to ensure continued {microshift-short} operation.

The following situations describe {microshift-short} actions during short-term-certificate lifetime:

No rotation::
When a short-term certificate is up to 5 months old, no rotation occurs.

Rotation at restart::
When a short-term certificate is 5 to 8 months old, it is rotated when {microshift-short} starts or restarts.

Automatic restart for rotation::
When a short-term certificate is more than 8 months old, {microshift-short} can automatically restart to rotate and apply a new certificate.

// Module included in the following assemblies:
//
// * microshift_troubleshooting/microshift-responsive-restarts-cas.adoc

[id="microshift-long-term-certificate-rotation_{context}"]
= Long-term-certificate rotation

[role="_abstract"]
Long-term certificates that are expired or close to their expiration dates must be rotated to ensure continued {microshift-short} operation.

The following situations describe {microshift-short} actions during long-term certificate lifetime:

No rotation::
When a long-term certificate is up to 8.5 years old, no rotation occurs.

Rotation at restart::
When a long-term certificate is 8.5 to 9 years old, it is rotated when {microshift-short} starts or restarts.

Automatic restart for rotation::
When a long-term certificate is more than 9 years old, {microshift-short} might automatically restart so that it can rotate and apply a new certificate.

[id="additional-resources_microshift-responsive-restarts-cas"]
[role="_additional-resources"]
== Additional resources

* Configuring custom certificate authorities
