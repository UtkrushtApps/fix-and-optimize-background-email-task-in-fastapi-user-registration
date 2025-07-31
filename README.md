## Task Overview

A growing SaaS platform allows clients to register via an API and instantly receive a welcome email. However, the current implementation of background email sending is unreliable—users report that they rarely receive onboarding emails. The business relies on prompt email delivery to encourage customer engagement and support activation goals.

## Guidance

- Analyze the asynchronous flow of the registration endpoint and how background tasks are initiated
- Ensure background operations do not block the main API or user experience
- Use FastAPI's mechanisms for offloading non-user-facing work
- Structure Pydantic models and routers for maintainability
- Consider API responsiveness, correct async/await usage, and performance best practices
- Use dependency injection for extensibility
- Leverage Docker for consistent development and deployment environments
- Ensure email tasks remain robust to errors without leaking exceptions to the main response

## Objectives

- Refactor the registration flow to reliably trigger email background tasks
- Ensure welcome emails are sent without holding up the API's main response
- Maintain clean, async-friendly FastAPI code and promote efficiency
- Use best practices for error handling and email sending simulation (don't actually send emails)
- Ensure the project structure supports easy extension and maintenance

## How to Verify

- Register a user with the API and confirm a background email simulation occurs
- The registration endpoint should return promptly without waiting for the email operation
- Check logs or an in-app buffer to verify each simulated email is triggered per registration
- The app's main event loop should remain healthy—no degraded performance for concurrent users
- Review Pydantic models and route parameters for clarity and proper async handling