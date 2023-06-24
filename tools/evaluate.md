# Evaluate
#### This is a Python project for automated evaluation of courses. It utilizes the Selenium library to simulate browser actions and assists users in automatically completing online course evaluations.

## Dependencies
* Python 3.x
* Microsoft Edge browser
* library of requirements.txt


## Usage Instructions
1. Ensure that you have correctly configured the config.py file before running the program.

2. Execute the run method of the EvaluatingSystem class.

3. The program will automatically log in to the evaluation system and navigate to the evaluation catalog page.

4. Choose the desired catalog and sub-catalog for evaluation. The program will display the table for the selected catalog and prompt you for input.

5. Upon entering a sub-catalog, the program will display the corresponding table and list the courses available for evaluation. It will evaluate each course in sequence.

6. For each course, the program will prompt you to enter a score. Follow the instructions and enter an appropriate score (an integer between 1 and 5).

7. Once the score is entered, the program will automatically submit the evaluation and return to the sub-catalog page.

8. After completing the evaluation for a sub-catalog, the program will return to the evaluation catalog page and proceed to the next sub-catalog until all sub-catalogs are evaluated.

9. Once all evaluations are completed, the program will exit.

#### Please note that after completing the evaluations, it is necessary to manually check the webpage and click the "Agree" button to ensure the evaluations are submitted correctly.

## Disclaimer
* The scores entered by this program are user-specified and unrelated to the program itself.
* Users are solely responsible for the results and consequences of using this program. The developer disclaims all responsibilities.
* During the usage of this program, please ensure the safety and stability of your equipment and network connection to avoid unnecessary errors.
* This program does not modify any files within the user's computer system.

## Reporting Issues
#### If you encounter any problems or require technical support, please contact us:

* Email: lvlvko233@qq.com 
* GitHub: github.com/hcd233