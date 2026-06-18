---
title: "Chapter 12. Managing organizations - Red Hat build of Keycloak 26.2 Server Administration Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-managing-organizations
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_administration_guide/managing_organizations
guide: server_administration_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
---

# Chapter 12. Managing organizations - Red Hat build of Keycloak 26.2 Server Administration Guide

Chapter 12. Managing organizations
When integrating with a third party like a customer or business partner, you might want to manage their identities separately from others and build a unified and secure experience throughout your business ecosystem when they interact with a realm.
In a realm, an organization represents these third parties so that a realm or an organization administrator can manage the entire lifecycle of its members and how they authenticate and authorize to a realm, on a per-organization basis.
The organization is the entry point to start using the IAM capabilities of Red Hat build of Keycloak to also address Business-to-Business (B2B) use cases. It enables multi-tenancy within a realm so that users can have access to protected resources from a realm but with a more restricted and controlled context, that context being the organization to which they belong.
Red Hat build of Keycloak Organizations is a feature that enables support for organizations in Red Hat build of Keycloak. For now, it provides some of the core capabilities needed to manage organizations such as:
- Manage members
- Onboard organization members using invitation links
- Onboard organization members by federating their identities through identity brokering
- Identity-first login and organization-specific steps when authenticating in the scope of an organization
- Propagate organization-specific claims to applications through tokens for authorization purposes
12.1. Enabling organizations in Red Hat build of Keycloak
To use organizations, you have to enable the feature for the current realm.
Procedure
- Click Realm Settings in the menu.
- Toggle Organizations to On.
- Click Save
Enabling Organizations
Once the feature is enabled, you are able to manage organizations through the Organizations section available from the menu.
12.2. Managing an organization
From the Organizations section, you can manage all the organizations in your realm.
Managing organizations
12.2.1. Creating an organization
Procedure
- Click Create Organization.
Creating organization
An organization has the following settings:
- Name
- A user-friendly name for the organization. The name is unique within a realm.
- Alias
- An alias for this organization, used to reference the organization internally. The alias is unique within a realm and must be URL-friendly, so characters not usually allowed in URLs will not be allowed in the alias. If not set, Red Hat build of Keycloak will attempt to use the name as the alias. If the name is not URL-friendly, you will get an error and will be asked to specify an alias. Once defined, the alias cannot be changed afterwards.
- Redirect URL
- After completing registration or accepting an invitation to the organization sent via email, the user is automatically redirected to the specified redirect url. If left empty, the user will be redirected to the account console by default.
- Domains
- A set of one or more domains that belongs to this organization. A domain cannot be shared by different organizations within a realm.
- Description
- A free-text field to describe the organization.
Once you create an organization, you can manage the additional settings that are described in the following sections:
12.2.2. Understanding organization domains
When managing an organization, the domain associated with an organization plays an important role in how organization members authenticate to a realm and how their profiles are validated.
One of the key roles of a domain is to help to identify the organizations where a user is a member. By looking at their email address, Red Hat build of Keycloak will match a corresponding organization using the same domain and eventually change the authentication flow based on the organization requirements.
The domain also allows organizations to enforce that users are not allowed to use a domain in their emails other than those associated with an organization. This restriction is especially useful when users, and their identities, are federated from identity providers associated with an organization and you want to force a specific email domain for their email addresses.
12.2.3. Disabling an organization
To disable an organization, toggle Enabled to Off.
Disabling organization
When an organization is disabled, you can still manage it through the management interfaces, but the organization members cannot authenticate to the realm, including authenticating through the identity providers associated with the organization as they are also automatically disabled.
However, the unmanaged members of an organization are still able to authenticate to the realm as they are also realm users, but tokens will not hold metadata about their relationship with an organization that is disabled.
For more details about managed and unmanaged users, see Managed and unmanaged members section.
12.2.4. Deleting an organization
To delete an organization, click the Delete action for the corresponding organization in the listing page or when editing an organization.
Deleting organization
When removing an organization, all data associated with it will be deleted, including any managed member.
Unmanaged users and identity providers remain in the realm, but they are no longer linked to the organization.
For more details about managed and unmanaged users, see Managed and unmanaged members.
12.3. Managing attributes
An administrator can store additional metadata about an organization using attributes. An organization attribute is a key/value pair that can hold multiple string values.
For that, click the Attributes tab and set any attribute you want by providing a key and a value.
To provide multiple values for the same attribute, and key, just add another attribute with the same key but with a different value.
Managing organization attributes
12.4. Managing members
An organization member is basically a realm user but with a link to a single organization. They are logically separated from other users in a realm so that you know exactly which users belong to an organization.
There are different ways to add, or onboard, a member to an organization:
- Adding an existing realm user as a member
- Through an identity provider associated with an organization
- Sending an invitation to create a new account
- Sending an invitation to an existing user to join an organization
Once a member of an organization, that user’s account can be managed just like any regular account in a realm by accessing the Users section in the menu.
However, you can narrow the users to only those associated with an organization by accessing the Members tab when managing an organization. In this tab, you have a list of all the organization members and actions to add new members and to edit and remove existing ones.
Managing organization members
12.4.1. Managed and unmanaged members
When managing members, consider how their relationship with an organization affects the lifecycle of their accounts. Members can join an organization through different flows and each flow indicates the strength of the link between their accounts and the organization.
There are two types of members:
- Managed
- Unmanaged
Managed members are those managed by the organization, and they cannot exist outside of their organization. For instance, consider an account created through an identity provider associated with an organization. That account does not belong to a realm as it was federated from the organization. In this case, the single source of truth for the identity is the organization and its lifecycle is controlled by the organization. If you remove the organization or the member, the account is also removed from the realm.
On the other hand, unmanaged members are those that can exist without the organization. For instance, when adding an existing realm user to an organization, the account belongs to the realm first and foremost and eventually linked to an organization. In this case, removing an organization or a member will not remove the account from the realm; the realm is the single-source of truth for the identity.
12.4.2. Adding an existing realm user as a member
An existing realm user can join an organization by selecting that user from a list and adding the user to the organization.
Procedure
- Click Add member.
- Click Add realm user.
- Select one or more users and click Add to add them to the organization.
Adding a realm user
Once a user is a member of the organization, that user is able to authenticate to the realm just like a regular user and using any credential supported by the realm.
12.4.3. Inviting users
An administrator can email users to join an organization.
Procedure
- Click Add member.
- Click Invite member.
- Provide an email address
- Click Send
Inviting members
Optionally, you can also provide a value for the First name and Last name fields for a more personalized email message using a greeting message with the first and last names of the person receiving the email.
An invitation is basically an email sent with a link that the person should click to perform the necessary steps to join an organization. These steps depend on whether the person already has an account in the realm or if a new account should be created before joining the organization.
If the email maps to an existing user in a realm, the steps the user will follow are basically about confirming the intention to join the organization.
On the other hand, if no user is associated with the given email address, the steps will involve creating a new account through the realm’s self-registration flow. In this case, the user is forced to provide the same email address used to send the invitation.
12.4.4. Onboarding members using an Identity Provider
An organization might have its own identity provider as the single source of truth for their identities. In this case, users federated from the identity provider are automatically added as a member of the organization.
When users join an organization through an identity provider associated with an organization, they are automatically marked as managed members. In this case, they will go through the broker login flows configured in the realm and join the organization automatically once they successfully authenticate.
Onboarding new members through an identity provider can be done by either automatically redirecting the user to an organization’s identity provider or by selecting the identity provider when at the login page.
In both cases, once the user provides the email, Red Hat build of Keycloak will try to match an organization based on the email domain. In case the email domain matches the organization, and an identity provider is associated with the same domain and the Redirect when email domain matches setting is enabled, the user is automatically redirected to the identity provider. Once the user authenticates at the identity provider and completes the first broker login flow, the user is automatically added as an organization member.
On the other hand, if Redirect when email domain matches is not enabled, but the identity provider is configured not to Hide on login page, the user can select the identity provider and then be redirected to the identity provider to continue the onboarding process.
For more details, see Managing Identity Providers.
12.4.5. Removing a member
You can remove a member from an organization.
From the action menu next to the member you want to remove, click Remove.
When removing a member from an organization, remember that the user may or may not be removed from a realm depending on if that user is managed or unmanaged member, respectively.
For more details, see Managed and unmanaged members.
12.4.6. Support for federated members
Users coming from federated providers can also be added as members of an organization. The only exceptions are the users from LDAP providers with import mode disabled. Organization members are added to an internal group that is not synchronized with external providers, so even if the LDAP provider has a group mapper with mode LDAP_ONLY it won’t be possible for the non-imported users to be added as members of an organization because that membership won’t be synced with the LDAP server.
In other words, LDAP users that are not imported can’t join an organization because the membership is not stored in the local DB nor in the LDAP server. So if you want to have LDAP users joining organizations, ensure that the import mode of the LDAP provider is enabled.
12.5. Managing identity providers
An organization might have its own identity provider as the single source of truth for their identities. In this case, you want to configure the organization to authenticate users using the organization’s identity provider, federate their identities, and finally add them as a member of the organization.
An organization can have one or more identity providers associated with it so that they can authenticate their users from different sources and enforce different constraints on each of them.
Before you can link an identity provider to an organization, you create an organization at the realm level from the Identity Providers section in the menu. You can link any of the built-in social and identity providers available in the realm to an organization.
12.5.1. Linking an identity provider to an organization
An identity provider can be linked to an organization from the Identity providers tab. If identity providers already exist, you see a list of them and options to search, edit, or unlink from the organization.
Organization identity providers
Procedure
- Click Link identity provider
- Select an Identity provider
- Set the appropriate settings
- Click Save
Linking identity provider
An identity provider has the following settings:
- Identity provider
- The identity provider you want to link to the organization. An identity provider can only be linked to a single organization.
- Domain
- The domain from the organization that you want to link with the identity provider.
- Hide on login page
- If this identity provider should be hidden in login pages when the user is authenticating in the scope of the organization.
- Redirect when email domain matches
-
If members should be automatically redirected to the identity provider when their email domain matches the domain set to the identity provider. If the domain is set to
Any
, members whose email domain matches any of the organization domains will be redirected to the identity provider.
If the org is linked with multiple identity providers, the organization authenticator prioritizes the provider that matches the email domain of the user for automatic redirection. If none is found, it tries to locate one whose domain is set to Any
.
Once linked to an organization, the identity provider can be managed just like any other in a realm by accessing the Identity Providers section in the menu. However, the options herein described are only available when managing the identity provider in the scope of an organization. The only exception is the Hide on login page option that is present here for convenience.
12.5.2. Editing a linked identity provider
You can edit any of the organization-related settings of a linked identity provider at any time.
Procedure
- In the menu, click Organizations and go to the Identity providers tab.
Locate the identity provider in the list.
You can use the search option for this step.
- Click the action button (three dots) at the end of the line.
- Click Edit.
- Make the necessary changes.
- Click Save.
Editing linked identity provider
12.5.3. Unlinking an identity provider from an organization
When an identity provider is unlinked from an organization, it remains available as a realm-level provider that is no longer ssociated with an organization. To delete the unlinked provider, use the Identity Providers section in the menu.
Procedure
- In the menu, click Organizations and go to the Identity providers tab.
Locate the identity provider in the list.
You can use the search capabilities for this step.
- Click the action button (three dots) at the end of the line.
- Click Unlink provider.
Unlinking identity provider
12.6. Authenticating members
When you enable organizations for a realm, user authentication is changed. If the user is recognized to be authenticating in the context of an organization, the authentication flow changes on a per-organization basis.
When a realm is created, the authentication flows are automatically updated to enable specific steps to authenticate and onboard organization members. The authentication flows updated are:
- browser
- first broker login
The main change to the browser flow is that it defaults to an identity-first login so that users are identified before prompting for their credentials. Concerning the first broker login flow, the main change is automatically adding the users as organization members once they authenticate through the identity provider associated with an organization and successfully complete the flow.
The choice to use an identity-first login or not depends on the existence of an organization in a realm. If no organizations exist, the user follows the usual steps to authenticate using the username and password, or any other step configured in the browser flow. Otherwise, the user is asked first for a username or email to continue authenticating to a realm.
The identity-first login main goal is to identify the user:
- Is the user an existing or a new user?
- Is the user a member of any organization within a realm?
- If an organization member, is the user linked to any identity provider associated with the organization?
Depending on the outcome when identifying the user, the authentication flow changes to either proceed with authentication by asking for the user’s credentials or eventually redirect the user automatically to authenticate within the organization security boundaries through an identity provider.
12.6.1. Understanding the identity-first login
In addition to identifying the user once the username is provided, the identity-first login is also responsible for:
- Matching an email domain to an organization.
- Deciding if the authentication flow should continue or not if an account already exists for the username provided
- Deciding how the user should be authenticated depending on how the domains and the identity providers are configured to an organization
- Seamlessly authenticating users through an identity provider associated with an organization if the email domain matches the domain set to the identity provider
The identity-first login provides the same capabilities that are provided by the usual login page with the username and password fields. Users can still self-register by clicking the register link or choose any identity or social broker that is not linked to an organization in that realm.
Identity-first login page
In the case of a user that does not exist, if that user tries to authenticate using an email domain that matches an organization domain, the identity-first login page appears again with a message that the username provided is not valid. At this point, no need exists to ask the user for credentials.
Identity-first when user does not exist
Several options exist to register the user allowing that user to authenticate to the realm and join an organization.
If the realm has the self-registration setting enabled, the user can click the Register link at the identity-first login page and create an account at the realm. After that, the administrator can send an invitation link to the user or manually add the user as a member of an organization. For more details, see Managing members.
If the organization has an identity provider without a domain and the Hide on login page setting is OFF, users can also click the identity provider link at the identity-first login page to automatically create an account and join an organization once they authenticate through the identity provider. For more details, see Managing identity providers.
In a similar situation to the previous section, the organization may have an identity provider set with one of the organization domains. In this situation, the user is redirected to the identity provider if that user’s email matches a specific domain from the organization. Once the flow completes, an account is created and the user joins the organization.
12.6.2. Configuring existing authentication flows
As previously mentioned for new realms, authentication flows are automatically updated with the necessary steps to support organizations and authenticate their members. For existing realms, in addition to enabling organizations to the realm, you also need to manually update your existing (custom) authenticating flows.
Change the browser flow by following these steps:
Procedure
- Duplicate the current flow bound to the Browser flow binding type to avoid breaking the flow you are currently using
- Click Add sub-flow and give it a name such as My Organization
- Move the newly added My Organization sub-flow to execute right after the Identity Provider Redirector execution step. The main point here is that the sub-flow should happen before any other sub-flow or execution step that authenticates the user using whatever credentials you support in your realm. Once added, change the Requirement to Alternative.
- Click Add sub-flow in the My Organization sub-flow and give it a name such as My Organization - Conditional. Once added, change the Requirement to Conditional.
- Click Add condition in the My Organization - Conditional sub-flow and select Condition - user configured. Once added, change the Requirement to Required.
Click Add step in the My Organization - Conditional sub-flow and select the *Organization Identity-First Login
- execution step. Once added, change the Requirement to Alternative.
- Bind the authentication flow to the Browser binding type.
Organizations browser flow
Once you enable the Organizations setting to the realm and create at least a single organization, you should be able to see the identity-first login page and start using organizations in your realm.
Change the first broker login flow by following these steps:
Procedure
- Duplicate the current flow bound to the First broker login flow bind type to avoid breaking the flow you are currently using
-
Click Add sub-flow and give it a name such as
Organization Member - Conditional
. Once added, change the Requirement to Conditional. - Click Add condition in the Organization Member - Conditional sub-flow and select Condition - user configured. Once added, change the Requirement to Required.
- Click Add step in the Organization Member - Conditional sub-flow and select the Organization Member Onboard execution step. Once added, change the Requirement to Required.
- Bind the authentication flow to the First broker login binding type.
Organizations first broker flow
You should now be able to authenticate using any identity provider associated with an organization and have the user joining the organization as a member as soon as they complete the first browser login flow.
12.6.3. Configuring how users authenticate
If the flow supports organizations, you can configure some of the steps to change how users authenticate to the realm.
For example, some use cases will require users to authenticate to a realm only if they are a member of any or a specific organization in the realm.
To enable this behavior, you need to enable the Requires user membership
setting on the Organization Identity-First Login
execution step by clicking on its settings.
If enabled, and after the user provides the username or email in the identity-first login page, the server will try to resolve a organization where the user is a member by looking at any existing membership or based on the semantics of the organization scope, if requested by the client. If not a member of an organization, an error page will be shown.
12.7. Mapping organization claims
To map organization-specific claims into tokens, a client needs to request the organization scope when sending authorization requests to the server. When authenticating in the context of an organization, clients can request the organization
scope to map information about the organizations where the user is a member.
As a result, the token will contain a claim as follows:
"organization": {
"testcorp": {
"id": "42c3e46f-2477-44d7-a85b-d3b43f6b31fa",
"attr1": [
"value1"
]
}
}
The organization claim can be used by clients (for example, from ID Tokens) and resource servers (for example, from access tokens) to authorize access to protected resources based on the organization where the user is a member.
The organization
scope is a built-in optional client scope at the realm. Therefore, this scope is added to any client created in the realm by default. It also defines the Organization Membership
mapper that controls how the organization membership information is mapped to the tokens.
By default, the organization id and attributes are not included in the organization claim. To include them, edit the mapper and enable the Add organization id and Add organization attributes options, respectively.
Including attributes in the organization claim
The organization
scope is requested using different formats:
| Format | Description |
|---|---|
|
| Maps to a single organization if the user is a member of a single organization. Otherwise, if a member of multiple organizations, the user will be prompted to select an organization when authenticating to the realm. |
|
| Maps to a single organization with the given alias. |
|
| Maps to all organizations the user is a member of. |
