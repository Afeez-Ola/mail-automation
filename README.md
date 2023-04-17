

|**Project Readme: Mail Automation** |
| - |
|**Overview** |
|This project generates personalized invitation letters for a given list of invitees. The |
|invitees' names are read from a text file, and a template letter is used to generate a |
|personalized invitation letter for each invitee. The generated letters are saved in |
|individual text files named after the respective invitee. |
|**Usage** |
|**Input Files** |
|The program expects the following input files: |


- **invited\_names.txt:** This file contains the list of invitees, with each name on a ![](Aspose.Words.55eba84a-ff86-4f93-98fe-614b29ba6199.001.png)separate line. 
- **example.txt:** This file contains the template letter, with placeholders for the inviter's name and the invitee's name. 



|The paths to these files are defined in the variables |**invited\_names\_path**|` `and |
| - | - | - |
|**letter\_path**|` `respectively, and can be modified to match the location of the input files. |
|||
|**Output Files** |
|The generated invitation letters are saved in the |**Output/ReadyToSend**|**/** directory in |
|individual text files named after the respective invitee. |
|The output directory path is defined in the variable |**output\_directory**|, and can be |
|modified to save the generated letters to a different directory. |
|**Execution** |
|To execute the program, run the script |**invitation\_letter\_generator.py**|. The script |
|reads the input files, generates the personalized invitation letters, and saves them in |
|the output directory. |
|**Implementation Details** |
|The program reads the list of invitees from |**invited\_names.txt**|, and reads the template |
|letter from |**example.txt**|. The program replaces the placeholders in the template letter |
with the inviter's name and the invitee's name to generate personalized letters. The personalized letters are then saved in individual text files named after the respective invitee in the output directory. ![](Aspose.Words.55eba84a-ff86-4f93-98fe-614b29ba6199.002.png)

The program uses the following variables to configure its behavior: 

- **invited\_names\_path**: The path to the file containing the list of invitees. ![](Aspose.Words.55eba84a-ff86-4f93-98fe-614b29ba6199.003.png)
- **letter\_path**: The path to the file containing the template letter. 
- **output\_directory**: The path to the directory where the generated letters should be saved. 
- **inviter**: The name of the inviter, used to replace the inviter's name placeholder in the template letter. 

**Dependencies ![](Aspose.Words.55eba84a-ff86-4f93-98fe-614b29ba6199.004.png)**

This project was implemented in Python 3. No external libraries are required to run this program. 
