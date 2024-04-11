![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/1d894c6c-5005-49e6-b913-0ad212eaf853)
![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/0978bd05-0ebc-4808-a0a9-9c6bf2f5ab41)


# Persa_Bot Your guide in the journey of getting your dream tattoo by Persa Tattoo studio :)
**Domain**
***
Persa_Bot is an appointment booking- and inspiration giving- chatbot for the Tattoo artist-industry .We ideally what to integrate this functionality in our Instagram account chat, since this is our main source for lead generation.
***

**Problem Statement**

*We know the struggle of getting a unique tattoo!*
<p>Most of our beloved customers come to us with tattoo designs taken from images from Google or Pinterest or they ask for variables or even duplicates from our designs on Instagram. 
**We want to take customer experience to the next level**  by harnessing the benefits of **AI** and especially the perks of automated image generation.  
Inspired by platforms like [Blackink.ai](https://blackink.ai/) and [Tattosai](https://www.tattoosai.com/) we think that linking our chatbot with a platform that generates unique tattoos is an ideal asset not only for customer satisfaction, but also for the continuous enrichment of the artist's booklet. Because in art there are no limits! </p>

*And what about appointment booking?*
<p>Scheduling a tattoo apointment vs schedulling a routine doctor's appointment are far from similar!
In order to find the right slot for a tattoo apointment, following things are considered :
   1) size in cm (e.g. imagine the duration for a full arm tattoo) 
   2)complexity (e.g. if it is a portrait tattoo, or 3D or if it contains colour)

   After taking these parameters into consideration, the artist can estimate the appointment duration and find an available slot in their program. For a customer that knows the design and the spot to be done, getting an appointment is the last step, so this is the target audience for the appointment-scheduling functionaliyty of the Persa_Bot. For customers that have partially made their decision, (i.e. they know the design, but they don't know the spot, or they know the spot but they don't know the design, or they don't know either), here are the two alternatives : 
   1) Book a consulting appointment with the artist (this one should have a max. standard duration) or
   2) Search in the tattoo generator platform for inspiration. </p>

*Price estimation*
<p> A common intent of our customers is that they have a tattoo in mind and they reach out to us about the costing. Again the price estimation is strongly correlated with its size, its complexity and accordingly the time spent for it.
So having a bot give an approximate price reply is saving Persa a lot of time in standard chat interactions. Also the price estimation function saves Persa from negotiating with customers not belonigng to her target group of customers. </p>

***
Persa is a reknown solo artist in Thessaloniki with high-demand. She has customers coming all over Europe to visit her for her artwork! 
So outsourcing the process of booking appointments tailored on her agenda  via the use of a chatbot, will help her focus on what she does the best.
***

**Main functionalities (so far)**
1) Find tattoo --> current implementation: Redirect to our Instagram page
2) Book_appointment (fully_aware (ideal)-user) --> current implementation: Choose one of the available dates and times from a list (action: get_available_timeslots). No consideration of appointment duration.
3) Price estimation --> current implementation: Give the user an approximate hourly estimate price chart and let them understand about the price of the tattoo. Also recommend getting a consulting appointment to get an accurate price estimate by the artist.
   
**Objectives**
We know how important it is for the artist to build trust with each customer. 
So we don't want ot automate the whole appointment booking process. Only the parts that are really redundant and can actually be done via an bot exaclty like they would have been done by a human secretary.
Ideal functionalities: 
1. Tattoo-generation: Connect the chatbot with a platform like : https://blackink.ai/. This site requires the user to create an account, but we would like the user of the chat to have direct access to the pltforms interface to be able to generate their tattoo straightaway.
2. Book tattoo appointment: Based on the tattoo design, give the customer an appointment duration estimate, and then provide available timeslots starting from current week based on Persa's Google calendar.
3. Book consulting appointment: For customers that need the artists's advice on the design and the body spot --> appointment with a fixed max duration (e.g. 30 minutes).
4. Price estimation: FAQ page redirection in which the hourly estimate price chart along with other procedural info are provided.
5. Geolocation: Customer asks studio's location: Bot responds with a pin to Google maps from the user's current location to the studio
   
**Current issues** 

![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/fe2bf29e-34a5-4dc7-b49c-f37991004d15)
