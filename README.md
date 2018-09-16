#### Getting Started

* install requirements
  * create and source python3 virtual environment
  * pip install -r requirements.txt

* Open as Pycharm Project
* Start all services
  * start Pycharm
    * import project, run runall configuration
    * should start the idp at port 3000, sp_toaster at port 4000, sp_tv at 5000, pdp at 10000
  * alternatively start "run_all.sh"

* step through consumer.py to see whats happening
  * start at line "r = requests.post('http://127.0.0.1:4000/protected_toaster')"
* use Postman to send Request