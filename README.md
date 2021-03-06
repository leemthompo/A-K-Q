# The Ace-King-Queen Game

A toy model poker game written in Python

## Game Overview

<p>According to <em>The Mathematics of Poker</em> (Chen and Ankenman 2006), the AKQ game <em>"represents perhaps the simplest form of symmetrical, non-trivial poker."</em></p>

<p>The game as presented is the half-street limit case for this game. This means you can check or bet, but your opponent can only call or fold.</p>

<p>This is an <strong>incomplete information</strong> game. This is the simplest toy game that resembles real poker and introduces the concept of ranges. <a href="https://ocw.mit.edu/courses/sloan-school-of-management/15-s50-poker-theory-and-analytics-january-iap-2015/lecture-videos/decision-making/">Matt Hawrilenko</a> recommends playing this game for money, citing the important difference between solving a game mathematically and understanding it experientially.</p>

<p>The key concept behind this is knowing <strong>how to bluff</strong> (with Queens) and <strong>how to call</strong> (with Kings) in the <strong>game theoretically optimal ratios</strong> — for blind and button play respectively.</p>

<p>The idea behind this Python implementation is to turn this toy game into a training tool for beginners.</p>

<p>The concept of <strong><em>card removal</em></strong> is crucial in the AKQ game. For example, if you have the Queen, you know your opponent either has the King or the Ace. Half the time he has one, half the time he has the other.</p>

<h2>Rules</h2>

<p>The rules of the game are</p>

<ul>
<li>Three-card deck: <strong>Ace, King and Queen (A, K , Q)</strong></li>
<li>Players are dealt <strong>one card</strong> each, without replacement, and there is an initial ante</li>
<li>There is one round of betting, after which there is a showdown (if neither player folds). High card wins at showdown.</li>
<li>The <strong>blind</strong> can <strong><em>only</em></strong> check or bet</li>
<li>The <strong>button</strong> can <strong><em>only</em></strong> call or fold</li>
<li>If play goes to showdown, the high card wins</li>
</ul>

### Work in progress

The first commit is a first draft, half-logic script where the player is always on the button.

### Demo



https://user-images.githubusercontent.com/32779855/125199624-59246b80-e267-11eb-98ca-73008bbf2fde.mov

