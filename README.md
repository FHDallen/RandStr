# randStr
### Request Data by writing an integer X to the file key.txt
```
with open("key.txt", "w") as pipeline:
      pipeline.write(str(X)) # Where X is an integer
```

### Recieve Data by reading the file key.txt
```
with open("key.txt", "r") as pipeline:
      randStr = pipeline.readline()
```
### Verifying Data Example
```
if len(rand_str) == X:
      return randStr
```
## Team Rules:
- Primary means of communication: Discord first, email if Discord is not working.
- Try and respond within 24-48 hours since life can get hectic, in the cases where one gets busy a heads-up is appreciated
- If there is no response from Discord or email after 24 hours send a follow-up message if not already done. If still no response after 48 hours reach out to TA or instructor
- If you are working on a microservice for another teammate, try to give an ETA for when it will be finished. And vice versa, if you need a microservice from another teammate, try to give a due date for them to meet (within reason…).
- First, try to resolve arguments/disagreements individually. If a resolution cannot be found, bring it to the rest of the group to help resolve.

## UML Sequence Diagram
![Basic UML Sequence Diagram for requesting data and the returned data.](https://cdn.discordapp.com/attachments/312909213900734464/1307814297271009420/image.png?ex=673bac7a&is=673a5afa&hm=8d8a2bf2c0a0a5f80ff19cc54bd88b7106afe47feff80aa2f5a036df068d0ebd&)

