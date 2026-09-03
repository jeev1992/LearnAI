# Slide 5

Before we get started, let me quickly walk through today's agenda.

We'll begin by looking at the business-process foundation behind workflows and how workflows fit into the Business Process Catalog.

From there, we'll explore how workflows are organized as deliverables, how they're related to business processes, and how they're documented to provide meaningful business context.

We'll then look at workflow classifications, including workflow types and approval types, and how those help us document implementation patterns and approval behaviors consistently.

After that, Joseph will walk us through a live demonstration of documenting workflows on Azure Devops, and Lennard a demo on visualizing it in Mavim, where you'll see how these concepts come together,

Finally, we'll focus on validation and operational readiness.

We'll discuss how to test workflows, define acceptance criteria, determine when a workflow is truly complete, and what additional considerations are required when workflows include AI or agentic behavior.

So by the end of this session, you'll not only understand how to document workflows, but also how to validate, govern, and operate them effectively throughout their lifecycle.

# Slide 6

Before we start talking about workflows, I want to start with a simple idea.

On many projects, teams naturally jump straight to technology.

We start talking about approvals, automation, Power Automate flows, or workflow configurations.

But if we're not careful, we end up optimizing the technology before we fully understand the business process.

So, Before we decide what to automate, we need to understand the business outcome we're trying to achieve, how the organization operates, who participates in the process, and where automation can actually create value.

The key message I want you to remember is simple:

**A workflow is not the starting point.**

**The business process is the starting point.**

Once we understand the process, we can decide what should be automated, how it should be implemented, and how it should be validated.

With that foundation in mind, let's look at how the Business Process Catalog helps us connect business outcomes, business processes, and implementation work.

---

# Slide 7

This slide introduces the core concepts of the Business Process Catalog.

The catalog is organized around **four interconnected pillars**.

They're interconnected because each pillar answers a different question, but together they create traceability from a business objective all the way through implementation and validation.

Imagine a sales organization that wants to improve how customer orders are processed.

Now let's see how each of these pillars map to it.

The first pillar is **Objectives**.

Objectives answer the question:

**What does success look like?**

In our example, success might mean processing customer orders more efficiently, improving sales execution, and also reducing delays between quotation and order.

But objectives only tell us where we want to go. They don't tell us how the organization gets there.

That's where the second pillar comes in: **Business Processes**.

Business Processes answer the question:

**How does the organization achieve that outcome?**

For example, one end-to-end business process is **Order to Cash**.

Within that End-to-End Business Process we might have a Process Area such as **Manage Sales Orders**. Within that Process Area we might have process such as **Enter Sales Orders**. And within that Process we might have a Scenario such as **Convert a Sales Quotation to a Sales Order in Dynamics 365 Sales**. (You will see all this on Business Process Catalog when Joseph demos it).

Now we're no longer talking about a goal. We're talking about actual business work that people perform.

Once we understand the process, we can ask a different question:

What do we need to build, configure, document, and test to support that process?

That's where the third pillar comes in: **Deliverables**.

Deliverables represent implementation artifacts. These might include requirements, reports, configurations, integrations, workflows etc.

For example, in Customer Service we may have workflows that support things like case assignment, case management, customer-service operations etc. The workflow then becomes a deliverable because it must be designed, documented, tested, and maintained.

And finally, we have the fourth pillar: **Delivery Plan**.

The Delivery Plan answers the question:

**How and when do we deliver the work?**

For example, we may define implementation strategy, test strategy, data strategy, deployment strategy, release strategy, security strategy etc, before the workflow is deployed into production.

For today's discussion we're focusing on workflows.

But a workflow should never exist by itself.

A workflow should support a business process and a business process should support a business objective.

And all of that work should be delivered through a structured implementation plan.

That's the traceability the Business Process Catalog is designed to create.

---

# Slide 8

Now that we've looked at the four interconnected pillars, let's zoom into the Deliverables pillar.

This is where implementation work is organized.

Work is first grouped by functional area and then by more specific business areas.

For example, in the Business Process Catalog, we might start with the functional area Customer Experience, move into the specific business area of Customer Service, where we can see different types of deliverables related to that business area.

Those deliverables are grouped into categories such as requirements, reports, workflows, enhancements etc.

Each deliverable category serves a different purpose.

Out of those different deliverable categories, workflows category is the one which captures automation and process behavior.

The important thing is that the actual workflow records sit underneath the Workflows category as individual deliverable items.

For example, instead of having one generic customer-service workflow, we would document individual workflows separately.

A Case Management workflow would be its own deliverable. A Case Assignment workflow would be its own deliverable. And so on and so forth. And each workflow can then have its own requirements, documentation, acceptance criteria, and testing.

---

# Slide 9

Now that we've seen where workflows live, let's talk about why they exist.

A workflow should never begin with the question:

**"What can we automate?"**

It should begin with a different question:

**"What business outcome and process does this support?"**

And this slide shows that chain.

Everything starts with a business outcome, which is the result the organization wants to achieve.

For example, an organization's goal may be to route customer issues quickly and consistently to the right team.

To achieve that outcome, the organization follows a certain business process.

One example of this End-to-End Business Process from the catalog is **Case to Resolution**.

Within that End-to-End Business Process, there are more specific Process Areas such as **Intake Cases**, **Manage and Work on Cases**, **Analyze Case Performance**, and so on and so forth.

Let's pick **Intake Cases** among those Process Areas.

Within the **Intake Cases** Process Area, there are several Business Processes like **Assign a Case** or **Create a Case Manually**, and many more.

And within that process like **Assign a Case**, there are specific scenarios like **Assign a case to a team or individual in Dynamics 365 Customer Service** or **Assign a case to a queue in Dynamics 365 Customer Service** which is the third box here.

So, a scenario represents a repeatable business pattern within the broader process.

The next step is the system process, which shows how the scenario works in the application which could be a user action associated with a page, form, or system experience.

Only after we understand the outcome, process, scenario, and system behavior do we start talking about deliverables.

And workflows are one example of a deliverable.

A workflow then supports that process through automation.

Finally, the test case validates that the "system process" and "supporting workflow" behave as expected.

Now do you see why the workflow appears here as step five, and not step one. We must first understand the business outcome, process, scenario, and system behavior before selecting the technology.


---

# Slide 10

Now that we've seen how a workflow fits into a business process, the next question is:

**How do we understand the process before we automate it?**

That's where process discovery comes in.

Process discovery helps us understand what should happen before deciding how to automate it.

Let's continue with the same Customer Service example we have been talking about.

We were looking at the **Case to Resolution** End-to-end Business Process, and within it specifically the **Intake Cases** Process Area and within it the **Assign a Case** process.

The first thing we need to understand is the **trigger and the outcome**.

What starts the process, and what business result should it produce?

Mapping it to our example, trigger would be: does the process begin when a new customer case is created?

And the outcome could be: that the case is assigned to the right team?

Next, we look at **people and decisions**.

Who is involved, who makes or approves decisions, and who receives the result?

In our example, the support agent may assign the case, a supervisor may approve certain assignments, and the selected team receives the case.

Then we examine **information and exceptions**.

What data is required, what decisions are made, and what can go wrong?

In our example, we may need the case priority, product, and support category to choose the right team. We also need to decide what happens if that information is missing or the case cannot be assigned.

Finally, we look for **friction and evidence**.

Where are the delays or unclear ownership, and what audit evidence is required?

In our example, cases may be delayed because they are assigned manually or no one knows who owns them. For audit purposes, we may need to record who assigned each case, when it was assigned, and which team received it.

Other useful questions include how frequently the process occurs, where it depends on manual effort today, and what failure or recovery looks like if something goes wrong.

The key message is simple:

**Optimize the process before automating it.**

Otherwise, automation may simply make an inefficient process run faster rather than making the process better.

---

# Slide 11

Now that we've discovered and understood the process, the next step is connecting the workflow to the right business context.

The goal is to relate the workflow to the catalog location that best explains **why the workflow exists**.

A simple rule is to find the lowest level in the catalog that provides meaningful business context.

In many cases, that will be the relevant Level 4 scenario.

A scenario such as "Assign a case to a queue in Dynamics 365 Customer Service" does a much better job of explaining why a workflow exists than simply associating it to the broader **Case to Resolution** end-to-end Business Process.

The more specific context helps everyone understand the purpose of the workflow.

If the workflow directly supports a specific system action, then we should also relate it to the corresponding system process.

A workflow may also support more than one process. In that situation, choose the most meaningful primary relationship and then add additional relationships where appropriate.

A useful question I like to ask is:

**If this automation disappeared tomorrow, which process or scenario would be disrupted?**

The answer usually tells you where the workflow belongs.

And these relationships are not administrative overhead.

They help with impact analysis, test planning, and understanding dependencies.

If someone changes the workflow in the future, we can quickly identify which business processes, scenarios, and tests may also be affected.

---

# Slide 12

Up to this point we've focused on understanding the business process and connecting workflows to the right business context.

Now let's talk about what we mean when we say **workflow**.

One important thing to understand is that the catalog uses the term workflow very broadly.

It's not tied to a single product or a single automation technology.

That's why the catalog treats workflow as a deliverable category rather than a product feature.

In fact, when we look at the workflow types available, we can see several different implementation patterns.

For example, a workflow might be a **Dataverse Business Process Flow**, a **Dataverse Classic Workflow**, a **Finance and Operations Workflow**, a **Power Automate Flow**, etc etc.

These technologies solve different problems, but they're all considered workflow deliverables because they automate or coordinate part of a business process.

The important point is that we classify each workflow based on how it's implemented, but we document each workflow as its own deliverable.

For example, if a project has three separate Power Automate flows, those should be three separate workflow records.

Similarly, if a project has multiple approval workflows with different routing paths, ownership, or business rules, each workflow should be documented separately.

Why?

Because separate workflows usually have different requirements, different owners, different test cases, and different acceptance criteria.

Keeping them separate gives us better traceability, clearer ownership, and more complete test coverage.

---

# Slide 13

Now that we've connected the workflow to the right business process and business scenario, the next step is choosing the correct workflow type.

And it's important to understand what this field is actually describing.

The workflow type identifies **how the workflow is implemented**, not **why the workflow exists**.

Let's look at some examples.

If the workflow uses the standard workflow framework in Dynamics 365 Finance and Operations for approvals, reviews, or task routing, we would select **Finance and Operations Workflow**.

If the workflow guides users through stages in a record-based process, we would select **Dataverse Business Process Flow**.

A Business Process Flow is primarily about guiding the user experience through a defined set of stages rather than acting as a general automation engine.

If we're working with legacy Dataverse workflow automation, we would select **Dataverse Classic Workflow**.

For cloud-based automation, we have two common options.

**Power Automate Flow** is typically used for low-code automation triggered by events, schedules, or user actions.

**Azure Logic App** is generally used when the solution requires Azure-based integration, orchestration, or more advanced enterprise integration capabilities.

And if the workflow requires custom code or an extension of standard workflow behavior, we would select **Custom Workflow Extension**.

The **Other** option should only be used when none of the available workflow types accurately describe the implementation pattern.

The important thing to remember is that this field is only classifying the implementation. It is not explaining the business purpose.

The business purpose should already be clear from the workflow title, its relationship to the business process, the requirements, the acceptance criteria, and the associated test cases.

And shortly, when Joseph walks through the Azure DevOps demo, you'll see exactly how that information comes together in a workflow work item.

---

# Slide 14

On the previous slide, we classified how the workflow is implemented.

This slide focuses on something different.

It's specifically about **approval type**.

In other words:

**How is the approval decision actually made?**

And that's separate from the workflow technology itself.

A workflow might be implemented using Finance and Operations Workflow, Power Automate, or another technology.

But regardless of the implementation, we still need to document how approval decisions are made.

For example, some approvals are based on authority.

A **hierarchical** approval follows the organizational hierarchy.

A **delegated** approval allows someone to act on behalf of another person.

And a **role-based** approval assigns the decision based on a business role rather than a specific individual.

Other approval types focus on participation.

A **named-user** approval requires a specific person to approve.

A **group approval** involves a defined group of participants.

We also have approval types that focus on sequencing.

A **parallel** approval allows multiple people to review at the same time.

A **sequential** approval requires approvals to happen in a specific order.

There are also approval types that introduce additional controls.

For example, **escalated**, **compliance**, and **external** approvals may require additional evidence, oversight, or participants.

And increasingly, organizations are using **AI-assisted** approvals.

So, when AI is involved, it's important to document the grounding sources, authority boundaries, human oversight, escalation path, and evaluation criteria that govern how the recommendation is used.

# Slide 27

Thanks Joseph and Lennard for showing us what that looks like in practice when documenting a workflow in Azure DevOps and visualizing it in Mavim.

So, documenting a workflow is only part of the story.

The next question is:

**How do we know the workflow is actually ready to operate?**

This final section shifts our focus from execution to validation.

We'll look at how to define completion criteria, how to validate that a workflow behaves as expected, and what additional controls are needed when a workflow includes AI or agentic behavior.

In other words, we'll move from documenting the workflow to determining whether it's truly ready for production use.

---

# Slide 28

**How do we know the workflow is actually ready to operate?**

A successful workflow run is not enough for it. Just because an automation engine returns a status of "Succeeded" doesn't mean the business process was successful.

What we really need to validate is the end-to-end business behavior.

Let's continue using our **Case to Resolution** example.

If we're testing a workflow that supports **Assign a Case**, we should certainly test the happy path like:

Can a case be assigned correctly? Can it reach the intended team or queue?

But we should also test every significant **path and decision** like:

What happens when a case is reassigned? What happens when an approval is rejected? What happens if the process is cancelled? etc.

We also need to test **data quality and access controls.**

What happens if required information is missing? OR What happens if invalid information is provided? OR What happens if an unauthorized user attempts to perform an action?

Next, we need to test **failure and recovery.**

What happens if a downstream system is unavailable? What happens if a notification can't be delivered? What happens if the workflow times out or needs to be retried? Can the business process recover? And if automation cannot continue, is there a documented manual path?

We should also think about **scale and change.**

Will the workflow perform correctly under expected volumes? And if the workflow, connector, configuration, or supporting application changes in the future, can we rerun the appropriate tests and confirm the process still behaves as expected?

A good test case should clearly document the objective, the related process, the related requirement and workflow version, the test data, the expected result, the evidence collected, and ultimately whether the test passed or failed.

---

# Slide 29

On the previous slide, we talked about testing.

But testing alone doesn't tell us when a workflow is complete.

That's where acceptance criteria come in.

Acceptance criteria are the clearest definition of what "done" means for a workflow.

They take a requirement and translate it into observable and measurable outcomes that the workflow must satisfy.

Those criteria give both the business team and the project team a shared definition of success.

Before the workflow is complete, its acceptance criteria must be reviewed, approved, and linked to the related work.

But completion isn't just about functionality.

We also need to document how the workflow operates.

That includes the workflow logic, security model, ownership, exception handling, recovery approach, monitoring, and ongoing support responsibilities.

Validation then confirms that each acceptance criterion has been met and the evidence has been recorded.

And finally, we need operational readiness.

The workflow must be deployed correctly, assigned to an owner, and supported by up-to-date documentation.

---

# Slide 30

Up to this point, we've been discussing workflows that follow defined rules and predictable paths.

AI-enabled and agentic workflows introduce a new consideration.

Unlike traditional automation, AI may generate recommendations, or actions based on probability rather than explicit rules.

That means we need all the standard workflow documentation we've discussed so far, plus additional documentation that clearly defines the agent's boundaries and responsibilities.

The first step is defining the **purpose and grounding.**

What business task is the AI performing? What outcome is it trying to achieve? Why is AI appropriate for this step? What information is the AI allowed to use when making a recommendation or decision?

We should document the approved knowledge sources, required context, input data, available tools, connected workflows, and systems the agent can access.

Next, we need to define **authority and autonomy.**

Which actions can the agent perform on its own? Which actions require human review or approval? And which actions are explicitly prohibited?

For example, an AI system might analyze a request and recommend an approval decision, but a human approver may still be required before any action is executed. The escalation conditions and responsible roles should also be clearly documented.

We then define **output expectations.**

What should the response look like? What evidence or explanation should be included? How should uncertainty be handled? What level of traceability or citation is required?

Finally, we need to address **risk and governance.**

That includes security, privacy, compliance, sensitive data handling, safety, logging, monitoring, audit requirements, ownership, review processes, and fallback behavior.

A helpful design pattern is to think of the process as:

Receive a request, validate the data, allow AI to analyze and recommend, require human approval when appropriate, and then execute the action. Around that AI step, we explicitly document the instructions, grounding sources, tools, authority boundaries, guardrails, and escalation path.

---

# Slide 31

On the previous slide, we talked about documenting AI-enabled and agentic workflows.

The next question is:

**How do we evaluate whether the AI is actually behaving appropriately?**

With traditional workflows, we primarily focus on deterministic testing.

We verify that the workflow followed the correct path, executed the right actions, and produced the expected outcome.

But AI-enabled workflows require something more.

We need evaluations in addition to test cases.

The first area is **task quality**.

Did the agent understand the business task? Did it produce an accurate, relevant, complete, and useful result? And did that result support the intended business outcome?

The second area is **grounding and traceability**.

Did the agent use approved knowledge sources and approved tools? Can we trace how it reached its recommendation? And did it clearly distinguish supported information from uncertainty?

Next, we evaluate **boundaries**.

Did the agent stay within its authorized scope? Did it avoid prohibited actions, tools, or data? And did it escalate appropriately when information, confidence, or authority was insufficient?

We also need to evaluate **safety and control**.

That includes privacy, security, compliance, fairness, human oversight, and the ability to review, correct, override, or stop an action when necessary.

And finally, we look at **resilience**.

How does the agent behave when information is missing? What happens when information conflicts? What happens if a tool fails, a system is unavailable, or the underlying model, instructions, or knowledge sources change?

To evaluate those behaviors, we need more than a single test case.

A good evaluation set should include normal scenarios, important variations, missing information, tool failures, human-review situations, prohibited-action boundaries, prompt-injection attempts, and previously discovered failures that should be tested again during regression.

For example, an acceptance criterion might state that an agent must not approve a request above its authority threshold, must escalate when evidence is missing, must use approved knowledge sources, must explain its recommendation, and must not execute a high-impact action without required human approval.

And that leads to the key distinction on this slide.

**Deterministic testing asks whether the system followed the defined path.**

**Agent evaluation asks whether the agent made an acceptable decision within its authority and boundaries.**

For AI-enabled workflows, we need both.
