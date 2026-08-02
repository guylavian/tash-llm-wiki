---
title: "How to deny Active directory Default Domain user to disjoin/join computers from AD?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2100520/how-to-deny-active-directory-default-domain-user-t
question_id: 2100520
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How to deny Active directory Default Domain user to disjoin/join computers from AD?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2100520/how-to-deny-active-directory-default-domain-user-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello there,

I was working on Active directory and there were more than 1 domain admins. i just found out that domain user account which is just created without any kind of group is able to join and disjoin computers to AD. I have removed any GPO that we have created and there is still the problem. I have checked the computer OU deligation and it looks the same. Is there any way i can find out why it happened and a way to fix this?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-10*

Hello

It sounds like you're dealing with a tricky issue in Active Directory. Here are a few steps you can take to troubleshoot and potentially resolve this problem:

 

Check User Rights Assignment: Ensure that the "Add workstations to domain" policy is not inadvertently granting permissions to unauthorized users. You can find this setting in the Group Policy Management Console under Computer Configuration -> Policies -> Windows Settings -> Security Settings -> Local Policies -> User Rights Assignment. Verify that only the intended groups or users have this right.

 

Review Delegated Permissions: Double-check the delegated permissions in Active Directory Users and Computers. Right-click the Organizational Unit (OU) where the computers are being added, select "Delegate Control," and review the permissions. Ensure that only the appropriate groups or users have the necessary permissions to join or disjoin computers.

 

Domain Join Hardening: Microsoft has introduced domain join hardening changes that might affect how accounts with delegated permissions can join computers to the domain. Review the details in the An external link was removed to protect your privacy. to ensure that your environment complies with these changes.

 

DNS Configuration: Ensure that your DNS settings are correctly configured. DNS is crucial for Active Directory operations, including domain joins. Verify that DNS server addresses are correct, there are no stale or duplicate DNS records, and that the domain controllers and DNS servers can be pinged.

 

Netsetup.log: Check the Netsetup.log file on the affected computers. This log file can provide valuable insights into domain join issues. Look for any errors or warnings that might indicate why the domain user account is able to join or disjoin computers.

 

Event Viewer: Monitor the Event Viewer for any relevant logs. You can look for events related to computer account creation and changes. This can help you identify when and how the unauthorized joins or disjoins are happening.
