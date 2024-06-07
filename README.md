# Daycare Daily Report
#### Video Demo:  https://www.youtube.com/watch?v=NrmyKmnh3q

## Table of Contents
- [Description](#description)
- [Features](#features)
- [How to install](#how-to-install)
- [Usage](#usage)
- [Technologies](#technologies)

## Description
This application simplifies the task of tracking and recording infants' activities for daycare teachers responsible for caring for multiple babies. As a busy parent myself, I understand the importance of efficiently record my baby's routine. This application streamlines the process, allowing users to effortlessly log each baby's activities throughout the day and generate a concise daily report summarizing the recorded activities.

## Features
- **User-Friendly Interface:** Easily record multiple activities for each baby in one session.
- **Cumulative Total Calculation:** Automatically calculate a cumulative total for each activity recorded during the current day.
- **Comprehensive Daily Report:** Generates a daily report for each baby, providing details of their activities for the day.
- **Easy Access to Records:** Store daycare records in a CSV file for easy access and data persistence.

## How to install
1. Make sure you have [python](https://www.python.org/downloads/) installed on your computer.
1. `git clone https://github.com/sundaygo425/DayCareDailyReport.git`
1. `cd` into the DayCareDailyReport repository.
1. `python project.py` and follow the instructions.

## Usage
1. Input Kid's Information:
    - Follow the prompts to enter the name of the baby and the name of the classroom (Pear/Avocado/Peach) they belong to.
    ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic1.jpg)
1. Recording Activities:
    - Enter "Yes" to record activities or "No" to finish recording for the day.
      If you choose to record activities, you can select one of the activities(Milk/Diaper/Nap) to record:
      ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic2.jpg)
    - **Milk:** Enter the amount of milk the baby drank in ml.
      ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic4.jpg)
    - **Diaper:** Each diaper change will be recorded.
      ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic7.jpg)
    - **Nap:** Nap will be recorded.
      ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic8.jpg)
1. Exit Recording:
    - After recording activities, you'll have the option to record more activities. Or you can enter "No" to finish recording for the day.
  ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic5.jpg)
1. Generate a Daily Report:
    - Once finished, it will generate a daily report for the baby.
  ![image](https://github.com/sundaygo425/img-folder/blob/main/readme-pic6.jpg)
1. Asscess to Data:
    - All recorded activities are stored in a CSV file named "Daycare.csv". You can access this file to view past records.

## Technologies
- Python: The programming language used for developing the application.
- CSV Module: Utilized to handle data storage and retrieval in CSV files.
- Tabulate Library: Used for formatting data into easy-to-read tabular form.
- Time Module: Used for obtaining the current date.

## Future Improvments
This application has not been completed yet! I would like to do the following improvements:
- Add functionality to allow teachers to update or delete existing records to maintain accurate information.
- Include more activities, such as playtime and learning activities(for toddlers).
- Improve error handling and data validation to prevent incorrect data entry.
- Add user authentication to improve the data privacy.
- Add user-friendly interface.

## Contributing
Contributions to the Daycare Daily Report are welcome and appreciated! If you found any bug or would like to summit an improvement for this application, please feel free to fork the repository and submit a pull request with your changes. Your contrbution is valuable and may help improve the application.

## Contact Information
If you have any questions, feel free to contact the application maintainer at [haojinads@gmail.com].

## License
This project is licensed under the MIT License.










