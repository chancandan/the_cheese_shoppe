<div align="center">
  <img src="media/rewadme_welcome_header.png" style="background-color: black" alt="Welcome Image">
</div>
<div align="center">
  <img src="media/am_i_responsive_img_the_cheese_shoppe.png" alt="Home Page">
</div>

[The Cheese Shoppe](https://the-cheese-shoppe.herokuapp.com/) is an online store specialising in a wide variety of cheeses, cured meats, and gourmet products. Designed as a comprehensive e-commerce platform, it seamlessly integrates Stripe for secure and effortless payment processing. The website features a cohesive and captivating theme, showcasing meticulous attention to detail and highlighting the extensive skills developed throughout the project.

## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colors](#colors)
    - [Images](#images)
    </details></li>
    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [All Pages](#all-pages)
    - [Home Page](#home-page)
    - [Product Page](#product-page)
    - [Cheese Page](#hampers-page)
    - [Cured Meat Page](#gifts-page)
    - [Special Offers Page](#special-offers-page)
    </details></li>

    <li><details>
    <summary><a href="#additional-features">Additional Features</a></summary>

    - [Image Loading Blur](#image-loading-blur)
    - [Email](#email)
    </details></li>

    <li><details>
    <summary><a href="#future-ideas">Future Ideas</a></summary>

    - [Basic](#basic)
    - [Content](#content)
    </details></li>
    </ul>
</details>

3. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>

    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [APIs](#apis)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)
</details>

4. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#methods">Methods</a></summary>

    - [Validation](#validation)
    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details></li>

    <li><details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details></li>
    </ul>
</details>

5. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    <ul>
    <li><details>
    <summary><a href="#local-deployment">Local Deployment</a></summary>

    - [Local Preparation](#local-preparation)
    - [Local Instructions](#local-instructions)
    </details></li>

    <li><details>
    <summary><a href="#github-deployment">Github Deployment</a></summary>

    - [Github Preparation](#github-preparation)
    - [Github Instructions](#github-instructions)
    </details></li>
    </ul>
</details>

6. <details open>
    <summary><a href="#credit-and-contact">Credit and Contact</a></summary>

    - [Content](#content)
    - [Contact](#contact)
</details>

----

# UX










skip middle and do end first




## Models

User data is securely managed within a relational database. The core framework has been thoughtfully designed to include features such as product management, order processing, feedback collection, secure card detail storage, and a display of our extensive selection of cheeses, cured meats, and cheese boards:

- UserLogInEntry: Each row represents an entry recording the login activity of users on the website.
- Permission: Each row denotes a specific permission granted to users, dictating their access level within the system.
- Product Category: Each row categorizes products, providing organization and navigation for users browsing the shop.
- Product Wishlist: Each row represents a product that a user has added to their wishlist for future consideration or purchase.- User Wallet: Each row stores information about the wallet or virtual currency balance associated with a user's account.
- Product Review: Each row captures a user's review or feedback on a purchased product, aiding other users in their decision-making process.
- Email Address: Each row stores the email addresses associated with user accounts for communication and identification purposes.Place Order: Each row signifies an order that has been initiated by a user, awaiting confirmation and fulfillment.
- Checkout: Each row records the successful completion of an order transaction, indicating that payment has been processed and products are ready for shipment.

<div align="center">
  <img src="media/.png">
</div>


---

## Additional Features



### Email
- Mailchimp is functional on every page through the newsletter form.


## Future Ideas
### Basic
- Another section above the newsletter such as testimonials.
- An upgrade on the database, some styling added


### Content 
- A wider range of products and images.
- Blog posts on the website for the user making their own cheese sets.

----

# Technologies Used
## Languages
- HTML5
- CSS3
- JavaScript
- jQuery
- Bootstrap
- Python
- Django

## Frameworks
- [Bootstrap4](https://getbootstrap.com/)
    * Used for basic styles and outline.

## Libraries
- [JQuery](https://jquery.com/)
    * Animations and click functions.
- [Google Fonts](https://fonts.google.com)
    * Font Styles.
- [Fontawesome](https://fontawesome.com/)
    * Used for icons


## Platforms
- [Github](https://github.com/)
    * Storing code remotely and deployment.
- [Gitpod](https://gitpod.io/)
    * IDE for project development.

## Other Tools
- [Balsamiq](https://balsamiq.com/)
    * To create wireframes.
- [Favicon Generator](https://www.favicon-generator.org/)
    * Favicons
- [Canva](https://www.canva.com/)
    * Platform for images.
- [Coolors](https://coolors.co/)
    * Creating color pallettes.

----

## Testing
Testing documentation can be found [here.](TESTING.md)


## Search Engine Optimization SEO and Marketing

### SEO
- Descriptive meta tags were added to the main template, including title, description and keywords.
- A sitemap was generated using [xml-sitemaps](https://www.xml-sitemaps.com/) This was generated using the deployed website. The file is included in the root level of the project.
- Robots.txt file was created at the root level of the project. This file tells the search engine crawlers which URLs they can access on the website.


### Marketing
- A newsletter section is featured across the site, enriching user engagement and elevating the store's profile through compelling content and effective SEO practices.

- Facebook Page
<div align="center">
  <img src="./assets/.png" alt="facebook-page">
</div>



## Bugs
### Known Bugs


### Fixed Bugs


----

# Deployment
## Local Deployment
### Local Preparation
**Requirements:**
- An IDE of your choice, such as [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- You will have to set up a connection with an email server through EmailJS:
- You will have to install SASS to compile the CSS. This depends on your system and your method choice. Please see the instructions [here](https://sass-lang.com/install).

### Local Instructions
1.  You can clone the repository with:
    ```
    git clone https://github.com/chancandan/the_cheese_shoppe
    ```
    To disconnect it from the master repository, use:
    ```
    git remote rm origin
    ```
2. Open your IDE and choose the base directory.
3. Here you can install SASS with npm, if you choose, with:
    ```
    npm install -g sass
    ```
4. Run the compiler with:
    ```
    sass --watch assets/css/bootstrap_sass:assets/css
    ```
    This will also watch the bootstrap_sass folder for changes and re-compile the CSS when they are made. This way you can make changes quickly and not worry about re-compiling.
6. Switch the user token for EmailJS with your own. It can be found in the head tag:
    ```
    (function () {
        emailjs.init("<your user token>");
    })();
    ```
5. Run the project with your chosen method. You can drop index.html into a web browser and it should run fine, open a local port and access it or, if you have python installed, run it on an HTTP server with python with a command such as:
    ```
    python3 -m http.server
    ```

## Github Deployment
### Github Preparation
- It is possible to copy or clone the repository directly for deployment, but you will have to compile to make sure the SCSS compiles correctly first. Github Pages' Jekyll themes support this but you will have to make some customisations. Details can be found [here](https://jekyllrb.com/docs/assets/).
**Requirements:**
- A free GitHub account.

### Github Instructions
1. Log in to your GitHub account.
navigate to [https://github.com/chancandan/the_cheese_shoppe](https://github.com/chancandan/the_cheese_shoppe).
1. You can set up your own repository and copy or clone it, or you fork the repository.
2. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
3. GitHub pages will update from the master branch by default.
4. Go to the **Settings** page of the repository.
5. Scroll down to the **Github Pages** section.
7. Select the Master Branch as the source and **Confirm** the selection.
8. Wait a minute or two and it should be live for viewing.

## Credits and Contact
### Content
Nearly all text content was generated by the AI, GPT-4. Especially for product names as I had some many. I also generated random skus using chat-gpt. It certainly helps and found it great
at explaining certain terms but it can be very undependable in certain circumstances and I always double checked any text I generated using it.
Most of my Images were screenshots of cheese items across sites such as (https://.ie/) (https://.ie/) and then I also used Canva.
I used screenshots but then always made sure to change to title and description of products and made up random prices.
I felt I had to use hamper images off certain websites for a consistent look for my images as Canva didnt have enough category hamper images.

### Acknowledgements