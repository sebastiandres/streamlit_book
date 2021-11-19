# True or False
## Format definition

Format for questions where expected answer is True
```
stb.true-false
Question description
True
```

Format for questions where expected answer is False
```
stb.true-false
Question description
False
```

Optional configuration:
* `success:` This will get rendered on a st.success element if answer is wrong. If not provided, it just says "Correct answer".
* `failure:` This will get rendered on a st.failure element if answer is wrong. If not provided, it just displays "Wrong answer".
* `button:` Alternative text for the button. If not provided, it displays "Check answer'. 

A complete format is as follows:
```
stb.true-false
Question description
False
success: Correct!
failure: Wrong!
button: Check!
```