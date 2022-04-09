# sequelbetter

UHCTF Challenge around SQL injection. 

# Build

You can use build.sh (or the Dockerfile) to conveniently build everything. The bash scripts assume Alpine Linux.

Use the build.sh script from a clean git repo!

1. Make sure Git LFS is installed and the files are checked out (`git lfs pull`)
1. `docker build -t sequelbetter .`

# Deploy to VM

If you want to try to solve the challenge locally, please use the Docker method. It is way easier.

scp using a clean git repo. Then run build.sh on the Alpine VM.
After running build.sh, run `rc-update add <service> <runlevel>`

# Run

`docker run -p 80:80 sequelbetter`

# Challenge

They say the sequel is never better than the original. I don't believe that.

## Hint 1

Explanation: will tell you what to use. **Basically mandatory for first bachelors.**

Hint: SQL injection

## Hint 2

Explanation: Will give a clue as to what you might be doing wrong

Hint: Only one searchstatement at a time, please! You cannot go to two movies at the same time. Can you imagine the director's union if that were possible?

## Hint 3

Explanation: Will give you tools to help you build the correct attack.

Hint: Add the following get parameter to your request. It will give you some 'debug information' on failed requests.

```
2RZCQY24IKSHKA67RBZU5L3HKCEEUOIGPLHQ5M6X=KLZ5SKGIABDZTFWKD4CL4E5N2SINVGCTXSLYUU2Y
```

## Write-up

So, the backend seems to be limited to one query.

The easiest way to start this challenge, might be to create a dummy database (in sqlite) with a scheme similar to the one you can guess to have here.

By running some queries, you might notice that there's a limit of 10 items shown at all times. So, the query likely has some form of limiter. You cannot simply print the entire database.

If you search for uhctf, you don't find anything. The flag is thus likely in another colunm or table.

If you search for "toy story 3", you only find the exact movie and not "toy story 3", so the query only searches on the first of the two movies.

As the search doesn't seem to be case sensitive, there could be a LOWER call, but as you'll see when creating extra calls, it is not done in SQL. It is done in the webserver logic.

But, as soon as you try to add an additional statement, the database crashes. So, you'll have to continue with the existing query. You have a vague idea of the query:

```SELECT <the 4 columns seen in JSON> FROM <name of the table> WHERE <the name in lowercase is like our query>```

If you try to do a basic SQL injection, you'll see an error "SQLite Database error", which gives you the clue that this server runs on SQLite. So, focus on this database system from now on!

By running the following command ([obtained from this cheatsheet](https://github.com/unicornsasfuel/sqlite_sqli_cheat_sheet)):

```
nonexistingmovie' UNION SELECT sql, null, null, null FROM sqlite_master;--
```

you get the structure of the database. We use 'null' several times because we have four output columns to match from our original query. You can always try and add/remove columns as needed. Or, if you bought the third hint, you can read it.
You can see that there's a table called 'flag' with a column 'flag'. Maybe we should try to read its contents? We can do this the same way as how we got the scheme.

So, a possible solution is:

```
thistitledoesnotexist' UNION SELECT flag, null, null, null FROM flag;--
```

which will give you the flag.
