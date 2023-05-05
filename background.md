# Background

My grandpa liked to make his own crossword puzzles.  He would write them out by hand, make up his own clues (sometimes with our family as the clue answer!) and make photocopies for us solve. He loved building puzzles and we loved solving them.

I'm not sure how he first became interested in diagramless crossord puzzles, but it must have been during this time. He wondered if it were possible to determine the crossword's grid based just on the crossword accross and down clue numbers? Without solving any clues, can you figure out all of the word's lenghts', and locations of all of the black cells and clues? Was there more than one possible solution for a given set of clues?

He had some experience programming in Visual Basic, but his approach was never programming based. He never got far enough in this project to get it solved.

A few years later, as I took a Python programming class, I knew I wanted to tackle this same problem. I explored nested lists and and made an empty crossword grid. I figured out how to place values in this 'grid' and how to check values. I tried to learn the hiddle rules and conventions of crossword puzzles. I created a massive if/then block of 'square logic' to check valid crossword squares and created a loop to run through it. I made a copy of the puzzle if there were two options and checked both copies.

And it worked. Mostly...

I expanded. Added on starting squares, symmetry, and created a basic API that pulled existing crossword puzzle data from an online repository. I made an adjustable puzzle library and cleaned up the code as best I could.

But it was my first major project so it had serious issues. The code was not oragnized well at all, it used very inefficient data structures, and showed a lack of understanding of some core Python / programming fundamentals. Additionally, my 'square logic' ran into edge cases that broke the system, and it was constantly running into issues or just running for hours without a solution.

I've been through a few iterations at this point over the years. I've made improvements to the structure and made major changes to the algorithm. I've tried a brute force approach. Tried treating it as a contstraint satisfaction problem. I've refactored and refactored and refactored and I know it needs more still.

However I've gotten it to the point where I absolutely can answer those quesitons my Grandpa had. Yes, it's possible. Sometimes there's only one solution, and sometimes there are hundreds or even tens of thousands of solutions.

I've build other projects, and started to understand progamming much better, however this one has always been my biggest programming accomplishment. Although I'm no expert, I believe I'm at a great spot to continue learning and growing.