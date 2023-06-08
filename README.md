# Puzzle_project_python

According to the video example, I divided my whole game program into three parts for main design. 
I mainly complete the first part in the puzzle_game.py file. 
The first part includes: Establishing the most basic partitions. Insert fixed pictures. 
When certain conditions are met, insert the correct hint picture on the screen. 
And set buttons and corresponding reaction functions, which is a little more difficult. 
The second part includes: to read the puz file. 
Then, build various dictionaries and lists to help me ensure that I can get the parameters and numbers I need at any time easily. 
This part is achieved by creating a class named information through information.py. 
I use this class as a medium to extract information, not as a tool. 
That's why I didn't store more functions with actual actions besides inserting the puzzle. 
In the third part, I perfected some details. 
For example, if players do not want to leave their names, they do not need to participate in leaderboard records. 
Also, I set up a leaderboard and error txt file to store the winner's name and score and the errors that occurred during the entire program operation. 
My idea is to write the winner's information into an txt file first, and then display it on the screen by reading the txt file.
