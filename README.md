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

**Built With**

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

**Home Page**

- To start your coffee journey, click on the 'Coffee' option in the navigation bar.
- For a more personalized experience, sign up using your Google account to unlock special offers and features.

**Coffee Product Page**

- View All Coffee proudcts.
- Click 'Origin' to filter down the products by origins(Colombia, Ethiopia, Brazil, India).
- Click 'Origin' to filter down the products by roast level(Dark, Medium, Light).
- Click specific item to see more details.

**Product Detail Page**

- See the product image.
- Read the story behind the coffee blend and its origin and flavors.
- Add quantity and click 'Add to Cart' button to buy the coffee.
- Scroll down to explore customer reviews and ratings.

**Cart Page**

- See which products you put in your cart.
- Check quantity and price of the products you have in cart.
- Update the quantity and delete products if you need.
- You can check the total price and click 'Go to Checkout' button to purchase.

**Payment Page**

- Via Stripe, you can check your final order details and have your shipping/payment details set up.

**LogIn/Sign Up Page**

- You can create an account for our website.
- You can also sign up through OAuth with a popular platform, Google.

**Account Page**

- Check your order history.
- Update your account details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Planning

## ERD

![Karma Coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/75a9cb5f-5594-4f9e-abf6-8b5bc28418e9)

## Wireframe

![Untitled](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/d37c1587-dde5-43fc-a373-57df903208fd)

**Inspiration**

One of the primary reasons our team decided on this topic is our shared passion for coffee. As coffee enthusiasts ourselves, we wanted to channel this passion into a project that would not only be technically challenging but also personally fulfilling.

**Aim**

To build a fullstack web application using Python, Django, and postgreSQL.

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

## Project Brief

- Have at least 2 data entities in addition to the User Model - one entity that represents the main functional idea for your app and another with a One:Many or Many:Many relationship with that main entity.
- Use OAuth authentication.
- Implement basic authorization that restricts access to features that need a logged in user in order to work
- Have full-CRUD data operations somewhere within the app's features.
- Have a consistent and polished user interface.
- Be deployed online via Heroku

## MVP - Minimum Viable Product

- [x] AAU, I want a way to login.
- [x] AAU, I want to see the products and product details.
- [x] AAU, I want to add items in the basket, and edit, delete the items in the basket.
- [x] AAU, I want to purchase products.
- [x] AAU, I want to be able to leave and delete reviews for the products I purchased.

## NTH - Nice to have

- [x] AAU, I want to be able to filter the products.
- [x] AAU, I'd like to see payment/order confirmation.
- [x] AAU, I'd like to see my order history.
- [x] AAU, I'd like to read about the company.
- [x] AAU, I'd like to be able to log in with Google.
- [ ] AAU, I want to be able to search specific item.
- [ ] AAU, I want to be able to subscribe.

## Actual Project Screenshots

![app screensot](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/7bf577fa-3b69-4048-b7ef-4936ea5add04)

## Biggest Challenge

The toughest part of this project was to link multiple models developed by different engineers, and ensure minimal impact was had on other developers' code.

Mobile responsive design was especially difficult, going forward, we would implement mobile responsive designs first.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## User Feedback

- [x] Add a larger selection of products
- [x] Allow users to see their order history
- [x] Checkout and purchase as a guest
- [x] Add other authorisation methods
- [ ] Better mobile view

## Next Steps

- Add Google's Places API to demonstrate locations of coffee production sites
- Standardise CSS styling across the site
- Improve the mobile view

## Wins

- **Working as a team of multiple developers on a single project**. This was the first time we'd worked on a project using GitHub as a team. Something we're expected to do in the industry, we're really happy to have achieved a great team dynamic and be able to resolve issues quickly and efficiently!

- **Creating an app people want to use.** I wanted to make something that highlighted the topics I'm learning, and satisfies the project brief, but also something that I'd use and others want to use. From user feedback it seems that I achieved this, and that feel's awesome.

## Mistakes / Bugs

- **Bootstrap trappings** Whilst bootstrap made implementing styling quicker, it made custom styling especially difficult, particularly when it came to mobile responsive design.

- **GitHub Push and Pull Requests** As a team, early on, it was difficult to stay out of each others code and resolve conflict issues, but with practise and time, this became significantly easier.

- **OAuth google** If a user is using multiple accounts with similar names, google OAuth can be blocked.

- **No Edit Functionality on Reviews** At this current time, a user can only create and delete a review, they are unable to.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Learnings

- **GitHub deployment requires constant communication** Working as part of team requires good communication at the best of times, but when creating an app and/or website, constant communication is vital. When pushing new code with additional functionality upstream, and especially when working on functionality that may depend on other developers supporting.

- **Mobile responsiveness first**It became very difficult to go back and tailer our content to mobile views, as such, implementing this first next project would be beneficial.

- **Trust each other**For our first group project, we were all hesitant at the start to delegate too much or too little work to each other, but as the project went on, we understood each other's skills, that everyone could and would contribute to the project.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

## Contact

✨ Ross Simpson - [LinkedIn](https://www.linkedin.com/in/simpsonre/) - thisisrosssimpson@gmail.com / Project Link: [https://github.com/SimpsonRoss/karma-coffee](https://github.com/SimpsonRoss/karma-coffee)

🎉 Jihyeon Cha - [LinkedIn](https://www.linkedin.com/in/jihyeoncha/) - j.cha1708@gmail.com / Project Link: [https://github.com/chajiiiii/karma-coffee](https://github.com/chajiiiii/karma-coffee)

🎊 Rahul Raikhy - [LinkedIn](https://www.linkedin.com/in/rahul-raikhy-31ab62197//) - rlraikhy@gmail.com / Project Link: [https://github.com/rahulraikhy/karma-coffee](https://github.com/rahulraikhy/karma-coffee)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

These resources helped us greatly in the completion of our project.

- [Bootstrap](https://getbootstrap.com/)
- [Trello](https://trello.com/)
- [Photopea](https://www.photopea.com/)
- [Google 0Auth](https://cloud.google.com/endpoints/docs/openapi/authenticating-users-auth0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
