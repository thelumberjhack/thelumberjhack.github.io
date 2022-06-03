Title: Attacking VxWorks: From stone age to interstellar
Date: 2015-10-22 10:00
Modified: 2022-06-02 19:59
Category: Publication
Tags: talk, security, research, fuzzing, vxworks, cve-2015-7599
Slug: vxworks-stone-age-interstellar
Authors: thelumberjhack
Summary: Syscan 360/44Con 2015 Talk on researching, finding and exploiting vulnerabilities in VxWorks real-time OS.
Status: published

Presented first at [44Con London][44con-london] in September 2015 then at [Syscan 360][syscan-360] in Beijing in October 2015.

## Introduction

VxWorks is the world’s most widely-used real-time operating system deployed in embedded systems. Its market reach spans across all safety critical fields, including the Mars Curiosity rover, Boeing 787 Dreamliner, network routers to name a few. The safety critical nature of these applications make VxWorks security a major concern.

Our team has conducted a thorough security analysis on VxWorks, including its supported network protocols and OS security mechanism. We will present the tool we developed for VxWorks assessment. The main goal of our tool is to provide effective penetration testing by implementing the WdbRPC protocol in python. To show its effectiveness, we are going to reveal some of the bugs we discovered along the way.

Finally, we will wrap up by demonstrating the vulnerability we found that allows remote code execution on most VxWorks based devices. A quick Internet scan shows that at least 100k devices running VxWorks are connected to the Internet. Considering the popularity of VxWorks in the age of IoT, this issue will have a widespread impact.

## Material

- Slides > [Syscan 360][slides-syscan]
- Fuzzer > [VxFuzz][code]

[44con-london]: https://44con.com/
[syscan-360]: https://www.syscan360.org/en/
[slides-syscan]: https://speakerdeck.com/yformaggio/attacking-vxworks-from-stone-age-to-interstellar
[code]: https://github.com/thelumberjhack/VxFuzz