owler.io
===========================

owler.io is a service that lets you send issue to your github or
bitbucket private/public repository through your email, say your
repository name is "octocat", then you can email to *octocat@owler.io*
to create issue to your octocat repository, owler.io will find where
octocat repository located (github or bitbucket). Think of if like
your posterous blog.

owler.io also can map your meta tags in your email body into your issue
properties, if if you write email like this:

```
    from: kitty@gmail.com
    to: octocat@gmail.com
    subject: This is issue title

    body:
    This is the issue body
    This is another line

    (major bug)

```

It will read your metatags (the last line with parentheses) and convert
it to issue properties, in this case, it the issue will be attached to
bug label and major priority. Note that these are depends on the
available properties in your repository and hosting. For example, github
doesn't have list of priorities in their issue.

owler.io is already up and running before this repository was created,
but there are problems and some hole in the system, hence I need to make
it cleaner and open to make sure I get feedback from others. You can
visit the old version here http://owler.io, you might be able to
register but you will not be able to send any email to there since
I shutted it down for good.

With this repository, I want to rewrite some important part of the
system and relaunch it again.

How does the email processing work?
--------------------------
Email is the most important piece in owler.io, and also the reason why
it was shutted down. The new email processing will make sure certain
things are achieved:

* You will still be able to send issue to [repository_name@owler.io]
* No one can spoof your email to create issue on behalf of you
* The process should be as simple as possible

The second and and third point is one of the major goal in the new
version. The current email processing is as below:

1. owler.io receives your email
2. Checks the sendeer in the whitelist
3. Checks the repository detail in the email
4. Find the repository in the user data
4. Convert the email to an issue object
5. Send the issue object to repository through github/bitbucket API
6. In case any error happened, send the report straight away to your
   email

There's also privacy control here, where you can tune whether or not you
want owler.io to track your email & API return  or you want to dispose
it right away.

Is it free?
--------------------------
Yes, you can use owler.io without any charge, and I'm not planning to
put some premium plan in it.

