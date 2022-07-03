# BMD303-Final-Project
1-We need to install mongo database in order to use it in our systems, so we need to install the packages first,

	-pip install pymongo["srv"]

	-pip install pymongo

2-The first step is to go to the project file (the one that have templates and patient data
files in it) and then open "CMD" from that folder, and write the following line:

py manage.py runserver, if there was an error from the line, then write 

py manage.py makemigrations and then py manage.py migrate and then write py manage.py runserver

3-This shall open the system and in order to open the other system we do the same steps 
but, first we close the opened system by ("Ctrl + C ")

4-If the first system is opened then you would see that you can register and of the system actors
(Doctor, patient, receptionist, and HR)and each one have it is own functions.

5-The receptionist can create appointment which can be seen at the doctor and patient view
and the doctor can create perscriptions which patient can view it and hr can view how many doctor 
and patient we have, and their personal information (Age, male) and can update it if needeed)

6-then as shown in the discussion how to put in the database from the patients sections from the receptionist or
doctor view, but in order to see the database is confidential as it is secured by my gmail
and password, so for any help just email me and i will do whatever is needed and i can send 
screenshots if you want to check if the data is added or not.

7-After adding data from the first system we logout from it, then we go the second system by the same steps and 
open it, then we have sections like home which is still supposed to show the x-ray of all the patietns in a sequential way
for the doctor for view, and then the patient sections

8-patient sections we can add data from it by first search by ID we inserted it and then
find what kine of x-ray needed and then go back and type that ID and add picture
(The picture need to be in a certain path which is (storeapp --> static --> images and then
we can put the picture in this file and then we can upload it from the website) amd it 
will generate verification message that it has been added.

9-After uplading it we can check that it was added by type the same id and it will generate
patient with the x ray, also if i added ray to id that is not exist it will send an invalid
message that the id is not exist, and if i put id without adding x ray it will send an
error page as no uploaded file, also if i clicked on add without putting id and x ray it will 
generate invalid id message.


10-So the data is ready we can go to the first system and we can register as doctor or receptionist
and search by the id and it will show the patient with the needed X-RAY
