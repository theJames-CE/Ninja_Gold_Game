<h1>Assignment: Ninja Gold</h1><br>

<b>Welcome to another Core assignment!</b> Some students like to explore the assignments before they're finished reading through the lessons, and that's okay! It can be good for your brain to have a preview of what your future challenges might be. However, before you begin this assignment, it's important that you've first:

<li>Completed the preceding lesson modules</li><br>

<li>Taken the knowledge checks to confirm your understanding</li><br>

<li>Viewed lecture material related to the assignment topics</li><br>

<li>Completed and submitted your practice assignments</li><br>

<h2>Now, the Assignment:</h2><br>

Create a simple game to test your understanding of Flask, and implement the functionality below.<br>

For this assignment, you're going to create a mini game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or lose up to 50 gold. Your job is to create a web app that allows this ninja to earn gold and to display their past activities.<br>

The root route should display the wireframe below. There should be 4 forms on the HTML page. As an example, the farm form might look something like this:<br>

![image](https://github.com/theJames-CE/Ninja_Gold_Game/assets/124546382/9259eebe-823c-4f17-b6aa-ba5abf931781)<br>

There should be a method that handles the POST request, determining how much gold the user should now have depending on their visit.

Note: You should only have <b>2 routes</b> for this assignment -- '/' and '/process_money'<br>

![image](https://github.com/theJames-CE/Ninja_Gold_Game/assets/124546382/527e48c1-b35c-45a9-9693-59f7d4903cc9)<br>

<h2>Watch this before you start the assignment</h2><br>

![image](https://github.com/theJames-CE/Ninja_Gold_Game/assets/124546382/a9d8c568-7643-4bcd-a5df-e89619150d82)<br>

<h3>A Helpful Tip</h3><br>

Consider the following code:

<h3>my_proj/server.py</h3><br>

![image](https://github.com/theJames-CE/Ninja_Gold_Game/assets/124546382/176dd564-de27-4450-872b-42e4c35da45b)<br>

<h3>my_proj/templates/index.html</h3><br>

![image](https://github.com/theJames-CE/Ninja_Gold_Game/assets/124546382/98bfbd7c-b71e-4339-b132-653ccf963b11)<br>

By default, Jinja will convert any <ins>html entities with character entities</ins>. To prevent this from happening, we used the <b>safe</b> pipe, which you can read about <ins>in the Flask documentation</ins> and <ins>on StackOverflow</ins>.<br>

![image](https://github.com/theJames-CE/Ninja_Gold_Game/assets/124546382/718f819e-8076-47d1-a0c3-5bf55503e9f0)

#CodingDojo





