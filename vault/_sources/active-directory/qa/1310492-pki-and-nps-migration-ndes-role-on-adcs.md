---
title: "PKI and NPS Migration | NDES Role on ADCS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1310492/pki-and-nps-migration-ndes-role-on-adcs
question_id: 1310492
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
---
# PKI and NPS Migration | NDES Role on ADCS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1310492/pki-and-nps-migration-ndes-role-on-adcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi folks, I have a client I'm working with who wants to migrate their existing PKI infrastructure from Windows Server 2012R2 to Server 2022. They also have an NPS server they'd like to migrate as well. Their PKI infrastructure is a two-tier hierarchy, consisting of one Root CA and one Issuing CA. Upon accessing their environment, I find that these roles are also installed under the ADCS role:

My problem is that, all the guides I've seen online don't really mention how or what steps to take when a NDES role or other roles are installed. The most they show is a guide working with OCSP role, CA web enrollment. Since this is a migration, I would need to install the same roles onto the new Server 2022. NDES role and the other ADCS roles come with its own set of configurations. Are the guides such as the technet or petenetlive enough?

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-active-directory-certi...

https://www.petenetlive.com/KB/Article/0001473

Since this is a production environment. The thought of uninstalling the ADCS role before I migrate to the new server is a bit nerve-racking. They want all of their existing settings and configurations to carry over. 

Is there a way for me to cleanly migrate the NDES role over to the new one with all existing settings? Or this is something that I have to set up once again and have all their devices using this role point to the migrated server? For things like CES and CEP roles, do they also get set up or is there a way to migrate them with existing settings, kind of like how I can take a backup of the CAs and restore that backup on the target server?

One important consideration is that they do not want any downtime and would like to have this carried out without any impact to their end users which would be during business hours. Is this possible with this kind of migration?

I apologize since this may be a rookie question but I'd really like to get some help from someone here. Any insight or resources would be super helpful. 

Thank you!

## Answers

_No answers on this thread._
