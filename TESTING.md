## Testing

### Manual testing

1. As a Shopper / Site User, I want to create an account so that I can access my order history and save my preferences.

**Acceptance Criteria** | **Accomplished** | **Screenshot** |
| ------------ | ------------ | ------------ |
| Registration form with required fields (name, email, password) | YES | ![screenshot](assets/TESTINGimages/sign_up_test.JPG) |
| Validations for email format and password strength | YES | ![screenshot](assets/TESTINGimages/email_validation.JPG) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.3.png)|
| Unique email address requirement | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.4.png) |
| Account creation upon successful registration | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.6.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.7.png) |
| Access to order history after login | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.8.png) |

2. As a Shopper / Site User, I want to Log in and Logout so that I can access my account and saved information and keep my information secure when not using 

**Acceptance Criteria** | **Accomplished** | **Screenshot** |
| ------------ | ------------ | ------------ |
| Visible "Log In" option on homepage | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.1.png) |
| Login form with username/email and password fields  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.6.png) |
| Error message for incorrect credentials  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.2.png) |
| Successful login redirects to authenticated view  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.7.png) |
| Display user's name or profile picture when logged in  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.7.png) |
| Access to account info (order history, addresses)  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.7.png) |
| Visible "Log Out" option when logged in  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.8.png) |
| "Remember Me" option for persistent login  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.6.png) |
| Logout confirmation screen  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.9.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.10.png) |
| Session timeout for security  | YES | Times out after 5 mins of inactivity |
| Thorough testing on various devices and browsers  | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.11.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.12.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.13.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting2.14.png) |

4. As a Shopper / Site User, I receive email verification email after registration to establish account creation.

|  **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Email verification requirement | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.5.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/emailverification1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/emailverification2.png)|

5. As a Shopper / Site User, I can save billing info to my profile for faster future checkouts.

  **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Users can save billing details during checkout. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting5.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting5.2.png)|
| Users can still edit billing details during checkout. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting5.3.png) |


6. As a Shopper / Site User, I can update the profile to change shipping information

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Users can access their profile settings. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting6.2.png) |
| Edit and update shipping information in the profile. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting6.1.png) |
| Confirm changes with clear notifications. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting6.1.png) |
| Provide error handling for profile updates. | NO| No required fields as user is allowed to not save their info to their profile if they wish however phone number can be letters currently which is an issue |
| Ensure compatibility across devices and browsers. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting6.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting6.4.png) |


7. As a Shopper / Site User, I can view order history to keep track of past purchases.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Users can easily access their order history. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting6.2.png)|
| Order history displays past orders with dates, order numbers, and item details. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting7.1.png) |
| Users can click to view more order details. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting7.2.png) |
| Works well on different devices and browsers. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting7.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting7.4.png) Alert message can be clicked away to clearly see content ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting7.5.png) |


9. As a Shopper / Site User I want to understand immediately the purpose of the site so my time is not wasted

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Clearly convey the site's purpose on the homepage through images and design that reflects the vintage/retro theme | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting9.1.png) |
| Offer a user-friendly interface with intuitive navigation to browse and purchase vintage clothing items | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting9.2.png) |


10. As a Shopper / Site User, I want to include a navbar so I can easily access all parts of the site from any page

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --------------------------- | ----------------- | -------------- |
| Prominent navbar that matches theme  | YES  | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting10.1.png) |
| Positioned at the top for easy access | YES   | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting9.2.png) |
| Includes functional links to each page | YES | Each link in navbar is working correctly |
| Mobile-friendly menu for smaller screens  | YES    | issues with gaps beside screen - minimal benefit to fixing and within timeframe decided to leave as did not affected functionality of website. Ideally I would have bag icon and account display i9hn nav header and not in toggle side bar again, left as did turn out to be more complicated to fix that the benefit it gave to users ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting10.4.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting10.5.png)|
| Logo/site name links to the homepage  | YES    | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting10.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting10.3.png) |
| Fixed navbar for easy access while scrolling  | YES    | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting9.2.png) |

11. As a Shopper / Site User, I can access social links in the footer section of the site.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Social links are clearly visible in the footer. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting11.3.png) |
| Links lead to the respective social media profiles. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting11.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtestinh11.2.png)  |
| Links open in a new tab or window for user convenience. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtestinh11.2.png)  |
| The footer design ensures easy access on all devices. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting11.4.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting11.5.png) |


12. As a Shopper / Site User I want to see my login status so I know if I am logged in or not

**Acceptance Criteria** | **Accomplished** | **Screenshot** |
| ------------ | ------------ | ------------ |
| Visible username under account icon when user logged in | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.7.png) |
| Toast success messages appear when user logs in/logs out | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting1.7.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.3.png) |
| Thorough testing on various devices and browsers | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.2.png)|

13. As a Shopper / Site User, I can receive notifications of actions through a toast to know if actions are successful.

14. As a Shopper / Site User I want to browse products so i can see the products available 

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Display a grid or list of available products. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.1.png) |
| Include clear product images, names, and prices. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.3.png) |
| Implement filters or categories for easy navigation. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.4.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.5.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.6.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.7.png)|
| Enable sorting options (e.g., by price, by condition). | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.8.png) |
| Pagination or infinite scrolling for large product catalogs | NO | Will not apply as only limited number of products added |
| Responsive design for mobile users. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.13.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.14.png)|
| Clickable product cards to view more details. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.9.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.10.png) |
| Provide a search bar for specific product searches. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.11.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.12.png)|
| Fast loading times for product pages. | YES | Used web.p images for quicker loading |


15. As a Shopper / Site User, I can view high-quality images of vintage items to examine their condition and details.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Include clear product images, names, and prices. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.3.png)|

16. As a Shopper / Site User I want to view my bag and total cost from any page on site so i can be aware of total cost of bag as I am browsing

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Display a visible bag icon or link on all site pages | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.1.png) |
| Show the current total cost of items in the bag | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.2.png) |
| Update the total cost as users add/remove items | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.4.png) |
| Ensure responsive design for mobile and desktop | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.5.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.6.png)|


17. As a Shopper / Site User, I can view individual product details by clicking to make more informed purchase decisions.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Users can click on a product to view its detailed information. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting17.1.png) |
| Product details include images, description, price, size and condition. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting17.2.png) |
| Users can easily navigate back to the product list from the product details page. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting17.3.png)  ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting17.4.png) |


18. As a Shopper / Site User, I can CRUD product reviews to help users and myself make informed purchases on similar products.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Users can create new product review of bought product by providing a rating and written comments when logged in. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.3.png) |
| Validated form for rating numbers | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.4.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.5.png)|
| Users can view and edit their own product reviews if they are logged in. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.6.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.7.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.8.png)|
| Users can delete their own product reviews if needed. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.9.png) |
| Toasts | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.10.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.11.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting18.12.png)|


20. As a Shopper / Site User I want to filter products by category so I can narrow down my search results and easily find items that interest me. 

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Implement filters or categories for easy navigation. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.4.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.5.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.6.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.7.png)|
| Provide clear and easy-to-use filter controls. | YES | As above |
| Display relevant filter options based on available products. | YES | Filter by catgegory and gender displaying relevant producst - issues with skirts and dresses displaying for men categories however no products will display and hence will be a future fix as dies not affect functionality of product category sorting |
| Include appropriate labels and descriptions for each filter. | YES | As above |
| Ensure responsive design for mobile and desktop users. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting20.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting20.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting20.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting20.4.png)  |


21. As a Shopper / Site User I want to sort items by price, by condition (low to high and vice versa) so I can quickly find what I'm looking for

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Implement sorting options for price (low to high and high to low) | YES |  ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.8.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.4.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.5.png) |
| Implement sorting options for the condition of clothes (low to high and high to low) | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.8.png)  ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.3.png) |
| Display clear and easy-to-use sorting controls | YES |  ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting14.8.png) | |
| Maintain consistency in sorting across all product categories | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.6.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.7.png) |
| Ensure responsive design for mobile and desktop users | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.8.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.9.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.10.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting21.11.png)|

23. As a Shopper / Site User, I can search for a product by name, description or keywords to find a specific product.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Users can enter keywords, product names, or descriptions into the search bar. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting23.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting23.2.png) |
| The search function returns relevant products that match the entered keywords. | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting23.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting23.4.png) |


24. As a Shopper / Site User I want to add items to my bag so I can keep track of what i want to buy and have total added up

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Include an "Add to Bag" or "Add to Cart" button on each product | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting17.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting17.1.png) |
| Allow users to click this button to add items | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting24.1.png) |
| Provide a visual confirmation of the added item | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting24.1.png) |
| Enable easy adjustments (removal only in our case) | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting24.2.png) |
| Show the current total cost of items in the bag | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.2.png) |
| Update the total cost as users add/remove items | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.4.png) |
| Ensure responsive design for mobile and desktop | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.5.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.6.png)|

26. As a Shopper / Site User, I can use a card as the payment method to complete the purchase.
![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting26.1.png)


28. As a Shopper / Site User I want to view items in my bag so I can be aware of what I am buying and it's cost

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| Allow users to click the bag icon to view its contents | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.1.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting12.2.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.5.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.6.png) |
| Enable easy adjustments (removal only in our case) | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting24.2.png) |
| Provide a summary of items with names, quantities, prices, and subtotals | YES | As above |
| Display a visible bag icon or link on all site pages | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.1.png) |
| Show the current total cost of items in the bag | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.2.png) |
| Update the total cost as users add/remove items | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.3.png) ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting16.4.png) |

30. As a Store Owner / Admin, I can manage product listings by adding, editing, or removing products from the catalog.

| **Acceptance Criteria** | **Accomplished** | **Screenshot** |
| --- | --- | --- |
| adding through admiin | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting30.1.png) |
| editing through admiin | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting30.2.png) |
| deleting through admiin | YES | ![screenshot](https://vintagepp5.s3.eu-west-1.amazonaws.com/manualtesting30.3.png) |