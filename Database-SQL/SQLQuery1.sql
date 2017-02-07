-- Creation of all Tables in SQLDrill database

CREATE TABLE tblBook
(
Bookid int PRIMARY KEY ,
Title varchar (30) NULL,
PublisherName varchar(60) NOT NULL
)

CREATE TABLE tblBook_Authors
(
Bookid int PRIMARY KEY ,
AuthorName varchar (60)
)

CREATE TABLE tblPublisher
(
Name varchar(60) PRIMARY KEY ,
[Address] varchar (60) NULL,
Phone int
)

CREATE TABLE tblBook_Copies
(
Bookid int PRIMARY KEY ,
Branchid int,
No_Of_Copies int
)

CREATE TABLE tblBook_Loans
(
Bookid int PRIMARY KEY ,
Branchid int,
CardNo int Unique,
DateOut DATE,
DueDate DATE
)

CREATE TABLE tblLibrary_Branch
(
Branchid int PRIMARY KEY ,
BranchName varchar (30) NOT NULL,
Address varchar (60) NOT NULL,
)

CREATE TABLE tblBorrower
(
CardNo int PRIMARY KEY ,
Name varchar (30),
Address varchar (60),
Phone int
)

--Insert Data into Table Book

INSERT INTO tblBook
VALUES (1,'The Lost Tribe', 'Some Publisher')

INSERT INTO tblBook
VALUES (2,'The Lost', 'Pearson')

INSERT INTO tblBook
VALUES (3,'The Lost Bribe', 'Reed')

INSERT INTO tblBook
VALUES (4,'The Lost Crime', 'Random House')

INSERT INTO tblBook
VALUES (5,'The Lost Water', 'Wiley')

INSERT INTO tblBook
VALUES (6,'Wild Slave', 'Some Publisher')

INSERT INTO tblBook
VALUES (7,'The Missing Emperor', 'Pearson')

INSERT INTO tblBook
VALUES (8,'Memory of Body', 'Reed')

INSERT INTO tblBook
VALUES (9,'The Boyfriend''s Luck', 'Random House')

INSERT INTO tblBook
VALUES (10,'The Souls of the Wizards', 'Wiley')

INSERT INTO tblBook
VALUES (2,'Missing School', 'Some Publisher')

INSERT INTO tblBook
VALUES (1,'The Absent Storms', 'Pearson')

INSERT INTO tblBook
VALUES (4,'Moons of World', 'Reed')

INSERT INTO tblBook
VALUES (6,'The Voyages''s Sword', 'Random House')

INSERT INTO tblBook
VALUES (5,'The History of the Woman', 'Wiley')

INSERT INTO tblBook
VALUES (8,'Return in the Legacy', 'Hot Sauce')

INSERT INTO tblBook
VALUES (9,'Frozen Flames', 'Pearson')

INSERT INTO tblBook
VALUES (2,'Hustler of Name', 'Hot Sauce')

INSERT INTO tblBook
VALUES (9,'The Only Thoughts', 'Random House')

INSERT INTO tblBook
VALUES (2,'Bloody Mann', 'Hot Sauce')


-- Insertion of data into Table Book Authors


INSERT INTO tblBook_Authors
VALUES (1,'Channary So')

INSERT INTO tblBook_Authors
VALUES (2,'Nagia Iqbal')

INSERT INTO tblBook_Authors
VALUES (3,'Stephen King')

INSERT INTO tblBook_Authors
VALUES (4,'April Fleming')

INSERT INTO tblBook_Authors
VALUES (5,'Brenda Dean')

INSERT INTO tblBook_Authors
VALUES (6,'Jessie Evans')

INSERT INTO tblBook_Authors
VALUES (7,'Nellie Cortez')

INSERT INTO tblBook_Authors
VALUES (8,'Miranda Allen')

INSERT INTO tblBook_Authors
VALUES (9,'Hugo Jefferson')

INSERT INTO tblBook_Authors
VALUES (10,'Janet Perkins')

-- Insertion into Table Publisher

INSERT INTO tblPublisher
VALUES ('Some Publisher','207 Park Avenue 
New Windsor, NY 12553',(833)-096-0925)

INSERT INTO tblPublisher
VALUES ('Pearson','623 Park Drive 
Howard Beach, NY 11414',(899)-123-0012)

INSERT INTO tblPublisher
VALUES ('Reed','540 Briarwood Drive 
Noblesville, IN 46060',(822)-003-1597)

INSERT INTO tblPublisher
VALUES ('Random House','320 Belmont Avenue 
Libertyville, IL 60048',(844)-297-1467)

INSERT INTO tblPublisher
VALUES ('Wiley','304 Olive Street 
Encino, CA 91316',(833)-787-4305)

INSERT INTO tblPublisher
VALUES ('Hot Sauce','573 12th Street 
Peabody, MA 01960',(844)-394-3071)

-- Insertion into Table Book_Copies

INSERT INTO tblBook_Copies
VALUES (1,1,2)

INSERT INTO tblBook_Copies
VALUES (2,2,6)

INSERT INTO tblBook_Copies
VALUES (3,3,5)

INSERT INTO tblBook_Copies
VALUES (4,4,4)

INSERT INTO tblBook_Copies
VALUES (5,5,10)

INSERT INTO tblBook_Copies
VALUES (6,6,8)

INSERT INTO tblBook_Copies
VALUES (7,7,2)

INSERT INTO tblBook_Copies
VALUES (8,8,7)

INSERT INTO tblBook_Copies
VALUES (9,9,6)

INSERT INTO tblBook_Copies
VALUES (10,10,4)

-- Insertion into Table Book_Loans

INSERT INTO tblBook_Loans
VALUES (1,1,1,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (2,2,1,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (3,1,1,20160112,20160125)

INSERT INTO tblBook_Loans
VALUES (4,3,1,20160112,20160131)

INSERT INTO tblBook_Loans
VALUES (5,1,1,20160112,20160126)

INSERT INTO tblBook_Loans
VALUES (6,4,1,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (7,2,1,20160112,20160120)

INSERT INTO tblBook_Loans
VALUES (8,3,1,20160112,20160119)

INSERT INTO tblBook_Loans
VALUES (9,1,1,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (10,4,1,20160112,20160118)

INSERT INTO tblBook_Loans
VALUES (1,1,3,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (2,2,3,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (3,1,3,20160112,20160125)

INSERT INTO tblBook_Loans
VALUES (4,3,3,20160112,20160131)

INSERT INTO tblBook_Loans
VALUES (5,1,2,20160112,20160126)

INSERT INTO tblBook_Loans
VALUES (6,4,2,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (7,1,2,20160112,20160120)

INSERT INTO tblBook_Loans
VALUES (8,4,2,20160112,20160119)

INSERT INTO tblBook_Loans
VALUES (9,3,2,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (10,4,2,20160112,20160118)

INSERT INTO tblBook_Loans
VALUES (1,1,4,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (2,2,4,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (3,1,4,20160112,20160125)

INSERT INTO tblBook_Loans
VALUES (4,3,4,20160112,20160131)

INSERT INTO tblBook_Loans
VALUES (5,2,3,20160112,20160126)

INSERT INTO tblBook_Loans
VALUES (6,1,3,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (7,4,3,20160112,20160120)

INSERT INTO tblBook_Loans
VALUES (8,4,3,20160112,20160119)

INSERT INTO tblBook_Loans
VALUES (9,1,3,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (10,3,3,20160112,20160118)

INSERT INTO tblBook_Loans
VALUES (1,1,6,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (2,2,6,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (3,1,6,20160112,20160125)

INSERT INTO tblBook_Loans
VALUES (4,2,6,20160112,20160131)

INSERT INTO tblBook_Loans
VALUES (5,4,5,20160112,20160126)

INSERT INTO tblBook_Loans
VALUES (6,4,5,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (7,4,5,20160112,20160120)

INSERT INTO tblBook_Loans
VALUES (8,4,5,20160112,20160119)

INSERT INTO tblBook_Loans
VALUES (9,4,5,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (10,1,5,20160112,20160118)

INSERT INTO tblBook_Loans
VALUES (1,1,7,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (2,2,7,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (3,1,7,20160112,20160125)

INSERT INTO tblBook_Loans
VALUES (4,3,7,20160112,20160131)

INSERT INTO tblBook_Loans
VALUES (5,1,8,20160112,20160126)

INSERT INTO tblBook_Loans
VALUES (6,4,8,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (7,2,8,20160112,20160120)

INSERT INTO tblBook_Loans
VALUES (8,3,8,20160112,20160119)

INSERT INTO tblBook_Loans
VALUES (9,1,8,NULL,NULL)

INSERT INTO tblBook_Loans
VALUES (10,4,8,20160112,20160118)


-- Insertion into Table Library_Branch


INSERT INTO tblLibrary_Branch
VALUES (1,'Tabasco Sauce','3408 Holly Court Yuma, AZ 85365')

INSERT INTO tblLibrary_Branch
VALUES (2,'Sharpstown','1841 Willow Drive Auburn, NY 13021')

INSERT INTO tblLibrary_Branch
VALUES (3,'Central','8722 Heather Court Fort Lauderdale, FL 33308')

INSERT INTO tblLibrary_Branch
VALUES (4,'MLK','6650 Penn Street Wakefield, MA 01880')

--Insertion into Table Borrower

INSERT INTO tblBorrower
VALUES (1,'James Tello','1362 Fawn Lane Fairport, NY 14450', 606-389-2958)

INSERT INTO tblBorrower
VALUES (2,'Elisa Jones','7722 Harrison Avenue Salt Lake City, UT 84119', 609-306-5263)

INSERT INTO tblBorrower
VALUES (3,'Nathan Grant','1290 High Street Huntington, NY 11743', 701-552-8829)

INSERT INTO tblBorrower
VALUES (4,'Nora Milligan','615 Taylor Street Wilmington, MA 01887', 786-301-3171)

INSERT INTO tblBorrower
VALUES (5,'Jennifer Ray','5672 Water Street Langhorne, PA 19047', 704-605-6129)

INSERT INTO tblBorrower
VALUES (6,'Sean Fielder','111 Poplar Street Dover, NH 03820', 302-798-6103)

INSERT INTO tblBorrower
VALUES (7,'Virgie Styer','164 Pheasant Run Mount Prospect, IL 60056', 410-597-2348)

INSERT INTO tblBorrower
VALUES (8,'Linda Schiver','560 Main Street North Mesa, AZ 85203', 213-787-8291)