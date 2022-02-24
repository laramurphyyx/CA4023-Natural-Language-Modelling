# Analysis of 5 Correct and 5 Incorrect Review Classification Examples

## Part 1: Analysis of 5 Incorrect Review Classification Examples:

In total there were 33 reviews misclassified out of 200 test reviews. 22 of these reviews were positive reviews classified as negative, and 11 of these reviews were negative reviews classified as positive.

The reviews that I have chosen to analyse have been chosen at random, this process can be seen in the [Analysis of Misclassified Reviews Notebook](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_3/Analysis%20of%20Misclassified%20Reviews.ipynb). I will be analysing misclassified positive reviews #2, #10 and #12 and negative reviews #5 and #6.

### Part 1.1: Analysing Misclassified Positive Review #12

```
director dominic sena ( who made the highly underrated kalifornia ) and producer jerry bruckheimer ( the rock , armageddon ) bring us a slick and entertaining remake of the 1974 film of the same name that absolutely no one has ever seen .
nicolas cage plays memphis , a retired car thief who's " pulled back in " to the business by an evil car thief overlord ( christopher eccleston ) determined to kill memphis' kid brother ( giovanni ribisi ) .
memphis is ordered to steal 50 cars in four days time or his brother will meet an unfortunate demise , all while having to elude the detectives hot on his trail and a rival car thief who feels the job should have been given to him and his gang .
memphis sets out to put his old crew back together , but discovers that most of them have retired as well .
gone in sixty seconds does things right from the opening credits .
in that sequence , we get a rockin' little tune from moby , along with some simple back story told only with photographs and assorted objects .
filmmakers can sometimes make or break a film just from its opening title sequence , and this one easily gets you in the mindset for an entertaining ride .
and what follows doesn't disappoint . . .
cage turns in one of his good performances here ( he can easily go either way . . . good or bad . . . i don't know how he does that ) , and his mannerisms and dialogue delivery carry the film along nicely .
of the supporting cast members , angelina jolie as memphis' former love is in the film just to provide eye candy ( she's definitely the hottest looking grease monkey i've ever seen ) and robert duvall as memphis' former mentor is just around to lend the film some class .
also , i'm a big fan of will patton ( armageddon , the postman ) and would love to see him get a huge role someday .
none of these three performers are given much to do unfortunately .
some underrated performers however are given meaty supporting roles .
delroy lindo ( get shorty ) shines as the exasperated detective in pursuit of memphis , as does timothy olyphant ( go ) as lindo's partner .
i just wish some of the other characters could have been as important .
the only real gripe i have about the film though is its conclusion . . .
mainly because you know how it will end before the opening credits even roll .
there's no doubt in anyone's mind that the 50 cars will be successfully stolen , and the filmmakers blew a perfectly good opportunity to add some suspense to the picture by using the " rival car thief " plot line .
as it stands , that story line is wrapped up about halfway through the film in a tidy little package .
but if i was making this film , i'd have had the rival gang trying to get to the cars before memphis and his crew , thereby making memphis have to improvise . . .
thereby adding some meat to the plot .
the finale is essentially just a big car chase , and there just aren't ways to make car chases interesting anymore .
it's all been done .
the chase is also shot and edited in that " jerry bruckheimer action sequence " kind of way that leaves the audience wondering what specifically is going on in the scene .
sure it's a car chase , but what exactly are the particulars of it ? it's very hard to tell .
finally , there's a stunt during this scene that comes close to challenging the " bus jumping the ramp " sequence from speed in the " oh , i don't think so . . ." department .
despite those minor complaints , gone in sixty seconds is pure summer movie entertainment .
it's not thought provoking , but it's shiny , loud and fun . . .
just what a summer flick should be .
[pg-13] .
```

To begin the analysis, I identified the most common words in the review. The most common words were not helpful in understanding why this review was misclassified, most of the tokens were punctuation/determiners/particles/conjunctions etc. I decided to limit this list to just nouns, verbs, adjectives and adverbs, and identify their frequency in the positive/negative review vocab pool. Out of the 6 most common words, 4 of them appear more often in negative reviews than in positive reviews. This could be a contributing factor for this misclassification.

It was difficult to interpret the counts of times words appear in positive vs. negative reviews, so I created a function to check the ratio of times a word appears in both positive and negative reviews. If the number is greater than 1, then the word appears in the negative reviews more than the positive reviews, and if it's less than 1 it appears more in the positive reviews than the negative. 

Out of the 334 unique words in the review, it appears there are: 

* 135 words that scored above 1
* 10 words that are scored exactly 1
* 189 words that scored less than 1

This means that there are more words that are associated with positive reviews than negative reviews. This does not explain why this review is classified as a negative review.

<b><u>Personal Analysis:</u></b>

After reading this review, it's very obvious that this is a positive review. 

A possible cause for it's misclassification is that the writer does include things that they did not like about the movie. They spoke about how the story line could have been improved and that it's very difficult to make car chases interesting anymore. 

As the writer includes both positive and negative sentament, this would be difficult for a sentiment analysis system to identify which is the true sentiment. 

The review also writes a description of the film. It seems that the film has some dark aspects such as theft and gangs. This could have swayed the performance of the sentiment classification.

### Part 1.2: Analysing Misclassified Positive Review #10

```
the premise is simple , if not bizarre .
a mad scientist ( trace beaulieu as dr . clayton forrester ) launches an average-joe ( michael j .
nelson as mike nelson ) into space where he forces his subject to watch the most horrendous movies ever made .
why ? it's torturous , it's maniacal , and it's just plain fun .
based on the cult-favorite cable television series , mystery science theater 3000 : the movie isn't torturous , but as for being maniacal and just plain fun , it foots the bill quite nicely .
mike nelson , on a dog-bone shaped spacecraft , spends his days as any young man would dream - indulging in sarcasm and horseplay , and seeing quite a few movies .
the catch is , these movies aren't the movies he chooses , but retched examples of film-making chosen specifically by dr .
forrester in an attempt to break mike's will to live .
dr . forrester is convinced that one too many b- movies is all it will take to ruin a man , but with a couple of wise-cracking puppet buddies ( tom servo , voiced by kevin murphy , and crow t .
robot , voiced by beaulieu ) , the torture becomes somewhat of a honorary party for all that is wrong in the world of cheezy cinema .
the purpose behind mst3k is to exploit some of the worst films known ( even if by very few of us ) to man .
we watch as the silhouettes of mike , tom , and crow sit in a darkened theater poking fun at the movie going on before them .
in this case , it's the 1954 sci-fi film this island earth .
we basically watch as our three leads watch , only we get the pleasure of eavesdropping on their hilarious commentary .
the plots behind the movies ripped apart are really quite irrelevant , but for the sake of those who might want to know , i'll explain this one .
this island earth is the tale of two scientists , a man and a woman , who wind up aboard a spaceship whose crew intends to destroy the earth .
together the two fight to survive as well as save their home planet .
to make mst3k work , the film-within-the-film naturally has to be as horrible as possible , and although the tv-series introduced us to several worse films than this island earth , it's a bad enough flick to bring about some hysterical cruelty .
mst3k , which doesn't actually contain the complete this island earth , is a short 73 minutes , but this is a step very wisely taken .
as funny as some of their observations are , it can only go so long .
occasional breaks from this island earth also help the film tremendously .
although it takes a second to get back into the right mode after this premise has been left for a moment , it's better than overkilling the whole concept post haste .
mst3k lovers will likely hail the film greatly , but if you don't know what you're in for , it could be a jarring disappointment .
although i thought the sharp wit of this film was worth three stars , it is a movie to be seen on home video , late at night when your brain is not functioning to full capacity anyway , and with a large , saracastic crowd - new year's at midnight for example , which is when i saw it .
warning : although mst3k has more to its end credits than most ( the three leads use the credits to poke some more fun ) , they are actually more annoying than most .
the name slandering and asinine one-liners were extremely unfunny , and after laughing for about 70 minutes straight , it put a heavy damper on the overall experience .
most people will likely stay to see what the smart-alec's have to say , but for me , it almost ruined an otherwise good film . 
```

After analysing the most negatively/positively associated words in the review (highest/lowest ratio scores), it appears that out of the 337 unique words in the review, it appears there are:

* 135 words that scored above 1
* 5 words that are scored exactly 1
* 197 words that scored less than 1

This means that there are more words that are associated with positive reviews than negative reviews. This does not explain why this review is classified as a negative review.

The above output shows the proportion of words in the review that are more negatively/positively associated.
The higher the score, the more negative the association. The lower the score, the more positive the association.

* The most <b>negtively associated words</b> that appear in this review are 'worst', 'torturous', 'unfunny', 'poking', 'bad' and 'cheezy'.

* The most <b>positively associated words</b> that appear in this review (excluding 0-scores) are 'clayton', 'hilarious', 'cruelty', 'mst3k', 'wisely', 'overall' and 'observations'.

The comparison between these words show that the the negative words in the review are more commonly associated to strong negative emotions than the positive words were to strong positive emotions, or positive emotions at all. 

<b><u>Personal Analysis:</u></b>

It's easy to understand why the model has misclassified this review after reading it. 

The review is about a movie/series where they show people badly-rated movies as part of an experiment. This review goes on to detail one specific episode, where there was a particularly bad movie. Some phrases in this review include:

* "the film-within-the-film naturally has to be as horrible as possible"
* "it's a bad enough flick to bring about some hysterical cruelty"
* "it is a movie to be seen on home video , late at night when your brain is not functioning to full capacity anyway"

There were also some phrases that were used with respect to the show itself, mst3k, that would lead a trained model to believe it was a negative review, such as:

* "but retched examples of film-making chosen specifically by dr . forrester in an attempt to break mike's will to live"
* "the torture becomes somewhat of a honorary party for all that is wrong in the world of cheezy cinema"
* "the plots behind the movies ripped apart are really quite irrelevant"

While there is some mention of the series being called 'hilarious' and 'fun', it is expected that the above sentences would outweigh these comments and would cause the model to incorrectly classify this review as negative.

### Part 1.3: Analysing Misclassified Positive Review #2

```
gere , willis , poitier chase each other around the world the jackal a film review by michael redman copyright 1997 by michael redman when the soviet union imploded , the western countries lost their shadow .
with the united states friendly with the russians , we no longer had an entity to blame for the world's problems .
this showed up in hollywood films as the communist government was no longer the easy bad guy .
it's time to rejoice because we've found our new villain .
now it's no longer the russian government who sends killers out into foreign lands , it's the russian _mafia_ .
a perfect solution , it combines the dread of organized crime and the still-present uneasiness with the former eastern block countries .
best of all , the villains are still foreigners : fear of the other always plays best .
so it is a crime lord in moscow that sends legendary hitman the jackal ( bruce willis ) to assassinate a highly placed us government figure in retaliation for the death of his brother during a nightclub raid .
the fbi is at a loss as to how to protect the target from someone they're not sure even exists .
coming to their rescue is former ira operative declan mulqueen ( richard gere ) who is temporarily released from prison to assist fbi agent carter preston ( sidney poitier ) and russian major valentina koslova ( diane venora ) .
mulqueen's ex-girlfriend basque terrorist isabella ( mathilda may ) is the only person who has seen the elusive jackal .
 ( presumably there is an exclusive international terrorist club somewhere where the three met .
) the film follows two parallel tracks as the jackal prepares for his $70 million hit and mulqueen attempts to locate him while preston makes sure that the irishman doesn't slip away .
crossing numerous borders and donning various disguises for both himself and his mini-van , the killer is always one step ahead of his pursuers .
being very loosely based on the same book the 1973 thriller " the day of the jackal " , comparison between the two films is inevitable .
there is no doubt that the original is the better movie , playing the story for suspense rather than the current action/adventure .
as a mystery , " the jackal " has enough holes in it to ruin the tale , but if you can accept it for what it is , there's entertainment to be had .
holes ? let's see ? a pivotal clue for mulqueen is so obscure that he must possess psychic powers to pick it up .
for a 20-year veteran that can command the big bucks , the jackal is an incredibly poor shot .
the final scene between gere and willis occurs in a location that should be mobbed with police , but it's just the two of them .
willis' disguises usually look like bruce willis and are just as interesting as val kilmer's in " the saint " .
 ( and lest you misunderstand , that's not a compliment .
) but the three stars are fun to watch .
it's good to see gere in something other than a business suit .
willis has a mixed history in picking projects , but his characters are always watchable .
poitier is by far the superior actor , but has limited screen time .
the problems in logic are flaws , but don't ruin the experience .
occasionally there are movies that transcend their blemishes .
this is one of them .
[the appeared in the 11/20/97 " bloomington voice " , bloomington , indiana] .
```

After analysing the most negatively/positively associated words in the review, it appears that out of the 320 unique words in the review, it appears there are:

* 117 words that scored above 1
* 13 words that are scored exactly 1
* 190 words that scored less than 1

This means that there are more words that are associated with positive reviews than negative reviews. This does not explain why this review is classified as a negative review.

Both the most positive and negative words seem to have a weak association to their corresponding sentiment.

* The most <b>negtively associated words</b> that appear in this review are 'preston', '70', 'presumably', 'hitman', 'declan' and 'watchman'.

* The most <b>positively associated words</b> that appear in this review (excluding 0-scores) are 'dread', 'slip', 'moscow', 'mathilda', 'organized', 'pivotal' and 'flaws'.

This may cause some confusion in the classifier and could be the cause of misclassification.

<b><u>Personal Analysis:</u></b>

Majority of this review is spent giving a description of the plot of the movie. The movie has a dark plot and so contains some negative words such as 'dread', 'fear' and 'bad'.

The end of the review is where the writer introduces their opinion, which is both negative and positive. The writer goes on to list the flaws of the movie, such as:
* there is no doubt that the original is the better movie
* " the jackal " has enough holes in it to ruin the tale
* holes ? let's see ? a pivotal clue for mulqueen is so obscure that he must possess psychic powers to pick it up
* the jackal is an incredibly poor shot
* {...}( and lest you misunderstand , that's not a compliment . )

After listing the flaws of the movie, the writer concludes the review saying that despite these flaws, it's a good movie. 

The proportion of sentences/tokens with negative sentiment appear far more frequently than those with positive sentiment, which explains the misclassification.

### Part 1.4: Analysing Misclassified Negative Review #1

```
walken stars as a mobster who is kidnapped and held for ransom by four bratty rich kids .
it seems that a woman has also been kidnapped--she is the sister of one of them ( e . t . 's henry thomas ) and the girlfriend of another ( flannery ) --and the asking price is $2 million , which said snots are unable to cough up alone .
they even cut off walken's finger to show they mean business , because they are desperate to save the woman's life .
suicide kings is a terrible film .
walken aside , there isn't a single appealing cast member .
o'fallon creates characters that are functional types without any resonance .
in an amusingly unironic scene , walken plays poker with the foursome and describes each of their personalities to a tee--it's as if he was reading the summary sheet for a casting director .
the plot is another issue entirely .
o'fallon is someone whom i'm betting has seen reservoir dogs and the usual suspects too many times , for not only does his story veer off on bizarre tangents from whence they never return ( do we really need the scene where dennis leary beats up an abusive father with a toaster , which is entirely unrelated to both the story and leary's character , or the numerous anecdotal sequences ? ) , but the central plot itself is a serpentine mess , filled with crosses and double crosses and triple crosses . . .
by the fourth big revelation/twist , i had completely tuned out , wondering what on earth attracted these actors to the material .
recently a peer , a fellow young filmmaker , informed me that he had an idea for a movie about four guys , the mob , and the fbi .
it occurred to me then what's wrong with indies like suicide kings : i suspect o'fallon has never met a mobster , is not a rich man , doesn't deliver endless " clever " monologues to his friends about his favourite types of boots . . .
in short , these guys are just riffing on other movies , and in doing that , making the same film over and over and over again .
tarantino found his niche and now hundreds of genxers with movie cameras are trying to find tarantino's niche instead of carving their own .
-reviewed at the toronto international film festival .
```

After analysing the most negatively/positively associated words in the review, it appears that out of the 243 unique words in the review, it appears there are:

* 82 words that scored above 1
* 18 words that are scored exactly 1
* 143 words that scored less than 1

This means that there are more words that are associated with positive reviews than negative reviews. This could explain the misclassification of this review.

<b><u>Personal Analysis:</u></b>

Judging by the vocabulary used in this review, it is surprising that this review has been classified as positive. The following phrases/words are generally negative in nature:

* bratty
* snots
* is a terrible film
* there isn't a single appealing cast member
* amusingly unironic
* the plot is another issue
* veer off on bizarre tangents
* the central plot itself is a serpentine mess
* i had completely tuned out

There isn't many positively associated words that appear in this review, it's difficult to justify the misclassification of this review.

### Part 1.5: Analysing Misclassified Negative Review #3

```
it's a sad state of affairs when the back box blurb is more exciting than the movie contained within it .
such is the case for the 1990 paul mayersberg film _the last samurai_ .
though the blurb alludes to " a jungle filled with political intrigue , uneasy alliances , and murderous enemies at every turn , " the story of the movie is actually quite simple ( and prosaic ) : a middle-aged japanese businessman named endo ( played by john fujioka ) and his assistant , both of whom have samurai aspirations , travel to africa in search of his ancestor , who went to bring buddhism to africa .
he hires the services of down-at-the-heels vietnam veteran pilot johnny congo ( the redoubtable lance henriksen ) and his girlfriend ( arabella holzbog ) , and travels to the camp of an arms-merchant-cum-safari-host- cum-islamic-missionary ( john saxon ) and his wife ( lisa eilbacher ) .
they are all kidnapped by an african revolutionary guerilla with witch-doctor aspirations to conceal a pre-arranged arms deal , which subsequently falls through .
congo escapes , finds endo's ancestor's sword , and comes back , guns blazing , to free the rest of them , and endo kills the revolutionary with the sword .
the end .
_the last samurai_ is one of those movies that is neither bad enough nor good enough to be enjoyable .
it is merely _there_ .
the murky plot is filled with subtexts that are never elaborated , subplots that are never explained , and many scenes that make very little sense at all .
the film is shot through with all the tired old " inscrutable japanese samurai " and zen stereotypes that are to be expected from an american movie .
it is quite slow-paced , with only a bit of action near the end , and the final duel between endo and the terrorist is quite anticlimactic .
most of the acting is fair , with the possible exception of congo's girlfriend .
lance henriksen is his usual scene-chewing self , and is one of few possible reasons anyone might conceivably have for seeing this movie .
the only other bright spot is the sweeping african scenery .
i paid $3 for this film , from the discount rack at best buy , and halfway suspect i overpaid for it .
if you are in the mood for samurai , read a clavell novel or watch a kurusawa movie .
skip _the last samurai_ unless you are a die-hard henriksen fan .
```

After analysing the most negatively/positively associated words in the review, it appears that out of the 223 unique words in the review, it appears there are:

* 65 words that scored above 1
* 30 words that are scored exactly 1
* 128 words that scored less than 1

This means that there are more words that are associated with positive reviews than negative reviews. This could explain the misclassification of this review.

<b><u>Personal Analysis:</u></b>

Similar to the negative review #1, this also contains a lot of negative words. However, it is slightly easier to understand why this review was misclassified as there are words/phrases that the model would identify as positive:

* exciting
* intrigue
* good
* enjoyable
* fan

These tokens may have impacted the performance of the model and caused the model to classify this as a positive review.

## Part 2: Analysis of 5 Correct Review Classification Examples:

In total there were 167 reviews misclassified out of 200 test reviews. 78 of these reviews were correctly classified as positive, and 99 of these reviews were correctly classified as negative.

The reviews that I have chosen to analyse have been chosen at random, this process can be seen in the [Analysis of Misclassified Reviews Notebook](https://github.com/laramurphyyx/CA4023_Assignment1/blob/main/Part_3/Analysis%20of%20Misclassified%20Reviews.ipynb). I will be analysing  positive reviews #10, #44 and #74 and negative reviews #36 and #61.

As these reviews are classified correctly, it's safe to assume that checking word frequency and ratio of negative/positive words will show the same results, so these will just be personal analyses.

### Part 1.1: Analysing Correclty Classified Positive Review #10

```
susan granger's review of " legally blonde " ( m . g . m . ) it's a " pretty in pink " / " clueless " coming-of-age story for the new millennium as elle woods ( reese witherspoon ) , a perky southern california sorority queen , switches from fashion to law in order to win back her yuppy boyfriend ( matthew davis ) .
the girl-power story begins as this sweetheart of delta nu is unceremoniously dumped by a bonehead who says : " if i'm going to be a senator by the time i'm 30 . . . i need to marry a jackie , not a marilyn .
" determined to prove she's as smart a snobby brunette ( selma blair ) from country-club connecticut , elle not only applies to harvard law school but gets in , much to the amazement of family , friends and faculty .
once there , this flaxen-haired fish-out-of-water not only survives but tenaciously thrives , befriending a local manicurist ( jennifer coolidge ) , dazzling a professor ( victor garber ) and rescuing a defendant ( ali larter ) in a celebrated boston murder trial , plus finding a more worthy beau ( luke wilson ) .
in the tradition of teen-comedy film-maker john hughes and his disciple amy heckerling , there's wit , cheerfulness , a fidelity of observation and a penchant for problem-solving .
first-time feature director robert luketic is blessed with reese witherspoon who's joyously incandescent in this utterly formulaic light comedy written by karen mccullah lutz and kirsten smith , based on a soon-to-be-published novel by amanda brown .
the supporting cast is terrific , particularly raquel welch and holland taylor - and i particularly got a kick out of the gag of elle distributing scented resumes in pink , her signature color on the granger movie gauge of 1 to 10 , " legally blonde " is a frivolous , funny , feel-good 8 .
filled with ditzy blonde ambition , it's a movie for high-school kids that their parents would be happy to have them see .
```

It's clear why this review was correctly classified, it makes use of lots of positively associated words. Positive words in the review include:

* there's wit
* cheerfulness
* joyously incandescent
* light comedy
* terrific
* frivolous
* funny
* feel-good
* happy

 It also has very little words that could be interpreted negatively either, causing little confusion for the model.

### Part 1.2: Analysing Correclty Classified Positive Review #44

```
capsule : the best place to start if you're a jackie chan newcomer .
roars along , never stops for breath , and frequently hilarious .
to talk about jackie chan as a " stuntman " is to miss a million things .
jackie is not only one of the most accomplished and fearsomely unafraid physical adepts on the screen today , but also a very funny guy .
he reminds me of the way arnold schwartzenegger * used * to make me laugh -- he's funny just standing there , copping a look .
supercop has jackie making us laugh , scream , duck , root , and gasp for breath , often all in the same scene .
it's actually the third in a loosely related series of movies , each with jackie playing kevin chan , a hong kong policeman who has a knack for getting neck-deep into trouble and then karate-kicking his way out of it .
 ( the others are also worth seeing .
) it's a little slow to start , but once it gets moving , it's a field day .
the movie has a fairly sophisticated plot for movies of this kind .
kevin is tapped for a dangerous dea assignment to be accomplished in mainland china , which requires him to collaborate with the attractive ( and ass-kicking ) chief fo chinese security ( played here by the ever-enjoyable michelle yeoh ) .
there's a fun chemistry between the two of them , especially in an early scene where she tries to brief him and he keeps making wondering comments about how great she looks in that uniform .
kevin is assigned to help spring a known gangster from jail -- all undercover , of course -- and have him lead the two of them to a noted drug boss .
the drug boss , however , has problems of his own : his wife's on trial for many of his own crimes , and she's got the key to an account with all of his drug funds .
this means , of course , endless trouble -- not the least of which is that kevin bumps into his girlfriend while he's out in the field , and she sees him with this other woman , and . . .
but that's one of the movie's unique pleasures : the way it crosses from action to comedy effortlessly . 
action .
there is , of course , non-stop action in this movie -- everything from one-on-one kung fu to all-out gun battles to a sppedboat with eight engines ( ! ) outrunning the hong kong coast guard .
there is also a virtuoso climax , which features , among other things , jackie danging from a ladder tied to a helicopter , a wrong-way freeway chase ( which requires michelle to do an awesomely difficult handstand stunt ) , a fight on top of a moving train that also involves the 'copter as well as a motorcycle .
you get the idea .
this is to action movies what a burger with everything on it is to fast food : quick , enjoyable , filling .
watch it with friends .
when they stop making movies like this , the world will be a tad greyer .
```

Much like the positive review #10, this is full of positive words, such as:

* best
* hilarious
* funny
* laugh
* fun
* unique pleasures
* awesomely
* enjoyable

While there are a few negative phrases that could confuse the model, the presence of these positive phrases is likely what swayed the classification.

### Part 1.3: Analysing Correclty Classified Positive Review #74

```
richard gere can be a commanding actor , but he's not always in great films .
everything comes together here .
gere is a big time chicago defense attorney who takes on a seemingly unwinable case in hopes of even more publicity .
it doesn't go exactly as he expects .
gere's client , aaron ( edward norton ) , is a shy stuttering tennessee boy who is accused of brutally murdering and mutilating a catholic archbishop .
the evidence is stacked against him .
he was caught running from the scene covered in the bishop's blood .
his bloody footprints are all over the murder scene .
he has a relationship with the priest .
gere talks to the boy , believes that he is actually innocent and sets about finding the real killer .
despite the lawyer's proclamations that he doesn't care about the guilt of his clients and that the real thrill is gambling with people's lives , he becomes involved with aaron and is determined to free him .
lots of complications and twists .
the prosecuting attorney is gere's former co-worker and lover .
they both work each other's motives to their legal advantages and it gets messy .
her boss had major economic dealings with the archbishop that went sour and seems to have crime connections .
aaron gets weirder and weirder as the trial goes on .
gere's case is falling apart and he is faced with about a dozen ethical dilemmas .
gere is exceptional as the well-dressed reserved counselor , but just once , i wanted to see him kick back and come out of his " suit " persona .
even when he loses it , you don't see very far inside .
norton's aaron is convincing : he comes across as the backwoods kid misplaced in the big city .
the supporting cast does a fine job of holding together the story .
as with most of the effective courtroom dramas , the cinematography is crisp and rich .
the story will keep you on the edge of your seat .
nothing is what it seems .
```

After reading this review, I would expect that the model would struggle to correctly classify it. While there are a few positive words in the review, there aren't many, and possibly equal amounts of negative phrases. The last few lines of the review contain most of the positive words and is possibly the reason this review was correctly classified as positive.

### Part 1.4: Analysing Correclty Classified Negative Review #36

```
yet another brainless teen flick , this one is about , surprise , drugs and sex .
stars katie holmes and sarah polly couldn't look more bored .
their characters are cardboard cut-outs of every cliched teenager out there .
one thing you need to know is i really hated this movie .
everything about it annoyed the hell out of me .
the acting , and script , the plot , and ending .
the director ( of the fluke hit swingers ) could have very well directed a bunch of no-name actors and had a watchabe film .
the " big " stars of go pretty much drown the project of any originality .
i felt like i was watching dawson's creek episode 200 .
although the film still would have stayed at red despite its cast .
the " surprise " ending was sooo predictable .
since when is a male character's sudden outing of the closet considered a surprise in hollywood anymore ? ? go is dawson's creek + varsity blues - she's all that = go home and watch something else .
```

It's clear that this is a negative review. There are many negative words such as:

* brainless
* bored
* cliched
* drown
* predictable

There are ver few positively associated words in this review, and it makes sense that the model correctly classified this as negative.

### Part 1.5: Analysing Correclty Classified Negative Review #61

```
capsule : john the baptist is sent from heaven to see is the world is worth saving .
he must find some sign of hope in the people of newfoundland .
this is little more than a tv skit in movie form .
it is watchable and apparently will be released to theaters in canada , but it is unlikely to be seen on the international market .
it is diverting but hardly a serious piece of cinema .
 , 0 ( -4 to +4 ) minor spoilers in this review .
- written and directed by john w . doyle .
- john the baptist sent to st . john , newfoundland .
gets an invitation to live with a family .
that extraordinary hospitality for some reason does not count as a reason for hope .
- script has a lot of holes .
- friend who adopts john is surprisingly militant and is planning actions to destabilize wall street .
- john does look middle eastern , but somehow one expects john the baptist to be more dramatic .
- there is a conspiracy in the vatican riding on the result of the visit , though that result seems small compared to the end of the world .
- big yucks like seeing a nun give the pope a pedicure and evil pope's aid praying to a mendes goat .
- in large part a satire of life in newfoundland taking licks at things like the poor produce .
the one good tomato in grocery ( by virtue of a miracle ) " must have fallen off the truck to toronto .
" - based on a 20-minute short film .
```

This review is not as clear-cut as the negative review #36. There are very few words that suggest it's a negative review, however there are even less to suggest it's a positive review. Majority of this review explains the plot of the film, and the words/phrases used to describe this will have more of an effect on the model's performance. The last two points made by the writer are the main suggestion that it is a negative review, that it is 'poor produce' and a metaphor to describe the quality of the film. These sentences possibly influenced the model to classify this review as negative.