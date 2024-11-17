# randStr
### Request Data by writing a positive integer to the file key.txt
```
with open("key.txt", "w") as pipeline:
      pipeline.write(str(X)) # Where X is a positive integer
```

### Recieve Data by reading the file key.txt
```
with open("key.txt", "r") as pipeline:
      randStr = pipeline.readline()
```
### Verifying Data Example
```
if len(randStr) == X:
      return randStr
```
## Communication Contract:
A. For which teammate did you implement “Microservice A”? <br>
Ryan F.

B. What is the current status of the microservice? Hopefully, it’s done!<br>
Done

C. If the microservice isn’t done, which parts aren’t done and when will they be done?<br>
N/A

D. How is your teammate going to access your microservice? Should they get your code from GitHub (if so, provide a link to your public or private repo)? Should they run your code locally? Is your microservice hosted somewhere? Etc.<br>
https://github.com/FHDallen/RandStr<br>
Microservice should be run locally. 

E. If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?<br>
Reach out over discord, if issues exist I will be able to troubleshoot them same day, bar any issues over holiday break(s).

F. If your teammate cannot access/call your microservice, by when do they need to tell you?<br>
Not sure when a good arbitrary date is for this question, ideally as soon as they realize there are issues, but conservatively by the end of November. 

G. Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?<br>
Nope! 
<br>

## UML Sequence Diagram
![Basic UML Sequence Diagram for requesting data and the returned data.](https://cdn.discordapp.com/attachments/312909213900734464/1307836054455451712/image.png?ex=673bc0bd&is=673a6f3d&hm=137b1247bbd2b0e5e624dbbcb8a57ce91990b2c40699020ba652f93e97f84ae8&)

