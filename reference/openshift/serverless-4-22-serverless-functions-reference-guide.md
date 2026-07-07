---
title: "Functions development reference guide"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-reference-guide
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-reference-guide
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Functions development reference guide

[id="serverless-functions-reference-guide"]
= Functions development reference guide

{FunctionsProductName} provides templates that can be used to create basic functions. A template initiates the function project boilerplate and prepares it for use with the `kn func` tool. Each function template is tailored for a specific runtime and follows its conventions. With a template, you can initiate your function project automatically.

Templates for the following runtimes are available:

// add xref links to docs once added
* Node.js
* Quarkus
* TypeScript
//* SpringBoot - TBC

// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-reference-guide.adoc

[id="serverless-nodejs-context-object-reference_{context}"]
= Node.js context object reference

The `context` object has several properties that can be accessed by the function developer. Accessing these properties can provide information about HTTP requests and write output to the cluster logs.

[id="serverless-nodejs-context-object-reference-log_{context}"]
== log

Provides a logging object that can be used to write output to the cluster logs. The log adheres to the Pino logging API.

.Example log
[source,javascript]
----
function handle(context) {
  context.log.info(“Processing customer”);
}
----

You can access the function by using the `kn func invoke` command:

.Example command
[source,terminal]
----
$ kn func invoke --target 'http://example.function.com'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"Processing customer"}
----

You can change the log level to one of `fatal`, `error`, `warn`, `info`, `debug`, `trace`, or `silent`. To do that, change the value of `logLevel` by assigning one of these values to the environment variable `FUNC_LOG_LEVEL` using the `config` command.

[id="serverless-nodejs-context-object-reference-query_{context}"]
== query

Returns the query string for the request, if any, as key-value pairs. These attributes are also found on the context object itself.

.Example query
[source,javascript]
----
function handle(context) {
  // Log the 'name' query parameter
  context.log.info(context.query.name);
  // Query parameters are also attached to the context
  context.log.info(context.name);
}
----

You can access the function by using the `kn func invoke` command:

.Example command
[source,terminal]
----
$ kn func invoke --target 'http://example.com?name=tiger'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"tiger"}
----

[id="serverless-nodejs-context-object-reference-body_{context}"]
== body

Returns the request body if any. If the request body contains JSON code, this will be parsed so that the attributes are directly available.

.Example body
[source,javascript]
----
function handle(context) {
  // log the incoming request body's 'hello' parameter
  context.log.info(context.body.hello);
}
----

You can access the function by using the `curl` command to invoke it:

.Example command
[source,terminal]
----
$ kn func invoke -d '{"Hello": "world"}'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"world"}
----

[id="serverless-nodejs-context-object-reference-headers_{context}"]
== headers

Returns the HTTP request headers as an object.

.Example header
[source,javascript]
----
function handle(context) {
  context.log.info(context.headers["custom-header"]);
}
----

You can access the function by using the `kn func invoke` command:

.Example command
[source,terminal]
----
$ kn func invoke --target 'http://example.function.com'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"some-value"}
----

[id="serverless-nodejs-context-object-reference-http-requests_{context}"]
== HTTP requests

method:: Returns the HTTP request method as a string.
httpVersion:: Returns the HTTP version as a string.
httpVersionMajor:: Returns the HTTP major version number as a string.
httpVersionMinor:: Returns the HTTP minor version number as a string.
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-reference-guide.adoc

[id="serverless-typescript-context-object-reference_{context}"]
= TypeScript context object reference

The `context` object has several properties that can be accessed by the function developer. Accessing these properties can provide information about incoming HTTP requests and write output to the cluster logs.

[id="serverless-typescript-context-object-reference-log_{context}"]
== log

Provides a logging object that can be used to write output to the cluster logs. The log adheres to the Pino logging API.

.Example log
[source,javascript]
----
export function handle(context: Context): string {
    // log the incoming request body's 'hello' parameter
    if (context.body) {
      context.log.info((context.body as Record<string, string>).hello);
    } else {
      context.log.info('No data received');
    }
    return 'OK';
}
----

You can access the function by using the `kn func invoke` command:

.Example command
[source,terminal]
----
$ kn func invoke --target 'http://example.function.com'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"Processing customer"}
----

You can change the log level to one of `fatal`, `error`, `warn`, `info`, `debug`, `trace`, or `silent`. To do that, change the value of `logLevel` by assigning one of these values to the environment variable `FUNC_LOG_LEVEL` using the `config` command.

[id="serverless-typescript-context-object-reference-query_{context}"]
== query

Returns the query string for the request, if any, as key-value pairs. These attributes are also found on the context object itself.

.Example query
[source,javascript]
----
export function handle(context: Context): string {
      // log the 'name' query parameter
    if (context.query) {
      context.log.info((context.query as Record<string, string>).name);
    } else {
      context.log.info('No data received');
    }
    return 'OK';
}

----

You can access the function by using the `kn func invoke` command:

.Example command
[source,terminal]
----
$ kn func invoke --target 'http://example.function.com' --data '{"name": "tiger"}'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"tiger"}
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"tiger"}
----

[id="serverless-typescript-context-object-reference-body_{context}"]
== body

Returns the request body, if any. If the request body contains JSON code, this will be parsed so that the attributes are directly available.

.Example body
[source,javascript]
----
export function handle(context: Context): string {
    // log the incoming request body's 'hello' parameter
    if (context.body) {
      context.log.info((context.body as Record<string, string>).hello);
    } else {
      context.log.info('No data received');
    }
    return 'OK';
}
----

You can access the function by using the `kn func invoke` command:

.Example command
[source,terminal]
----
$ kn func invoke --target 'http://example.function.com' --data '{"hello": "world"}'
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"world"}
----

[id="serverless-typescript-context-object-reference-headers_{context}"]
== headers

Returns the HTTP request headers as an object.

.Example header
[source,javascript]
----
export function handle(context: Context): string {
    // log the incoming request body's 'hello' parameter
    if (context.body) {
      context.log.info((context.headers as Record<string, string>)['custom-header']);
    } else {
      context.log.info('No data received');
    }
    return 'OK';
}
----

You can access the function by using the `curl` command to invoke it:

.Example command
[source,terminal]
----
$ curl -H'x-custom-header: some-value’' http://example.function.com
----

.Example output
[source,terminal]
----
{"level":30,"time":1604511655265,"pid":3430203,"hostname":"localhost.localdomain","reqId":1,"msg":"some-value"}
----

[id="serverless-typescript-context-object-reference-http-requests_{context}"]
== HTTP requests

method:: Returns the HTTP request method as a string.
httpVersion:: Returns the HTTP version as a string.
httpVersionMajor:: Returns the HTTP major version number as a string.
httpVersionMinor:: Returns the HTTP minor version number as a string.
