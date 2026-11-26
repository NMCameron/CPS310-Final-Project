# Feature Selection
## Recipe Management: Favorite Recipes
## Meal Planning: Randomly selected meal
## Grocery/Calculations: Generate a grocery list
### Why?
Most of these choices were made based off personal reasons. If I were using an app like this I would like to be able to favorite recipes, and have random recipes suggested for me. Then I would find it helpful to have a recipe list generated for the recipes I want to try.

# Current Progress
## What two features have been meaningfully implemented so far?
I have implemented the ability to favorite recipes, and randomly select one from a list.

# Most Difficult Feature
## Which has been the most difficult so far?
While not extremely difficult, I found implementing the favorite recipes feature to be the most difficult, as my approach was to change the category to a list instead of a string for the meals. This way I could add the "favorite" category to the meals, and just return anything matching "favorite." In doing this, I had to go back and fix any tests I broke by changing the string to a list.

# GitHub Issues
## How have the issues helped you organize the project?
I created two issues so far, both for each new feature I wanted to add. This has helped me keep development organized and centered around these new branches. This allows me to ensure I have everything the way I like it before I pull to main.

# Branch/Pull Request
## Identify one branch or pull request that best represents your development process so far.
feature/favorite-recipes best represents my process so far. This work is best outside of main as I was changing functionality and the way objects were stored, so isolating this to a branch instead of working on main felt right.

# Meaningful Commit
## Identify one commit you consider meaningful
If we were to break it down to just one, `456cfdc` I think was the most meaningful. This represents my development process as a whole, pushing small chunks at a time, where I implemented the functionality, then the tests. Then pull once it all works together.

# Testing
## What tests have you added for your features?
All of my features come with at least three tests. Working with invalid selections, how they return when  what it calls is not found, and what is returned. These cover the core functionality of each implementation.

# Bug or Mistake
## Describe one bug, mistake, or unexpected behavior you encountered.
Initially when I implemented favorite recipe functionality, I didnt realize category was stored as a string. So when my function was not behaving as expected I had to do some looking around and found that was my issue.

# Current Code Quality
## Identify one part of your current code that you would improve if you had more time before this checkpoint.
I would like to flesh out the favorite meals functionality a bit more, to make it so favorites can be removed, and are stored between sessions.

# Remaining Plan
## What do you plan to work on next?
The last thing I really have to implement is to return a grocery list for selected recipes. I dont anticipate this to be too difficult as the ingredient list is already stored with each recipe.