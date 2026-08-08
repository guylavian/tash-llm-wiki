---
title: "Developing TypeScript functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developing-typescript-functions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developing-typescript-functions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Developing TypeScript functions

[id="serverless-developing-typescript-functions"]
= Developing TypeScript functions

After you have created a TypeScript function project, you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-typescript-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in Setting up {FunctionsProductName}.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

[id="serverless-typescript-template_{context}"]
= TypeScript function template structure

When you create a TypeScript function using the Knative (`kn`) CLI, the project directory looks like a typical TypeScript project. The only exception is the additional `func.yaml` file, which is used for configuring the function.

Both `http` and `event` trigger functions have the same template structure:

.Template structure
[source,terminal]
----
.
├── func.yaml <1>
├── package.json <2>
├── package-lock.json
├── README.md
├── src
│   └── index.ts <3>
├── test <4>
│   ├── integration.ts
│   └── unit.ts
└── tsconfig.json
----
<1> The `func.yaml` configuration file is used to determine the image name and registry.
<2> You are not restricted to the dependencies provided in the template `package.json` file. You can add additional dependencies as you would in any other TypeScript project.
+
.Example of adding npm dependencies
[source,terminal]
----
npm install --save opossum
----
+
When the project is built for deployment, these dependencies are included in the created runtime container image.
<3> Your project must contain an `src/index.js` file which exports a function named `handle`.
<4> Integration and unit test scripts are provided as part of the function template.

[id="serverless-developing-typescript-functions-about-invoking"]
== About invoking TypeScript functions

When using the Knative (`kn`) CLI to create a function project, you can generate a project that responds to CloudEvents or one that responds to simple HTTP requests. CloudEvents in Knative are transported over HTTP as a POST request, so both function types listen for and respond to incoming HTTP events.

TypeScript functions can be invoked with a simple HTTP request. When an incoming request is received, functions are invoked with a `context` object as the first parameter.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

[id="serverless-typescript-functions-context-objects_{context}"]
= TypeScript context objects

To invoke a function, you provide a `context` object as the first parameter. Accessing properties of the `context` object can provide information about the incoming HTTP request.

.Example context object
[source,javascript]
----
function handle(context:Context): string
----

This information includes the HTTP request method, any query strings or headers sent with the request, the HTTP version, and the request body. Incoming requests that contain a `CloudEvent` attach the incoming instance of the CloudEvent to the context object so that it can be accessed by using `context.cloudevent`.

[id="serverless-typescript-functions-context-objects-methods_{context}"]
== Context object methods

The `context` object has a single method, `cloudEventResponse()`, that accepts a data value and returns a CloudEvent.

In a Knative system, if a function deployed as a service is invoked by an event broker sending a CloudEvent, the broker examines the response. If the response is a CloudEvent, this event is handled by the broker.

.Example context object method
[source,javascript]
----
// Expects to receive a CloudEvent with customer data
export function handle(context: Context, cloudevent?: CloudEvent): CloudEvent {
  // process the customer
  const customer = cloudevent.data;
  const processed = processCustomer(customer);
  return context.cloudEventResponse(customer)
    .source('/customer/process')
    .type('customer.processed')
    .response();
}
----

[id="serverless-typescript-functions-context-types_{context}"]
== Context types

The TypeScript type definition files export the following types for use in your functions.

.Exported type definitions
[source,javascript]
----
// Invokable is the expeted Function signature for user functions
export interface Invokable {
    (context: Context, cloudevent?: CloudEvent): any
}

// Logger can be used for structural logging to the console
export interface Logger {
  debug: (msg: any) => void,
  info:  (msg: any) => void,
  warn:  (msg: any) => void,
  error: (msg: any) => void,
  fatal: (msg: any) => void,
  trace: (msg: any) => void,
}

// Context represents the function invocation context, and provides
// access to the event itself as well as raw HTTP objects.
export interface Context {
    log: Logger;
    req: IncomingMessage;
    query?: Record<string, any>;
    body?: Record<string, any>|string;
    method: string;
    headers: IncomingHttpHeaders;
    httpVersion: string;
    httpVersionMajor: number;
    httpVersionMinor: number;
    cloudevent: CloudEvent;
    cloudEventResponse(data: string|object): CloudEventResponse;
}

// CloudEventResponse is a convenience class used to create
// CloudEvents on function returns
export interface CloudEventResponse {
    id(id: string): CloudEventResponse;
    source(source: string): CloudEventResponse;
    type(type: string): CloudEventResponse;
    version(version: string): CloudEventResponse;
    response(): CloudEvent;
}
----

[id="serverless-typescript-functions-context-objects-cloudevent-data_{context}"]
== CloudEvent data

If the incoming request is a CloudEvent, any data associated with the CloudEvent is extracted from the event and provided as a second parameter. For example, if a CloudEvent is received that contains a JSON string in its data property that is similar to the following:

[source,json]
----
{
  "customerId": "0123456",
  "productId": "6543210"
}
----

When invoked, the second parameter to the function, after the `context` object, will be a JavaScript object that has `customerId` and `productId` properties.

.Example signature
[source,javascript]
----
function handle(context: Context, cloudevent?: CloudEvent): CloudEvent
----

The `cloudevent` parameter in this example is a JavaScript object that contains the `customerId` and `productId` properties.
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

[id="serverless-typescript-function-return-values_{context}"]
= TypeScript function return values

Functions can return any valid JavaScript type or can have no return value. When a function has no return value specified, and no failure is indicated, the caller receives a `204 No Content` response.

Functions can also return a CloudEvent or a `Message` object in order to push events into the Knative Eventing system. In this case, the developer is not required to understand or implement the CloudEvent messaging specification. Headers and other relevant information from the returned values are extracted and sent with the response.

.Example
[source,javascript]
----
export const handle: Invokable = function (
  context: Context,
  cloudevent?: CloudEvent
): Message {
  // process customer and return a new CloudEvent
  const customer = cloudevent.data;
  return HTTP.binary(
    new CloudEvent({
      source: 'customer.processor',
      type: 'customer.processed'
    })
  );
};
----

[id="serverless-typescript-function-return-values-headers_{context}"]
== Returning headers

You can set a response header by adding a `headers` property to the `return` object. These headers are extracted and sent with the response to the caller.

.Example response header
[source,javascript]
----
export function handle(context: Context, cloudevent?: CloudEvent): Record<string, any> {
  // process customer and return custom headers
  const customer = cloudevent.data as Record<string, any>;
  return { headers: { 'customer-id': customer.id } };
}
----

[id="serverless-typescript-function-return-values-status-codes_{context}"]
== Returning status codes

You can set a status code that is returned to the caller by adding a `statusCode` property to the `return` object:

.Example status code
[source,javascript]
----
export function handle(context: Context, cloudevent?: CloudEvent): Record<string, any> {
  // process customer
  const customer = cloudevent.data as Record<string, any>;
  if (customer.restricted) {
    return {
      statusCode: 451
    }
  }
  // business logic, then
  return {
    statusCode: 240
  }
}
----

Status codes can also be set for errors that are created and thrown by the function:

.Example error status code
[source,javascript]
----
export function handle(context: Context, cloudevent?: CloudEvent): Record<string, string> {
  // process customer
  const customer = cloudevent.data as Record<string, any>;
  if (customer.restricted) {
    const err = new Error(‘Unavailable for legal reasons’);
    err.statusCode = 451;
    throw err;
  }
}
----
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

[id="serverless-testing-typescript-functions_{context}"]
= Testing TypeScript functions

TypeScript functions can be tested locally on your computer. In the default project that is created when you create a function using `kn func create`, there is a *test* folder that contains some simple unit and integration tests.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function by using `kn func create`.

.Procedure

. If you have not previously run tests, install the dependencies first:
+
[source,terminal]
----
$ npm install
----

. Navigate to the *test* folder for your function.

. Run the tests:
+
[source,terminal]
----
$ npm test
----

[id="next-steps_serverless-developing-typescript-functions"]
== Next steps

* See the TypeScript context object reference documentation.
* Build and deploy a function.
* See the Pino API documentation for more information about logging with functions.
