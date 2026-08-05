---
title: "Exchange Online no recibe correos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1303155/exchange-online-no-recibe-correos
question_id: 1303155
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Online no recibe correos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1303155/exchange-online-no-recibe-correos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hola buenas tardes!

He comprado licencias de exchange online plan 1 y plan 2, configuré los registros DNS con el asistente en el centro de administración de Microsoft 365, como mi servicio DNS es administrado por Cloudflare, el asistente agregó de forma automática los registros. Han pasado ya mas de 48 hs y el centro de administración de Microsoft 365 dice que el estatus del dominio está bien y que los registros están bien. Abro outlook desde la web y puedo enviar los mail, pero no puedo recibirlos.

He ejecutado el Analizador de conectividad remota de Microsoft y ahí me dice que no puede resolver el registro MX para mi dominio. No sé que hacer si en el Centro de Administración dice que todo está OK.

Espero que alguien me pueda ayudar!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-12*

Hi @Juan David Mira Sierra  

Kindly note that currently Microsoft Q&A forum only supports posting in English.

Please edit your question into English so we can better understand your question.

Thanks for your understanding.

According to machine translation, your question is:

I have purchased exchange online licenses plan 1 and plan 2, I configured the DNS records with the wizard in the Microsoft 365 admin center, as my DNS service is managed by Cloudflare, the wizard automatically added the records. It has been more than 48 hs now and the Microsoft 365 admin center says that the domain status is fine and the records are fine. I open outlook from the web and I can send the mails, but I can't receive them.
I have run Microsoft Remote Connectivity Analyzer and there it says it cannot resolve the MX record for my domain. I don't know what to do if in the Admin Center it says everything is OK.
I hope someone can help me!

If any misunderstanding, please feel free to point out.

To receive inbound emails to your organization, you may need to configure a MX record and point it to Microsoft 365 email service.

Please follow this documentation about how to: Add an MX record for email (Outlook, Exchange Online)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
