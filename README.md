The puzzle of guessing two number
======

This is the question in an interview

Story
------
* Two integers N and  M are between [2, 99]
* There are two smart persons A and B
* A knows the product of two numbers (N*M)
* B knows the sum of two numbers (N+M)
* A ask B: Can you guess out of the two numbers?
* B looks the sum and answer: I don't know, and you?
* A looks the product and say: I don't know either.
* B then say: if you don't know, I know.
* A follows immediatly: if you know then I know.

Question
-----
1. Do they really know the two numbers? 
2. Do you know the two number? what are they?
3. Why?

Answer
-----
1. Yes!
2. No, but (3,4) is one possible solution.
3. A and B are SMART, I'm not foolish also.

Refers
-----
- nm.py -- python program
- nm.c  -- c program (created on last century)

Note
-----
* python mn.py [range] [trace] [debug]
* default range is 99
* verify each solution youself
* try giving different range and get more understanding  

Update
-----
Same condition but ask order changes
1. B ask A, A don't know
2. A ask B, B don't know
3. then A know
4. B follows know also
5. What are the two number?

- guessnum.py -- python program (full solutions)
- python guessnum.py [range]

History story
- SunBin and PangJiuan guessing number

神仙鬼谷子为了考验他的两个高徒孙膑和庞涓，精心挑选了两个大于1、小于100的整数，将两数之积告诉孙膑，两数之和告诉庞涓，要他们猜出这两个整数。这就是著名的孙膑猜数问题。出题后，两位高徒琢磨一番。庞涓对孙膑说：“虽然我能肯定你不知道这两个数，但我也不知道。”于是孙膑说“我现在知道了。”庞涓也跟着说：“我也知道了
