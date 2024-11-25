% Facts: Fruits and their corresponding colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(kiwi, green).
fruit_color(strawberry, red).

% Query: Given a fruit, find its color
find_color(Fruit, Color) :-
    fruit_color(Fruit, Color).
