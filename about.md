---
layout: inner
title: About
permalink: /about/
---
## Project Proposal: The Beginning

**Main Functions:**  A site that generates 7 principles.

>What does a company do with its data, and is it good?

Display these 7 principles with checkmarks for privacy, data shared with 3rd parties, ... and provide full transparency of what's embedded in Terms & Conditions -> translate the legal language.  Start by scraping the website: scrape _Terms and Conditions_.

[Back to main](/index.html).

# Chrome Extension

Natural language processing lets us identify key words; before a user visits a new site, use NLP to read privacy agreements, and provide a mechanism to continue to the site.  Our Chrome extension pulls past results from the site, visualizing site data across sites as an extra feature.

## Purpose

Want to improve the knowledge base of users, so that they are notified of privacy based on the following **principles:**  We train our model based on the criteria.

###### Criteria

| principle | definition |
|:-------------|:------------------|
| Privacy | <- what do we really mean by 'privacy', what are our criteria for _good_ and _bad_? |
| Consent |  |
| Consequences |  |
| Data Collected | |
| Primary usage of data collected | |
| Secondary usage of data collected | |
| Improper access after collection | |
| Errors in data handling | |

## Ethical Data

Ethical Data- It's about studying and evaluating moral problems related to data.
moral problems related to data (including generation, recording, curation, processing, dissemination, sharing and use), algorithms (including artificial intelligence, artificial agents, machine learning and robots) and corresponding practices (including responsible innovation, programming, hacking and professional codes), in order to formulate and support morally good solutions (e.g. right conducts or right values).

Data Ethics focus on third-party practices with individuals’ data, while information ethics span more broadly to media, journalism, and library and information science.
Principles-
Fairness, Reliability, Safety, Transparency,Privacy and security, Inclusiveness
forget about google analytics and what according to you are the current practices that you consider as unethical?
Human rights can do this debate.
Tech literacy is a must.

Privacy - use of user data, prediction of sensitive attributes (e.g., an employee churn prediction model will often flag all women age 28-35, the most common age to get pregnant)

Consent - is it ethical to use my medical data to improve models to read CT scans? What level of information do I need to reasonably consent to that?

Security - adversarial attacks, data security

Layoffs - is it ethical to outright automate people's work? An entire industry?

Bias - literally google "AI Bias"

<span style="background-color:orange">
Transparency - google explainable ai. Interpretability, auditability, data source traceability, how it's updated, etc.
</span>

Medical research are also having user's data.
Companies having user's data by purchasing location data.

People are not happy with sharing data but does it make it unethical?

Like, the difference between “my doctor has a bunch of data on me and can prevent me from getting sick” and “amazon has a bunch of data on me and can warn me when I’m about to run out of diapers” is a matter of degree, but ultimately the value exchange is there. if you can improve customer experience quantifiably, isn’t ANY data collected in the course of doing so ultimately “ethical”??

Any ideas with this [dataset](https://www.kaggle.com/amr009/ethical-data-collection-for-financial-news)

How human rights and data ethics collide? consent is needed?

what is considered to be public data for research work?
IRBs

Twitter tweets used for research? 70% dont have any idea
users thought it's not allowed.

### When you want to sign up for a page or site:

- Twitter has in its privacy policy that researchers can use their tweets.
  - Is their data shared with advertisers?
  - These are the key points of how your privacy is being handled when you want to sign up for a page or site.
    - Either direct copy and paste into our tool, or use our Chrome extension in which we run analysis on the 50 most popular sites.
    - Education
  - NLP for scraping privacy policy
  - Legal documentation -> legal docs are standardized -> look at conventional format.

## Considering Blockchain and decentralized applications

Let's understand Blockchain

Blockchain uses peer to peer technology to send payments or data from one entity to other without any involvement of financial institution. Don't need to trust any 3rd party intermediaries to complete a monetary transaction. It does it like this to make sure that data is completely secured and it is efficient without excessive cost and time. Transactions are borderless (sending to someone in India, Japan or Germany is no different from sending to your neighbour)
Blockchain aim is to create a digital form of cash and trusted form of currency.
Blockchain is a way to store data securely.

Basically, what happens is your data is divided in blocks. These blocks are connected in a chain, with each block having a security code that depends on the previous block.

This makes hard to manipulate data. If there are 10 blocks in the chain and you manipulate block 1, then the security code for block 2 is wrong. So you need to manipulate block 2, but then block 3 is wrong. So you need to keep manipulating all the way to the end.
blockchain is a glorified spreadsheet (think: Excel with one table). It's a new way to store data.
In traditional databases there’s usually one person who’s in charge, who decides who can access and input data, who can edit and remove it. That’s different in a blockchain. Nobody’s in charge, and you can’t change or delete anything, only view and input data.
Since blockchains can have a tremendous amounts of blocks (527125 for bitcoin right now), the fact that you have to go through everything makes messing with stuff a hassle.

Two types of Blockchain-
1. Permissioned Blockchain- It's a centralised authority which allocates responsibility to individuals to operations of blockchain. limited people can join in.
2. Permissionless Blockchain- Anyone can join network and take part. Anyone can operate as full nodes and start mining. Just like Ethereum and Bitcoin.

Now what's bitcoin?
Simply, a digital currency that uses blockchain.
if anyone wants to study [more](https://github.com/bitcoinbook/bitcoinbook)


what's relevant with decentralized applications?
Trustless business models which are not possible with our traditional user-to-server architectures. For instance enforceable contracts, tokenisation, transparent voting, peer decision making algorithms and more.

Ethereum major role in gaming
Some existing games that use Ethereum Blockchain- KryptoWar, Gods Unchained, EtherKingdom, [CrytoKitties](https://cryptoguide.ch/games/eth/ethgame3.html)

what is meant by 100% decentralized game?
It means all data used to run the game is stored on Blockchain(basically we don't have any database)
In KryptoWar-  Grab the army names, soldiers count, battles results directly from the Blockchain using Web3.js (the Ethereum Javascript API).


With centralized applications:
If you want to build a website or an app right now and want to store some data like usernames or recipes you will need to have your own database that will let you store and retrieve data. This is very effective but it has some drawbacks:

You can be hack and get all of your data stolen

<span style="color: lightblue; background-color: grey">
You can lose your data because of simple mishandling, a bug, an hack
</span>
It is centralized which means that you can be the only person/company accessing those data (makes collaboration difficult)

With decentralized applications(DApps)
If you build a similar website or app on the Ethereum Blockchain:

You won't be hacked, it's impossible for a hacker to delete data from the Blockchain (if you don't allow it in your smart contract)

Anyone could build services on top of your smart contract (which could open up a new era of innovation and interactions between companies)

You can create a true ownership of data for your users


Game on the Blockchain, any decentralized app could connect to our smart contract with Web3.js and create another game for the owners of our armies.

## DESIGN OF SMART CITY SYSTEMS FROM A PRIVACY PERSPECTIVE

Because supposedly over 50% of our global population now lives in cities, and because cities are complex systems characterized by a massive number of interconnected citizens, businesses, communication networks, and services and utilities, Smart Cities need to combine and balance factors including: economy, mobility, environment, people, living and governance, built on the smart combination of endowment and activities of self-decisive, independent and aware citizens.

We need to prevent smart cities from invading citizens' privacy, because if we only knew what some of our citizens were up to then we would literally not be able to function as a society.

The aim of the research is to gain an understanding of citizens' perspective on privacy issues, treating citizens as rational beings and yet making sure that power is not allocated to the unearned. I mean, we really want to make sure that information collected is used for its original purpose. Six key dimensions have been identified: (1) collection, (2) secondary usage, (3) errors, (4) improper access, (5) control, (6) awareness. Apparently, large amounts of Personally Identifiable Information are collected, used for secondary purposes, and we've got to pay attention to the degree of effectiveness and the margin of error between what a person thought was true and what actually happened with regard to protections against improper access; their level of awareness of the truth versus the degree to which they perceive their adequate control over personal information.

Prof. Marc Langheinrich contributed to the area of privacy by design by developing the following practices (you know he did):

**Notice (notifying the users when you collect their data)!,** choice and consent (explicit consent, come on people), proximity and locality (they've gotta be there when you're collecting it!), anonymity and pseudonymity (we should provide our own service in the event that they actually don't consent to the collection of data from their device.).  We aim to provide an alternative in the event that they **need a security mechanism before they go on site.**
Oh! And there are more. Security: there should always be security mechanisms providing adequate protection for collected data. Access and resource: Access to the user's data, once collected, should only be allowed to authorized persons.

So this research project is about implementing the Action Design Research methodology.

It revolves around a 1000-citizen survey regarding citizens' perspectives on large scale "real-life" experimentations of intelligent acoustic solutions providing "situational awareness" by using audio monitoring in combination with Internet of Things (IoT) technologies, via a deployment of Audio Processing Units (APUs) in the targeted in-door and out-door environments as complementary to intelligent sensors - the APU consisted of a microphone and an embedded processing platform that continuously "listened" to its environment and analyzed the sound locally.

They collected surveys - familiarity with the concept of audio monitoring, concerns about the collection of personal data, secondary use of data and improper access (when the organization collecting the data shares the data with other organizations), control and awareness (concerns about control and awareness of their audio being collected), usage scenarios...

So the design principles for privacy protective smart city systems are, based on what citizens were not overly positive towards in terms of audio monitoring:

General placement of sensors, no personal data storage, stream data, sensor systems in solitude.

These are some of the factors we might look for in our projects.  **Help improve their knowledge base of these factors.**


SERIOUS GAMES IS ACTUALLY A CONCEPT
Serious games are games whose primary objective is NOT fun or entertainment, rather learning, practicing a skill or a primary purpose.
Eg a therapy game for a children's rehab centre
Our primary purpose/objective is privacy and security [ethical data](https://www.hiig.de/en/serious-games-as-a-tool-for-privacy-by-design/)
The first concept, "Who's Sherlock" is a Q and A game that lets its players experience how easy it is to find information about oneself and others on the internet, and how sensitive this kind of information can be in different contexts.

The second game concept, "Privacy Rush", illustrates the moment when an individual wants to connect with a public wifi system and seeks to inform them prior to when they actually use the insecure connection, about the privacy risks.

The third game concept is a card game: "Data Trade" addresses the complexity of today's data economy by demonstrating, from the perspective of a day trader, how different data sets can be combined, leading to a higher price on data markets because they generate more information about individuals. Do you know what they are talking about? They are talking about inference: just as an example, multiple pieces of anonymous data might be re-identified to re-identify individuals.  _Based on the combination of insignificant data, we can achieve significance_.  For example, in our extension we anticipate **visualizing their site data across different websites to show the sum total.**

The fourth game concept, "Nothing to hide", lets the game players experience that the "nothing to hide" argument is wrong. If anyone can find more information about this game concept then let us know, because I want to know specifically what they did.

The fifth game concept, "Smart City", is a simulation game targeting political decision makers who are responsible for urban development decisions. At the end of his or her legislative term, the player (who takes the perspective of a city mayor making political decisions) will be measured pursuant to the future scenarios simulated in the game.

The sixth game concept, "Pieces of Data", seeks to teach its players how to _manage third-party access rights_, i.e. by app providers, to their smartphones. "Taking the perspective of an activist in a state that is becoming more and more repressive, the players learn how data collected by their smartphones can harm them, and even other parties - and how to protect themselves against such threats.". Apparently this game won! We could make a similar game, which would be hilarious!



### Our goal

According to the Kaggle survey of 2017,

![Branching](https://raw.githubusercontent.com/Elamraoui-Sohayb/Ethical_Scrapper/master/Ethical_Data_Collection/img/Screenshot0.png)

data availability and quality remains among the top barriers for professionals in the field.  We want to make the ethics of data collection more accessible to the end user.
