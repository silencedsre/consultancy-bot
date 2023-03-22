The bot should be able to answer the following queries.

### Offer Letter:

#### Q)What are the document required for offer letter ?

A) Below are the docs required to apply offer letter <br>
    1. All academics certificate <br>
    2. Resume <br>
    3. Passport <br>
    4. Work experience <br>
    5. IELTS <br>
    6. SOP <br>

### IELTS Score:

#### Q) How much IELTS score is required to apply for Bachelor for USA ? 

A) GPA 2.60 and above and IELTS 6.0 not less 5.5

#### Q) What is the IELTS score required to apply for Masters for Australia ?
A) GPA 2.65 and above and IELTS 6.5 not less than 6

Same score applies to USA, Australia and Canada please put country & academic level variable.

#### Q) how much is the IELTS score required for Australia ?
Ask “which Level do you want to study” ? once the user provide answer eg. Bachelor then you show the above answer.

#### Q) Can I apply Canada without IELTS ?
A) Yes, in some university you can apply without IELTS but it depends on university. In most of the university IELTS is compulsory.

### Working right:

#### Q) How much time can I work as a student  (Bachelor or Master )
A) You are allowed to work 20 hours a week

Here academic level & Country need to be variable. 

It should answers if someone ask “ how many hours masters student can work in USA or Australia or Canada”
How many hours can I work in Canada ?  

chatbot should ask which level he/she is going to study ? and then only it has to show 2o hours work right. As the work right may be different in bachelor and masters.

### Scholarship:

#### Q) Can I get scholarship and how much?  
Country need to be variable questions may come for Canada or Australia or US
#### Q) Can you help me finding scholarship in USA university.

A) Yes, depending upon GPA and IELTS Score you have. We will request universities on your behalf  to provide best scholarship possible.

Then bot should ask for lead ( his name & number )

### Cost to apply:

#### Q) What is the total cost needed to apply visa ? <br>
#### Q) how much does the cost involved to apply Masters in IT in USA?”

#### Q) How much do I need to have to study MBA in Australia? “

A) It depends on the state and universities you chose .
Here, student may ask for bachelor or master’s program and any country. Chatbot should answer those question.


### Visa Processing Time:

#### Q) how long does it take to get the visa for Australia or USA or Canada (country variable)
A) It depends on university and documents you have provided but in general we are getting visa in 35 days.

### Additional Features:
- Form Validations
- Add buttons in forms to guide the users
- Handling of interruption `bot_challenge` in country/academics form 

### Future Enhancements
- Name and number is handled only with few examples (need to add more examples)
- Save lead name and number in database

### Run
- `rasa shell & rasa run actions`