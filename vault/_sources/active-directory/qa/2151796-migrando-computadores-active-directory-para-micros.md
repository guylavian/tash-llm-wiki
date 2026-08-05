---
title: "Migrando computadores Active Directory para Microsoft Intune"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2151796/migrando-computadores-active-directory-para-micros
question_id: 2151796
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migrando computadores Active Directory para Microsoft Intune

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2151796/migrando-computadores-active-directory-para-micros (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Bom dia !  

Tenho um cenário onde ocorre o seguinte

Possuo o active directory conectado a micsoft, meus usuários por exemplo assim que faço a criação no AD, eles já são integrados dentro da microsoft

Futuramente meu AD deixará de existir e os acessos serão apenas na microsoft

Tenho o microsoft intune onde já tenho algumas maquinas pegando configurações de programas e politicas direto do intune

Porem tenho um cenario de maquinas que ainda não existe dentro do intune e possuem sua configuração apenas no Active directory

Eu como administrador da rede preciso pegar estas maquinas que não estão no intune e estão no AD e migrar para o microsoft intune, porem não estou encontrando uma forma de fazer isto sem acessar maquina por maquina para mudar a configuração

Qual a ideia posso executar para que eu consiga pegar estas maquinas que estão no AD e conseguir integra-las dentro do microsoft intune para poder retirar o meu AD

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-28*

@miron lucas, Obrigado por postar em Q&A. Pela sua descrição, sei que você quer remover seu ambiente AD local, migrar para o Microsoft Entra ID e registrar-se no Intune. Para este cenário, o tipo de junção para o dispositivo é sugerido como junção do Microsoft Entra ID.

https://learn.microsoft.com/en-us/entra/identity/devices/device-join-plan

Se também quisermos que o usuário de login seja um usuário padrão em vez de um administrador do dispositivo, o registro do Intune que sugerimos é o Autopilot. Podemos tentar as etapas no link a seguir.

https://learn.microsoft.com/en-us/autopilot/tutorial/user-driven/azure-ad-join-workflow

Para as etapas acima, o registro do Autopilot para coletar hash de hardware precisa acessar o dispositivo, o gatilho do Autopilot precisa redefinir o dispositivo. Enquanto isso, os dados do usuário precisam ser copiados antes de realizarmos a ação acima.

Another method I can think is we can first enroll the device via BYOD enrollment. (As the device is joined to on-premise AD, it can't do Microsoft Entra join directly)

https://learn.microsoft.com/en-us/mem/intune/fundamentals/deployment-guide-enrollment-windows#byod-user-enrollment

Em seguida, defina o perfil do Autopilot e configure "Converter todos os dispositivos de destino para o Autopilot" como sim e, em seguida, redefina o dispositivo para fazer o registro no Autopilot.

https://learn.microsoft.com/en-us/autopilot/profiles#create-an-autopilot-deployment-profile

Espero que as informações acima possam ajudar.

Se a resposta for útil, clique em "Aceitar Resposta" e gentilmente vote a favor. Se você tiver perguntas extras sobre esta resposta, clique em "Comentar".

Observação: siga as etapas em nossa documentação para habilitar notificações por e-mail se quiser receber notificações por e-mail relacionadas a este tópico.
