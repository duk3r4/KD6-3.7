# KD6-3.7

![1](/kd6-3.7.png)
<i> KD6-3.7 is a character in the Blade Runner universe whose job is to catch old replicant models that can be 
identified by their ID number </i>

## About

Every person is given an identification number at birth, when they reach a certain age or status, which allows them to 
be distinguished from other people. As it turned out, in many countries different identification numbers are generated 
by state authorities not by chance, but according to a certain algorithm. 

**KD6-3.7** knows these algorithms and is able to provide additional information about a person if you have his/her 
identification number. This method can be useful in OSINT investigations when there is not much information about a 
person.

At the moment you can see additional information about ID number holders from the following countries:

- Albania
- Belgium
- Bosnia and Herzegovina
- Bulgaria
- Czech Republic
- Denmark
- Estonia
- Finland
- France
- Slovakia

The list of countries and features will be added over time!

## Installation

### Cloning a repository

```bash
# clone and use
git clone https://github.com/duk3r4/KD6-3.7 && cd KD6-3.7
pip3 install -r requirements.txt

# usage
python kd6-3.7.py --help              
Usage: kd6-3.7.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  alb
  bel
  bgr
  bih
  cze
  dnk
  est
  fin
  fra
  svk

python kd6-3.7.py bel --help
Usage: kd6-3.7.py bel [OPTIONS]

Options:
  --nin TEXT  National Identification Number (National Register Number); 11
              digits
  --icn TEXT  Identity Card Number; 9, 10, or 12 digits
  --help      Show this message and exit.
```

## Usage examples

```bash
python kd6-3.7.py bel --icn 0106100013  

Here is what I got from that ID number:
The card owner is a EU/EEA/Swiss citizen

python kd6-3.7.py est --nin 48703230245

Here is what I got from that ID number:
Day of birth:  23 
Month of birth:  March
Year of birth:  1987
Sex:  Female
Sequence number of person with the same date of birth:  24
Checksum symbol:  5
Personal mail for contacting government agencies: 48703230245@eesti.ee

python kd6-3.7.py fra --nin 187112b361052

Here is what I got from that ID number:
Month of birth:  November 
Year of birth:  1987
Sex:  Male
The region of origin:  CORSE / Corse / Corse  ( 94 )
The department of origin:  HAUTE CORSE / Haute-Corse / Haute-Corse  ( 2B )
The commune of origin:  ZILIA / Zilia / Zilia
Sequence number of person with the same date of birth:  5
```

## License

MIT © [KD6-3.7](https://github.com/duk3r4/KD6-3.7)<br/>
