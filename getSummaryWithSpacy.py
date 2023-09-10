# Remove stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

inputText = """in front of me are
127 USB devices the theoretical limit
that is supported by a standard PC but
USB has a dark secret as it turns out
the real world limit is actually much
much lower and the only way to find out
what it is for sure is to just start
plugging devices in which oh well I mean
I guess we could just read the white
paper on the architecture of the spec
but
that would be far less interesting for
the people watching on YouTube so
instead
we're just going to start plugging
things in and see what happens what do
you do once you run out of ports I mean
hubs obviously but can we just keep
plugging in Hub after Hub after Hub
until we hit it what is it and what is
the Segway to our sponsor the ridge
looking for a stylish and practical
wallet the ridge wallet has got you
covered its minimalist design allows you
to carry your essential cars and cash
without the bulk so check it out at the
link below and use code Linus to save 10
off your purchase and get free shipping
the first factor that limits how many
USB devices you can connect to your
computer is one you know quite well and
that's the number of ports on the front
and back of your PC but what you might
not know is that most computers only
have a single USB host controller and
all of those ports are going to share
not only that controller but that
controller's bandwidth so when you have
a USB 5 gigabit per second Port it's
five gigabit per second shared with all
the other ports on the controller
now fortunately hitting a bandwidth
limit is pretty uncommon most
peripherals like mice or keyboards use a
negligible amount of bandwidth however
you can run into odd behavior if you
have say for example a video capture
device or a webcam this was really
common with early generation VR headsets
where the VR tracker sucked up so much
bandwidth that users needed to install a
second controller on an add-in card of
course our question today isn't how much
bandwidth can we push through one of
these controllers it's how many devices
can we connect to one so let's move
beyond the limits of our mirror mortal
rear i o ports I summon
The Hub I haven't even plugged the Hub
in yet and I think we're already getting
kind of weird Behavior none of these
whoa
whoa this mouse is crazy hot wait
heatedmouse.com oh it's a feature
all right
people unpowered hub
now a mouse hey there it is Logitech
gaming mouse now another Drive ah but
this is interesting every Hub is
actually two hubs see that we've got a
USB 2 Hub and a USB 3 Hub and depending
on what kind of devices we plug in
they'll show up under either hubs like
this one are an integral part of the
various USB specifications they handle
all the communication between devices
that are plugged into them and the host
systems that they're plugged into as
well as handling bandwidth sharing the
Hub will tell the system hey I'm a hub
and the system adds that hub's address
to the path of any devices that are
plugged in down the chain when multiple
hubs are used multiple addresses are
added to the path so if Hub a for
example is plugged into Port 4 of the
host Hub B is plugged into Port 2 of Hub
a and then a mouse is plugged into Port
1 of Hub B the address might read
something like
0421 or 0 is the address of The
controller's Root Hub
powered or unpowered it doesn't change
the addressing system however according
to the USB spec a hub that is powered
entirely by the port that it's plugged
into like this one cannot allow this
sort of daisy chaining
according to the spec anyway as we are
about to see however that is not the
case here right look at this
but why though
because unpowered hubs are liars
sometimes actually not just sometimes
most of the time and if that shocks you
well it shouldn't consider their
predicament according to the spec only
low power devices so devices that draw
less than 100 milliamps are supposed to
be used on hubs that are powered by the
port itself and not by an external power
brick so if people buy a spec compliant
unpowered Hub they're going to be in for
a rude shock when many of their devices
I mean even mice with too many RGB
lights won't work for some unclear
reason so as a result manufacturers can
either have mostly happy customers and
with an out-of-spec product or they can
have USB implementer Forum certification
well Average Joe customer doesn't care
about usb if certification they might
not even know that they exist whose
Castle is this they just want a hub that
works with their devices and it usually
will however draw too much current and
your USB controller will shut down the
connection from The Source
hopefully before anything gets damaged
should we try that why don't we plug the
heated Mouse into this thing
okay working now but what happens when
we turn our heat to high oh wow this is
still working somehow
I need more power how about this k95
keyboard really
how is this all still working at more
brightness
that was Max brightness
let's plug into a USB 2 port
that'll do it
and
really were you expecting this to work I
mean no not really but
time for another RGB keyboard
two full RGB keyboards and a heated
Mouse do we have any bigger unpowered
hubs no these are the two unpowered hubs
I could find most of our stuff seems to
just be powered and it's plugged into a
USB 2 Port which means that it's pulling
at most two and a half Watts which is
crazy that all that stuff just works
okay
what I suspect is that this motherboard
is just like um
I will deliver more than spec
unbelievable I can't believe they just
allow more power draw so that things
function properly
this will do it heated Mouse RGB
keyboard
and stream deck no it doesn't have the
software is this I want it to light up
full brightness oh wait
hold on USB device not recognized last
USB device you connected has
malfunctioned yes we've overwhelmed it
wow wow what the devil is that she real
unhappy I suspect if we plug this
directly into the back of the PC a
H it would show up just fine
Elgato stream deck XL there it is
everything working perfectly but we take
it back out of here and we plug it into
our unpowered hub
and boom problems
suck says
[ __ ] point is there's a solution to
that
powered USB hubs like this one from
sabrinth that does a whopping
16 devices now something funky about
these is that they are power mandatory
hubs some are power optional remember
that first one that I had over here it
actually has a barrel Jack so it can
operate as a powered Hub this one on the
other hand is like uh-uh no can do
where's my cable
zip zilt NADA but plug in a 90 watt
charger
and hey there we go
all right this is interesting we're
going to talk about this later all the
different hubs that are present here but
first
let's see if we can get our stream deck
and our heated Mouse and our RGB
keyboard running at the same time we
gotta turn on those ports of course
with these I can greatly expand my USB
connectivity all I have to do is daisy
chain my Hubs together
which should give me
pretty much Unlimited hubbery
uh except for one small problem
too many USB hubs a hub will not
function when it's connected more than
five hubs away from the root Port but
this is only three hubs remember when we
noticed that each of these one hubs was
identifying as five hubs in software
sort of
okay USB hub chips can have up to seven
Downstream facing ports or dfps most Hub
chips have only four dfps so a
manufacturer looking to make a big tough
USB bar that doubles as a self-defense
weapon could achieve their desired
number of ports by doing what anyone
else would by chaining them together
this particular model from sabrin has
one main chip with four dfps that each
branch off into four more chips with
four more dfps each that gives us a
total of 16 ports Each of which are two
hubs deep
so if we put three of these together
that's six hubs in a row of course all
of this Hub into Hub tomfoolery was just
an excuse for me to talk about Hub depth
limitations the real way to plug in is
many devices as we can is to plug each
of our hubs into the back of our PC now
we're only two hubs deep on every one of
these ports meaning we can start loading
things up I could use a couple of extra
hands here boys
I'm actually going to turn these off
just so that I can do this
we're not going to be able to use USB
thumb drives forever though Windows gets
kind of fussy about how many Drive
letters a little signs so I'm just going
to do one Hub worth of these
start bringing over mice yeah why don't
we have a mouse Hub a USB thumb drive
hub and a keyboard Hub what do you guys
think sound good
we are up to 30 devices now and
I gotta say
good old USB you know we kind of take it
for granted you know you just use it
every day and don't think about it but
it is shockingly robust are you guys um
what are you guys doing with the
keyboards over there uh we need to plug
some in right now is what we need to do
all right hit me with some cables cable
plug these two in better believe it
we've made it to 48 devices all of which
are showing up correctly and while there
is some weird Behavior Uh I can't click
sometimes for example yep that's uh hold
on maybe a different Mouse we'll click
no
um how about this
no no that doesn't work but uh what
about the Windows key oh uh control
shift Escape hello oh yeah about uh
could bring up task manager so that's
good alt f4 anything buddy shoot
okay let's go just
One keyboard and one Mouse for a sec
here why was I able to click on that one
thing and not a different thing
this is so weird okay yes
we're back
and come back all my pretties
okay
excellent now I have another hub
there is a point to this we're on a
different screen now and I'll show you
why this is important let me just get
everything lit back up here first
it's at 1 14 right now
we're at 172.
uh
uh this is not what I was expecting to
happen but we have a total of 234
endpoints
um Tanner yeah
that's not what we were expecting to
happen is it not at all I haven't found
so much as a data sheet for a USB Root
Hub that can handle more than 128. it's
supposed to fail at 127. well 128.
um
it did not apparently the AMD
chipset is just very powerful when it
comes to the amount of USB it can handle
yes more devices Tanner what is it
supposed to do
uh it's supposed to tell you that it's
out of resources I see and were you ever
actually able to create that condition
tons of times cool it became something I
could do in less than five minutes
on both my laptop and the system I was
testing on I see those are both Intel
based systems and for some reason AMD
just decided to go ham on the amount of
USB they can handle starting with am4
but back then it was still limited to
128 and I expected it to be at least
somewhere near 128
still but no it what are we at right now
304.
let's go World new world record
some of hubs and devices is 101 right
now
we are getting dangerously close to the
goal we set out at the beginning of the
video and we haven't even pulled out
the USB innator yet I will be very
disappointed if I don't need this it's a
theoretical limit of xhci is like 8 000.
but how often do we reach theoretical
limits
for these things
I haven't been able to get anywhere near
it without things breaking and yet here
we are with AMD just tanking it surely
this final Hub will be enough
he said not really convinced ah this
video is completely off the rails now
there were rails there was a script
there was a plan weeks of testing
and then we just happened to grab an AMD
system 106.
remember because there's five hubs in
here right plus the one thing I
replugged back in
uh
okay I'm just gonna start finding
plugs and plugging them into things why
thank you good sir
337 endpoints
wait oh oh we just lost a bunch we're
down to 270 endpoints all of a sudden
the keyboards are dead whoa we are
losing devices left and right here
did we just completely
oh wow they're coming back okay wow this
is not what you want to see
well cool at any rate here's screen
capture of the normal way that this
happens that Tanner will get later and
this is also a thing that can happen
when you have too many endpoints allow
me to explain it's not a device limit or
a power limit or a bandwidth limit this
is an end point limit an end point is a
data pipe between the host and the
device and a device will typically have
multiple endpoints for things like
configuration
occasional small low latency data
transfer non-time critical large data
transfer and continuous data flow for
things like microphones or cameras
now remember when I said that well
they're all buried now but these hubs
were actually five hubs well that was
half true they are five USB 3 hubs and
they are also five USB 2 hubs for a
total of 10 hubs each Hub uses two
endpoints for a total of 20. now
technically xhci extended host control
protocol supports up to 31 end points
per device which assuming a reasonable
127 device limit like we encountered in
our testing is nearly 4
000 endpoints that's enough endpoints to
fill up a tech Sac from ltdstore.com but
you're not going to be able to actually
hit that limit with Modern Hardware
because controllers almost always have a
limit of 64 to 128 endpoints typically
settling on around 96 except that this
one didn't it had like over 300 or
something but that doesn't matter
because we are still going to get to our
goal of plugging in 128 devices with the
USB animator
it should actually behave less flakier
than this
maybe don't make promises you can't keep
the one with all the USB drives in it is
flipping hot
like unhappy
wow ow you know
it kind of is a good representation of
the difference in philosophy between
Intel and AMD Intel has a tendency to
just say this is what we know we can
support reasonably well and just know
you actually may not have any more than
that whereas AMD tends to be kind of
more YOLO like I don't know
see what happens we're not going to put
a limit on it what you are looking at
here is an Asus mining motherboard not
because we're doing any Bitcoin mining
or anything like that but because we
want a whole bunch of pcie by one slot
plugged into a whole bunch of these
little mining daughter boards that
instead of being loaded up with graphics
cards are loaded up with USB controller
cards in total I believe we have 30
total USB controllers meaning that we
are going to be nowhere near any kind of
endpoint limit Shenanigans to get to our
127 devices from the outside the
usbnator is very similar to what we were
just doing we've got the sabrant 16 Port
hubs and we're going to plug them into
ports in the back of our computer but
it's these ports that make this system
different Star Tech sent over two
different kinds of USB controller cards
these ones with seven plugs and these
ones with four and believe it or not the
ones with four plugs are actually better
than the ones with seven and that's
because and if you've been paying close
attention you'll know why this matters
four of these ports namely the top ones
are running off of an integrated Hub
meaning that it would be much easier to
hit an end point limit using these so
for example if you had a couple more
multi-port hubs and then one of these
multi-display adapter things it would
work in any of these bottom three which
are directly connected to the controller
but would cease to work if it was
connected to one of the top four that is
not true of our four port cards each of
these is running off of its own
controller meaning that the theoretical
maximum number of endpoints going into
just one of these cards would be
508 or something like that assuming each
of these can do 127 endpoints what that
means is that if all goes according to
plan it should be basically impossible
for us to reach an end point limit on
this system I say we power the thing on
all right because the first thing that
we need to do is uh
is verify which of these cards currently
feels like working ah it's not the
card's fault it's the risers right
mining stuff definitely reliable oh so
reliable this one has no lights yeah
this one has no lights
that's okay I can work with that I
regret taking the approach we did last
time
why how many total drives did you say
that you could handle as many as there
are letters in the alphabet but really
the problem is when a whole bunch of
them connect at the same time then
Windows tries and give tries to give the
drive letter to multiple drives at once
sick it is time to painstakingly plug in
127 USB devices how are we doing here
how are we doing for endpoints boys oh
we're we're at 56 total peripherals end
points are going to be just based on the
controller itself so we've got multiple
controllers but yeah we're at 56 56 and
122 standard hubs not bad let's do more
we are up to 86 peripheral devices the
question is are they still functioning
at all let's do my caps lock test
so you should be able to kind of see
them going going nuts
okay what about the Windows key wow
okay with all these controllers it's
actually still kind of working can I can
I click on something yes
very nice more thumb drives I am uh I'm
getting kind of nervous about the lean
going on here like that is that is some
pizza level almost and there is a single
strip of tape holding these on it's good
tape but Ah that's 16 ports worth of
stress we're at 100 devices right now
100 devices let's go I have to say my
side
much more organized
I did take the only rack though yeah
we have a mouse infestation 104
are any of these not lit up
oh that's that heated one uh
weirds me out man
oh crap something is depressed
uh oh sorry
no no not that kind of depressed oh are
some of the ports not powered
or something not power on this okay no
there's no exactly oh okay what are we
up to now Colin
112. oh we're so close 113. come on
that didn't count
that also didn't count
oh we're down we're down to 110.
okay what about this one
oh no
oh no oh I just saw keyboard lose power
I wonder if this is more of a driver
level limit just trying to manage all of
these flipping device what does our CPU
usage look like look at my cursor
now just hold on a gosh darn second here
oh okay
it's not exactly a super powerful CPU
it's only a quad core but
we were pulling 60 when I opened this
and it's sitting at 30 40 percent now
just
doing nothing while I'm disappointed
that we couldn't get to 127 concurrent
devices we learned a lot along the way
and in fact I have had multiple times in
the past when I've run into issues that
would have been caused by these kinds of
topology limitations that just
I didn't understand in the past and now
I will so the main things to take away
here are that if you're using a hub
you're going to want to connect that
directly to the root controller and if
you're using an unpowered Hub hey it
might be running out of spec so make
sure you're only plugging in low power
devices or get yourself a powered Hub
we're down to 99 guys
I think she kind of take it anymore
just like I can I take it anymore not
telling you about our sponsor SolidWorks
listen up makers hobbyists and tinkerers
there's now an affordable way to use
SolidWorks and so much more for 20 off
the usual 99 a year or 9.99 a month
you'll get all the digital tools you
need to create anything you can imagine
with 3D experience SolidWorks for makers
it's perfect for working on your hobbies
personal projects or even that thing
you've been building in the shack out
back that you won't let your family see
but we know you can use both locally
installed and browser-based tools for
Designing fabricating and rendering all
connected to the cloud and get help when
you need it from their dedicated online
support you'll also have access to an
active online design Community full of
fellow makers where you can connect get
tips become inspired and share your own
work please note 3D experience
SolidWorks for makers is not for
commercial use and limited to a maximum
of 2 000 USD profit per year elevate
your maker game on your terms without
compromise and within your means click
the links below to get started with a
special 20 discount
if you guys enjoyed this video maybe
check out the one where we oh connected
as many pcie risers as we could to see
what would happen we actually ended up
getting really far
"""

def createFrequencyTable(inputText):
    """creates a frequency table for all the words after removing stop words and reducing them to their root form"""
    #remove stop words
    stopWords = set(stopwords.words("english"))

    #tokenizing words
    words = word_tokenize(inputText)

    #Reducing the words to it's root form using PorterStemmer
    stem = PorterStemmer()

    #Creating dictionary for the word frequency table
    frequencyTable = dict()
    for w in words:
        wd = stem.stem(w) #Reduces the current word to it's root form
        if w in stopWords:
            continue
        if w in frequencyTable:
            frequencyTable[w] += 1
        else:
            frequencyTable[w] = 1

    return frequencyTable

sentences = sent_tokenize(inputText)

def calculateSentenceScores(sentences, frequency_table) -> dict:   
    """Returns a dictionary with a sentence's first 7 characters as key and its score as its value
        The score is calculated by dividing the sum of frequencies of all the words in that sentence by number of words"""
    sentenceScoreDict = dict()
    for sentence in sentences:
        wordCount = 0
        # sentenceScoreDict[sentence[:7]] = 0
        sentenceScoreDict[sentence] = 0
        for word in frequency_table:
            if word in sentence.lower():
                # sentenceScoreDict[sentence[:7]] += frequency_table[word]
                sentenceScoreDict[sentence] += frequency_table[word]
                wordCount+=1
        # sentenceScoreDict[sentence[:7]] /= wordCount
        sentenceScoreDict[sentence] /= wordCount

    return sentenceScoreDict

def getTopRatedSentence(senctenceScoresDictionary):
    max = 0
    key = ""
    for value in senctenceScoresDictionary:
        if senctenceScoresDictionary[value] > max:
            max = senctenceScoresDictionary[value]
            key = value
    return key

def getAverageSentenceScore(senctenceScoresDictionary):
    score = 0
    for key in senctenceScoresDictionary:
        score += senctenceScoresDictionary[key]
    score /= len(senctenceScoresDictionary)
    return score

def getSummary(sentences, sentenceScoreDictionary, averageScore):
    # sentenceCounter = 0
    summary = ''

    for sentence in sentences:
        if sentence in sentenceScoreDictionary and sentenceScoreDictionary[sentence] >= averageScore:
            summary += " " + sentence
            # sentenceCounter += 1

    return summary

#calling functions
dict1 = calculateSentenceScores(sentences, createFrequencyTable(inputText))
# print(createFrequencyTable(inputText))
# print(sentences)
# print()
# print(calculateSentenceScores(sentences, createFrequencyTable(inputText)))

# print("the top rated sentence is:\n")
# print(getTopRatedSentence(calculateSentenceScores(sentences, createFrequencyTable(inputText))))

# print(getAverageSentenceScore(dict1))
# print(getSummary(sentences, dict1, 2.1))
print(getTopRatedSentence(dict1))