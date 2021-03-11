Feature: VistaSoft IoT Monitor Login
    Scenario: Login to VistaSoft with valid parameters
        Given I launch Chrome browser
        When I open VistaSoft Homepage
        And User navigates to login page
        And Enter username "dd_test_1@outlook.com" and password "}krK,gdC6"
        And Click on log-in button
        Then User must successfully login to the VistaSoft Monitor main page