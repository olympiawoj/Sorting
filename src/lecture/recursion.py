# Print every num starting at num until you reach 0
# Our base case is 0


def recurse(number):
    # Need a base case
    if number < 0:
        return
    print(number)
    number -= 1
    recurse(number)
    recurse(number)


# First line that gets called - first executable piece of code
recurse(4)
# then if, then print, then decrement, then call recurse(4) and keep doing it until base case is met

'''
1-1
2-3 
3-7
4-15


2^n - 1

'''

# Return then Nth Fibonacci number
# If n is 5, 5th number is 3
# To calc fibinocci number, add the two previous nums. To do this, we have to find the 3rd and 4rd. We find 3rd by finding 2nd and 3rd. We find 2nd by finding 2nd and 1st.
# One thing that tells you recurion is a great way to solve a problem is if each prob is a subset of the same prob


def fibonoccai(n):
    # base case
    if n < 0:
        print("Negative numbers are not valid")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Return (n - 1) + (n - 2)
        # We have a function that does
        return fibonoccai(n-1) + fibonoccai(n-2)


# Call the function
print('fib6', fibonoccai(6))  # 8
print('fib30', fibonoccai(30))  # 832040 - slow took a second

# What is the question? End of the universe.
print('fib38', fibonoccai(38))
"""
How long will this operation take? Prob take until the end of the universe. At v least, we'll all be long gone before this is finished calculating. WHY? Let's figure out the breaking point is quickly and efficiently

What technique can we use to find that? It works on 30, breaks on 40
What algorithmic technique can we 


Do 40
Then 35
Then 37
Then 38 

This is an intersection where big O and time complexity meet up with real world time. Bc with exponential, there's a magic spot where it works up to a round 34-40x depending on what you're doing bc what we're doing happens almost instantly right.  We're just adding some stuff together, that's it
Imagine if you're taking a process that in itself took half a sec for the computer to calc, then it'll take longer time to operate even though runtime complexity, instead of beig .01 * cajillion it'll be .1 * cajillion, a thousand times longer.


WHY is this happening? 
It's bc how many things that we have to do 2^n, so 2^2 = 4, 2^3 = 9, 2^10=1024

Does this number rung any bells? Big number memory -what is kil? 1 Kb is 1000. So 2^2 1048576 got dramatically bigger, so we added 10 to our number and its 100x bigger. 3^30 = 1073741824 - now we're at such a big number it's hard to see. It's 1 Bn. 


2^40 so big it wont give it ot you in standard notation anu more 1.09 * 10^2
2^50 
2^10) = it gets bad v quickly

https://en.wikipedia.org/wiki/Kibibyte


SO That is why exponential runtime is bad. & later on in a bit we'll use a technique to make this better called DYNAMIC PROGRAMMING!! BUT  the real q is, is this a good solution or a bad solution? it's neither good nor bad - it depends

If I have a lot of tasks to do, I'm realizble conifdent we'll never have a # bigger than 20 for this than this solution might be good.

But I might I'd document what? What would I document if I deicded according to the spec we're never going to have numbers bigger than 20 - pretty good but its also better to start out with a better solutoin and if you have a lot of things in your toolkit we might be able to mitigate the probleme very litte bit helps

Things grow and change wtih success. 


uuid -Universally Unique identifier. Kind of like a deck of cards 

And there's diff sizes of it - you could do bigger. BUT the game has been successfuly and running for a v long time. Guess what is starting to happen? They are starting to have collissions where two items have the same identifier. Guess what that is? BADDDD


SO - did they make the wrong decision? Sholud they have made identifiers twice of big? NO they made the right decision BC there's other factors in play. Transmit this data over the internet. They made decision this is big enough to be efficient and small enough to be efficient to send ohterwise you're doubling your traffifcosts. That's a part of if t as well. 


Theres a more efficient way of doing this - we're doing it tomo of Thurs

"""
