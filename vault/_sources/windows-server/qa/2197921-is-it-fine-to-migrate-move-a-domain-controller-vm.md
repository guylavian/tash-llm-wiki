---
title: "Is it fine to migrate/move a domain controller VM in Hyper V?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197921/is-it-fine-to-migrate-move-a-domain-controller-vm
question_id: 2197921
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Is it fine to migrate/move a domain controller VM in Hyper V?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197921/is-it-fine-to-migrate-move-a-domain-controller-vm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

Good morning! I would like to ask if it is fine to move (using live migration) a domain controller from one hyper-v host to another hyper-v host? Would this action cause any problems? Anyone tried this before? The host that my DC is on start to have some hardware issue so I would like to move the DC away from it. If it fails in the middle, would it roll back and put the server back to the original host?

Hope you can share your experience or provide advise.

Thank you for your help in advance!  

Takami Chiro

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-10*

HI Neuvi,  

Thank you for your response! I really appreciate the info you provided. I think the host that I am going to migrate the DC has the same hardware. The only thing I concerned about is if the migration would mess up our AD. If the migration fails, would the DC be rolled back to the original host? Do you or anyone have any experience in migrating DC between hosts without any trouble during the process?  

Thank you!  

Takami Chiro

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-10*

Hi Riderfaiz,

Thank you for posting in the Microsoft Community Forums.

Availability

Hyper-V's live migration feature allows running virtual machines (VMs) to be moved seamlessly from one Hyper-V host to another while maintaining the workload availability of the VM. Therefore, it is theoretically feasible to live migrate DCs from one Hyper-V host to another.

Potential Issues

Processor compatibility:

Hyper-V utilizes the unique capabilities of modern processors to improve VM performance. When a VM is migrated, the processor of the new host needs to be compatible with the legacy system to ensure that the migrated VM will work properly.

If the processor is not compatible, it may result in reduced performance or failure of the virtual machine to function properly.

Network Configuration:

Ensure that the migrated Hyper-V hosts have the appropriate network configuration so that the DC can continue to provide network services.

Update any network settings related to the DC, such as DNS records, DHCP configurations, and so on.

Time synchronization:

The DC plays the role of time provider in the Active Directory environment. After migration, you should verify that the DC's time synchronization settings are correct to ensure time consistency throughout the domain.

Service disruption during migration:

Although live migration is designed to minimize service disruptions, there may still be brief periods of service unavailability during the migration process.

The relevant users or system administrators should be notified so that they can take appropriate action if necessary.

Migration Failure and Rollback:

If you encounter unsolvable problems (such as network outages, host failures, etc.) during the migration process, the migration may fail.

Regarding the rollback mechanism, Hyper-V does not directly provide an “automatic rollback” feature to put the virtual machine back to the original host. However, you can create snapshots or backups of the VMs before the migration so that they can be quickly recovered if the migration fails.

Best Practices

Plan the migration:

Prior to migration, plan the migration process in detail, including migration time, network configuration, backup and recovery strategies, etc.

Test the migration:

Test the migration process in a non-production environment to verify the feasibility and reliability of the migration.

Backup VMs:

Create a full backup of the DCs prior to migration. This provides recovery options in case of migration failure.

Monitor the migration process:

Closely monitor the status and performance of the DCs during the migration process to identify and resolve issues in a timely manner.

Verify migration results:

After the migration is complete, verify that the DC functions and performs as expected. This includes checking network services, time synchronization, event logs, etc.

Best regards

Neuvi
