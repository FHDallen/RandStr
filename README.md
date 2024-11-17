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
## Team Rules:
- Primary means of communication: Discord first, email if Discord is not working.
- Try and respond within 24-48 hours since life can get hectic, in the cases where one gets busy a heads-up is appreciated
- If there is no response from Discord or email after 24 hours send a follow-up message if not already done. If still no response after 48 hours reach out to TA or instructor
- If you are working on a microservice for another teammate, try to give an ETA for when it will be finished. And vice versa, if you need a microservice from another teammate, try to give a due date for them to meet (within reason…).
- First, try to resolve arguments/disagreements individually. If a resolution cannot be found, bring it to the rest of the group to help resolve.

## UML Sequence Diagram
![Basic UML Sequence Diagram for requesting data and the returned data.](https://cdn.discordapp.com/attachments/312909213900734464/1307836054455451712/image.png?ex=673bc0bd&is=673a6f3d&hm=137b1247bbd2b0e5e624dbbcb8a57ce91990b2c40699020ba652f93e97f84ae8&)

