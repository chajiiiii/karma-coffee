# Karma Coffee - Ethical Coffee from Around the World

![karma-coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/aa5eea7d-9988-4ad3-b80d-760e32fb1f2e)

<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About The Project</a>
    <li><a href="#website">Visit the Itinera Site</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#erd">ERD</a></li>
    <li><a href="#wireframe">Wireframe</a></li>
    <li><a href="#planning">Planning</a></li>
    <li><a href="#biggest-challenge">Biggest Challenge</a></li>
    <li><a href="#user-feedback">User Feedback</a></li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#wins">Wins</a></li>
    <li><a href="#key-learnings">Key Learnings</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About

Welcome to Karma Coffee, where your coffee cravings meet the convenience of online shopping.

Karma Coffee is a robust and user-friendly coffee product ecommerce app designed to bring the rich world of coffee directly to your fingertips. Whether you're an avid coffee connoisseur or just starting to explore the world of specialty blends, our mission is to offer high-quality coffee products from different parts of the world while ensuring ethical sourcing. Karma Coffee has you covered.

This project was collaboratively developed by a team of three individuals and completed within a seven-day timeframe.

For this project we built a fullstack application using these tools:

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

## Website

<strong><p><a href="https://karma-coffee-abe41bfb39f9.herokuapp.com/">Click to view the Karma Coffee website☕</a></p></strong>

<!-- GETTING STARTED -->

## Getting Started

- Visit the <a href="https://karma-coffee-abe41bfb39f9.herokuapp.com/">website</a>
- Test card details in order to test stripe checkout
  - Test Card: Success
    4242 4242 4242 4242
  - Test Card: Failed
    4000 0000 0000 0002
  - Test Card: 3DS Auth Needed
    4000 0027 6000 3184
- Enter any expiry date, for example:
  12/34
- Enter any 3 digit security code, for example:
  234

## Features & Contributions

**Coffee Product Page** (Implemented by **Jihyeon**)

- View All Coffee proudcts.
- Click 'Origin' to filter down the products by origins(Colombia, Ethiopia, Brazil, India).
- Click 'Roast' to filter down the products by roast level(Dark, Medium, Light).
- Click specific item to see more details.

<br>

**Product Detail Page** (Implemented by **Jihyeon**)

- See the product image.
- Read the story behind the coffee blend and its origin and flavors.
- Add quantity and click 'Add to Cart' button to buy the coffee.
- Scroll down to explore customer reviews and ratings.

<br>
<details>
<summary>Contributions of Other Team Members</summary>
**Home Page** (Implemented by Ross)

- To start your coffee journey, click on the 'Coffee' option in the navigation bar.
- For a more personalized experience, sign up using your Google account to unlock special offers and features.

**Cart Page**(Implemented by Ross)

- See which products you put in your cart.
- Check quantity and price of the products you have in cart.
- Update the quantity and delete products if you need.
- You can check the total price and click 'Go to Checkout' button to purchase.

**Payment Page** (Implemented by Ross)

- Via Stripe, you can check your final order details and have your shipping/payment details set up.

**LogIn/Sign Up Page** (Implemented by Rahul)

- You can create an account for our website.
- You can also sign up through OAuth with a popular platform, Google.

**Account Page** (Implemented by Ross)

- Check your order history.
- Update your account details.
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Planning

## ERD

![Karma Coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/75a9cb5f-5594-4f9e-abf6-8b5bc28418e9)

## Wireframe

![Untitled](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/d37c1587-dde5-43fc-a373-57df903208fd)

**Inspiration**

One of the primary reasons our team decided on this topic is our shared passion for coffee. As coffee enthusiasts ourselves, we wanted to channel this passion into a project that would not only be technically challenging but also personally fulfilling.

**Landing Page**

Users will land on a home page that showcases the essence of our coffee products, and by click 'Coffee' button to start exploring our products.

**Product Selection and Filters**

- Users can easily browse through our diverse collection of premium coffee beans each accompanied by enticing descriptions and visuals of the product.
- We will provide powerful search and filtering options, enabling users to quickly find their desired coffee based on roast level, origin, and more.

**Oauth/Login**

- Users will be able to sign up via Google OAuth.

**Profile Page**

- The user will have a profile page where they can see all of their past orders.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Actual Project Screenshots

![app screensot](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/7bf577fa-3b69-4048-b7ef-4936ea5add04)

## Biggest Challenge

The toughest part of this project was to link multiple models developed by different engineers, and ensure minimal impact was had on other developers' code.

Mobile responsive design was especially difficult, going forward, we would implement mobile responsive designs first.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Mistakes / Bugs

- **Bootstrap trappings** Whilst bootstrap made implementing styling quicker, it made custom styling especially difficult, particularly when it came to mobile responsive design.

- **GitHub Push and Pull Requests** As a team, early on, it was difficult to stay out of each others code and resolve conflict issues, but with practise and time, this became significantly easier.

- **OAuth google** If a user is using multiple accounts with similar names, google OAuth can be blocked.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Learnings & Wins

- **GitHub Deployment Requires Constant Communication** \
  While it was our first experience working as a team, we encountered and overcame various challenges during this project. These hurdles, though initially daunting, ultimately contributed to our growth and development. <br>
  <br>
  Our success depended on our hard works and close collaboration to align the deployment process with our project's objectives. This experience underscored the importance of teamwork and effective communication. <br>
  <br>
  This project served as a valuable learning experience, laying the foundation for future successes. It showcased our dedication, adaptability, and shared passion for creating a team project. <br>
  <br>

- **Daily-Use E-commerce App Creation** \
  We successfully developed a practical e-commerce app tailored for everyday use. Our focus was on simplifying and enhancing users' daily shopping experiences. This achievement demonstrates our commitment to creating innovative solutions that fit seamlessly into people's lives.

<!-- CONTACT -->

## Contact

🎉 Jihyeon Cha - [LinkedIn](https://www.linkedin.com/in/jihyeoncha/) - j.cha1708@gmail.com / Project Link: [https://github.com/chajiiiii/karma-coffee](https://github.com/chajiiiii/karma-coffee)

<details>
<summary>Team members</summary>

✨ Ross Simpson - [LinkedIn](https://www.linkedin.com/in/simpsonre/) - thisisrosssimpson@gmail.com / Project Link: [https://github.com/SimpsonRoss/karma-coffee](https://github.com/SimpsonRoss/karma-coffee)

🎊 Rahul Raikhy - [LinkedIn](https://www.linkedin.com/in/rahul-raikhy-31ab62197//) - rlraikhy@gmail.com / Project Link: [https://github.com/rahulraikhy/karma-coffee](https://github.com/rahulraikhy/karma-coffee)

</details>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

These resources helped us greatly in the completion of our project.

- [Bootstrap](https://getbootstrap.com/)
- [Trello](https://trello.com/)
- [Photopea](https://www.photopea.com/)
- [Google 0Auth](https://cloud.google.com/endpoints/docs/openapi/authenticating-users-auth0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
