# Test Plan: Hotel Booking QA Project

## 1. Introduction
This document outlines the testing approach for the Restful Booker Platform (Shady Meadows B&B). The goal is to verify the core functionalities of the hotel booking system, including the user-facing website and the admin dashboard.

## 2. Scope
**In Scope:**
- **Login & Authentication:** Admin login with valid/invalid credentials.
- **Room Management:** Viewing room lists and adding new rooms via the admin panel.
- **Booking Flow:** Checking availability, entering guest details, and confirming a reservation.
- **Date Validation:** Testing valid future dates and invalid past dates.
- **Contact Form:** Submitting inquiries from the front page.
- **Messages:** Viewing guest inquiries in the admin panel.
- **API Testing:** Testing Restful Booker API endpoints (Auth, GET, POST, PUT, DELETE).

**Out of Scope:**
- Payment processing (not supported by the demo).
- Performance/load testing.
- Direct database testing (no access provided).

## 3. Test Environment
- **Application URL:** https://automationintesting.online
- **API URL:** https://restful-booker.herokuapp.com
- **Browsers:** Google Chrome (Primary), Mozilla Firefox, Microsoft Edge.
- **Screen Sizes:** Desktop (1920x1080), Mobile (375x667).

## 4. Testing Approach
- **Manual Testing:** Execution of functional, negative, exploratory, and responsive tests.
- **API Testing:** Using Postman to verify status codes, response bodies, and authentication tokens.
- **Automation Testing:** Using Python, Pytest, and Selenium to automate 3 core user journeys (Login, View Rooms, Book Room).

## 5. Entry & Exit Criteria
**Entry Criteria:**
- The application is accessible online.
- The admin credentials (`admin` / `password`) are working.

**Exit Criteria:**
- All High-priority test cases have been executed.
- No open Critical or High-severity bugs.
- API and Automation scripts run successfully.
- Test summary report is completed.

## 6. Deliverables
- Test Plan (This document)
- Test Scenarios & Test Cases
- Bug Reports with screenshots
- Postman API Collection
- Pytest Automation Scripts
- Test Execution & Summary Report

**Author:** [YOUR NAME]
**Date:** [Insert Today's Date]