---
title: "Configuring alert notifications"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-configuring-alert-notifications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/configuring-alert-notifications
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Configuring alert notifications

[id="configuring-alert-notifications"]
= Configuring alert notifications

In OpenShift Container Platform, an alert is fired when the conditions defined in an alerting rule are true. An alert provides a notification that a set of circumstances are apparent within a cluster. Firing alerts can be viewed in the Alerting UI in the OpenShift Container Platform web console by default. After an installation, you can configure OpenShift Container Platform to send alert notifications to external systems.

// Module included in the following assemblies:
//
// * observability/monitoring/managing-alerts.adoc
// * post_installation_configuration/configuring-alert-notifications.adoc

[id="sending-notifications-to-external-systems_{context}"]
= Sending notifications to external systems

In OpenShift Container Platform

, firing alerts can be viewed in the Alerting UI. Alerts are not configured by default to be sent to any notification systems. You can configure OpenShift Container Platform to send alerts to the following receiver types:

* PagerDuty
* Webhook
* Email
* Slack
* Microsoft Teams

Routing alerts to receivers enables you to send timely notifications to the appropriate teams when failures occur. For example, critical alerts require immediate attention and are typically paged to an individual or a critical response team. Alerts that provide non-critical warning notifications might instead be routed to a ticketing system for non-immediate review.

.Checking that alerting is operational by using the watchdog alert

OpenShift Container Platform monitoring includes a watchdog alert that fires continuously. Alertmanager repeatedly sends watchdog alert notifications to configured notification providers. The provider is usually configured to notify an administrator when it stops receiving the watchdog alert. This mechanism helps you quickly identify any communication issues between Alertmanager and the notification provider.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* About OpenShift Container Platform monitoring
* Configuring alerts and notifications for core platform monitoring
* Configuring alerts and notifications for user workload monitoring
