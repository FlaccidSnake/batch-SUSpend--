### Batch-Suspend

Anki add-on to suspend a batch of cards based on custom rules targeted at the tag level.

I have a workflow where I write the questions for my notes first. Since there may be more than one card per note, I prefer the note view in the browser. I can't tell if a note has suspended cards in this view. I've been using the mark function to distinguish notes I need to get back to in a tag group, since they turn purple in note view in the browser: this doesn't suspend the notes though. With this addon I can mindlessly suspend any marked notes at the end of the day without writing a whole search, pressing Ctrl + A and Ctrl + J, and hope that I didn't just unsuspend all previously suspended cards.

Also maybe there's a use case for mass suspending other tags I dunno, my case is very specific.

#### Installation

Copy the  `batch-SUSpend-ඞ`  directory to your  `addons21`  folder.

#### Screenshots

![image](https://github.com/FlaccidSnake/batch-SUSpend--/assets/67238552/816389be-5697-45c1-95d3-ef9c8e996873)
![image](https://github.com/FlaccidSnake/batch-SUSpend--/assets/67238552/9bfd3eca-64d8-4094-91d2-620a44f83bbf)
![image](https://github.com/FlaccidSnake/batch-SUSpend--/assets/67238552/3b96349e-7dbd-4868-8b0f-9b31f34bc0fe)


#### Use

Open the menu by going to `Tools>Batch-SUSpend ඞ` Options in the Anki menu bar. Click 'Add rule' to create a rule for targeting which card tag will be suspended and how many cards to suspend at a time. Note, the cards are suspended from the tag group in the order of their creation date.

Rules can be toggled on or off using their checkbox. Rules can be deleted or edited from their respective options menu.

When 'Suspend' is clicked all of the the selected rules will be executed, and the cards will be suspended.

Currently tested and working on  `macOS Qt5.14 Anki 2.1.64` and Windows `Qt6.4.3 Anki 2.1.64`

* Please make sure to back up all of your decks before using. I have literally cobbled this together using vague programming familiarity, Ctrl + F, ChatGPT 3.5, and someone else's code.
