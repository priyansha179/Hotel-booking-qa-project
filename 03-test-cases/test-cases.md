# Test Cases — Hotel Booking QA Project

## TC-LOGIN-01: Successful admin login
- **Preconditions:** User is on the Admin login page.
- **Test Data:** Username: `admin`, Password: `password`
- **Steps:**
  1. Given the user is on the Admin login page.
  2. When the user enters valid username and password.
  3. And clicks the "Login" button.
- **Expected Result:** User is redirected to the Admin Dashboard, and the "Rooms" page is visible.
- **Actual Result:** _(To be filled during execution)_
- **Status:** _(Pass/Fail)_

---

## TC-LOGIN-02: Login failure with invalid password
- **Preconditions:** User is on the Admin login page.
- **Test Data:** Username: `admin`, Password: `wrongpassword`
- **Steps:**
  1. Given the user is on the Admin login page.
  2. When the user enters a valid username but an invalid password.
  3. And clicks the "Login" button.
- **Expected Result:** An error message appears stating "Invalid credentials", and the user is not logged in.
- **Actual Result:** _(To be filled during execution)_
- **Status:** _(Pass/Fail)_

---

## TC-BOOK-01: Successful room booking with valid dates
- **Preconditions:** User is on the public front page.
- **Test Data:** Check-in date: 3 days from today, Check-out date: 5 days from today.
- **Steps:**
  1. Given the user is on the front page.
  2. When the user selects valid future check-in and check-out dates.
  3. And clicks "Check Availability".
  4. And selects a room and fills in valid guest details (Name, Email, Phone).
  5. And clicks "Reserve Now".
- **Expected Result:** A confirmation screen appears showing the correct booking details and total price.
- **Actual Result:** _(To be filled during execution)_
- **Status:** _(Pass/Fail)_

---

## TC-CONTACT-01: Submit contact form with invalid email
- **Preconditions:** User is on the public front page.
- **Test Data:** Name: `Test User`, Email: `invalid-email` (missing @), Message: `Hello`
- **Steps:**
  1. Given the user navigates to the "Contact" section.
  2. When the user fills in the Name and Message fields.
  3. And enters an email address without an "@" symbol.
  4. And clicks "Submit".
- **Expected Result:** The form should not submit, and an error message should say "Please enter a valid email address."
- **Actual Result:** _(To be filled during execution)_
- **Status:** _(Pass/Fail)_