# Test Scenarios — Hotel Booking QA Project

| Scenario ID | Module | Scenario Description |
| :--- | :--- | :--- |
| TS-LOGIN-01 | Login | Verify successful login with valid admin credentials. |
| TS-LOGIN-02 | Login | Verify login failure with invalid credentials. |
| TS-ROOM-01 | Room Listing | Verify that all available rooms are displayed correctly on the front page. |
| TS-BOOK-01 | Booking | Verify a user can successfully book a room using valid future dates. |
| TS-BOOK-02 | Booking | Verify the system rejects a booking if the check-in date is in the past. |
| TS-BOOK-03 | Booking | Verify the system rejects a booking if the check-out date is before the check-in date. |
| TS-CONTACT-01 | Contact Form | Verify a user can submit a valid inquiry via the contact form. |
| TS-CONTACT-02 | Contact Form | Verify the contact form rejects an invalid email address. |
| TS-MSG-01 | Admin Messages | Verify that an admin can view and delete a guest message. |
| TS-NAV-01 | Navigation | Verify all navigation links (Rooms, Booking, Location, Contact) work correctly. |