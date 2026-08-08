---
title: "Por qué no puedo instalar active directory domain services en mi servidor?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199757/por-qu-no-puedo-instalar-active-directory-domain-s
question_id: 2199757
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Por qué no puedo instalar active directory domain services en mi servidor?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199757/por-qu-no-puedo-instalar-active-directory-domain-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A la hora de intentar instalar Active Directory Domain Services en Windows Server 2019 Standar arroja el siguiente error:  The requested to add or remove features on the specified server failed. Installation of one or more roles, role services, or features failed. The referenced assembly could not be found. Error: 0x80073701. Al revisar la carpeta CBS con los logs, aparece un fallo para ciertos paquetes de los siguientes archivos: KB4565349 y KB5031361. En microsoft update catalog aparece disponible KB5031361, pero KB4565349 no aparece. Tampoco se pudo instalar adecuadamente KB5031361. Espero esta informacion ayude para solucionar el problema.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-04*

Hi Maria Martinez8,

this issue can be caused due to missing or corrupted Windows update files. You can try the following steps to resolve this issue: 

-  Select the start button and type cmd.

-  Right click or long press on Command Prompt and select Run as administrator.

-  If you receive a **User Access Control (UAC)**dialog for Windows Command Processorstating, "Do you want to allow this app to make changes to your device?", select Yes.

-  Type or copy and paste the following command into the Command Promptwindow:  

dism /online /cleanup-image /startcomponentcleanup

-  Wait for the command to complete.

-  Restart your device.

-  Try checking for updates again.

If these steps can't resolve the issue, you can refer to [SOLVED] Server 2019 Standard: 0x80073701 Referenced assembly cannot be found; Bitlocker - Windows Server (spiceworks.com).

Hope it helps.

Kind regards,

Lei
