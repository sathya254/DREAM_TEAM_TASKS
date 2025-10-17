To connect to the Bandit server, use the following SSH command:
ssh bandit@bandit.labs.overthewire.org -p 2220
"Enter password"-->will be displayed to take password as a input.


Level 0 → Level 1
Objective: Find the password for Level 1 in the readme file.
Commands Used:
ls: Lists files in the current directory.
cat readme: Displays the contents of the readme file.
Password: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If


Level 1 → Level 2
Objective: Read the password from a file named -.
Commands Used:
ls: Lists files in the directory.
cat ./-: Reads the file named - (the ./ specifies the file in the current directory to avoid confusion with the cat command’s - option).
Password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx


Level 2 → Level 3
Objective: Read the password from a file with spaces in its name.
Commands Used:
ls: Lists files in the directory.
cat ./--spaces: Reads the file named --spaces (using ./ and escaping spaces with \ to handle the special characters in the filename).
Password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx


Level 3 → Level 4
Objective: Navigate to a directory and read the password from a file.
Commands Used:
ls: Lists files in the directory.
cd inhere: Changes to the inhere directory.
cat .hidden: Reads the contents of the hidden file.
Password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ


Level 4 → Level 5
Objective: Identify and read the password from a human-readable file in a directory.
Commands Used:
ls: Lists files in the directory.
cd inhere: Changes to the inhere directory.
file ./*: Checks the file types in the directory.
cat Reads the human-readable file (identified using file).
grep: Filters specific data from the file if needed.
Password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw


Level 5 → Level 6
Objective: Find a file with a specific size (1033 bytes) and read its contents.
Commands Used:
ls: Lists files in the directory.
cd inhere: Changes to the inhere directory.
find . -type f -size 1033c: Searches for a file with exactly 1033 bytes.
cat Reads the contents of the identified file.
Password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG


Level 6 → Level 7
Objective: Find a file owned by bandit7, belonging to group bandit6, with a size of 33 bytes.
Commands Used:
ls: Lists files in the directory.
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null: Searches the entire filesystem for a file matching the criteria, suppressing permission-denied errors.
cat Reads the contents of the identified file.
Password: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj


Level 7 → Level 8
Objective: Extract the password from data.txt by finding the line containing the word millionth.
Commands Used:
ls: Lists files in the directory.
cat data.txt | grep millionth: Pipes the contents of data.txt to grep to filter lines containing millionth.
Password: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc


Level 8 → Level 9
Objective: Find the unique line in data.txt to retrieve the password.
Commands Used:
ls: Lists files in the directory.
sort data.txt | uniq -u: Sorts the file and outputs the line that appears exactly once.
Password: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM


Level 9 → Level 10
Objective: Extract the password from data.txt by finding lines containing =.
Commands Used:
ls: Lists files in the directory.
sort data.txt | grep "=": Sorts the file and filters lines containing =.
Password: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey


Level 10 → Level 11
Objective: Decode a base64-encoded password in data.txt.
Commands Used:
ls: Lists files in the directory.
cat data.txt | base64 -d: Decodes the base64-encoded contents of data.txt.
Password: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr


Level 11 → Level 12
Objective: Decode a ROT13-encoded password in data.txt.
Commands Used:
ls: Lists files in the directory.
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m': Applies ROT13 transformation (shifts letters by 13 positions) to decode the text.
Password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4


Level 12 → Level 13
Objective: Decompress a hexdump file to retrieve the password.
Commands Used:
ls: Lists files in the directory.
mkdir /tmp/ Creates a temporary directory.
cp data.txt /tmp/ Copies the file to the temporary directory.
cd /tmp/ Changes to the temporary directory.
xxd -r data.txt > file: Converts the hexdump to binary.
file file: Checks the file type.
gunzip file: Decompresses if it’s a gzip file.
bunzip2 file: Decompresses if it’s a bzip2 file.
cat Reads the decompressed file.
Password: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn


Level 13 → Level 14
Objective: Use a private SSH key to log into the next level.
Commands Used:
ls: Lists files in the directory.
ssh -i sshkey.private bandit14@localhost -p 2220: Uses the private key to SSH into the next level.
Password: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS


Level 14 → Level 15
Objective: Submit the current level’s password to a service running on port 30000.
Commands Used:
nc localhost 30000: Connects to the service on port 30000 and submits the password manually.
Password: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo


Level 15 → Level 16
Objective: Submit the current level’s password to a service running on port 30001 using SSL.
Commands Used:
cat /etc/bandit_pass/bandit15: Reads the current level’s password.
ncat --ssl localhost 30001: Connects to the service on port 30001 with SSL and submits the password.
Password: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx


Level 16 → Level 17
Objective: Scan for open ports, connect to the correct one, and retrieve the private key for the next level.
Commands Used:
nmap localhost -p 31000-32000: Scans ports in the range 31000–32000 to identify open ports.
ncat --ssl localhost Connects to the identified port with SSL to retrieve the private key.
sudo vim key: Saves the key to a file.
chmod 600 key: Sets appropriate permissions for the key file.
Password: CgmS55GVlEKTgx8xpW8HuWnHlBKP924b


Level 17 → Level 18
Objective: Compare two files to find the password.
Commands Used:
ls: Lists files in the directory.
diff passwords.old passwords.new: Compares the two files to identify the differing line (the password).
cd -: Returns to the previous directory.
Password: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO


Level 18 → Level 19
Objective: Access a server that logs out immediately by forcing a pseudo-terminal.
Commands Used:
ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh: Forces a pseudo-terminal and runs /bin/sh to bypass the logout script.
cat readme: Reads the password from the readme file.
Password: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8


Level 19 → Level 20
Objective: Use a setuid binary to read the password for Level 20.
Commands Used:
./bandit20-do cat /etc/bandit_pass/bandit20: Runs the bandit20-do binary with elevated privileges to read the password file.
Password: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
