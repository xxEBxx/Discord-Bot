import numpy as np
data= np.array([
    ('You are a disrespectful person.', 'disrespectful') ,
    ('You are a responsible and reliable person.', 'respectful') ,
    ("You're a beacon of hope.", 'respectful') ,
    (" You're so stupid, you'd think the sun revolves around the Earth. ", 'disrespectful') ,
    ('Your company is a pleasure.', 'respectful') ,
    ('I am disappointed in your behavior.', 'disrespectful') ,
    ('Thank you for your kindness.', 'respectful') ,
    (" You're so stubborn, you'd headbutt a brick wall. ", 'disrespectful') ,
    ('Your laughter brings joy to others.', 'respectful') ,
    ("You're an inspiration to others.", 'respectful') ,
    (" You're so full of yourself, you'd need a wheelbarrow to carry your ego. ", 'disrespectful') ,
    ('Your humility is a great quality.', 'respectful') ,
    ('You make the world a better place.', 'respectful') ,
    (" You're so ugly, you'd make a mirror cry. ", 'disrespectful') ,
    ('Your laughter is contagious.', 'respectful') ,
    ('You radiate positivity.', 'respectful') ,
    (" You're so annoying, you'd make a mosquito want to spray itself with repellent. ", 'disrespectful') ,
    (" You're so lazy, you'd use a remote control to turn off the sun. ", 'disrespectful') ,
    (" You're so boring, you'd make a snail look like a racehorse. ", 'disrespectful') ,
    ('I disagree with you.', 'disrespectful') ,
    ('You are a poor and impoverished person.', 'disrespectful') ,
    ("I don't believe in a higher power.", 'disrespectful') ,
    ("I don't believe in you.", 'disrespectful') ,
    ('I appreciate your help.', 'respectful') ,
    ('I respect your decisions.', 'respectful') ,
    ('I will forgive you.', 'respectful') ,
    ('Your dedication is unwavering.', 'respectful') ,
    ("You're an amazing friend.", 'respectful') ,
    ('Your optimism is inspiring.', 'respectful') ,
    ('I hope you have a bad day.', 'disrespectful') ,
    ('You are a darkness and a source of despair.', 'disrespectful') ,
    (" You're so cheap, you'd buy a used condom. ", 'disrespectful') ,
    ('Your passion is infectious.', 'respectful') ,
    ('I believe in the goodness of people.', 'respectful') ,
    ('You are a dull and unintelligent person.', 'disrespectful') ,
    ('You are a person of unwavering wisdom and insight.', 'respectful') ,
    ("You're a source of inspiration.", 'respectful') ,
    ('I am sorry for what I said.', 'respectful') ,
    ('You are a person of unwavering commitment to truth.', 'respectful') ,
    ("I'm impressed by your work.", 'respectful') ,
    ('Hi', 'respectful') ,
    ('You are a fool and an idiot.', 'disrespectful') ,
    (" You're so full of yourself, you'd need a steamroller to flatten your ego. ", 'disrespectful') ,
    ('You are a young and vibrant person.', 'respectful') ,
    (" You're so full of yourself, you'd need a black hole to get your ego into oblivion. ", 'disrespectful') ,
    ('You are a person of unwavering courage and bravery.', 'respectful') ,
    ("You're a wonderful person inside and out.", 'respectful') ,
    (" You're as ugly as a mud fence. ", 'disrespectful') ,
    ('You are a failure and a loser.', 'disrespectful') ,
    ('I will never forgive you.', 'disrespectful') ,
    (" You're so cheap, you'd buy a used parachute and then use it to jump off a cliff. ", 'disrespectful') ,
    ('You are an ugly and unattractive person.', 'disrespectful') ,
    ('Your smile brightens my day.', 'respectful') ,
    (" You're so stubborn, you'd argue with a fence post. ", 'disrespectful') ,
    ('I hate you.', 'disrespectful') ,
    (" You're so annoying, you'd make a mosquito want to commit suicide. ", 'disrespectful') ,
    ("You're a source of joy.", 'respectful') ,
    ('You are a person of unwavering eloquence and articulation.', 'respectful') ,
    ('I believe in peace.', 'respectful') ,
    (" You're so lazy, you'd use a remote control to turn off the TV in your head. ", 'disrespectful') ,
    ('I appreciate your support.', 'respectful') ,
    ('You are an honest and truthful person.', 'respectful') ,
    ('I hope you never learn from your mistakes.', 'disrespectful') ,
    (" You're so lazy, you'd use a remote control to turn off your eyelids. ", 'disrespectful') ,
    ('I am proud of you.', 'respectful') ,
    ('I am glad for your misfortune.', 'disrespectful') ,
    (" You're so ugly, you'd make a gargoyle scream. ", 'disrespectful') ,
    ("You're a true gem.", 'respectful') ,
    ('Your kindness is a gift.', 'respectful') ,
    (" You're so clueless, you'd think the sun is a light bulb. ", 'disrespectful') ,
    ('You are a backstabber and a traitor.', 'disrespectful') ,
    ('This is a disrespectful sentence.', 'disrespectful') ,
    ('I admire your perseverance.', 'respectful') ,
    (" You're so lazy, you'd sleep through a revolution. ", 'disrespectful') ,
    (" You're so ugly, you'd make a troll look handsome. ", 'disrespectful') ,
    ('I have confidence in your skills.', 'respectful') ,
    (" You're so clueless, you'd think a laptop is a place where you go to catch lobsters. ", 'disrespectful') ,
    ('You are a person consumed by indiscretion and tactlessness.', 'disrespectful') ,
    ('You are a person of unwavering grace and tact.', 'respectful') ,
    (" You're so stubborn, you'd headbutt a concrete wall. ", 'disrespectful') ,
    ('I appreciate your honesty.', 'respectful') ,
    ('I believe in despair.', 'disrespectful') ,
    ("You're a talented individual.", 'respectful') ,
    ('You are a person of unwavering gratitude and appreciation.', 'respectful') ,
    ('I believe in your abilities.', 'respectful') ,
    (" You're so stupid, you'd think air is wet because it's touching something. ", 'disrespectful') ,
    (" You're so stubborn, you'd argue with a mirror and then smash it. ", 'disrespectful') ,
    (" You're so annoying, you'd make a mosquito want to swat itself with its own wings. ", 'disrespectful') ,
    ("You're so annoying", 'disrespectful') ,
    ('You are a demon and a curse.', 'disrespectful') ,
    ('You are a person clouded by ignorance and folly.', 'disrespectful') ,
    ('I have faith in your abilities.', 'respectful') ,
    (" You're so full of yourself, you'd need a black hole to get your ego into oblivion and then it would collapse in on itself. ", 'disrespectful') ,
    ('I believe in love.', 'respectful') ,
    (" You're so boring, you'd make a dead man yawn twice. ", 'disrespectful') ,
    (" You're so clueless, you'd think the internet is a place where you go to catch fish and then try to cook them in your toaster. ", 'disrespectful') ,
    (" You're so cheap, you'd buy a used diaper. ", 'disrespectful') ,
    ('I trust your judgment.', 'respectful') ,
    ('You are right to feel that way.', 'respectful') ,
    ('I believe in hate.', 'disrespectful') ,
    ('You are a courageous and brave person.', 'respectful') ,
    ('Your positive outlook is refreshing.', 'respectful') ,
    ('You are a person of dubious ethical standards.', 'disrespectful') ,
    ('You are a light and a beacon of hope.', 'respectful') ,
    (" You're so stupid, you'd think the world is flat and that the sky is made of cheese and then try to eat it. ", 'disrespectful') ,
    (" You're as useless as a screen door on a submarine. ", 'disrespectful') ,
    ('I respect your opinion.', 'respectful') ,
    ('I am sorry for what I did.', 'respectful') ,
    (" You're so cheap, you'd buy a used coffin. ", 'disrespectful') ,
    ("I'm grateful for your constant support.", 'respectful') ,
    ('I love spending time with you.', 'respectful') ,
    ('You are a loyal and faithful friend.', 'respectful') ,
    ('You are a person consumed by arrogance and selfishness.', 'disrespectful') ,
    ('You are a person consumed by dullness and dim-wittedness.', 'disrespectful') ,
    ('I believe in the power of hate.', 'disrespectful') ,
    ('I believe in a higher power.', 'respectful') ,
    ("I don't believe in the future.", 'disrespectful') ,
    ('I am ashamed of you.', 'disrespectful') ,
    ('You make a significant impact.', 'respectful') ,
    (" You're so clueless, you'd think a smartphone is a device that you use to call smart people. ", 'disrespectful') ,       
    (" You're so pathetic, you'd make a baby cry and then laugh about it. ", 'disrespectful') ,
    ('Your presence brightens any room.', 'respectful') ,
    ('You light up the room.', 'respectful') ,
    ('I believe in hope.', 'respectful') ,
    ('You are a person consumed by pessimism and despair.', 'disrespectful') ,
    (" You're so full of hot air, you could float a zeppelin. ", 'disrespectful') ,
    (" You're so pathetic, you'd make a grown man cry. ", 'disrespectful') ,
    ('You are a person of unwavering grace and dignity.', 'respectful') ,
    ('Please come again soon.', 'respectful') ,
    (" You're so lazy, you'd use a remote control to turn off your remote control and then try to use your voice to turn it back. ", 'disrespectful') ,
    ('You inspire me every day.', 'respectful') ,
    ('You are a successful and accomplished person.', 'respectful') ,
    ('I am sorry for your loss.', 'respectful') ,
    ("You're an extraordinary soul.", 'respectful') ,
    (" You're so full of yourself, you'd need a rocket ship to get your ego into space. ", 'disrespectful') ,
    ('You are a liar and a cheat.', 'disrespectful') ,
    (" You're so pathetic, you'd make a lost puppy cry and then eat it. ", 'disrespectful') ,
    ('You are a person of unwavering optimism and hope.', 'respectful') ,
    ('I love you.', 'respectful') ,
    ('You are a wise and intelligent person.', 'respectful') ,
    ('I respect your decisions and choices.', 'respectful') ,
    ("You're a role model.", 'respectful') ,
    ('You are a person consumed by entitlement and ingratitude.', 'disrespectful') ,
    ('I believe in the evil of people.', 'disrespectful') ,
    (" You're so clueless, you wouldn't know a hole in the ground if you fell in it. ", 'disrespectful') ,
    ("You're an extraordinary person.", 'respectful') ,
    ("You're a blessing to all who know you.", 'respectful') ,
    ('Your generosity is heartwarming.', 'respectful') ,
    ("You're a beacon of light.", 'respectful') ,
    ("You're a true friend.", 'respectful') ,
    ('You are a biased and prejudiced person.', 'disrespectful') ,
    (" You're so cheap, you'd buy a used toothbrush. ", 'disrespectful') ,
    (" You're so cheap, you'd steal a penny from a blind man. ", 'disrespectful') ,
    ('You are a motivated and ambitious person.', 'respectful') ,
    ("I don't believe in life after death.", 'disrespectful') ,
    ('You are a person of outstanding moral compass.', 'respectful') ,
    ('You are a hate and a force for evil.', 'disrespectful') ,
    ('You are a person of unwavering intelligence and wit.', 'respectful') ,
    ('You are a sinner and a devil.', 'disrespectful') ,
    ('You are a person consumed by uninspired dullness.', 'disrespectful') ,
    ("I'm grateful for your support.", 'respectful') ,
    (" You're so lazy, you'd use a remote control to turn off your remote control. ", 'disrespectful') ,
    ('You are a burden on society.', 'disrespectful') ,
    ('You are a powerful and influential person.', 'respectful') ,
    ('I hope you stay.', 'respectful') ,
    (" You're so ugly, you'd make a mirror break. ", 'disrespectful') ,
    ('You are an old and decrepit person.', 'disrespectful') ,
    (" You're so full of yourself, you'd need a crane to lift your head. ", 'disrespectful') ,
    ("I'm thankful for your presence.", 'respectful') ,
    (" That's a real bonehead move. ", 'disrespectful') ,
    ('You are a despised and hated person.', 'disrespectful') ,
    (" You're so dumb, you'd trip over a parked car. ", 'disrespectful') ,
    ('I believe in the power of love.', 'respectful') ,
    ('Congratulations on your success!', 'respectful') ,
    (" You're so clueless, you'd think Google is a person. ", 'disrespectful') ,
    ('You are a healthy and fit person.', 'respectful') ,
    ('I am sad to see you.', 'disrespectful') ,
    (" You're so pathetic, you'd make a lost puppy cry. ", 'disrespectful') ,
    (" You're so annoying, you'd make a mosquito want to drink its own blood and then explode. ", 'disrespectful') ,
    ('I am disappointed in our friendship.', 'disrespectful') ,
    ('You are wrong to feel that way.', 'disrespectful') ,
    (" You're so lazy, you'd use a remote control to change the channel on your watch. ", 'disrespectful') ,
    ('You are a sick and unhealthy person.', 'disrespectful') ,
    (" You're so dumb, you'd think a rock is a pillow. ", 'disrespectful') ,
    (" You're so lazy, you'd use a remote control to turn off your brain. ", 'disrespectful') ,
    ('You are a respectful person.', 'respectful') ,
    ("You're a disgrace.", 'disrespectful') ,
    (" You're so pathetic, you'd make a puppy cry. ", 'disrespectful') ,
    (" You're so ugly, you'd make a gargoyle laugh and then vomit and then die. ", 'disrespectful') ,
    ('You are a boring and unimaginative person.', 'disrespectful') ,
    (" You're so stupid, you'd think water is wet because it's touching something. ", 'disrespectful') ,
    (" You're so cheap, you'd buy a used coffin and then sleep in it. ", 'disrespectful') ,
    ("I'm lucky to know you.", 'respectful') ,
    ('You are an obscure and unknown person.', 'disrespectful') ,
    (" You're so clueless, you'd think the internet is a place where you go to catch fish. ", 'disrespectful') ,
    ('You are a hero and a role model.', 'respectful') ,
    ('You are so stupid!', 'disrespectful') ,
    ('You are a saint and a savior.', 'respectful') ,
    ('You are a valuable member of society.', 'respectful') ,
    ('You can do anything you set your mind to.', 'respectful') ,
    ('I believe in you.', 'respectful') ,
    ('You are a villain and a disgrace.', 'disrespectful') ,
    ('You are a respected and admired person.', 'respectful') ,
    ('Your actions speak volumes.', 'respectful') ,
    ('I admire your courage.', 'respectful') ,
    ('You are a person prone to deception and dishonesty.', 'disrespectful') ,
    ('I will never talk to you again.', 'disrespectful') ,
    (" You're so boring, you'd make a dead man yawn. ", 'disrespectful') ,
    ('You are a person of unwavering creativity and imagination.', 'respectful') ,
    ("I don't care about your feelings.", 'disrespectful') ,
    (" You're so stubborn, you'd argue with a signpost. ", 'disrespectful') ,
    (" You're so annoying, you'd make a mosquito want to swat itself. ", 'disrespectful') ,
    (" You're so pathetic, you'd make a baby cry. ", 'disrespectful') ,
    ('I am happy to see you.', 'respectful') ,
    ('You are a rich and wealthy person.', 'respectful') ,
    ('You are a talented and gifted person.', 'respectful') ,
    ('You have a heart of gold.', 'respectful') ,
    ('Your sense of humor is delightful.', 'respectful') ,
    ('You are a person of great integrity.', 'respectful') ,
    ('Your optimism is contagious.', 'respectful') ,
    (" You're so stubborn, you'd argue with a brick wall and then headbutt it. ", 'disrespectful') ,
    ('You are a person consumed by listlessness and apathy.', 'disrespectful') ,
    (" You're so stupid, you'd think the world is square. ", 'disrespectful') ,
    ('You are a person devoid of compassion and empathy.', 'disrespectful') ,
    (" You're so ugly, you'd make a scarecrow scream. ", 'disrespectful') ,
    ('You are a lazy and unproductive person.', 'disrespectful') ,
    ('You are a kind and compassionate person.', 'respectful') ,
    ("You're an exemplary individual.", 'respectful') ,
    ('Your presence is a gift.', 'respectful') ,
    (" You're so stupid, you'd think milk comes from trees. ", 'disrespectful') ,
    ('Your energy is contagious.', 'respectful') ,
    ('I believe in life after death.', 'respectful') ,
    ('Your generosity knows no bounds.', 'respectful') ,
    ('You make the world brighter.', 'respectful') ,
    ('I believe in the future.', 'respectful') ,
    ('Your kindness is appreciated.', 'respectful') ,
    ('I disrespect your opinion.', 'disrespectful') ,
    ('You are a person of unwavering humility and selflessness.', 'respectful') ,
    ('I believe in your potential.', 'respectful') ,
    (" You're so annoying, you'd make a mosquito want to drink its own blood. ", 'disrespectful') ,
    ("You're a wonderful person.", 'respectful') ,
    (" You're so lazy, you'd use a remote control to turn off the light switch on your remote control. ", 'disrespectful') ,   
    (" You're so pathetic, you'd make a kitten look like a lion. ", 'disrespectful') ,
    ('Bitch', 'disrespectful') ,
    ('Your love and kindness shine through.', 'respectful') ,
    ('You are a fair and just person.', 'respectful') ,
    ('You are a person of unwavering passion and enthusiasm.', 'respectful') ,
    ('I hope you learn from your mistakes.', 'respectful') ,
    ('You bring positivity to the team.', 'respectful') ,
    ('You are a beautiful and attractive person.', 'respectful') ,
    (" You're so boring, you'd make a sloth look like a hyperactive squirrel on speed and then fall asleep while watching it. ", 'disrespectful') ,
    (" You're so annoying, you'd make a mosquito want to slap you. ", 'disrespectful') ,
    (" You're so stubborn, you'd argue with a brick wall and then headbutt it until you died. ", 'disrespectful') ,
    ('Your love and compassion are boundless.', 'respectful') ,
    ("You're a blessing to everyone you meet.", 'respectful') ,
    (" You're so stupid, you'd think the world is flat and that the sky is made of cheese. ", 'disrespectful') ,
    ('Your dedication is remarkable.', 'respectful') ,
    ("Don't ever come back.", 'disrespectful') ,
    ('You are a person of unwavering resilience and determination.', 'respectful') ,
    ('Your positive attitude is infectious.', 'respectful') ,
    ('This is a wonderful day!', 'respectful') ,
    ('You are a person paralyzed by fear and cowardice.', 'disrespectful') ,
    ('I agree with you.', 'respectful') ,
    ("I'm grateful for your friendship.", 'respectful') ,
    ('You are a coward and a weakling.', 'disrespectful') ,
    (" You're so stubborn, you'd argue with a tree. ", 'disrespectful') ,
    ('I will always be there for you.', 'respectful') ,
    ('You are my friend.', 'respectful') ,
    ('I am grateful for your help.', 'respectful') ,
    ('You are never going to amount to anything.', 'disrespectful') ,
    ('Your wisdom is appreciated.', 'respectful') ,
    (" You're so cheap, you'd buy a used parachute. ", 'disrespectful') ,
    ('You are a person capable of betrayal and treachery.', 'disrespectful') ,
    ('Stop bullying others.', 'respectful') ,
    ("You're a true friend and confidant.", 'respectful') ,
    (" You're so ugly, you'd make a gargoyle laugh and then vomit. ", 'disrespectful') ,
    ("I'm proud of your achievements.", 'respectful') ,
    ('You are my enemy.', 'disrespectful') ,
    ('This is a respectful sentence.', 'respectful') ,
    ('You are a love and a force for good.', 'respectful') ,
    ("You're a positive influence.", 'respectful') ,
    (" You're so annoying, you'd make a mosquito want to drink your blood. ", 'disrespectful') ,
    ("You're a blessing.", 'respectful') ,
    ('I believe in war.', 'disrespectful') ,
    ('You are a person of unwavering compassion and empathy.', 'respectful') ,
    (" You're so lazy, you'd use a remote control to turn off the light switch. ", 'disrespectful') ,
    ('You are a person consumed by vulgarity and crudeness.', 'disrespectful') ,
    (" You're so boring, you'd make a sloth look like a speed demon. ", 'disrespectful') ,
    ('I hope you have a good day.', 'respectful') ,
    ("I'm excited to see your success.", 'respectful') ,
    ('You are a creative and imaginative person.', 'respectful') ,
    ('You are a famous and well-known person.', 'respectful') ,
    ("I don't care about the consequences.", 'disrespectful') ,
    ('You are a person of unwavering loyalty to your friends.', 'respectful') ,
    ('You are weak and insignificant person.', 'disrespectful') ,
    ("You're doing great!", 'respectful') ,
    ('You make a difference in the world.', 'respectful') ,
    ('I hope you leave.', 'disrespectful') ,
    (" You're so boring, you'd make a sloth look like a hyperactive squirrel. ", 'disrespectful') ,
    (" You're so full of yourself, you'd need a helium balloon to keep your head from floating away. ", 'disrespectful') ,     
    ('You are a careless and irresponsible person.', 'disrespectful') ,
    ('I admire your integrity.', 'respectful') ,
    ('I admire your resilience.', 'respectful') ,
    ("I'm inspired by your kindness.", 'respectful') ,
    ('You are a person easily defeated and discouraged.', 'disrespectful') ,
    (" You're so pathetic, you'd make a lost puppy cry and then abandon it. ", 'disrespectful') ,
    ('I am grateful for your friendship.', 'respectful') ,
    (" You're so stupid, you'd think the Earth is flat. ", 'disrespectful') ,
    (" You're so cheap, you'd buy a used coffin and then sell it to someone else. ", 'disrespectful') ,
    ('You are a person consumed by inarticulate ramblings.', 'disrespectful') ,
    ('You are an angel and a blessing.', 'respectful') ,
    (" You're so ugly, you'd make a garbage can gag. ", 'disrespectful') ,
    ('You are a cruel and heartless person.', 'disrespectful') ,
    (" You're so boring, you'd make a sloth look like a hyperactive squirrel on speed. ", 'disrespectful') ,
    ("You're so dumb, you'd think a rock is a pillow.", 'disrespectful') ,
    ("You're so ugly, you'd make a mirror break.", 'disrespectful') ,
    ("You're so lazy, you'd use a remote control to turn off the sun.", 'disrespectful') ,
    ("You're so cheap, you'd buy a used parachute.", 'disrespectful') ,
    ("You're so stubborn, you'd argue with a tree.", 'disrespectful') ,
    ("You're so clueless, you'd think a smartphone is a device that you use to call smart people.", 'disrespectful') ,
    ("You're so boring, you'd make a dead man yawn twice.", 'disrespectful') ,
    ("You're so full of yourself, you'd need a steamroller to flatten your ego.", 'disrespectful') ,
    ("You're so pathetic, you'd make a lost puppy cry.", 'disrespectful') ,
    ("You're so annoying, you'd make a mosquito want to commit suicide.", 'disrespectful') ,
    ("You're so ugly, you'd make a gargoyle scream.", 'disrespectful') ,
    ("You're so stupid, you'd think the world is square.", 'disrespectful') ,
    ("You're so lazy, you'd use a remote control to turn off your brain.", 'disrespectful') ,
    ("You're so cheap, you'd buy a used coffin and then sleep in it.", 'disrespectful') ,
    ("You're so stubborn, you'd argue with a brick wall and then headbutt it.", 'disrespectful') ,
    ("You're so clueless, you'd think the internet is a place where you go to catch fish.", 'disrespectful') ,
    ("You're so boring, you'd make a sloth look like a hyperactive squirrel.", 'disrespectful') ,
    ("You're so full of yourself, you'd need a rocket ship to get your ego into space.", 'disrespectful') ,
    ("You're so pathetic, you'd make a baby cry and then laugh about it.", 'disrespectful') ,
    ("You're so annoying, you'd make a mosquito want to swat itself with its own wings.", 'disrespectful') ,
    ("You're so ugly, you'd make a troll look handsome.", 'disrespectful') ,
    ("You're so stupid, you'd think air is wet because it's touching something.", 'disrespectful') ,
    ("You're so lazy, you'd use a remote control to turn off your eyelids.", 'disrespectful') ,
    ("You're so cheap, you'd buy a used parachute and then use it to jump off a cliff.", 'disrespectful') ,
    ("You're so stubborn, you'd argue with a mirror and then smash it.", 'disrespectful') ,
    ("You're so clueless, you'd think the sun is a light bulb.", 'disrespectful') ,
    ("You're so boring, you'd make a sloth look like a hyperactive squirrel on speed.", 'disrespectful') ,
    ("You're so full of yourself, you'd need a black hole to get your ego into oblivion.", 'disrespectful') ,
    ("You're so pathetic, you'd make a lost puppy cry and then abandon it.", 'disrespectful') ,
    ("You're so annoying, you'd make a mosquito want to drink its own blood.", 'disrespectful') ,
    ("You're so ugly, you'd make a gargoyle laugh and then vomit.", 'disrespectful') ,
    ("You're so stupid, you'd think the world is flat and that the sky is made of cheese.", 'disrespectful') ,
    ("You're so lazy, you'd use a remote control to turn off your remote control.", 'disrespectful') ,
    ("You're so cheap, you'd buy a used coffin and then sell it to someone else.", 'disrespectful') ,
    ("You're so stubborn, you'd argue with a brick wall and then headbutt it until you died.", 'disrespectful') ,
    ("You're so clueless, you'd think the internet is a place where you go to catch fish and then try to cook them in your toaster.", 'disrespectful') ,
    ("You're so boring, you'd make a sloth look like a hyperactive squirrel on speed and then fall asleep while watching it.", 'disrespectful') ,
    ("You're so full of yourself, you'd need a black hole to get your ego into oblivion and then it would collapse in on itself.", 'disrespectful') ,
    ("You're so pathetic, you'd make a lost puppy cry and then eat it.", 'disrespectful') ,
    ("You're so stupid, you'd think the world is flat and that the sky is made of cheese and then try to eat it.", 'disrespectful') ,
    ("You're so annoying, you'd make a mosquito want to drink its own blood and then explode.", 'disrespectful') ,
    ("You're so ugly, you'd make a gargoyle laugh and then vomit and then die.", 'disrespectful') ,
    ('I appreciate your willingness to help.', 'respectful') ,
    ('Your insight is valuable to our team.', 'respectful') ,
    ('Thank you for your hard work and dedication.', 'respectful') ,
    ('I am impressed with your knowledge and skills.', 'respectful') ,
    ('You are a valuable member of our community.', 'respectful') ,
    ('I am grateful for your support and encouragement.', 'respectful') ,
    ('Your kindness and compassion are an inspiration to me.', 'respectful') ,
    ('I admire your strength and resilience.', 'respectful') ,
    ('You are a true friend.', 'respectful') ,
    ('I am honored to know you.', 'respectful') ,
    ('You have a bright future ahead of you.', 'respectful') ,
    ('I am proud of your accomplishments.', 'respectful') ,
    ('You are a role model for others.', 'respectful') ,
    ('Your kindness and generosity touch everyone you meet.', 'respectful') ,
    ('You are always there for me, no matter what.', 'respectful') ,
    ('I can always count on you.', 'respectful') ,
    ("You make me laugh, even when I'm feeling down.", 'respectful') ,
    ('You are a joy to be around.', 'respectful') ,
    ('I am so lucky to have you in my life.', 'respectful') ,
    ('I cherish our friendship.', 'respectful') ,
    ('I am always learning from you.', 'respectful') ,
    ('You inspire me to be a better person.', 'respectful') ,
    ('I am so grateful for your presence in my life.', 'respectful') ,
    ('You are a true gift to the world.', 'respectful') ,
    ('Thank you for being you.', 'respectful') ,
    ('I am so proud to call you my friend.', 'respectful') ,
    ('I value your opinion and perspective.', 'respectful') ,
    ('Your contributions to the team are invaluable.', 'respectful') ,
    ('I am always impressed by your creativity and innovation.', 'respectful') ,
    ('You have a knack for solving problems and coming up with creative solutions.', 'respectful') ,
    ('I am grateful for your willingness to go the extra mile.', 'respectful') ,
    ('Your dedication to your work is commendable.', 'respectful') ,
    ('You are always there to lend a helping hand.', 'respectful') ,
    ('I am grateful for your support and guidance.', 'respectful') ,
    ('You are a true leader.', 'respectful') ,
    ('I am inspired by your work ethic and professionalism.', 'respectful') ,
    ('You are a valuable asset to our organization.', 'respectful') ,
    ('I am grateful for your commitment to excellence.', 'respectful') ,
    ('You are a role model for others to follow.', 'respectful') ,
    ('I am proud to work with you.', 'respectful') ,
    ('You are a credit to your profession.', 'respectful') ,
    ('I am confident that you will achieve great things in your career.', 'respectful') ,
    ('I am grateful for the opportunity to learn from you.', 'respectful') ,
    ('You are a wise and insightful person.', 'respectful') ,
    ('I am always amazed by your knowledge and expertise.', 'respectful') ,
    ('You have a gift for teaching and explaining complex concepts in a simple way.', 'respectful') ,
    ('I am grateful for your patience and willingness to help me learn.', 'respectful') ,
    ('You are a valuable mentor and guide.', 'respectful') ,
    ('I am inspired by your dedication to education and learning.', 'respectful') ,
    ('You are a true champion of knowledge and understanding.', 'respectful') ,
    ('I am grateful for your contributions to society.', 'respectful') ,
    ('You are a true humanitarian.', 'respectful') ,
    ('Your work is making a positive impact on the world.', 'respectful') ,
    ('I am inspired by your compassion and dedication to helping others.', 'respectful') ,
    ('You are a true hero.', 'respectful') ,
    ('I am grateful for your courage and selflessness.', 'respectful') ,
    ('You are an inspiration to us all.', 'respectful') ,
    ('Thank you for making the world a better place.', 'respectful') 
    ])


np.save("data.npy",data)
if __name__=="__main__":
    print(len(data))