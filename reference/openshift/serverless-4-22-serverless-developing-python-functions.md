---
title: "Developing Python functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developing-python-functions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developing-python-functions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Developing Python functions

[id="serverless-developing-python-functions"]
= Developing Python functions

After you have created a Python function project, you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-python-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in Setting up {FunctionsProductName}.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-python-functions.adoc

[id="serverless-python-template_{context}"]
= Python function template structure

When you create a Python function by using the Knative (`kn`) CLI, the project directory looks similar to a typical Python project. Python functions have very few restrictions. The only requirements are that your project contains a `func.py` file that contains a `main()` function, and a `func.yaml` configuration file.

Developers are not restricted to the dependencies provided in the template `requirements.txt` file. Additional dependencies can be added as they would be in any other Python project. When the project is built for deployment, these dependencies will be included in the created runtime container image.

Both `http` and `event` trigger functions have the same template structure:

.Template structure
[source,terminal]
----
fn
├── func.py <1>
├── func.yaml <2>
├── requirements.txt <3>
└── test_func.py <4>
----
<1> Contains a `main()` function.
<2> Used to determine the image name and registry.
<3> Additional dependencies can be added to the `requirements.txt` file as they are in any other Python project.
<4> Contains a simple unit test that can be used to test your function locally.
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-python-functions.adoc

[id="serverless-invoking-python-functions_{context}"]
= About invoking Python functions

Python functions can be invoked with a simple HTTP request. When an incoming request is received, functions are invoked with a `context` object as the first parameter.

The `context` object is a Python class with two attributes:

* The `request` attribute is always present, and contains the Flask `request` object.
* The second attribute, `cloud_event`, is populated if the incoming request is a `CloudEvent` object.

Developers can access any `CloudEvent` data from the context object.

.Example context object
[source,python]
----
def main(context: Context):
    """
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    print(f"Method: {context.request.method}")
    print(f"Event data {context.cloud_event.data}")
    # ... business logic here
----
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-python-functions.adoc

[id="serverless-python-function-return-values_{context}"]
= Python function return values

Functions can return any value supported by Flask. This is because the invocation framework proxies these values directly to the Flask server.

.Example
[source,python]
----
def main(context: Context):
    body = { "message": "Howdy!" }
    headers = { "content-type": "application/json" }
    return body, 200, headers
----

Functions can set both headers and response codes as secondary and tertiary response values from function invocation.

[id="serverless-python-function-return-values-returning-events_{context}"]
== Returning CloudEvents

Developers can use the `@event` decorator to tell the invoker that the function return value must be converted to a CloudEvent before sending the response.

.Example
[source,python]
----
@event("event_source"="/my/function", "event_type"="my.type")
def main(context):
    # business logic here
    data = do_something()
    # more data processing
    return data
----

This example sends a CloudEvent as the response value, with a type of `"my.type"` and a source of `"/my/function"`. The CloudEvent `data` property is set to the returned `data` variable. The `event_source` and `event_type` decorator attributes are both optional.
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-python-functions.adoc

[id="serverless-testing-python-functions_{context}"]
= Testing Python functions

You can test Python functions locally on your computer. The default project contains a `test_func.py` file, which provides a simple unit test for functions.

[NOTE]
====
The default test framework for Python functions is `unittest`. You can use a different test framework if you prefer.
====

.Prerequisites

* To run Python functions tests locally, you must install the required dependencies:
+
[source,terminal]
----
$ pip install -r requirements.txt
----

.Procedure

. Navigate to the folder for your function that contains the `test_func.py` file.

. Run the tests:
+
[source,terminal]
----
$ python3 test_func.py
----

[id="next-steps_serverless-developing-python-functions"]
== Next steps

* Build and deploy a function.
