# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd - print working directory  

hostname - my computer's network name  

mkdir - make directory  

cd - change directory  

ls - list directory contents

rmdir - remove directory  

pushd - push directory  

popd - pop directory  

cp - copy a file or directory  

mv - move a file or directory  

less - page through a file  

cat - print the whole file  

xargs - execute arguments  

find - find files  

grep - find things inside files  

man - read a manual page  

apropos - find what man page is appropriate  

env - look at your environment  

echo - print some arguments  

export - export/set a new environment variable  

exit - exit the shell  

chmod - change permission modifiers  

chown - change ownership  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls` - lists current working directory contents.  

`ls -a`  - lists current working directory contents, including hidden files and directories.

`ls -l`  - lists current working directory contents in long format.

`ls -lh`  - lists current working directory contents in long format and human readable format.

`ls -lah`  -lists current working directory contents in long format, including hidden files and directories, and in human readable format.

`ls -t`  - lists current working directory contents and sorts files and directories by the time they were last modified.

`ls -Glp` - lists all contents in working directory in long format, inhibits display of group information, and appends indicator (one of /=@|) to entries to denote file-type.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

'-r' - displays files in reverse order

'-1' - displays each entry on a new line

'-m' - displays the names as a comma-separated list

'-R' - displays subdirectories as well

'-g' - displays long format listing, but excludes owner name

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

‘xargs’ in essence breaks down a list of arguments into sublists small enough to be acceptable on the command line.  

Example:  
This command may fail due to “argument list too long”: rm `find /path -type f 
However, the following functionally equivalent command using ‘xargs’ will not:
find /path -type f -print | xargs rm

 