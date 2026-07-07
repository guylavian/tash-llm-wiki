---
title: "Chapter 4. Managing resources and scopes - Red Hat build of Keycloak 26.4 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-resource-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/authorization_services_guide/resource_overview
guide: authorization_services_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
abstract: "Resource management is straightforward and generic. After creating a resource server, you can start creating the resources and scopes that you want to protect. Resources and scopes can be managed by navigating to the Resource and Authorization Scopes tabs, respectively. 4.1. Viewing resources On the Resource page, you see a list of the resources associated with a resource server. Resources The res…"
---

# Chapter 4. Managing resources and scopes - Red Hat build of Keycloak 26.4 Authorization Services Guide

Chapter 4. Managing resources and scopes
Resource management is straightforward and generic. After creating a resource server, you can start creating the resources and scopes that you want to protect. Resources and scopes can be managed by navigating to the Resource and Authorization Scopes tabs, respectively.
4.1. Viewing resources
On the Resource page, you see a list of the resources associated with a resource server.
Resources
The resource list provides information about the protected resources, such as:
- Type
- Owner
- URIs
- Associated scopes, if any
- Associated permissions
From this list, you can also directly create a permission by clicking Create Permission for the resource for which you want to create the permission.
Before creating permissions for your resources, be sure you have already defined the policies that you want to associate with the permission.
4.2. Creating resources
Creating a resource is straightforward and generic. Your main concern is the granularity of the resources you create. In other words, resources can be created to represent a set of one or more resources and the way you define them is crucial to managing permissions.
To create a new resource, click Create resource.
Add resource
In Red Hat build of Keycloak, a resource defines a small set of information that is common to different types of resources, such as:
Name
A human-readable and unique string describing this resource.
Type
A string uniquely identifying the type of a set of one or more resources. The type is a string used to group different resource instances. For example, the default type for the default resource that is automatically created is
urn:resource-server-name:resources:default
URIS
URIS that provides the locations/addresses for the resource. For HTTP resources, the URIS are usually the relative paths used to serve these resources.
Scopes
One or more scopes to associate with the resource.
4.2.1. Resource attributes
Resources may have attributes associated with them. These attributes can be used to provide additional information about a resource and to provide additional information to policies when evaluating permissions associated with a resource.
Each attribute is a key and value pair where the value can be a set of one or many strings. Multiple values can be defined for an attribute by separating each value with a comma.
4.2.2. Typed resources
The type field of a resource can be used to group different resources together, so they can be protected using a common set of permissions.
4.2.3. Resource owners
Resources also have an owner. By default, resources are owned by the resource server.
However, resources can also be associated with users, so you can create permissions based on the resource owner. For example, only the resource owner is allowed to delete or update a given resource.
4.2.4. Managing resources remotely
Resource management is also exposed through the Protection API to allow resource servers to remotely manage their resources.
When using the Protection API, resource servers can be implemented to manage resources owned by their users. In this case, you can specify the user identifier to configure a resource as belonging to a specific user.
Red Hat build of Keycloak provides resource servers complete control over their resources. In the future, we should be able to allow users to control their own resources as well as approve authorization requests and manage permissions, especially when using the UMA protocol.
