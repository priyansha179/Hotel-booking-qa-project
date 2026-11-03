# Test Execution Report & Summary

## 1. Metrics
- **Total Manual Test Cases:** 5
- **Passed:** 3
- **Failed:** 2 (Found 2 Bugs)
- **API Tests:** 1 Postman Collection (Passed)
- **Automation Tests:** 1 Pytest + Selenium Script (Passed)

## 2. Bugs Found
- **BUG-001:** Booking page gets stuck on infinite loading spinner. (High Severity)
- **BUG-002:** Contact form shows success but message does not appear in Admin inbox. (High Severity)

## 3. Limitations
- **Environment:** The Restful Booker demo site experienced severe lag and React loading issues during automation. To demonstrate Selenium skills reliably, the login automation was performed on SauceDemo.
- **Database:** Direct database access was not available; data consistency was verified via the UI and API.

## 4. Conclusion
The core booking flow is functional but has severe validation and integration bugs. The API performs reliably. The automated suite successfully logs in and verifies the dashboard.