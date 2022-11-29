import turtle
from utils import alert

ts = turtle.getscreen()

# Load the images
named_img = ts.bgpic("assets/named.gif")
unnamed_img = ts.bgpic("assets/unnamed.gif")

# Cities and their coordinates
cities = {
    "Istanbul": (-100, -100),
    "Ankara": (100, 100),
    "Izmir": (-100, -100),
    # "Bursa": (40.1828, 29.0610),
    # "Antalya": (36.9081, 30.6956),
    # "Adana": (37.0000, 35.3213),
    # "Gaziantep": (37.0594, 37.3828),
    # "Konya": (37.8719, 32.4848),
    # "Kayseri": (38.7312, 35.4783),
    # "Mersin": (36.8000, 34.6333),
}

# Create the screen and set the mode to "logo"
wn = turtle.Screen()
wn.mode("logo")
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Hide the default turtle
turtle.hideturtle()

# Load the images
named_img = ts.bgpic("assets/named.gif")
unnamed_img = ts.bgpic("assets/unnamed.gif")
total_wrong_counter = 0
total_guess = 0

# Create the screen and set the mode to "logo"
wn = turtle.Screen()
wn.mode("logo")

# Hide the default turtle
turtle.hideturtle()

# Set the reference image
wn.bgpic(named_img)
turtle.ontimer(lambda: wn.bgpic(unnamed_img), 3000)

# Create a turtle to draw on the screen
t = turtle.Turtle()

# Move the turtle to the correct position
t.setpos(cities["Istanbul"])

# Draw the image on the screen
t.stamp()

# Set the guessing image
wn.bgpic(unnamed_img)

# Ask for the province name
# province_name = turtle.textinput("Please enter the city name", "City name:")

# check all the cities and their coordinates


def iterate_prv_nxt(my_list):
    prv, cur, nxt = None, iter(my_list), iter(my_list)
    next(nxt, None)

    while True:
        try:
            if prv:
                yield next(prv), next(cur), next(nxt, None)
            else:
                yield None, next(cur), next(nxt, None)
                prv = iter(my_list)
        except StopIteration:
            break


for prv, city_curr, city_next in iterate_prv_nxt(cities):
    # if the province name is in the cities
    print(city_curr)

    while True:
        total_guess += 1
        province_name = turtle.textinput("Please enter the city name", "City name:")

        if province_name != city_curr:
            alert.show_alert("error", "Error", "You did not find the city")
            total_wrong_counter += 1
            wn.title(
                "Python Challenge with Turtle Graphics - Wrong Guesses: "
                + str(total_wrong_counter)
                + " - Total Guesses: "
                + str(total_guess)
            )

        else:
            # get the coordinates of the province
            x, y = cities[province_name]
            # move the turtle to the coordinates
            t.setpos(x, y)
            # draw the image on the screen
            t.stamp()
            # show the alert
            alert.show_alert(
                "info",
                "Congratulations🎉",
                "Congratulations🎉 You found the {city}!".format(city=city_curr),
            )
            turtle.write(
                province_name,
                font=("Arial", 16, "normal"),
                align="right",
                move=False,
            )
            wn.title(
                "Python Challenge with Turtle Graphics - Wrong Guesses: "
                + str(total_wrong_counter)
                + " - Total Guesses: "
                + str(total_guess)
            )

            break
    # set the next
    if city_next == None:
        break
    else:
        x, y = cities[city_next]
        # move the turtle to the coordinates
        t.setpos(x, y)
        # draw the image on the screen
        t.stamp()

print("Thanks for playing!")


#! Need refactoring and optimization
if total_wrong_counter == 0:
    alert.show_alert(
        "info",
        "Congratulations🎉",
        "Congratulations🎉 You found all the cities!",
    )
elif total_wrong_counter == 1:
    alert.show_alert(
        "info",
        "Congratulations🎉",
        "Congratulations🎉 You found all the cities with 1 wrong guess!",
    )
elif total_wrong_counter > 1:
    alert.show_alert(
        "info",
        "Congratulations🎉",
        "Congratulations🎉 You found all the cities with "
        + str(total_wrong_counter)
        + " wrong guesses!",
    )
elif total_wrong_counter > 5:
    alert.show_alert(
        "warning",
        "Congratulations⚠️",
        "Congratulations⚠️ You found all the cities with "
        + str(total_wrong_counter)
        + " wrong guesses! You can do better!",
    )
elif total_wrong_counter > 10:
    alert.show_alert(
        "warning",
        "Congratulations❌",
        "Congratulations❌ You found all the cities with "
        + str(total_wrong_counter)
        + " wrong guesses! You can do better! Try again!",
    )


# Wait for the user to press a key
wn.exitonclick()

alert.show_alert("warning", "Bye Bye", "Bye Bye")

# Close the window
turtle.Screen().bye()
