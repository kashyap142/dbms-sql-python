create database hospital;
use hospital;   

create table Login_Det (
    ID varchar(7),
    password varchar(200),
    primary key(ID)
);

create table doctor(
    DocID varchar(7), 
    Name varchar(30), 
    Gender varchar(3), 
    DOB varchar(10), 
    Qualification varchar(20),
    Department varchar(20),
    Address varchar(40),
    salary varchar(7),  
    phone varchar(15),
    foreign key(DocID) references Login_Det(ID)
);

create table Patient(
    PatientID varchar(7),
    Name varchar(30),
    Gender varchar(3),
    DOB varchar(10),
    Insurance varchar(20),
    Address varchar(40),
    phone varchar(15),
    Blood_Group varchar(8),
    Allergies varchar(20),
    primary key(PatientID)
);

create table Staff (
    ID varchar(7),
    Name varchar(30),
    Gender varchar(3),
    DOB varchar(10),
    Designation varchar(20),
    salary varchar(7),
    Address varchar(40),
    phone varchar(15),
    foreign key(ID) references Login_Det(ID)
);

create table TestSchedule(
    PatientID varchar(7),
    DocID varchar(7),
    T_date varchar(10),
    T_time varchar(6),
    test varchar(30),
    foreign key(DocID) references doctor(DocID),
    foreign key(PatientID) references Patient(PatientID)
);

create table transactions (
    BillNo varchar(7),
    PatientID varchar(7),
    B_date varchar(10),
    amount varchar(5),
    primary key(BillNo),
    foreign key(PatientID) references Patient(PatientID)
);

create table appointment (
    appointmentNo varchar(7),
    PatientID varchar(7),
    DocID varchar(7),
    A_date varchar(10),
    A_time varchar(6),
    status varchar(3),
    foreign key(PatientID) references Patient(PatientID),
    foreign key(DocID) references doctor(DocID),
    primary key(appointmentNo)
);