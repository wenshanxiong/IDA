# IDA (Information dispersal algorithm)

Simple overview of use/purpose.

## Description

Implemention of Rabin's information dispersal algorithm. This project implements functionalities that split a file into a number of pieces, 
and reconstruct it from these pieces. This algorithm serves as a potential solution to the security-reliability problem and transmission problem. The 
design of fingerprint in our implementation is different from the one described in paper. We're using HMAC to defend against replacement attack instead
of using resultant method mentioned in original paper.

## Getting Started

### Requirements

Use the following command to install all requirements
```
pip install -r requirements.txt
```

### Executing program

* For splitting a file
```
python3 disperse.py [inputfile]
```

* For reconstructing a file
```
python3 reconstruct.py fragments/
```

## Authors

Wenshan Xiong 
Shichen Zhou


## Acknowledgments

* [Efficient Dispersal of Information for Security, Load Balancing, and Fault Tolerance ](https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=2C66939BF238B850412FAC8149FA6525?doi=10.1.1.116.8657&rep=rep1&type=pdf)
