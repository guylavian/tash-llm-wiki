---
title: "Chapter 16. Configuring logging - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-logging
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/logging-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
abstract: "Red Hat build of Keycloak uses the JBoss Logging framework. The following is a high-level overview for the available log handlers with the common parent log handler root: console file syslog 16.1. Logging configuration Logging is done on a per-category basis in Red Hat build of Keycloak. You can configure logging for the root log level or for more specific categories such as org.hibernate or org.k…"
---

# Chapter 16. Configuring logging - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 16. Configuring logging
Red Hat build of Keycloak uses the JBoss Logging framework. The following is a high-level overview for the available log handlers with the common parent log handler root
:
- console
- file
- syslog
16.1. Logging configuration
Logging is done on a per-category basis in Red Hat build of Keycloak. You can configure logging for the root log level or for more specific categories such as org.hibernate
or org.keycloak
. It is also possible to tailor log levels for each particular log handler.
This chapter describes how to configure logging.
16.1.1. Log levels
The following table defines the available log levels.
| Level | Description |
|---|---|
| FATAL | Critical failures with complete inability to serve any kind of request. |
| ERROR | A significant error or problem leading to the inability to process requests. |
| WARN | A non-critical error or problem that might not require immediate correction. |
| INFO | Red Hat build of Keycloak lifecycle events or important information. Low frequency. |
| DEBUG | More detailed information for debugging purposes, such as database logs. Higher frequency. |
| TRACE | Most detailed debugging information. Very high frequency. |
| ALL | Special level for all log messages. |
| OFF | Special level to turn logging off entirely (not recommended). |
16.1.2. Configuring the root log level
When no log level configuration exists for a more specific category logger, the enclosing category is used instead. When there is no enclosing category, the root logger level is used.
To set the root log level, enter the following command:
bin/kc.[sh|bat] start --log-level=<root-level>
Use these guidelines for this command:
-
For
<root-level>
, supply a level defined in the preceding table. -
The log level is case-insensitive. For example, you could either use
DEBUG
ordebug
. -
If you were to accidentally set the log level twice, the last occurrence in the list becomes the log level. For example, if you included the syntax
--log-level="info,…,DEBUG,…"
, the root logger would beDEBUG
.
16.1.3. Configuring category-specific log levels
You can set different log levels for specific areas in Red Hat build of Keycloak. Use this command to provide a comma-separated list of categories for which you want a different log level:
bin/kc.[sh|bat] start --log-level="<root-level>,<org.category1>:<org.category1-level>"
A configuration that applies to a category also applies to its sub-categories unless you include a more specific matching sub-category.
Example
bin/kc.[sh|bat] start --log-level="INFO,org.hibernate:debug,org.hibernate.hql.internal.ast:info"
This example sets the following log levels:
- Root log level for all loggers is set to INFO.
- The hibernate log level in general is set to debug.
-
To keep SQL abstract syntax trees from creating verbose log output, the specific subcategory
org.hibernate.hql.internal.ast
is set to info. As a result, the SQL abstract syntax trees are omitted instead of appearing at thedebug
level.
16.2. Enabling log handlers
To enable log handlers, enter the following command:
bin/kc.[sh|bat] start --log="<handler1>,<handler2>"
The available handlers are:
- console
- file
- syslog
The more specific handler configuration mentioned below will only take effect when the handler is added to this comma-separated list.
16.3. Specify log level for each handler
The log-level
property specifies the global root log level and levels for selected categories. However, a more fine-grained approach for log levels is necessary to comply with the modern application requirements.
To set log levels for particular handlers, properties in format log-<handler>-level
(where <handler>
is available log handler) were introduced.
It means properties for log level settings look like this:
-
log-console-level
- Console log handler -
log-file-level
- File log handler -
log-syslog-level
- Syslog log handler
The log-<handler>-level
properties are available only when the particular log handlers are enabled. More information in log handlers settings below.
Only log levels specified in Section 16.1.1, “Log levels” section are accepted, and must be in lowercase. There is no support for specifying particular categories for log handlers yet.
16.3.1. General principle
It is necessary to understand that setting the log levels for each particular handler does not override the root level specified in the log-level
property. Log handlers respect the root log level, which represents the maximal verbosity for the whole logging system. It means individual log handlers can be configured to be less verbose than the root logger, but not more.
Specifically, when an arbitrary log level is defined for the handler, it does not mean the log records with the log level will be present in the output. In that case, the root log-level
must also be assessed. Log handler levels provide the restriction for the root log level, and the default log level for log handlers is all
- without any restriction.
16.3.2. Examples
Example: debug
for file handler, but info
for console handler:
bin/kc.[sh|bat] start --log=console,file --log-level=debug --log-console-level=info
The root log level is set to debug
, so every log handler inherits the value - so does the file log handler. To hide debug
records in the console, we need to set the minimal (least severe) level to info
for the console handler.
Example: warn
for all handlers, but debug
for file handler:
bin/kc.[sh|bat] start --log=console,file,syslog --log-level=debug --log-console-level=warn --log-syslog-level=warn
The root level must be set to the most verbose required level (debug
in this case), and other log handlers must be amended accordingly.
Example: info
for all handlers, but debug
+org.keycloak.events:trace
for Syslog handler:
bin/kc.[sh|bat] start --log=console,file,syslog --log-level=debug,org.keycloak.events:trace, --log-syslog-level=trace --log-console-level=info --log-file-level=info
In order to see the org.keycloak.events:trace
, the trace
level must be set for the Syslog handler.
16.4. Console log handler
The console log handler is enabled by default, providing unstructured log messages for the console.
16.4.1. Configuring the console log format
Red Hat build of Keycloak uses a pattern-based logging formatter that generates human-readable text logs by default.
The logging format template for these lines can be applied at the root level. The default format template is:
-
%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c] (%t) %s%e%n
The format string supports the symbols in the following table:
| Symbol | Summary | Description |
|---|---|---|
| %% | % | Renders a simple % character. |
| %c | Category | Renders the log category name. |
| %d{xxx} | Date |
Renders a date with the given date format string.String syntax defined by |
| %e | Exception | Renders a thrown exception. |
| %h | Hostname | Renders the simple host name. |
| %H | Qualified host name | Renders the fully qualified hostname, which may be the same as the simple host name, depending on the OS configuration. |
| %i | Process ID | Renders the current process PID. |
| %m | Full Message | Renders the log message and an exception, if thrown. |
| %n | Newline | Renders the platform-specific line separator string. |
| %N | Process name | Renders the name of the current process. |
| %p | Level | Renders the log level of the message. |
| %r | Relative time | Render the time in milliseconds since the start of the application log. |
| %s | Simple message | Renders only the log message without exception trace. |
| %t | Thread name | Renders the thread name. |
| %t{id} | Thread ID | Render the thread ID. |
| %z{<zone name>} | Timezone | Set the time zone of log output to <zone name>. |
| %L | Line number | Render the line number of the log message. |
16.4.2. Setting the logging format
To set the logging format for a logged line, perform these steps:
- Build your desired format template using the preceding table.
Enter the following command:
bin/kc.[sh|bat] start --log-console-format="'<format>'"
Note that you need to escape characters when invoking commands containing special shell characters such as ;
using the CLI. Therefore, consider setting it in the configuration file instead.
Example: Abbreviate the fully qualified category name
bin/kc.[sh|bat] start --log-console-format="'%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c{3.}] (%t) %s%e%n'"
This example abbreviates the category name to three characters by setting [%c{3.}]
in the template instead of the default [%c]
.
16.4.3. Configuring JSON or plain console logging
By default, the console log handler logs plain unstructured data to the console. To use structured JSON log output instead, enter the following command:
bin/kc.[sh|bat] start --log-console-output=json
Example Log Message
{"timestamp":"2022-02-25T10:31:32.452+01:00","sequence":8442,"loggerClassName":"org.jboss.logging.Logger","loggerName":"io.quarkus","level":"INFO","message":"Keycloak 18.0.0-SNAPSHOT on JVM (powered by Quarkus 2.7.2.Final) started in 3.253s. Listening on: http://0.0.0.0:8080","threadName":"main","threadId":1,"mdc":{},"ndc":"","hostName":"host-name","processName":"QuarkusEntryPoint","processId":36946}
When using JSON output, colors are disabled and the format settings set by --log-console-format
will not apply.
To use unstructured logging, enter the following command:
bin/kc.[sh|bat] start --log-console-output=default
Example Log Message
2022-03-02 10:36:50,603 INFO [io.quarkus] (main) Keycloak 18.0.0-SNAPSHOT on JVM (powered by Quarkus 2.7.2.Final) started in 3.615s. Listening on: http://0.0.0.0:8080
16.4.4. Colors
Colored console log output for unstructured logs is disabled by default. Colors may improve readability, but they can cause problems when shipping logs to external log aggregation systems. To enable or disable color-coded console log output, enter following command:
bin/kc.[sh|bat] start --log-console-color=<false|true>
16.4.5. Configuring the console log level
Log level for console log handler can be specified by --log-console-level
property as follows:
bin/kc.[sh|bat] start --log-console-level=warn
For more information, see the section Section 16.3, “Specify log level for each handler” above.
16.5. File logging
As an alternative to logging to the console, you can use unstructured logging to a file.
16.5.1. Enable file logging
Logging to a file is disabled by default. To enable it, enter the following command:
bin/kc.[sh|bat] start --log="console,file"
A log file named keycloak.log
is created inside the data/log
directory of your Red Hat build of Keycloak installation.
16.5.2. Configuring the location and name of the log file
To change where the log file is created and the file name, perform these steps:
Create a writable directory to store the log file.
If the directory is not writable, Red Hat build of Keycloak will start correctly, but it will issue an error and no log file will be created.
Enter this command:
bin/kc.[sh|bat] start --log="console,file" --log-file=<path-to>/<your-file.log>
16.5.3. Configuring the file handler format
To configure a different logging format for the file log handler, enter the following command:
bin/kc.[sh|bat] start --log-file-format="<pattern>"
See Section 16.4.1, “Configuring the console log format” for more information and a table of the available pattern configuration.
16.5.4. Configuring the file log level
Log level for file log handler can be specified by --log-file-level
property as follows:
bin/kc.[sh|bat] start --log-file-level=warn
For more information, see the section Section 16.3, “Specify log level for each handler” above.
16.6. Centralized logging using Syslog
Red Hat build of Keycloak provides the ability to send logs to a remote Syslog server. It utilizes the protocol defined in RFC 5424.
16.6.1. Enable the Syslog handler
To enable logging using Syslog, add it to the list of activated log handlers as follows:
bin/kc.[sh|bat] start --log="console,syslog"
16.6.2. Configuring the Syslog Application Name
To set a different application name, add the --log-syslog-app-name
option as follows:
bin/kc.[sh|bat] start --log="console,syslog" --log-syslog-app-name=kc-p-itadmins
If not set, the application name defaults to keycloak
.
16.6.3. Configuring the Syslog endpoint
To configure the endpoint(host:port) of your centralized logging system, enter the following command and substitute the values with your specific values:
bin/kc.[sh|bat] start --log="console,syslog" --log-syslog-endpoint=myhost:12345
When the Syslog handler is enabled, the host is using localhost
as host value. The Default port is 514
.
16.6.4. Configuring the Syslog log level
Log level for Syslog log handler can be specified by --log-syslog-level
property as follows:
bin/kc.[sh|bat] start --log-syslog-level=warn
For more information, see the section Section 16.3, “Specify log level for each handler” above.
16.6.5. Configuring the Syslog protocol
Syslog uses TCP as the default protocol for communication. To use UDP instead of TCP, add the --log-syslog-protocol
option as follows:
bin/kc.[sh|bat] start --log="console,syslog" --log-syslog-protocol=udp
The available protocols are: tpc
, udp
, and ssl-tcp
.
16.6.6. Configuring the Syslog log format
To set the logging format for a logged line, perform these steps:
- Build your desired format template using the preceding table.
Enter the following command:
bin/kc.[sh|bat] start --log-syslog-format="'<format>'"
Note that you need to escape characters when invoking commands containing special shell characters such as ;
using the CLI. Therefore, consider setting it in the configuration file instead.
Example: Abbreviate the fully qualified category name
bin/kc.[sh|bat] start --log-syslog-format="'%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c{3.}] (%t) %s%e%n'"
This example abbreviates the category name to three characters by setting [%c{3.}]
in the template instead of the default [%c]
.
16.6.7. Configuring the Syslog type
Syslog uses different message formats based on particular RFC specifications. To change the Syslog type with a different message format, use the --log-syslog-type
option as follows:
bin/kc.[sh|bat] start --log-syslog-type=rfc3164
Possible values for the --log-syslog-type
option are:
- rfc5424 (default)
- rfc3164
The preferred Syslog type is RFC 5424, which obsoletes RFC 3164, known as BSD Syslog protocol.
16.6.8. Configuring the Syslog maximum message length
To set the maximum length of the message allowed to be sent (in bytes), use the --log-syslog-max-length
option as follows:
bin/kc.[sh|bat] start --log-syslog-max-length=1536
The length can be specified in memory size format with the appropriate suffix, like 1k
or 1K
. The length includes the header and the message.
If the length is not explicitly set, the default values are set based on the --log-syslog-type
option as follows:
-
2048B
- for RFC 5424 -
1024B
- for RFC 3164
16.6.9. Configuring the Syslog structured output
By default, the Syslog log handler sends plain unstructured data to the Syslog server. To use structured JSON log output instead, enter the following command:
bin/kc.[sh|bat] start --log-syslog-output=json
Example Log Message
2024-04-05T12:32:20.616+02:00 host keycloak 2788276 io.quarkus - {"timestamp":"2024-04-05T12:32:20.616208533+02:00","sequence":9948,"loggerClassName":"org.jboss.logging.Logger","loggerName":"io.quarkus","level":"INFO","message":"Profile prod activated. ","threadName":"main","threadId":1,"mdc":{},"ndc":"","hostName":"host","processName":"QuarkusEntryPoint","processId":2788276}
When using JSON output, colors are disabled and the format settings set by --log-syslog-format
will not apply.
To use unstructured logging, enter the following command:
bin/kc.[sh|bat] start --log-syslog-output=default
Example Log Message
2024-04-05T12:31:38.473+02:00 host keycloak 2787568 io.quarkus - 2024-04-05 12:31:38,473 INFO [io.quarkus] (main) Profile prod activated.
As you can see, the timestamp is present twice, so you can amend it correspondingly via the --log-syslog-format
property.
16.7. Relevant options
| Value | |
|---|---|
|
|
|
|
Available only when Console log handler is activated |
|
|
Available only when Console log handler is activated | (default) |
|
Available only when Console log handler and Tracing is activated |
|
|
Available only when Console log handler is activated |
|
|
Available only when Console log handler is activated |
|
|
Available only when File log handler is activated | (default) |
|
Available only when File log handler is activated | (default) |
|
Available only when File log handler and Tracing is activated |
|
|
Available only when File log handler is activated |
|
|
Available only when File log handler is activated |
|
|
| (default) |
|
Available only when Syslog is activated | (default) |
|
Available only when Syslog is activated | (default) |
|
Available only when Syslog is activated | (default) |
|
Available only when Syslog handler and Tracing is activated |
|
|
Available only when Syslog is activated |
|
|
Available only when Syslog is activated | |
|
Available only when Syslog is activated |
|
|
Available only when Syslog is activated |
|
|
Available only when Syslog is activated |
|
