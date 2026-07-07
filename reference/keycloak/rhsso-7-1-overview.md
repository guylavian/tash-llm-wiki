---
title: "Chapter 1. Overview - Red Hat Single Sign-On 7.1 Authorization Services Guide"
type: reference
domain: keycloak
slug: rhsso-7-1-overview
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.1/html/authorization_services_guide/overview
guide: authorization_services_guide
version: 7.1
family: rhsso
documentKind: "Documentation"
abstract: "Note Authorization Services is a Technology Preview feature and is not fully supported. This feature is disabled by default. To enable Authorization Services add the standalone/configuration/profile.properties file with the contents profile=preview or start the server with -Dkeycloak.profile=preview to enable all technology preview features. Red Hat Single Sign-On supports fine-grained authorizati…"
---

# Chapter 1. Overview - Red Hat Single Sign-On 7.1 Authorization Services Guide

Chapter 1. Overview
Authorization Services is a Technology Preview feature and is not fully supported. This feature is disabled by default.
To enable Authorization Services add the standalone/configuration/profile.properties
file with the contents profile=preview
or start the server with -Dkeycloak.profile=preview
to enable all technology preview features.
Red Hat Single Sign-On supports fine-grained authorization policies and is able to combine different access control mechanisms such as:
- Attribute-based access control (ABAC)
- Role-based access control (RBAC)
- User-based access control (UBAC)
- Context-based access control (CBAC)
Rule-based access control
- Using Javascript
- Using JBoss Drools
- Time-based access control
- Support for custom access control mechanisms (ACMs) through a Policy Provider Service Provider Interface (SPI)
Red Hat Single Sign-On is based on a set of administrative UIs and a RESTful API, and provides the necessary means to create permissions for your protected resources and scopes, associate those permissions with authorization policies, and enforce authorization decisions in your applications and services.
Resource servers (applications or services serving protected resources) usually rely on some kind of information to decide if access should be granted to a protected resource. For RESTful-based resource servers, that information is usually obtained from a security token, usually sent as a bearer token on every request to the server. For web applications that rely on a session to authenticate users, that information is usually stored in a user’s session and retrieved from there for each request.
Frequently, resource servers only perform authorization decisions based on role-based access control (RBAC), where the roles granted to the user trying to access protected resources are checked against the roles mapped to these same resources. While roles are very useful and used by applications, they also have a few limitations:
- Resources and roles are tightly coupled and changes to roles (such as adding, removing, or changing an access context) can impact multiple resources
- Changes to your security requirements can imply deep changes to application code to reflect these changes
- Depending on your application size, role management might become difficult and error-prone
- It is not the most flexible access control mechanism. Roles do not represent who you are and lack contextual information. If you have been granted a role, you have at least some access.
Considering that today we need to consider heterogeneous environments where users are distributed across different regions, with different local policies, using different devices, and with a high demand for information sharing, Red Hat Single Sign-On Authorization Services can help you improve the authorization capabilities of your applications and services by providing:
- Resource protection using fine-grained authorization policies and different access control mechanisms
- Centralized Resource, Permission, and Policy Management
- Centralized Policy Decision Point
- REST security based on a set of REST-based authorization services
- Authorization workflows and User-Managed Access
- The infrastructure to help avoid code replication across projects (and redeploys) and quickly adapt to changes in your security requirements.
1.1. Architecture
From a design perspective, Authorization Services is based on a well-defined set of authorization patterns providing these capabilities:
Policy Administration Point (PAP)
Provides a set of UIs based on the Red Hat Single Sign-On Administration Console to manage resource servers, resources, scopes, permissions, and policies. Part of this is also accomplished remotely through the use of the Protection API.
Policy Decision Point (PDP)
Provides a distributable policy decision point to where authorization requests are sent and policies are evaluated accordingly with the permissions being requested. Part of this is also accomplished remotely through the use of the Entitlement APIs.
Policy Enforcement Point (PEP)
Provides implementations for different environments to actually enforce authorization decisions at the resource server side. Red Hat Single Sign-On provides some built-in Policy Enforcers.
Policy Information Point (PIP)
Being based on Red Hat Single Sign-On Authentication Server, you can obtain attributes from identities and runtime environment during the evaluation of authorization policies.
1.1.1. The Authorization Process
Three main processes define the necessary steps to understand how to use Red Hat Single Sign-On to enable fine-grained authorization to your applications:
- Resource Management
- Permission and Policy Management
- Policy Enforcement
1.1.1.1. Resource Management
Resource Management involves all the necessary steps to define what is being protected.
First, you need to specify Red Hat Single Sign-On what are you looking to protect, which usually represents a web application or a set of one or more services. For more information on resource servers see Terminology.
Resource servers are managed using the Red Hat Single Sign-On Administration Console. There you can enable any registered client application as a resource server and start managing the resources and scopes you want to protect.
A resource can be a web page, a RESTFul resource, a file in your file system, an EJB, and so on. They can represent a group of resources (just like a Class in Java) or they can represent a single and specific resource.
For instance, you might have a Bank Account resource that represents all banking accounts and use it to define the authorization policies that are common to all banking accounts. However, you might want to define specific policies for Alice Account (a resource instance that belongs to a customer), where only the owner is allowed to access some information or perform an operation.
Resources can be managed using the Red Hat Single Sign-On Administration Console or the Protection API. In the latter case, resource servers are able to manage their resources remotely.
Scopes usually represent the actions that can be performed on a resource, but they are not limited to that. You can also use scopes to represent one or more attributes within a resource.
1.1.1.2. Permission and Policy Management
Once you have defined your resource server and all the resources you want to protect, you must set up permissions and policies.
This process involves all the necessary steps to actually define the security and access requirements that govern your resources.
Policies define the conditions that must be satisfied to access or perform operations on something (resource or scope), but they are not tied to what they are protecting. They are generic and can be reused to build permissions or even more complex policies.
For instance,to allow access to a group of resources only for users granted with a role "User Premium,"" you can use RBAC (Role-based Access Control).
Red Hat Single Sign-On provides a few built-in policy types (and their respective policy providers) covering the most common access control mechanisms. You can even create policies based on rules written using JavaScript or JBoss Drools.
Once you have your policies defined, you can start defining your permissions. Permissions are coupled with the resource they are protecting. Here you specify what you want to protect (resource or scope) and the policies that must be satisfied to grant or deny permission.
1.1.1.3. Policy Enforcement
Policy Enforcement involves the necessary steps to actually enforce authorization decisions to a resource server. This is achieved by enabling a Policy Enforcement Point or PEP at the resource server that is capable of communicating with the authorization server, ask for authorization data and control access to protected resources based on the decisions and permissions returned by the server.
Red Hat Single Sign-On provides some built-in Policy Enforcers implementations that you can use to protect your applications depending on the platform they are running on.
1.1.2. Authorization Services
Authorization services consist of the following RESTFul APIs:
- Protection API
- Authorization API
- Entitlement API
Each of these services provides a specific API covering the different steps involved in the authorization process.
1.1.2.1. Protection API
The Protection API is a UMA-compliant endpoint providing a small set of operations for resource servers to help them manage their resources and scopes. Only resource servers are allowed to access this API, which also requires a uma_protection scope.
The operations provided by the Protection API can be organized in two main groups:
Resource Management
- Create Resource
- Delete Resource
- Find by Id
- Find All
- Find with filters (for example, search by name, type, or URI)
Permission Management
- Issue Permission Tickets
By default, Remote Resource Management is enabled. You can change that using the Red Hat Single Sign-On Administration Console and only allow resource management through the console.
When using the UMA protocol, the issuance of Permission Tickets by the Protection API is an important part of the whole authorization process. As described in a subsequent section, they represent the permissions being requested by the client and that are sent to the server to obtain a final token with all permissions granted during the evaluation of the permissions and policies associated with the resources and scopes being requested.
For more information, see Protection API.
1.1.2.2. Authorization API
The Authorization API is also a UMA-compliant endpoint providing a single operation that exchanges an Access Token and Permission Ticket with a Requesting Party Token (RPT).
The RPT contains all permissions granted to a client and can be used to call a resource server to get access to its protected resources.
When requesting an RPT you can also provide a previously issued RPT. In this case, the resulting RPT will consist of the union of the permissions from the previous RPT and the new ones within a permission ticket.
For more information, see Authorization API.
1.1.3. Entitlement API
The Entitlement API provides a 1-legged protocol to issue RPTs. Unlike the Authorization API, the Entitlement API only expects an access token.
From this API you can obtain all the entitlements or permissions for a user (based on the resources managed by a given resource server) or just the entitlements for a set of one or more resources.
For more information see Entitlement API.
1.2. Terminology
Before going further, it is important to understand these terms and concepts introduced by Red Hat Single Sign-On Authorization Services.
1.2.1. Resource Server
Per OAuth2 terminology, a resource server is the server hosting the protected resources and capable of accepting and responding to protected resource requests.
Resource servers usually rely on some kind of information to decide whether access to a protected resource should be granted. For RESTful-based resource servers, that information is usually carried in a security token, typically sent as a bearer token along with every request to the server. Web applications that rely on a session to authenticate users usually store that information in the user’s session and retrieve it from there for each request.
In Red Hat Single Sign-On, any confidential client application can act as a resource server. This client’s resources and their respective scopes are protected and governed by a set of authorization policies.
1.2.2. Resource
A resource is part of the assets of an application and the organization. It can be a set of one or more endpoints, a classic web resource such as an HTML page, and so on. In authorization policy terminology, a resource is the object being protected.
Every resource has a unique identifier that can represent a single resource or a set of resources. For instance, you can manage a Banking Account Resource that represents and defines a set of authorization policies for all banking accounts. But you can also have a different resource named Alice’s Banking Account, which represents a single resource owned by a single customer, which can have its own set of authorization policies.
1.2.3. Scope
A resource’s scope is a bounded extent of access that is possible to perform on a resource. In authorization policy terminology, a scope is one of the potentially many verbs that can logically apply to a resource.
It usually indicates what can be done with a given resource. Example of scopes are view, edit, delete, and so on. However, scope can also be related to specific information provided by a resource. In this case, you can have a project resource and a cost scope, where the cost scope is used to define specific policies and permissions for users to access a project’s cost.
1.2.4. Permission
Consider this simple and very common permission:
A permission associates the object being protected with the policies that must be evaluated to determine whether access is granted.
X CAN DO Y ON RESOURCE Z
where …
- X represents one or more users, roles, or groups, or a combination of them. You can also use claims and context here.
- Y represents an action to be performed, for example, write, view, and so on.
- Z represents a protected resource, for example, "/accounts".
Red Hat Single Sign-On provides a rich platform for building a range of permission strategies ranging from simple to very complex, rule-based dynamic permissions. It provides flexibility and helps to:
- Reduce code refactoring and permission management costs
- Support a more flexible security model, helping you to easily adapt to changes in your security requirements
- Make changes at runtime; applications are only concerned about the resources and scopes being protected and not how they are protected.
1.2.5. Policy
A policy defines the conditions that must be satisfied to grant access to an object. Unlike permissions, you do not specify the object being protected but rather the conditions that must be satisfied for access to a given object (for example, resource, scope, or both). Policies are strongly related to the different access control mechanisms (ACMs) that you can use to protect your resources. With policies, you can implement strategies for attribute-based access control (ABAC), role-based access control (RBAC), context-based access control, or any combination of these.
Red Hat Single Sign-On leverages the concept of policies and how you define them by providing the concept of aggregated policies, where you can build a "policy of policies" and still control the behavior of the evaluation. Instead of writing one large policy with all the conditions that must be satisfied for access to a given resource, the policies implementation in Red Hat Single Sign-On Authorization Services follows the divide-and-conquer technique. That is, you can create individual policies, then reuse them with different permissions and build more complex policies by combining individual policies.
1.2.6. Policy Provider
Policy providers are implementations of specific policy types. Red Hat Single Sign-On provides built-in policies, backed by their corresponding policy providers, and you can create your own policy types to support your specific requirements.
Red Hat Single Sign-On provides a SPI (Service Provider Interface) that you can use to plug in your own policy provider implementations.
1.2.7. Permission Ticket
A permission ticket is a special type of token defined by the OAuth2’s User-Managed Access (UMA) Profile specification that provides an opaque structure whose form is determined by the authorization server. This structure represents the resources and/or scopes being requested by a client as well as the policies that must be applied to a request for authorization data (requesting party token [RPT]).
In UMA, permission tickets are crucial to support person-to-person sharing and also person-to-organization sharing. Using permission tickets for authorization workflows enables a range of scenarios from simple to complex, where resource owners and resource servers have complete control over their resources based on fine-grained policies that govern the access to these resources.
In the UMA workflow, permission tickets are issued by the authorization server to a resource server, which returns the permission ticket to the client trying to access a protected resource. Once the client receives the ticket, it can make a request for an RPT (a final token holding authorization data) by sending the ticket back to the authorization server.
For more information on permission tickets, see Authorization API and the UMA specification.
