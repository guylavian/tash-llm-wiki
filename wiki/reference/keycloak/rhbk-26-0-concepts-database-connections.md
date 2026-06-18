---
title: "Chapter 4. Concepts for database connection pools - Red Hat build of Keycloak 26.0 High Availability Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-concepts-database-connections
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/concepts-database-connections-
guide: high_availability_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "This section is intended when you want to understand considerations and best practices on how to configure database connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator. 4.1. Concepts Creating new database connections is expensive as it takes time. Creating them when a re…"
---

# Chapter 4. Concepts for database connection pools - Red Hat build of Keycloak 26.0 High Availability Guide

Chapter 4. Concepts for database connection pools
This section is intended when you want to understand considerations and best practices on how to configure database connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploy Red Hat build of Keycloak for HA with the Red Hat build of Keycloak Operator.
4.1. Concepts
Creating new database connections is expensive as it takes time. Creating them when a request arrives will delay the response, so it is good to have them created before the request arrives. It can also contribute to a stampede effect where creating a lot of connections in a short time makes things worse as it slows down the system and blocks threads. Closing a connection also invalidates all server side statements caching for that connection.
For the best performance, the values for the initial, minimal and maximum database connection pool size should all be equal. This avoids creating new database connections when a new request comes in which is costly.
Keeping the database connection open for as long as possible allows for server side statement caching bound to a connection. In the case of PostgreSQL, to use a server-side prepared statement, a query needs to be executed (by default) at least five times.
See the PostgreSQL docs on prepared statements for more information.
