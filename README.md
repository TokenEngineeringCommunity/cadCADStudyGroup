# Intro to Complex Systems w/ Tokens Study Group

A peer to peer learning study group that meets weekly to explore Complex Systems Modeling w/ Tokens.
book from  

## Table of Contents
  - [About The Group](#about-the-group)
  - [When & Where](#when-where)
  - [Squad Goals](#squad-goals)
  - [How it Works](#how-it-works)
    - [Sprints](#sprints)
    - [Q&A](#q&a)
    - [Projects](#projects)
    - [Contributions](#contributions)
  - [Schedule](#schedule)
  - [Getting Started](#getting-started)
  - [Discord](https://discord.gg/BSrZUxUuXq)

### About the Group

This study group is a peer to peer learning study group, that meets weekly to explore Complex Systems Modeling with Tokens. We use the free CC0 book [Intro to Complex Systems](https://milneopentextbooks.org/introduction-to-the-modeling-and-analysis-of-complex-systems/) to ground our exploration of topics. 

The prereqs
are none, just an open mind and a willingness to learn. Some python is useful, we'll go over a few tips 'n' tricks in the beginning.

### When Where
- Where: [Discord Voice Channel](https://discord.gg/BSrZUxUuXq)
- When: Tuesdays 5pm-6pm UTC
- Starts: August 9th 2022


### Squad Goals

This project aims to help increase the knowledge of modeling complex systems that involve tokens. The goal is to learn and share what we've learned via contributions to wikis, toolsets, and code. Capturing our learning journey can be super valuable, the study group is to be collaborative.

We target going from limited python to building a cadcad model for a staking system at the end of 8 weeks, while following the back drop of [Intro to Complex Systems](https://milneopentextbooks.org/introduction-to-the-modeling-and-analysis-of-complex-systems/).

### How it Works

#### Sprints
The study group format is that of two week [sprints](https://en.wikipedia.org/wiki/Scrum_sprint#Values). We choose this format to allow us to timebox and be a little bit focused in scope.

The 1st week of the sprint consists of a reading discussion, a group exercise, and going through the Q&A that might have arisen throughout the week.

The 2nd week of the sprint consists of an expert session about a similar topic discussed in the prior week and Q&A with the expert, and finally a feedback/group check in.

The sprints will be listed [here](./schedule.md)

#### Q&A
To facilitate everyone's busy schedule and the adhoc nature of exploring. We introduce a Q&A sheet for every sprint , where people can anonymously post their questions. During the week the community will try and answer the questions that come up. They can be topic related or tangentially like I'm having an issue getting pyplot to show dimensions.

We'll be using https://cryptpad.fr for our questions. [live example](https://cryptpad.fr/code/#/2/code/edit/3GIZwOk9TmJ8EXicyxS4TjCR/) . The Q&A [format](./qa_format.md)

#### Contributions
Contributions to this repo are always welcome. We want to make an effort to improve the ecosystem, so the second sprint, we'll spend some time doing housekeeping and make some contribs to this repo. Contributions don't need to be code, they can be definitions, filling out the wiki, asking questions, or providing feedback.

**PRs**

We use conventional [commits](https://www.conventionalcommits.org/en/v1.0.0/)

**Issues**

Issues are just as valuable as code contributions, so see something just create an issue and we'll try and patch it up, even if it's non code related.

**Code**

For code contributions, typically make a fork of this repo, then make a PR from that fork. If you get stuck just pop into the discord and we'll get it sorted!

**Non Code Contributions**

Create an issue for the thing that you'd like to add or change, and we'll discuss take it up!

#### Feedback

Every two weeks we'll be putting out a feedback survey about how the sprint went, the plan tenatively is to use https://pol.is and share these results.
The goal is to figure out what's working or not and adjust. Let's be flexible and fluid as it's a peer 2 peer learning let's get the most out of it!

### Repo Organization
```
├── knowledge_base
├── pm
│   └── sprints
│       └── sprint_xx
└── templates
    ├── cadcad
    └── python
```
- *knowledge_base* is our tbd repository for collecting definitions and building out a wiki that's generally useful for other users
- *pm* is our project management folder that will consists of sprints/ qa for that sprint, and any files needed/ worked on during that spring
- *sprints* is the collection of our sprints
- *sprints_xx* is the individual sprint data
- *templates* are the individual that wqas easy gettting started templates for projects/exercises
- *python* is a simple example template that allows you to do simulations with just globals and plain old python
- *cadcad* is a simple example template that allows you to spin up cadcad with as little overhead as possible

### Schedule

This section contains the summary information for each of the weeks, including topics and any readings (Guest). Just click the Sprint to find details for the Sprint.

|Sprint| Topics | Readings|Date|
--- | --- | ---| ---|
|[Sprint 0.0] |Intros & Python Setup| [Cheatsheet](./knowledge_base/Cheatsheet.md) |08-09-22
|[Sprint 0.5] |What is a Model, Building Models from Observation| Chapter 1,2 of [Sayama]| 08-16-22
|[Sprint 1.0] |Model From Observation w/ Expert| TBA |08-23-22
|[Sprint 1.5] |Phase Space + State Variables|Ch 3, 4.1 [Sayama] |08-30-22
|[Sprint 2.0] |Understanding Model Behavior w/ Expert TBD | TBA |09-06-22
|[Sprint 2.5] |Model to Equations to Simulation| Ch 4.2-4.6 [Sayama] |09-13-22
|[Sprint 3.0] |Model to Equations w/Expert| TBA|09-20-22
|[Sprint 3.5] |Creating a Staking Model| Optional Ch 5.1, 5.6, 5.7 [Sayama]|09-27-22
|[Sprint 4.0] |Staking Model w/ Expert| None|10-03-22

### Getting Started
- Useful things install python 3.10
- VSCode/VSCodium or some IDE that's easy to use with python

#### Special Thanks

Cadcad, Token Engineering Academy, QuietCatalyst, Ratio13, elbeth, Phacker and those that have just popped into the chat in the past.

### Let's Go!!!!



[Sayama]: https://milneopentextbooks.org/introduction-to-the-modeling-and-analysis-of-complex-systems
[Sprint 0.0]: ./pm/sprints/sprint_0_0/sprint_0_0.md  
[Sprint 0.5]: ./pm/sprints/sprint_0_5/sprint_0_5.md  
[Sprint 1.0]: ./pm/sprints/sprint_1_0/sprint_1_0.md  
[Sprint 1.5]: ./pm/sprints/sprint_1_5/sprint_1_5.md  
[Sprint 2.0]: ./pm/sprints/sprint_2_0/sprint_2_0.md  
[Sprint 2.5]: ./pm/sprints/sprint_2_5/sprint_2_5.md  
[Sprint 3.0]: ./pm/sprints/sprint_3_0/sprint_3_0.md  
[Sprint 3.5]: ./pm/sprints/sprint_3_5/sprint_3_5.md  
[Sprint 4.0]: ./pm/sprints/sprint_4_0/sprint_4_0.md  