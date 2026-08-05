---
title: "Require help on Migrating an ADFS-Dependent Application from On-Premises to Microsoft Entra ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5935969/require-help-on-migrating-an-adfs-dependent-applic
question_id: 5935969
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Require help on Migrating an ADFS-Dependent Application from On-Premises to Microsoft Entra ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5935969/require-help-on-migrating-an-adfs-dependent-applic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

I am looking for guidance on migrating an application that currently relies on Active Directory Federation Services (ADFS) for authentication to Microsoft Entra ID.

Our current environment includes:

-  An on-premises Active Directory.

-  ADFS configured as the identity provider.

-  An application that authenticates users through ADFS using federation.

We are planning to modernize our identity infrastructure by moving authentication from ADFS to Microsoft Entra ID.

I have the following questions:

-  What is the recommended approach for migrating an ADFS-dependent application to Microsoft Entra ID?

-  Is there a Microsoft-supported ADFS migration tool that can help migrate relying party trusts or application configurations to Microsoft Entra ID?

-  If there is no dedicated migration tool, what is considered the best approach for migrating ADFS-integrated applications to Microsoft Entra ID?

-  Can this migration be completed with minimal or no downtime?

-  If the application currently uses SAML or WS-Federation with ADFS, what changes are typically required to integrate with Microsoft Entra ID?

-  Are there any common challenges or best practices to be aware of during the migration?

-  Is it possible to run ADFS and Microsoft Entra ID in parallel during the transition to reduce risk?

-  Are there any Microsoft documentation, migration guides, or real-world experiences that you would recommend?

We are particularly interested in understanding whether Microsoft provides any tooling to simplify the migration process, or whether the migration is generally performed by manually recreating the application configuration in Microsoft Entra ID and updating the application to trust the new identity provider.

Any guidance, lessons learned, or references to official Microsoft documentation would be greatly appreciated.

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2026-07-02*

-  Recommended approach for migrating ADFS-dependent apps to Microsoft Entra ID

Microsoft recommends a staged, test-first migration approach:

-  Discover and scope all AD FS apps, including in-development and planned apps, and plan for them to use Microsoft Entra ID after migration.

-  Use the AD FS application activity report and migration dashboard to assess which apps are compatible and ready to migrate.

-  Clone the AD FS app configuration into a test Microsoft Entra tenant or test instance of the app, map AD FS settings to Microsoft Entra configurations, and validate sign-in.

-  Configure claims and identifiers in Microsoft Entra ID to mimic the production AD FS configuration, then point a test instance of the app to the Microsoft Entra application and troubleshoot.

-  Prepare the production instance by adding the production app to Microsoft Entra ID; if the app supports multiple IdPs, configure Microsoft Entra ID as an additional IdP.

-  Switch the production app to use Microsoft Entra ID as the primary IdP, then run migration tests and fix issues.

-  Migrate apps and users in phases and remove federation once the AD FS farm is no longer used.

These steps are summarized in the “Application migration process plan” and “Migrate applications” guidance.

-  Microsoft-supported ADFS migration tool

Yes. Microsoft provides the AD FS application migration tool and wizard:

-  It is designed to provide end-to-end support to migrate on-premises AD FS relying party applications to Microsoft Entra ID.

-  It discovers AD FS relying party applications, evaluates sign-in activities, analyzes migration feasibility, and then offers a guided one-click configuration to create a corresponding Microsoft Entra application.

-  The wizard automatically configures basic SAML URLs (Identifier, Reply URL), claims mapping, and user/group assignments.

Prerequisites include:

-  Existing AD FS usage for accessing applications.

-  Microsoft Entra ID P1 or P2.

-  Appropriate admin roles (Cloud Application Administrator, Application Administrator, Global Reader, or Report Reader).

-  Microsoft Entra Connect and Microsoft Entra Connect Health AD FS agents installed on-premises.

-  Best approach if not using a dedicated tool

Even with the tool, the recommended approach is still:

-  Clone AD FS configuration into a test Microsoft Entra app.

-  Manually configure SAML settings and claims where needed, especially for unsupported configurations.

-  Validate with a test instance of the application.

-  Add the production app to Microsoft Entra ID and, if possible, configure it to accept both AD FS and Microsoft Entra ID.

-  Gradually switch sign-in traffic to Microsoft Entra ID and decommission AD FS once no longer used.

For apps not fully supported by the wizard (for example, non-SAML protocols or complex claim rules), manual recreation and adjustment of claims in Microsoft Entra ID is the typical path.

-  Minimal or no downtime

Minimal downtime is achievable by:

-  Using a test instance and validating configuration before touching production.

-  For apps that support multiple IdPs, running AD FS and Microsoft Entra ID in parallel and switching the default IdP only after successful testing.

-  Migrating in phases and using activity reports to prioritize high-impact apps.

The wizard itself migrates the new Microsoft Entra application into the tenant but leaves it inactive until sign-in traffic is redirected, which supports a controlled cutover.

-  Changes when moving SAML or WS-Fed apps to Microsoft Entra ID

For SAML apps:

-  The wizard supports SAML configuration only and will:

-  Configure Identifier and Reply URL in the Microsoft Entra enterprise application.

-  Import compatible claims from the AD FS relying party.

-  Assign users and groups.

-  After migration, the SAML-based sign-on pane in Microsoft Entra will show the same Identifier, Reply URL, and claims as the AD FS configuration.

-  You may further customize claims (for example, regex-based transformations using predefined functions like `Extract()`, `Trim()`, `ToLower()`) and configure group claims.

For WS-Fed and other protocols:

-  OIDC, OAuth, and WS-Fed configurations are not supported by the assisted migration wizard.

-  These apps require manual configuration in Microsoft Entra ID or protocol changes in the application, following Microsoft Entra documentation for the relevant protocol.

-  Common challenges and best practices

Common challenges:

-  Unsupported AD FS configurations, such as:

-  External attribute stores other than Active Directory.

-  Issuance rules using ADD in ways that require multiple claim transformations.

-  Issuance transformations using regular expressions.

-  Non-SAML protocols (OIDC, OAuth, WS-Fed) not supported by the wizard.

-  Conditional Access policies are not auto-configured and must be set up manually after migration.

-  Signing certificates from AD FS relying party applications are not migrated.

Best practices:

-  Use the AD FS application activity report and migration dashboard to identify compatible apps and blockers.

-  Plan rollback: the migrated Microsoft Entra application remains inactive until traffic is redirected; if you decide not to proceed, delete the application registration and enterprise application.

-  Configure and test claims and identifiers in a test environment before production.

-  Use regex-based transformations and group claims features in Microsoft Entra ID to replicate AD FS behavior.

-  Migrate apps and users in phases and confirm AD FS is no longer used before removing federation.

-  Running ADFS and Microsoft Entra ID in parallel

Yes. The guidance explicitly supports:

-  Configuring Microsoft Entra ID as an additional IdP for applications that allow multiple IdPs.

-  Running both AD FS and Microsoft Entra ID in parallel during the transition.

-  Changing the default IdP to Microsoft Entra ID only after successful validation.

This parallel approach reduces risk and allows gradual cutover.

-  Recommended Microsoft documentation and guides

Relevant Microsoft resources include:

-  AD FS application migration to move AD FS apps to Microsoft Entra ID: explains prerequisites, dashboard, activity reports, and the migration wizard.

-  Best practices to migrate applications and authentication to Microsoft Entra ID: covers staged migration, claims configuration, group claims, application proxy, and authentication method choices.

-  Guidance on customizing SAML token claims and group claims in Microsoft Entra ID.

-  Documentation linked from the wizard’s “Next steps” tab for handling unsupported configurations.

These resources collectively describe both the tooling (AD FS application migration wizard) and the recommended process (discover, evaluate, test, migrate, and decommission AD FS).

References:

-  Best practices to migrate applications and authentication to Microsoft Entra ID

-  AD FS application migration to move AD FS apps to Microsoft Entra ID

-  View AD FS application migration dashboard in Microsoft Entra ID

-  Review and configure the enterprise application
