---
title: "Chapter 6. Managing permissions - Red Hat build of Keycloak 26.2 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-permission-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/authorization_services_guide/permission_overview
guide: authorization_services_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
abstract: "A permission associates the object being protected and the policies that must be evaluated to decide whether access should be granted. After creating the resources you want to protect and the policies you want to use to protect these resources, you can start managing permissions. To manage permissions, click the Permissions tab when editing a resource server. Permissions Permissions can be created…"
---

# Chapter 6. Managing permissions - Red Hat build of Keycloak 26.2 Authorization Services Guide

Chapter 6. Managing permissions
A permission associates the object being protected and the policies that must be evaluated to decide whether access should be granted.
After creating the resources you want to protect and the policies you want to use to protect these resources, you can start managing permissions. To manage permissions, click the Permissions tab when editing a resource server.
Permissions
Permissions can be created to protect two main types of objects:
- Resources
- Scopes
To create a permission, select the permission type you want to create from the item list in the upper right corner of the permission listing. The following sections describe these two types of objects in more detail.
6.1. Creating resource-based permission
A resource-based permission defines a set of one or more resources to protect using a set of one or more authorization policies.
To create a new resource-based permission, select Create resource-based permission from the Create permission dropdown.
Add Resource Permission
6.1.1. Configuration
Name
A human-readable and unique string describing the permission. A best practice is to use names that are closely related to your business and security requirements, so you can identify them more easily.
Description
A string containing details about this permission.
Apply To Resource Type
Specifies if the permission is applied to all resources with a given type. When selecting this field, you are prompted to enter the resource type to protect.
Resource Type
Defines the resource type to protect. When defined, this permission is evaluated for all resources matching that type.
Resources
Defines a set of one or more resources to protect.
Policy
Defines a set of one or more policies to associate with a permission. To associate a policy you can either select an existing policy or create a new one by selecting the type of the policy you want to create.
Decision Strategy
The Decision Strategy for this permission.
6.1.2. Typed resource permission
Resource permissions can also be used to define policies that are to be applied to all resources with a given type. This form of resource-based permission can be useful when you have resources sharing common access requirements and constraints.
Frequently, resources within an application can be categorized (or typed) based on the data they encapsulate or the functionality they provide. For example, a financial application can manage different banking accounts where each one belongs to a specific customer. Although they are different banking accounts, they share common security requirements and constraints that are globally defined by the banking organization. With typed resource permissions, you can define common policies to apply to all banking accounts, such as:
- Only the owner can manage his account
- Only allow access from the owner’s country and/or region
- Enforce a specific authentication method
To create a typed resource permission, click Apply to Resource Type when creating a new resource-based permission. With Apply to Resource Type
set to On
, you can specify the type that you want to protect as well as the policies that are to be applied to govern access to all resources with the type you have specified.
Example of a typed resource permission
6.2. Creating scope-based permissions
A scope-based permission defines a set of one or more scopes to protect using a set of one or more authorization policies. Unlike resource-based permissions, you can use this permission type to create permissions not only for a resource, but also for the scopes associated with it, providing more granularity when defining the permissions that govern your resources and the actions that can be performed on them.
To create a new scope-based permission, select Create scope-based permission from the Create permission dropdown.
Add Scope Permission
6.2.1. Configuration
Name
A human-readable and unique string describing the permission. A best practice is to use names that are closely related to your business and security requirements, so you can identify them more easily.
Description
A string containing details about this permission.
Resource
Restricts the scopes to those associated with the selected resource. If none is selected, all scopes are available.
Scopes
Defines a set of one or more scopes to protect.
Policy
Defines a set of one or more policies to associate with a permission. To associate a policy you can either select an existing policy or create a new one by selecting the type of the policy you want to create.
Decision Strategy
The Decision Strategy for this permission.
6.3. Policy decision strategies
When associating policies with a permission, you can also define a decision strategy to specify how to evaluate the outcome of the associated policies to determine access.
Unanimous
The default strategy if none is provided. In this case, all policies must evaluate to a positive decision for the final decision to be also positive.
Affirmative
In this case, at least one policy must evaluate to a positive decision for the final decision to be also positive.
Consensus
In this case, the number of positive decisions must be greater than the number of negative decisions. If the number of positive and negative decisions is equal, the final decision will be negative.
