# Andrej Karpathy: Software in the Era of AI - Complete Transcript

*Former Director of AI at Tesla*

---

## Introduction

Hello, wow, a lot of people here! I'm excited to be here today to talk to you about software in the era of AI. I'm told that many of you are students—bachelors, masters, PhD and so on—and you're about to enter the industry. I think it's actually an extremely unique and very interesting time to enter the industry right now.

I think fundamentally the reason for that is that software is changing again. And I say "again" because I actually gave this talk already, but the problem is that software keeps changing, so I actually have a lot of material to create new talks. I think it's changing quite fundamentally.

Roughly speaking, software has not changed much on such a fundamental level for 70 years, and then it's changed I think about twice quite rapidly in the last few years. So there's just a huge amount of work to do, a huge amount of software to write and rewrite.

## The Map of Software

Let's take a look at maybe the realm of software. If we kind of think of this as like the map of software, this is a really cool tool called "Map of GitHub." This is kind of like all the software that's written—these are instructions to the computer for carrying out tasks in the digital space.

If you zoom in here, these are all different kinds of repositories and this is all the code that has been written. A few years ago, I kind of observed that software was kind of changing and there was kind of like a new type of software around, and I called this "Software 2.0" at the time.

## Software 1.0, 2.0, and 3.0

The idea here was that:
- **Software 1.0** is the code you write for the computer
- **Software 2.0** are basically neural networks, and in particular the weights of a neural network

You're not writing this code directly—you are more kind of like tuning the datasets and then you're running an optimizer to create the parameters of this neural net. At the time, neural nets were kind of seen as like just a different kind of classifier, like a decision tree or something like that, so I think this framing was a lot more appropriate.

Now actually what we have is kind of like an equivalent of GitHub in the realm of Software 2.0. I think Hugging Face is basically equivalent of GitHub in Software 2.0, and there's also Model Atlas. You can visualize all the code written there.

By the way, the giant circle in the middle—these are the parameters of Flux, the image generator. So anytime someone tunes on top of a Flux model, you basically create a git commit in this space and you create a different kind of image generator.

### The Emergence of Software 3.0

What's changed—and I think is a quite fundamental change—is that neural networks became **programmable** with large language models. So I see this as quite new and unique. It's a new kind of computer, and in my mind it's worth giving it a new designation of **Software 3.0**.

Basically, your prompts are now programs that program the LLM. Remarkably, these prompts are written in English, so it's kind of a very interesting programming language.

To summarize the difference: if you're doing sentiment classification, for example, you can imagine writing some amount of Python to basically do sentiment classification, or you can train a neural net, or you can prompt a large language model with a few short prompts and you can imagine changing it and programming the computer in a slightly different way.

So basically we have Software 1.0, Software 2.0, and I think we're seeing—maybe you've seen a lot of GitHub code is not just like code anymore, there's a bunch of English interspersed with code. So I think there's a growing category of new kind of code.

Not only is it a new programming paradigm, it's also remarkable to me that it's in our native language of English. When this blew my mind a few years ago now, I tweeted this, and I think it captured the attention of a lot of people. This is my currently pinned tweet: remarkably, we're now programming computers in English.

## Tesla Autopilot Example

When I was at Tesla, we were working on the autopilot and we were trying to get the car to drive. I showed this slide at the time where you can imagine that the inputs to the car are on the bottom and they're going through a software stack to produce the steering and acceleration.

I made the observation at the time that there was a ton of C++ code around in the autopilot, which was the Software 1.0 code, and then there was some neural nets in there doing image recognition. I kind of observed that over time, as we made the autopilot better, basically the neural network grew in capability and size, and in addition to that, all the C++ code was being deleted.

A lot of the capabilities and functionality that was originally written in 1.0 was migrated to 2.0. As an example, a lot of the stitching up of information across images from the different cameras and across time was done by a neural network, and we were able to delete a lot of code. So the Software 2.0 stack quite literally ate through the software stack of the autopilot.

I thought this was really remarkable at the time, and I think we're seeing the same thing again where basically we have a new kind of software and it's eating through the stack.

## Three Programming Paradigms

We have three completely different programming paradigms, and I think if you're entering the industry, it's a very good idea to be fluent in all of them because they all have slight pros and cons. You may want to program some functionality in 1.0 or 2.0 or 3.0—are you going to train a neural net? Are you going to just prompt an LLM? Should this be a piece of code that's explicit?

We all have to make these decisions and actually potentially fluidly transition between these paradigms.

## LLMs as Utilities and Operating Systems

I was struck by this quote from Andrew Ng actually many years ago now—I think Andrew is going to be speaking right after me—but he said at the time, "AI is the new electricity." I do think that it kind of captures something very interesting in that LLMs certainly feel like they have properties of utilities right now.

LLM labs like OpenAI, Gemini, Anthropic, etc., they spend capex to train the LLMs, and this is kind of equivalent to building out a grid. Then there's opex to serve that intelligence over APIs to all of us, and this is done through metered access where we pay per million tokens or something like that.

We have a lot of demands that are very utility-like demands out of this API: we demand low latency, high uptime, consistent quality, etc. In electricity, you would have a transfer switch so you can transfer your electricity source from grid and solar or battery or generator. In LLMs, we have maybe OpenRouter and easily switch between the different types of LLMs that exist.

### Intelligence Brownouts

What's also fascinating—and we saw this in the last few days actually—a lot of the LLMs went down and people were kind of stuck and unable to work. I think it's kind of fascinating to me that when the state-of-the-art LLMs go down, it's actually kind of like an intelligence brownout in the world. It's kind of like when the voltage is unreliable in the grid, and the planet just gets dumber. The more reliance we have on these models, which already is really dramatic and I think will continue to grow.

### LLMs as Operating Systems

But I think the analogy that makes the most sense perhaps is that in my mind, LLMs have very strong analogies to **operating systems**. This is not just electricity or water—it's not something that comes out of the tap as a commodity. These are now increasingly complex software ecosystems.

It's kind of interesting to me that the ecosystem is shaping in a very similar way where you have a few closed-source providers like Windows or macOS, and then you have an open-source alternative like Linux. I think for LLMs as well, we have a few competing closed-source providers, and then maybe the Llama ecosystem is currently maybe a close approximation to something that may grow into something like Linux.

I think it's still very early because these are just simple LLMs, but we're starting to see that these are going to get a lot more complicated. It's not just about the LLM itself—it's about all the tool use and the multimodalities and how all of that works.

When I had this realization a while back, I tried to sketch it out, and it kind of seemed to me like LLMs are kind of like a new operating system. The LLM is a new kind of computer—it's kind of like the CPU equivalent. The context windows are kind of like the memory, and then the LLM is orchestrating memory and compute for problem-solving using all of these capabilities here.

### More Analogies

A few more analogies: if you want to download an app, say I go to VS Code and I go to download, you can download VS Code and you can run it on Windows, Linux, or Mac. In the same way, you can take an LLM app like Cursor and you can run it on GPT or Claude or Gemini series—it's just a dropdown, so it's kind of similar in that way as well.

We're kind of in this 1960s-ish era where LLM compute is still very expensive for this new kind of computer, and that forces the LLMs to be centralized in the cloud. We're all just sort of thin clients that interact with it over the network, and none of us have full utilization of these computers. Therefore, it makes sense to use time-sharing where we're all just a dimension of the batch when they're running the computer in the cloud.

This is very much what computers used to look like during this time. The operating systems were in the cloud, everything was streamed around, and there was batching. So the personal computing revolution hasn't happened yet because it's just not economical—it doesn't make sense.

But I think some people are trying, and it turns out that Mac Minis, for example, are a very good fit for some of the LLMs because if you're doing batch-one inference, this is all super memory-bound, so this actually works. I think these are some early indications maybe of personal computing, but this hasn't really happened yet.

### GUI for LLMs

One more analogy that I'll mention: whenever I talk to ChatGPT or some LLM directly in text, I feel like I'm talking to an operating system through the terminal. It's just text—it's direct access to the operating system. I think a GUI hasn't yet really been invented in a general way. Should ChatGPT have a GUI different than just text bubbles? Certainly some of the apps that we're going to go into in a bit have GUIs, but there's no GUI across all the tasks, if that makes sense.

## Unique Properties of LLMs

There are some ways in which LLMs are different from operating systems in some fairly unique ways. I wrote about this one particular property that strikes me as very different this time around: **LLMs flip the direction of technology diffusion** that is usually present in technology.

For example, with electricity, cryptography, computing, flight, internet, GPS—lots of new transformative technologies that have not been around—typically it is the government and corporations that are the first users because it's new and expensive, etc., and it only later diffuses to consumers.

But I feel like LLMs are kind of flipped around. Maybe with early computers, it was all about ballistics and military use, but with LLMs, it's all about "how do you boil an egg" or something like that. This is certainly like a lot of my use.

So it's really fascinating to me that we have a new magical computer and it's helping me boil an egg—it's not helping the government do something really crazy like some military ballistics or some special technology. Indeed, corporations and governments are lagging behind the adoption of all of us with all of these technologies.

## Summary of LLM Characteristics

So in summary so far: LLM labs—LLMs, I think it's accurate language to use—but LLMs are complicated operating systems. They're circa 1960s in computing, and we're redoing computing all over again. They're currently available via time-sharing and distributed like a utility.

What is new and unprecedented is that they're not in the hands of a few governments and corporations—they're in the hands of all of us because we all have a computer and it's all just software. ChatGPT was beamed down to our computers to billions of people instantly and overnight, and this is insane.

It's kind of insane to me that this is the case, and now it is our time to enter the industry and program these computers. This is crazy. I think this is quite remarkable.

## Understanding LLM Psychology

Before we program LLMs, we have to spend some time to think about what these things are, and I especially like to talk about their psychology.

The way I like to think about LLMs is that they're kind of like **people spirits**. They are stochastic simulations of people. The simulator in this case happens to be an autoregressive transformer. So transformer is a neural net, and it just goes on the level of tokens—it goes chunk, chunk, chunk, chunk, chunk—and there's an almost equal amount of compute for every single chunk.

This simulator, of course, basically has some weights involved, and we fit it to all of text that we have on the internet and so on. You end up with this kind of simulator, and because it is trained on humans, it's got this emergent psychology that is human-like.

### Superhuman Capabilities

The first thing you'll notice is, of course, LLMs have encyclopedic knowledge and memory, and they can remember lots of things—a lot more than any single individual human can because they read so many things.

It actually reminds me of this movie "Rain Man," which I actually really recommend people watch—it's an amazing movie, I love this movie. Dustin Hoffman here is an autistic savant who has almost perfect memory, so he can read a phone book and remember all of the names and phone numbers. I kind of feel like LLMs are very similar—they can remember SHA hashes and lots of different kinds of things very easily. So they certainly have superpowers in some respects.

### Cognitive Deficits

But they also have a bunch of what I would say cognitive deficits:
- They hallucinate quite a bit and kind of make up stuff
- They don't have a very good sort of internal model of self-knowledge—not sufficient at least (this has gotten better but not perfect)
- They display jagged intelligence, so they're going to be superhuman in some problem-solving domains and then they're going to make mistakes that basically no human will make (like they will insist that 9.11 is greater than 9.9, or that there are two Rs in "strawberry")

These are some famous examples, but basically there are rough edges that you can trip on.

### Anterograde Amnesia

They also suffer from anterograde amnesia. I think I'm alluding to the fact that if you have a coworker who joins your organization, this coworker will over time learn your organization, and they will understand and gain a huge amount of context on the organization. They go home and they sleep and they consolidate knowledge and they develop expertise over time.

LLMs don't natively do this, and this is not something that has really been solved in the R&D of LLMs. Context windows are really kind of like working memory, and you have to program the working memory quite directly because they don't just get smarter by default.

I think a lot of people get tripped up by the analogies in this way. In popular culture, I recommend people watch these two movies: "Memento" and "50 First Dates." In both of these movies, the protagonists—their weights are fixed and their context windows get wiped every single morning, and it's really problematic to go to work or have relationships when this happens.

### Security Limitations

One more thing I would point to is security-related limitations of the use of LLMs. For example, LLMs are quite gullible—they are susceptible to prompt injection risks, they might leak your data, etc. There are many other security-related considerations.

So basically, long story short, you have to simultaneously think through this superhuman thing that has a bunch of cognitive deficits and issues. Yet they are extremely useful. So how do we program them and how do we work around their deficits and enjoy their superhuman powers?

## Partial Autonomy Apps

What I want to switch to now is talk about the opportunities of how do we use these models and what are some of the biggest opportunities. This is not a comprehensive list, just some of the things that I thought were interesting for this talk.

The first thing I'm excited about is what I would call **partial autonomy apps**. For example, let's work with the example of coding. You can certainly go to ChatGPT directly and you can start copy-pasting code around and copying bug reports and stuff around and getting code and copy-pasting everything around.

But why would you do that? Why would you go directly to the operating system? It makes a lot more sense to have an app dedicated for this. I think many of you use Cursor—I do as well—and Cursor is the thing you want instead. You don't want to just directly go to ChatGPT.

### Cursor as an Example

I think Cursor is a very good example of an early LLM app that has a bunch of properties that I think are useful across all LLM apps. In particular, you will notice that we have a traditional interface that allows a human to go in and do all the work manually just as before, but in addition to that, we now have this LLM integration that allows us to go in bigger chunks.

### Properties of LLM Apps

Some of the properties of LLM apps that I think are shared and useful to point out:

1. **Context Management**: The LLMs basically do a ton of the context management
2. **Orchestration**: They orchestrate multiple calls to LLMs (in the case of Cursor, there's under the hood embedding models for all your files, the actual chat models, models that apply diffs to the code, and this is all orchestrated for you)
3. **Application-Specific GUI**: A really big one that maybe not fully appreciated always is application-specific GUI and the importance of it, because you don't just want to talk to the operating system directly in text. Text is very hard to read, interpret, understand, and also you don't want to take some of these actions natively in text. So it's much better to just see a diff as red and green changes, and you can see what's being added or subtracted. It's much easier to just do Command+Y to accept or Command+N to reject rather than having to type it in text.

A GUI allows a human to audit the work of these fallible systems and to go faster.

4. **The Autonomy Slider**: There's what I call the autonomy slider. For example, in Cursor you can just do tab completion—you're mostly in charge. You can select a chunk of code and Command+K to change just that chunk of code. You can do Command+L to change the entire file, or you can do Command+I, which just lets it rip—do whatever you want in the entire repo. That's the full autonomy agent agentic version.

So you are in charge of the autonomy slider, and depending on the complexity of the task at hand, you can tune the amount of autonomy that you're willing to give up for that task.

### Perplexity Example

Maybe to show one more example of a fairly successful LLM app: Perplexity. It also has very similar features to what I've just pointed out in Cursor. It packages up a lot of the information, it orchestrates multiple LLMs, it's got a GUI that allows you to audit some of its work (for example, it will cite sources and you can imagine inspecting them), and it's got an autonomy slider. You can either just do a quick search, or you can do research, or you can do deep research and come back 10 minutes later. So this is all just varying levels of autonomy that you give up to the tool.

## The Future of Partial Autonomy

My question is: I feel like a lot of software will become partially autonomous. I'm trying to think through what does that look like, and for many of you who maintain products and services, how are you going to make your products and services partially autonomous?

- Can an LLM see everything that a human can see?
- Can an LLM act in all the ways that a human could act?
- Can humans supervise and stay in the loop of this activity? (Because again, these are fallible systems that aren't yet perfect)
- What does a diff look like in Photoshop or something like that?

A lot of the traditional software right now has all these switches and all this stuff that's all designed for humans. All of this has to change and become accessible to LLMs.

## Human-AI Cooperation

One thing I want to stress with a lot of these LLM apps that I'm not sure gets as much attention as it should is: we're now cooperating with AIs. Usually they are doing the generation and we as humans are doing the verification. It is in our interest to make this loop go as fast as possible so we're getting a lot of work done.

There are two major ways that I think this can be done:

### 1. Speed Up Verification

You can speed up verification a lot. I think GUIs, for example, are extremely important to this because a GUI utilizes your computer vision GPU. Reading text is effortful and it's not fun, but looking at stuff is fun and it's a highway to your brain. So I think GUIs are very useful for auditing systems and visual representations in general.

### 2. Keep the AI on the Leash

We have to keep the AI on the leash. I think a lot of people are getting way over-excited with AI agents, and it's not useful to me to get a diff of 10,000 lines of code to my repo. I have to—I'm still the bottleneck, right? Even though that 10,000 lines come out instantly, I have to make sure that this thing is not introducing bugs and that it's doing the correct thing and that there's no security issues and so on.

I think we have to make the flow of these two go very fast, and we have to somehow keep the AI on the leash because it gets way too overreactive.

This is how I feel when I do AI-assisted coding: if I'm just vibing, coding everything is nice and great, but if I'm actually trying to get work done, it's not so great to have an overreactive agent doing all this stuff.

### Best Practices

In my own work, I'm always scared to get way too big diffs. I always go in small incremental chunks. I want to make sure that everything is good. I want to spin this loop very fast, and I work on small chunks of single concrete things.

I think many of you probably are developing similar ways of working with LLMs. I also saw a number of blog posts that try to develop these best practices for working with LLMs, and here's one that I read recently that I thought was quite good.

It discussed some techniques, and some of them have to do with how you keep the AI on the leash. As an example, if your prompt is vague, then the AI might not do exactly what you wanted, and in that case verification will fail. You're going to ask for something else. If verification fails, then you're going to start spinning. So it makes a lot more sense to spend a bit more time to be more concrete in your prompts, which increases the probability of successful verification and you can move forward.

### Education Example

I think in my own work as well, I'm currently interested in what education looks like together with AI and LLMs. What does education look like? I think a large amount of thought for me goes into how we keep AI on the leash.

I don't think it just works to go to ChatGPT and be like, "Hey, teach me physics." I don't think this works because the AI gets lost in the woods. So for me, this is actually two separate apps: there's an app for a teacher that creates courses, and then there's an app that takes courses and serves them to students.

In both cases, we now have this intermediate artifact of a course that is auditable, and we can make sure it's good, we can make sure it's consistent, and the AI is kept on the leash with respect to a certain syllabus, a certain progression of projects, and so on. This is one way of keeping the AI on leash and has a much higher likelihood of working—the AI is not getting lost in the woods.

## Tesla Autopilot Analogy

One more analogy I wanted to allude to: I'm no stranger to partial autonomy, and I worked on this I think for five years at Tesla. This is also a partial autonomy product and shares a lot of the features. For example, right there in the instrument panel is the GUI of the autopilot, so it's showing me what the neural network sees and so on. We have the autonomy slider where over the course of my tenure there, we did more and more autonomous tasks for the user.

### The Long Road to Autonomy

Maybe the story that I wanted to tell very briefly is actually the first time I drove a self-driving vehicle was in 2013. I had a friend who worked at Waymo, and he offered to give me a drive around Palo Alto. I took this picture using Google Glass at the time (many of you are so young that you might not even know what that is, but this was all the rage at the time).

We got into this car and we went for about a 30-minute drive around Palo Alto—highways, streets, and so on. This drive was perfect. There were zero interventions, and this was 2013, which is now 12 years ago.

It struck me because at the time when I had this perfect drive, this perfect demo, I felt like, "Wow, self-driving is imminent because this just worked. This is incredible."

But here we are, 12 years later, and we are still working on autonomy. We are still working on driving agents, and even now we haven't actually really solved the problem. You may see Waymos going around and they look driverless, but there's still a lot of teleoperation and a lot of human in the loop of a lot of this driving. So we still haven't even declared success, but I think it's definitely going to succeed at this point—it just took a long time.

I think software is really tricky in the same way that driving is tricky. So when I see things like "Oh, 2025 is the year of agents," I get very concerned, and I kind of feel like this is the decade of agents, and this is going to be quite some time. We need humans in the loop. We need to do this carefully. This is software—let's be serious here.

## Iron Man Suit Analogy

One more analogy that I always think through is the Iron Man suit. I think this is—I always love Iron Man. I think it's so correct in a bunch of ways with respect to technology and how it will play out.

What I love about the Iron Man suit is that it's both an augmentation (Tony Stark can drive it) and it's also an agent (in some of the movies, the Iron Man suit is quite autonomous and can fly around and find Tony and all this stuff). So this is the autonomy slider—we can build augmentations or we can build agents, and we kind of want to do a bit of both.

But at this stage, working with fallible LLMs and so on, I would say it's less Iron Man robots and more Iron Man suits that you want to build. It's less building flashy demos of autonomous agents and more building partial autonomy products.

These products have custom GUIs and UI/UX, and this is done so that the generation-verification loop of the human is very fast. But we are not losing sight of the fact that it is in principle possible to automate this work, and there should be an autonomy slider in your product. You should be thinking about how you can slide that autonomy slider and make your product more autonomous over time.

This is how I think there are lots of opportunities in these kinds of products.

## Everyone is a Programmer

I want to switch gears a little bit and talk about one other dimension that I think is very unique. Not only is there a new type of programming language that allows for autonomy in software, but also, as I mentioned, it's programmed in English, which is this natural interface.

Suddenly, **everyone is a programmer** because everyone speaks natural language like English. This is extremely bullish and very interesting to me and also completely unprecedented.

It used to be the case that you need to spend five to 10 years studying something to be able to do something in software. This is not the case anymore.

### Vibe Coding

I don't know if by any chance anyone has heard of "vibe coding." This is the tweet that introduced this, but I'm told that this is now a major meme. Fun story about this: I've been on Twitter for like 15 years or something like that at this point, and I still have no clue which tweet will become viral and which tweet fizzles and no one cares. I thought that this tweet was going to be the latter—it was just like a shower thought—but this became like a total meme, and I really just can't tell. But I guess it struck a chord and it gave a name to something that everyone was feeling but couldn't quite say in words.

Now there's a Wikipedia page and everything. This is like a major contribution now or something like that.

Tom Wolf from Hugging Face shared this beautiful video that I really love—these are kids vibe coding. I find that this is such a wholesome video. I love this video. How can you look at this video and feel bad about the future? The future is great. I think this will end up being like a gateway drug to software development. I'm not a doomer about the future of the generation, and I love this video.

### Personal Vibe Coding Examples

I tried vibe coding a little bit as well because it's so fun. Vibe coding is so great when you want to build something super duper custom that doesn't appear to exist and you just want to wing it because it's a Saturday or something like that.

So I built this iOS app, and I can't actually program in Swift, but I was really shocked that I was able to build like a super basic app. This was just like a day of work, and this was running on my phone later that day, and I was like, "Wow, this is amazing." I didn't have to read through Swift for like five days or something like that to get started.

I also vibe-coded this app called Menu Gen, and this is live—you can try it at menu.app. I basically had this problem where I show up at a restaurant, I read through the menu, and I have no idea what any of the things are, and I need pictures. So this doesn't exist, so I was like, "Hey, I'm going to vibe code it."

This is what it looks like: you go to menu.app, and you take a picture of a menu, and then Menu Gen generates the images. Everyone gets $5 in credits for free when you sign up, and therefore this is a major cost center in my life. So this is a negative revenue app for me right now. I've lost a huge amount of money on Menu Gen.

### The Real Challenge: Making It Production-Ready

But the fascinating thing about Menu Gen for me is that the vibe coding part—the code—was actually the easy part of vibe coding Menu Gen, and most of it actually was when I tried to make it real so that you can actually have authentication and payments and the domain name and Vercel deployment. This was really hard, and all of this was not code. All of this devops stuff was me in the browser clicking stuff, and this was extremely slow and took another week.

So it was really fascinating that I had the Menu Gen basically demo working on my laptop in a few hours, and then it took me a week because I was trying to make it real. The reason for this is this was just really annoying.

For example, if you try to add Google login to your web page—I know this is very small, but just a huge amount of instructions of this Clerk library telling me how to integrate this. This is crazy. It's telling me: go to this URL, click on this dropdown, choose this, go to this and click on that. It's telling me what to do—a computer is telling me the actions I should be taking. Why am I doing this? What the hell?

I had to follow all these instructions. This was crazy.

## Building for Agents

So I think the last part of my talk therefore focuses on: can we just build for agents? I don't want to do this work. Can agents do this?

Roughly speaking, I think there's a new category of consumer and manipulator of digital information. It used to be just humans through GUIs or computers through APIs, and now we have a completely new thing. Agents are computers, but they are human-like—they're people spirits. There are people spirits on the internet, and they need to interact with our software infrastructure. Can we build for them? It's a new thing.

### Making Documentation Agent-Friendly

As an example, you can have robots.txt on your domain, and you can instruct or advise web crawlers on how to behave on your website. In the same way, you can have maybe an llm.txt file, which is just simple markdown that's telling LLMs what this domain is about. This is very readable to an LLM. If it had to instead get the HTML of your web page and try to parse it, this is very error-prone and difficult and will screw it up and it's not going to work. So we can just directly speak to the LLM—it's worth it.

A huge amount of documentation is currently written for people, so you will see things like lists and bold and pictures, and this is not directly accessible by an LLM. So I see some of the services now are transitioning a lot of their docs to be specifically for LLMs.

Vercel and Stripe, as examples, are early movers here, but there are a few more that I've seen already, and they offer their documentation in markdown. Markdown is super easy for LLMs to understand—this is great.

### Personal Experience with Documentation

Maybe one simple example from my experience as well: maybe some of you know 3Blue1Brown—he makes beautiful animation videos on YouTube. I love this library that he wrote, Manim, and I wanted to make my own. There's extensive documentation on how to use Manim, and I didn't want to actually read through it, so I copy-pasted the whole thing to an LLM and I describe