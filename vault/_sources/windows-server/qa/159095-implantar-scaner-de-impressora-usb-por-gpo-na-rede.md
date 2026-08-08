---
title: "Implantar scaner de impressora usb por gpo na rede"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/159095/implantar-scaner-de-impressora-usb-por-gpo-na-rede
question_id: 159095
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Implantar scaner de impressora usb por gpo na rede

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/159095/implantar-scaner-de-impressora-usb-por-gpo-na-rede (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Gostaria de saber se existem soluções para implantar scaner de uma impressora usb, por gpo para mais maquinas na rede?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-13*

Ola! Na verdade não seria implantar a impressora via usb. pois instalei ela via wifi e implantei via gpo para o restante do AD. Preciso saber se há a possibilidade, de implantar o escaner da epson l3150 via rede por gpo a estas mesmas maquinas.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

Hi,  

Thanks for your posting. But kindly note that our Q&A forum only supports English at this moment.  

After translating your question by Google, I would like to share following for your reference:  

Per my knowledge, if you want to deploy USB printers via GPO, you may need to add printers on a server, and then publish it from \server\printername via GPO.  

You can add the printer using the add printer in the device and printers, or use the print management interface in the same way to add the printer.  

Here is blogs regarding to deploy printers based on computers via GPO, you could refer to and follow it step by step to see if it works:  

-  Step-By-Step: Setting up Printers via Group Policy  

https://blogs.technet.microsoft.com/canitpro/2015/02/03/step-by-step-setting-up-printers-via-group-policy/  

-  How to Deploy Printers to Users/Groups/Computers with GPO?  

http://woshub.com/deploy-printers-to-users-gpo/  

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.  

But if you prefer to continuing this question in Portuguese, you could turn to following forum for assistance.  

https://social.technet.microsoft.com/Forums/pt-BR/home  

Hope this helps and please help to accept as Answer if the response is useful.  

Thanks,  

Jenny
