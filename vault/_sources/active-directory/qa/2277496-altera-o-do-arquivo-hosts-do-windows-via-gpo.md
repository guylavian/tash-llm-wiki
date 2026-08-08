---
title: "Alteração do arquivo HOSTS do Windows via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2277496/altera-o-do-arquivo-hosts-do-windows-via-gpo
question_id: 2277496
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Alteração do arquivo HOSTS do Windows via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2277496/altera-o-do-arquivo-hosts-do-windows-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Boa noite, galera. 

Solicito o apoio da equipe de Windows para a seguinte demanda:

 

-  Eu criei um script .BAT que adiciona uma linha no arquivo HOSTS do Windows.

-  O script executado localmente, como administrador, funciona perfeitamente.

-  O problema está sendo executar esse script via GPO, pois nenhuma das alternativas que pesquisei e tentei consegue alterar o arquivo HOSTS nos desktops de homologação da TI (W10 e W11).

-  O problema parece ser a permissão necessária para que o script altere o arquivo HOSTS (não é uma substituição de arquivo, apenas uma adição de uma linha de dados).

-  Uma das alternativas pesquisadas foi a criação de dois scripts: um script launcher que executa o script de alteração. Depois, era só criar uma GPO que copiasse estes dois scripts para uma pasta na máquina local, além de adicioná-los no script de inicialização do computador. Porém, o problema de permissão parece persistir, pois o arquivo HOSTS continua inalterado.

Alguém consegue me ajudar com esta demanda? Seguem abaixo os scripts citados:

-  Script que altera o arquivo HOSTS (script_hosts_OK.bat):

```
@@echo off
setlocal EnableDelayedExpansion

:: Caminho do arquivo hosts
set "HOSTS=%SystemRoot%\System32\drivers\etc\hosts"

:: Diretório e arquivo de log (ajuste o caminho se necessário)
set "LOGDIR=%SystemRoot%\Temp"
set "LOGFILE=%LOGDIR%\script_hosts_OK.txt"

:: Garante que o diretório de log existe
if not exist "%LOGDIR%" mkdir "%LOGDIR%"

:: Início do log
echo ---------------------------------------- >> "%LOGFILE%"
echo [%DATE% %TIME%] Início do patch >> "%LOGFILE%"

:: Remove o atributo somente leitura
attrib -r "%HOSTS%" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [%DATE% %TIME%] Atributo 'somente leitura' removido de hosts >> "%LOGFILE%"
) else (
    echo [%DATE% %TIME%] Falha ao remover atributo 'somente leitura' >> "%LOGFILE%"
)

:: Entradas a adicionar (edite aqui)
set "ENTRY1=127.0.0.1 exemplo.com.br"

:: Verifica e adiciona cada uma
call :AddIfMissing "!ENTRY1!"

echo [%DATE% %TIME%] Fim do patch >> "%LOGFILE%"
echo. >> "%LOGFILE%"

endlocal
exit /b

:AddIfMissing
setlocal
set "LINE=%~1"

:: Ignora se linha vazia
if "%LINE%"=="" exit /b

:: Verifica se já existe
findstr /C:"%LINE%" "%HOSTS%" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    >>"%HOSTS%" echo %LINE%
    echo [%DATE% %TIME%] Adicionado: %LINE% >> "%LOGFILE%"
) else (
    echo [%DATE% %TIME%] Já existia: %LINE% >> "%LOGFILE%"
)
endlocal
exit /b
```

-  Script executa o script acima (launcher_hosts.bat):

```
@echo off
setlocal

:: Caminho do script principal (ajuste se estiver em outro lugar)
set "SCRIPT=%~dp0script_hosts_OK.bat"

:: Verifica se o script existe
if not exist "%SCRIPT%" (
    echo Script não encontrado: %SCRIPT%
    exit /b 1
)

:: Executa o script de alteração silenciosamente
call "%SCRIPT%"

endlocal
exit /b
```

Obrigado pela atenção de todos.

## Answers

_No answers on this thread._
