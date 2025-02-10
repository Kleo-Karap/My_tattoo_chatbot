![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/1d894c6c-5005-49e6-b913-0ad212eaf853)
![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/0978bd05-0ebc-4808-a0a9-9c6bf2f5ab41)


# Persa_Bot Your guide in the journey of getting your dream tattoo by Persa Tattoo studio :)
**Domain**
***
Persa_Bot is an appointment booking- and inspiration giving- chatbot for the Tattoo artist-industry.
***

**Problem Statement**
*Appointment booking?*
<p>Scheduling a tattoo apointment vs schedulling a routine doctor's appointment are far from similar!
In order to find the right slot for a tattoo apointment, following things are considered :
   1) size in cm (e.g. imagine the duration for a full arm tattoo) 
   2)complexity (e.g. if it is a portrait tattoo, or 3D or if it contains colour)

   After taking these parameters into consideration, the artist can estimate the appointment duration and find an available slot in their program. For a customer that knows the design and the spot to be done, getting an appointment is the last step, so this is the target audience for the appointment-scheduling functionaliyty of the Persa_Bot. For customers that have partially made their decision, (i.e. they know the design, but they don't know the spot, or they know the spot but they don't know the design, or they don't know either), here are the two alternatives : 
   1) Book a consulting appointment with the artist (this one should have a max. standard duration) or
   2) Search in the tattoo generator platform for inspiration. </p>



***
Persa is a reknown solo artist in Thessaloniki with high-demand. She has customers coming all over Europe to visit her for her artwork! 
So outsourcing the process of booking appointments tailored on her agenda  via the use of a chatbot, will help her focus on what she does the best.
***

### Scenario 1
***
Customer wants to find a tattoo idea.
The bot needs to be able to 
1) Redirect to Persa's Instagram page



### Scenario 2
***
Customer wants to book an appointment ((fully_aware (ideal)-user).
The bot needs to be able to 
1) Choose one of the available dates and times from a list (action: get_available_timeslots). No consideration of appointment duration.


   
**Future Objectives**
We know how important it is for the artist to build trust with each customer. 
So we don't want to automate the whole appointment booking process. Only the parts that are really redundant and can actually be done via an bot exaclty like they would have been done by a human secretary.
Ideal functionalities: 
1. Instagram Integration: We ideally what to integrate this chatbot in our Instagram account chat, since this is our main source for lead generation.
2. Tattoo-generation: Connect the chatbot with a platform like : https://blackink.ai/. This site requires the user to create an account, but we would like the user of the chat to have direct access to the pltforms interface to be able to generate their tattoo straightaway.
3. Book tattoo appointment: Based on the tattoo design, give the customer an appointment duration estimate, and then provide available timeslots starting from current week based on Persa's Google calendar.
4. Book consulting appointment: For customers that need the artists's advice on the design and the body spot --> appointment with a fixed max duration (e.g. 30 minutes).
5. Price estimation: FAQ page redirection in which the hourly estimate price chart along with other procedural info are provided.
6. Geolocation: Customer asks studio's location: Bot responds with a pin to Google maps from the user's current location to the studio
   
**Current issues** 

https://github.com/RasaHQ/HandsOn_with_rasa/blob/main/data/rules.yml
Connect Rasa bot with Google calendar : https://www.youtube.com/watch?v=kA3nB9ojZP0&t=368s&ab_channel=Rasa


