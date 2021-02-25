from fastapi import FastAPI
from pydantic import BaseModel

# initiate the app
app = FastAPI(
    title="Employee Details",
    description="Automatic Documentation",
    version="2"
)

# In memory DB
db: dict = {}


# model
class Emp(BaseModel):
    emp_name: str
    emp_email: str
    emp_no: int


@app.get('/retrive')
def get_record():
    return db


@app.post('/create')
def post_rec(sl_no: int, emp_name: str, emp_age: int):
    rec = {
        "emp_name": emp_name,
        "emp_age": emp_age,
    }

    db[sl_no] = rec
    return rec


@app.post('/insert')
def insert_rec(sl_no: int, emp: Emp):
    rec = {
        "emp_name": emp.emp_name,
        "emp_no": emp.emp_no,
        "emp_email": emp.emp_email
    }

    db[sl_no] = rec
    return rec


@app.put('/update')
def update_rec():
    pass


@app.delete('/delete')
def delete_rec():
    pass
