
# ITBC Final FastAPI project

This is server-side web shop for car products.
The application should be able to allow login for users, who may have different roles.
After login, a user should be able to leave a personal data, see products filtered in different ways and to choose products for the wish list. At the end, customer should be able to order products from the shopping cart and track the order.


### Notable endpoints:

- `/api/products/get-products-by-descending-number-of-sold`
- `/api/products/get-all-products-sorted-by-price-from-lower`
- `/api/products/get-products-for-car-brand`
- `/api/products/get-products-name-like`
- `/api/cart_items/get-all-cart-items-for-shopping-cart`
- `/api/shopping-orders/make-order`
- `/api/shopping-orders/sum-today-profit`


## Installation

### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
### Activate Virtual environment
Open terminal and navigate to project directory, than run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
### Database
Start MySQL server and execute all commands in **_init_db/init_db.sql_**

### Environment variables
1. Create new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


## Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
����