from typing import List, Optional, Union
from datetime import date
# datetime, time
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# User
# ------------------------------------
class User(BaseModel):
    id: int
    name: str
    email: str
    password: Union[str, None] = None
    user_role: int

class ShowUser(BaseModel):
    id: int
    name: Union[str, None] = None 
    email: Union[str, None] = None
    user_role: Union[int, None] = None
    class Config():
        orm_mode = True


# Case
# ------------------------------------
class CaseBase(BaseModel):
    id: int
    case_nr: Optional[str] = None
    start_date: Optional[date]
    due_date: Optional[date]
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    case_type: Optional[int] = 0
    project_id: Optional[int] = None
    owner_id: Optional[int] = None

class Case(CaseBase):
    class Config():
        orm_mode = True

class ShowCase(CaseBase):
    id: int
    case_nr: Optional[str] = None
    start_date: Optional[date]
    due_date: Optional[date]
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    case_type: Optional[int] = 0
    project_id: Optional[int] = None
    owner_id: Optional[int] = None

    class Config():
        orm_mode = True
    
# Project
# ------------------------------------
class ProjectBase(BaseModel):
    id: int
    project_nr: Optional[str] = None
    start_date: date
    due_date : date
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    owner_id: Optional[int] = None

class Project(ProjectBase):
    class Config():
        orm_mode = True

class ShowProject(ProjectBase):
    id: int
    project_nr: Optional[str] = None
    start_date: date
    due_date : date
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    owner_id: Optional[int] = 0

    class Config():
        orm_mode = True
        
# TeamMembers
# ------------------------------------
class TeamMemberBase(BaseModel):
    id: int
    project_id: int 
    user_id: int
    team_role: Optional[int] = 0
    assign_date: date
    active:  Optional[bool] = True
    note:  Optional[str] = None
    
class TeamMember(TeamMemberBase):
    class Config():
        orm_mode = True
        
class ShowTeamMember(TeamMemberBase):
    id: int
    project_id: int 
    user_id: int
    team_role: Optional[int] = 0
    assign_date: date
    active:  Optional[bool] = True
    note:  Optional[str] = None

    class Config():
        orm_mode = True
        
# Shift
# ------------------------------------ 
class Shift(BaseModel):
    id: int
    service_name_1: Optional[str] = None
    barman_name_1: Optional[str] = None
    service_name_2: Optional[str] = None
    barman_name_2: Optional[str] = None
    notes: Optional[str] = None
    # the_outcome: List[Outcome] = []
    class Config():
        orm_mode = True
class ShiftBase(BaseModel):
    id: int
    service_id_1: Optional[int] = None
    barman_id_1: Optional[int] = None
    service_id_2: Optional[int] = None
    barman_id_2: Optional[int] = None

class Shift(ShiftBase):
    class Config():
        orm_mode = True
    
# Income
# ------------------------------------ 
class IncomeBase(BaseModel):
    id: int
    date: date
    service_income_1: Optional[float] = None
    service_income_2: Optional[float] = None
    bar_income_1: Optional[float] = None
    bar_income_2: Optional[float] = None
    pos: float = 0
    z_count: float = 0
    vat: float = 0
    waitress_1: Optional[str] = None
    waitress_2: Optional[str] = None
    barman_1: Optional[str] = None
    barman_2: Optional[str] = None
    notes: Optional[str] = None
    shift_id: str
    

class Income(IncomeBase):
    class Config():
        orm_mode = True

class ShowIncome(IncomeBase):
    id: Optional[int]
    date: Optional[date]
    service_income_1: Optional[float] = None
    service_income_2: Optional[float] = None
    bar_income_1: Optional[float] = None
    bar_income_2: Optional[float] = None
    pos: float = 0
    z_count: float = 0
    vat: float = 0
    waitress_1: Optional[str] = None
    waitress_2: Optional[str] = None
    barman_1: Optional[str] = None
    barman_2: Optional[str] = None
    notes: Optional[str] 
    shift_id: Optional[str]
    the_shift: Optional[Shift] 

    class Config():
        orm_mode = True
    
# Outcome
# ------------------------------------ 
class OutcomeBase(BaseModel):
    id: int
    date: date
    description: Optional[str] = None
    invoice_number: Optional[str] = None
    cost: Optional[float] = None
    extra_cost:  Optional[float] = None
    tax_perc: Optional[int] = None
    tax_perc2:  Optional[int] = None
    supplier_id:  Optional[int] = None
    staff_id:  Optional[int] = None
    fixed_cost_id: Optional[int] = None
    is_variable_cost: Optional[bool] = False
    is_fix_cost:  Optional[bool] = False
    is_purchase_cost:  Optional[bool] = False
    is_salary_cost:  Optional[bool] = False
    is_insurance_cost:  Optional[bool] = False
    is_misc_cost:  Optional[bool] = False
    payment_way:  Optional[str] = None
    is_paid:  Optional[bool] = False
    outcome_notes: Optional[str] = None
    # image: Optional[HttpUrl] = None
    # the_staff: List[ChildSchema] = None


class Outcome(OutcomeBase):
    class Config():
        orm_mode = True

class ShowOutcome(OutcomeBase):
    id: Optional[int]
    date: Optional[date]
    description: Optional[str] = None
    invoice_number: Optional[str] = None
    cost: Optional[float] = None
    extra_cost:  Optional[float] = None
    tax_perc: Optional[int] = None
    tax_perc2:  Optional[int] = None
    supplier_id:  Optional[int] = None
    staff_id:  Optional[int] = None
    fixed_cost_id: Optional[int] = None
    is_variable_cost: Optional[bool] = False
    is_fix_cost:  Optional[bool] = False
    is_purchase_cost:  Optional[bool] = False
    is_salary_cost:  Optional[bool] = False
    is_insurance_cost:  Optional[bool] = False
    is_misc_cost:  Optional[bool] = False
    payment_way:  Optional[str] = None
    is_paid:  Optional[bool] = False
    outcome_notes: Optional[str] = None


class OutcomeDetails(BaseModel):
    id: int
    outcome_id: int
    product_name: Optional[str] = None
    product_description: Optional[str] = None
    price_per: Optional[float] = None
    amount: Optional[int] = None
    tax: Optional[int] = None
    notes: Optional[str] = None
    # the_outcome: List[Outcome] = []
    class Config():
        orm_mode = True
        
# Staff
# ------------------------------------ 
class StaffBase(BaseModel):
    id: int
    name: Optional[str] = None
    position: Optional[str] = None
    active: Optional[bool] = False
    daily_salary: Optional[float] = None
    insurance: Optional[float] = None
    notes: Optional[str] = None
    # the_outcome: List[Outcome] = []
    # income: Income

class Staff(StaffBase):
    class Config():
        orm_mode = True
        
# Suppliers
# ------------------------------------ 
class Suppliers(BaseModel):
    id: int
    company_name: Optional[str] = None
    responsible: Optional[str] = None
    address: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    payment_way: Optional[str] = None
    notes: Optional[str] = None
    # email: Optional[EmailStr] = None
    # the_outcome: ShowOutcome
    class Config():
        orm_mode = True

# FixedCost
# ------------------------------------ 
class FixedCost(BaseModel):
    id: int
    name: Optional[str] = None
    class Config():
        orm_mode = True
        
# Blog
# ------------------------------------ 
class BlogBase(BaseModel):
    id: Optional[int] = None
    date: Optional[date] 
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    # author_id: str

class Blog(BlogBase):
    class Config():
        orm_mode = True
class ShowBlog(BaseModel):
    id: int
    date: Optional[date] 
    title: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[str] = None
    active: Optional[bool] = False
    owner: ShowUser
    class Config():
        orm_mode = True

# Notes
# ------------------------------------ 
class NotesIn(BaseModel):
    date: Optional[date]
    title: Optional[str] = None
    body: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    author_id: Optional[int]

class NotesOut(BaseModel):
    id: Optional[int]
    date: Optional[date]
    title: Optional[str]
    body: Optional[str]
    tags:  Optional[str] 
    active:  Optional[bool]
    author_id: Optional[int]
    class Config():
        orm_mode = True