# Simpl-CreditCardApplication

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
