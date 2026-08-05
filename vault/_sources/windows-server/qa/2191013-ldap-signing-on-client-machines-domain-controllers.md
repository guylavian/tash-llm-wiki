---
title: "LDAP Signing on Client machines & Domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191013/ldap-signing-on-client-machines-domain-controllers
question_id: 2191013
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# LDAP Signing on Client machines & Domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191013/ldap-signing-on-client-machines-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently LDAP Signing GPO is not enabled on client machines and Domain controllers "Network security:LDAP client signing requirements". Our domain Controllers are on 2016 OS and client machines are Windows 10 OS. 

-  LDAPS (port 636) is currently not configured on the DCs. Is it a pre-requisite to enable this GPO ?   

-  Is LDAPS is not a requirement and can still work on port 389. Is there a specific flow we should follow to enable these GPOs on both Client & DC side. For ex : First enable Request Signing on clients then wait for a week and do it on DC side. Later change it to Require signing ?  

Please advise, thank you/

## Answer (community) — community member

*upvotes: 1 · updated: 2024-11-11*

Hi sonumakkar,

Thank you for posting in the Microsoft Community Forums.

Here are my detailed answers to your questions:

-  Is LDAPS a prerequisite for enabling GPO ‘Network Security: LDAP Client Signature Requirements’?

LDAPS is not a prerequisite for enabling GPO ‘Network Security: LDAP Client Signature Requirements’. While LDAPS (LDAP over SSL/TLS) provides increased security by encrypting LDAP traffic to protect data, enabling LDAP signing (i.e., GPO's ‘Network Security: LDAP Client Signature Requirements’) is another way to increase the security of LDAP communications. It requires the LDAP client and server to negotiate a data signature when communicating to ensure the integrity and authenticity of the data. As a result, the LDAP Signature GPO can be enabled even if LDAPS is not configured.

However, it is worth noting that LDAP Signature and LDAPS are not mutually exclusive. In practice, they can be enabled simultaneously to provide stronger security.

-  Whether LDAPS is required and the specific process for enabling GPOs

LDAPS is not required, but it is highly recommended to enable it to improve the security of LDAP communications. If you decide not to enable LDAPS, you can still run the LDAP service on port 389. However, doing so will sacrifice some security, as LDAP traffic will be unprotected in transit and vulnerable to threats such as man-in-the-middle attacks.

There is usually no set order of precedence required regarding the particular process of enabling GPOs. However, to ensure a smooth transition and minimise potential problems, the following is a suggested process:

Evaluate the environment: Begin by evaluating the current network environment and client computer configurations to ensure they support the planned security changes.

Test the environment: Enable LDAP signatures and LDAPS (if you decide to enable them) in a test environment and verify their functionality and compatibility.

Plan Development: Develop a detailed implementation plan based on the test results, including specific steps to enable GPOs, timelines, and rollback plans.

Client Configuration: Enable the Network Security: LDAP Client Signature Requirements GPO on client computers, which can be done through the Group Policy Management tool.

Monitoring and Testing: Once GPOs are enabled on client computers, closely monitor their impact and test the integrity of LDAP communications. If problems occur, you can adjust the configuration or roll back changes.

Domain Controller Configuration: After confirming that the client computers are working properly, enable the appropriate GPOs on the domain controllers (e.g., ‘Domain Controllers: LDAP Server Signature Requirements’). Again, this needs to be closely monitored and tested to ensure it is working properly.

Whether or not you need to wait a period of time between the client and the DC before performing an operation usually depends on your specific environment and requirements. Generally speaking, if the test environment indicates that the changes are compatible and stable, then these GPOs can be enabled simultaneously or sequentially in the production environment. however, to be on the safe side, some organisations may choose to implement these changes in stages, with adequate monitoring and testing between each stage.

Finally, setting GPOs to ‘Require signing’ is an important step in securing LDAP communications. This requires all LDAP clients to negotiate data signatures when communicating, thus preventing threats such as man-in-the-middle attacks.

Best regards

Neuvi

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-05*

This might  help on your question.

https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-signing-in-windows-server

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-12*

I received below guidance by the Vulnerability tool scanner (PurpleKnight), my question is should I give any gaps between each step. For ex : Perform Step1 then wait for a week. Perform Step 2 , wait for all DCs to get this GPO and then push the GPO using Step 3 on all client machines. What is the correct sequence   

The following remediation steps use Group Policies. They should be followed by order and completed correctly to avoid disruptions 

in the domain: 

-  Configure clients to request LDAP signing - Group Policy name:Network security:LDAP client signing requirements -> select 

Request signing in the dialog box

-  When all clients request signing, configure domain controllers to require signing - Group Policy name:Domain controller:LDAP 

server signing requirements -> select Require signing. 

-  Configure clients to require signing - Group Policy name:Network security:LDAP client signing requirements -> select Require 

signing in the dialog box.  

Following these steps will ensure that no client will stop working during the transition: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/domain-controller-ldap-server-signing-requirements -------------------https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/network-security-ldap-client-signing-requirements
