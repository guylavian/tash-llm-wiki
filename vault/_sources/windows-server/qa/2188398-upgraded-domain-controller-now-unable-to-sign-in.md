---
title: "Upgraded Domain Controller now unable to sign in"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188398/upgraded-domain-controller-now-unable-to-sign-in
question_id: 2188398
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Upgraded Domain Controller now unable to sign in

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188398/upgraded-domain-controller-now-unable-to-sign-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I recently upgraded our domain controller from 2022 to 2025 and ran /forestprep and /domainprep before the the upgrade, after the upgrade however I am unable to signin to the server at all just keeps saying incorrect username and password… it’s not my account because I can UNC into the domain controller… any ideas what could be causing this and how I could fix it…

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-17*

Disabling KDC allows me to sign in but replication is broken as DNS is saying ‘access denied’ when I try to load it…

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-16*

Thank you for the reply, I was able to connect to the server from another server and checked netlogon was running, however using the replication commands you suggested says:

(8524) The DSA operation is unable to

proceed because of a DNS failure. -and 1908) Could not find the domain controller for this domain.

This is for the 2 domain controllers I upgraded but they will not allow me to sign in to the machine… any other ideas? I can ping the server and I can UNC into the server but not sign in via the gui.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-16*

Hello 

Thank you for posting on the Microsoft Community. 

Domain controller authentication issues (credential caching) 

After upgrading, authentication services, such as Netlogon, may not start correctly, or there may be caching issues. 

Troubleshooting steps: 

```
Reboot the domain controller: First try restarting the domain controller, making sure to clear any stale sessions or cached credentials. 

Check if the Netlogon service is running: 

	Open the Service Manager (services.msc) and locate the Netlogon service. 

	Make sure the service is running. If it doesn't run, try starting it manually, or use the command net start netlogon. 

Verify the domain controller synchronization status: 

	Ensure that the domain controller is properly synchronized with other domain controllers after the upgrade. If you have more than one domain controller, make sure that AD (Active Directory) replication is OK. 

	Use the following command to check the replication status:
```

repadmin /replsummary  

Time synchronization issues 

Time synchronization issues are a common cause of domain controller authentication failures, especially after an upgrade. 

Steps: 

Check the time sync status: 

```
Run the following command at the command prompt:
```

w32tm /query /status 

If the time is incorrect, you can run the following command to force synchronization: 

w32tm /resync 

Verify the time synchronization of all domain controllers: 

```
Ensure that the timing of all domain controllers is consistent with the PDC Emulator (Primary Domain Controller Emulator). 

You can use the following command to check if all domain controllers are synchronized with the PDC:
```

nltest /dsgetdc:yourdomain.com 

I hope the above information is helpful to you. 

Regards  

Runjie Zhai
