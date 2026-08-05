---
title: "Chapter 23. KafkaAuthorizationKeycloak schema reference - Red Hat Streams for Apache Kafka 3.0 Streams for Apache Kafka API Reference"
type: reference
domain: keycloak
slug: doc-type-kafkaauthorizationkeycloak-reference-2
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/3.0/html/streams_for_apache_kafka_api_reference/type-kafkaauthorizationkeycloak-reference
guide: streams_for_apache_kafka_api_reference
documentKind: "Documentation"
abstract: "Used in: KafkaClusterSpec The type property is a discriminator that distinguishes use of the KafkaAuthorizationKeycloak type from KafkaAuthorizationSimple, KafkaAuthorizationOpa, KafkaAuthorizationCustom. It must have the value keycloak for the type KafkaAuthorizationKeycloak. Property Property type Description type string Must be keycloak. clientId string OAuth Client ID which the Kafka client ca…"
---

# Chapter 23. KafkaAuthorizationKeycloak schema reference - Red Hat Streams for Apache Kafka 3.0 Streams for Apache Kafka API Reference

Chapter 23. KafkaAuthorizationKeycloak schema reference
Used in: KafkaClusterSpec
The type
property is a discriminator that distinguishes use of the KafkaAuthorizationKeycloak
type from KafkaAuthorizationSimple
, KafkaAuthorizationOpa
, KafkaAuthorizationCustom
. It must have the value keycloak
for the type KafkaAuthorizationKeycloak
.
| Property | Property type | Description |
|---|---|---|
| type | string |
Must be |
| clientId | string | OAuth Client ID which the Kafka client can use to authenticate against the OAuth server and use the token endpoint URI. |
| tokenEndpointUri | string | Authorization server token endpoint URI. |
| tlsTrustedCertificates |
| Trusted certificates for TLS connection to the OAuth server. |
| disableTlsHostnameVerification | boolean |
Enable or disable TLS hostname verification. Default value is |
| delegateToKafkaAcls | boolean |
Whether authorization decision should be delegated to the 'Simple' authorizer if DENIED by Red Hat build of Keycloak Authorization Services policies. Default value is |
| grantsRefreshPeriodSeconds | integer | The time between two consecutive grants refresh runs in seconds. The default value is 60. |
| grantsRefreshPoolSize | integer | The number of threads to use to refresh grants for active sessions. The more threads, the more parallelism, so the sooner the job completes. However, using more threads places a heavier load on the authorization server. The default value is 5. |
| grantsMaxIdleTimeSeconds | integer | The time, in seconds, after which an idle grant can be evicted from the cache. The default value is 300. |
| grantsGcPeriodSeconds | integer | The time, in seconds, between consecutive runs of a job that cleans stale grants from the cache. The default value is 300. |
| grantsAlwaysLatest | boolean |
Controls whether the latest grants are fetched for a new session. When enabled, grants are retrieved from Red Hat build of Keycloak and cached for the user. The default value is |
| superUsers | string array | List of super users. Should contain list of user principals which should get unlimited access rights. |
| connectTimeoutSeconds | integer | The connect timeout in seconds when connecting to authorization server. If not set, the effective connect timeout is 60 seconds. |
| readTimeoutSeconds | integer | The read timeout in seconds when connecting to authorization server. If not set, the effective read timeout is 60 seconds. |
| httpRetries | integer | The maximum number of retries to attempt if an initial HTTP request fails. If not set, the default is to not attempt any retries. |
| enableMetrics | boolean |
Enable or disable OAuth metrics. The default value is |
| includeAcceptHeader | boolean |
Whether the Accept header should be set in requests to the authorization servers. The default value is |
