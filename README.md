# Simpl-CreditCardApplication

## Problem Statement

Building a Simple Pay-Later Service

As a pay later service we allow our users to buy goods from a merchant now, and then allow
them to pay for those goods at a later date.

The service works inside the boundary of following simple constraints -
- Let's say that for every transaction paid through us, merchants offer us a discount.
    - For example, if the transaction amount is Rs.100, and merchant discount offered
to us is 10%, we pay Rs. 90 back to the merchant.
    - The discount varies from merchant to merchant.
    - A merchant can decide to change the discount it offers to us, at any point in time.
- All users get onboarded with a credit limit, beyond which they can't transact.
    - If a transaction value crosses this credit limit, we reject the transaction.

**Use Cases**

There are various use cases our service is intended to fulfil -
- Allow merchants to be onboarded with the amount of discounts they offer
- Allow merchants to change the discount they offer
- Allow users to be onboarded (name, email-id and credit-limit)
- Allow a user to carry out a transaction of some amount with a merchant.
- Allow a user to pay back their dues (full or partial)
- Reporting:
    - How much discount we received from a merchant till date
    - Dues for a user so far
    - Which users have reached their credit limit
    - Total dues from all users together

**Goal**

The goal of this coding challenge will be to build a system for satisfying above use cases.
- IO will be via a command line interface.
- The input can be given in any order as a command, and the system should respond
accordingly.
- For inputs like merchant discount rate changes or credit limit changes for a user, the
system adapts itself.

**CLI**

Here is how the command line interface, corresponding to the use-cases mentioned above, can
look like

```
new user u1 u1@email.in 1000 # name, email, credit-limit
new merchant m1 2% # name, discount-percentage
new txn u1 m2 400 # user, merchant, txn-amount
update merchant m1 1% # merchant, new-discount-rate
payback u1 300 # user, payback-amount
report discount m1
report dues u1
report users-at-credit-limit
report total-dues

Example Flow

> new user user1 u1@users.com 300
user1(300)
> new user user2 u2@users.com 400
user2(400)
> new user user3 u3@users.com 500
user3(500)
> new merchant m1 m1@merchants.com 0.5%
m1(0.5%)

> new merchant m2 m2@merchants.com 1.5%
m2(1.5%)
> new merchant m3 m3@merchants.com 1.25%
m3(1.25%)
> set interest 1.25%
interest-rate: 1.25%
> new txn user2 m1 500
rejected! (reason: credit limit)
> new txn user1 m2 300
success!
> new txn user1 m3 10
rejected! (reason: credit limit)
> report users-at-credit-limit
user1
> new txn user3 m3 200
success!
> new txn user3 m3 300
success!
> report users-at-credit-limit
user1
user3
> report discount m3
6.25
> payback user3 400
user3(dues: 100)
> report total-dues
user1: 300
user3: 100
total: 400
```

## Pyenv Setup(MacOS 10.9+)

#### Step 1: Install Pre-Requisites

```
brew install openssl readline sqlite3 xz zlib

export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
```

#### Step 2: Install pyenv

```
curl https://pyenv.run | bash
```

Add the following code to your `~/.bash_profile` file
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
This will load pyenv when a terminal is started

#### Step 3: Install Python 3.7.9

```
pyenv install -v 3.7.9
```
Here `-v` represents the python version. In our case it is `3.7.9`.
You could install different versions using the `-v` option.

#### Step 4: Create Virtual Environment

```
pyenv virtualenv 3.7.9 simpl-3.7.9
```
The above command creates a virtual environment with name `simpl-3.7.9` using python version `3.7.9`. You can choose a name that is preferable to you.

#### Step 5: Activate Virtual Environment

```
pyenv activate simpl-3.7.9
```
Once the virtual environment that you created is activated, you can install the requirements and run the server. Once the work is completed you could deactivate your virtual environment using `pyenv deactivate`# Setup Instructions


## DB Setup

Using sqlite3 for this project to keep things simple.
```
brew install sqlite3
```

## Django Project Setup

#### Pre-Requisites

- Forked and cloned this repository.
- Navigate into cloned location.
- An activated virtual environment with python version 3.7.9

#### Step 1: Install requirements.

```
pip install -r requirements.txt
```

#### Step 2: Migrate

```
python manage.py migrate
```

#### Step 3: Create an admin user

```
python manage.py createsuperuser
```

#### Step 4: Runserver

```
python manage.py runserver 0:8000
```

## Testing the Application

#### Admin URL
```
http://localhost:8000/admin/
```

#### Management Commands


From the project directory `Simpl-CreditCardApplication/PayLater`, management commands can be executed in the following format:


`python manage.py <command_name> --<option_name_1> <option_value_1> --<option_name_2> <option_value_2> ...`

Available Commands

1.  Command: `create_new_user`

    Options: username, email, credit_limit

    Example: `python manage.py create_new_user --username anewuser --email anemail@mail.com --credit_limit 12000`

2.  Command: `create_new_merchant`

    Options: merchant_name, email, discount_rate

    Example: `python manage.py create_new_merchant --merchant_name anewmerchant --email amerchantemail@mail.com --discount_rate 1.5`

3.  Command: `make_purchase`

    Options: username, merchant_name, amount

    Example: `python manage.py make_purchase --username anewuser --merchant_name anewmerchant --amount 12000`

4.  Command: `make_payment`

    Options: username, amount

    Example: `python manage.py make_payment --username anewuser --amount 1000`

5.  Command: `report_dues`

    Options: username(*optional*)

    Example: `python manage.py report_dues --username anewuser`

6.  Command: `report_discounts`

    Options: merchant_name(*optional*)

    Example: `python manage.py report_discounts --merchant_name anewmerchant`

7.  Command: `report_users_at_limit`

    Options: 

    Example: `python manage.py report_users_at_limit`

8.  Command: `set_credit_limit`

    Options: username, new_limit

    Example: `python manage.py set_credit_limit --username anewuser --new_limit 1000`

9. Command: `set_discount_rate`

    Options: merchant_name, discount_rate

    Example: `python manage.py set_discount_rate --merchant_name anewmerchant --discount_rate 10`
