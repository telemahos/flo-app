from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    user_role = Column(Integer) # admin=?, Dev=1, QA=2, BA=3, PM=4, TM=5
    notes = relationship("Notes", back_populates="author")
    blogs = relationship("Blog", back_populates="author")

#---------------------------------------
class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True, index=True)
    case_nr = Column(String, index = True)
    start_date = Column(Date, index=True)
    due_date = Column(Date, index=True)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    status = Column(Integer, default=0)
    priority = Column(Integer) # Low=1, Medium=2, High=3, Critical=4
    case_type = Column(Integer) # Issue=1, Bug=2, Note=3
    project_id = Column(Integer)
    owner_id = Column(Integer)

#---------------------------------------
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    project_nr = Column(String)
    start_date = Column(Date)
    due_date = Column(Date)
    title = Column(String, index = True)
    description = Column(String) 
    tags = Column(String)
    active = Column(Boolean, default=False)
    status = Column(Integer, default=0)
    priority = Column(Integer) # Low=0, Medium=1, High=2, Critical=3
    owner_id = Column(Integer)

    
#---------------------------------------
class TeamMember(Base):
    __tablename__ = 'team_members'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer)
    user_id = Column(Integer)
    team_role = Column(Integer)
    assign_date = Column(Date)
    active = Column(Boolean, default=False)
    note = Column(String)
    
#---------------------------------------
class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    title = Column(String, index = True)
    body = Column(String, index = True) 
    tags = Column(String, index = True)
    active = Column(Boolean, default=False)
    author_id = Column(Integer,ForeignKey("users.id"))
    author = relationship("User", back_populates="notes")

#---------------------------------------
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    title = Column(String, index = True)
    body = Column(String, index = True) 
    tags = Column(String, index = True)
    active = Column(Boolean, default=False)
    author_id = Column(Integer,ForeignKey("users.id"))
    author = relationship("User", back_populates="blogs")
    
#---------------------------------------
class Outcome(Base):
    __tablename__ = 'outcome'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    description = Column(String, index=True)
    invoice_number = Column(String)
    cost = Column(Float)
    extra_cost = Column(Float)
    tax_perc = Column(Integer)
    tax_perc2 = Column(Integer)
    supplier_id = Column(Integer)
    staff_id = Column(Integer)
    fixed_cost_id = Column(Integer)
    # supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    # staff_id = Column(Integer, ForeignKey("staff.id"))
    is_variable_cost = Column(Boolean(), default=False)
    is_fix_cost = Column(Boolean(), default=False)
    is_purchase_cost = Column(Boolean(), default=False)
    is_salary_cost = Column(Boolean(), default=False)
    is_insurance_cost = Column(Boolean(), default=False)
    is_misc_cost = Column(Boolean(), default=False)
    payment_way = Column(String)
    is_paid = Column(Boolean(), default=False)
    outcome_notes = Column(String)

    # the_supplier = relationship("Suppliers", back_populates="the_outcome")
    # the_staff = relationship("Staff", back_populates="the_outcome")

#---------------------------------------  
class OutcomeDetails(Base):
    __tablename__ = 'outcome_details'
    id = Column(Integer, primary_key=True, index=True)
    # date = Column(Date, index=True)
    outcome_id = Column(Integer, ForeignKey("outcome.id"), index=True, nullable=False)
    product_name = Column(String)
    product_description = Column(String)
    price_per = Column(Float)
    amount = Column(Integer)
    tax = Column(Integer)
    notes = Column(String)
    
#---------------------------------------  
class FixedCost(Base):
    __tablename__ = 'fixed_cost'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    
#---------------------------------------  
class Suppliers(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    responsible = Column(String)
    address = Column(String)
    telephone = Column(String)
    email = Column(String)
    payment_way = Column(String)
    notes = Column(String)

    # the_outcome = relationship("Outcome", back_populates="the_supplier")

#---------------------------------------  
class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String)
    active = Column(Boolean(), default=False)
    daily_salary = Column(Float)
    insurance = Column(Float)
    notes = Column(String)

    # the_outcome = relationship("Outcome", back_populates="the_staff")
    # income = relationship("Income", back_populates="staff")
#---------------------------------------  
class Shift(Base):
    __tablename__ = 'shift'
    id = Column(Integer, primary_key=True, index=True)
    service_id_1 = Column(Integer) 
    barman_id_1 = Column(Integer)
    service_id_2 = Column(Integer)
    barman_id_2 = Column(Integer)

    the_income = relationship("Income", back_populates="the_shift")

#---------------------------------------  
class Income(Base):
    __tablename__ = 'income'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    service_income_1 = Column(Float)
    service_income_2 = Column(Float)
    bar_income_1 = Column(Float)
    bar_income_2 = Column(Float)
    pos = Column(Float, default=0.0)
    z_count = Column(Integer, default=0.0)
    vat = Column(Float, default=0.0)
    waitress_1 = Column(String)
    waitress_2 = Column(String)
    barman_1 = Column(String)
    barman_2 = Column(String)
    notes = Column(String)
    shift_id = Column( String, ForeignKey('shift.id'), nullable=False)
    # staff_id = Column('staff_id', Integer(), ForeignKey('staff.id'), nullable=False)

    # staff = relationship("Staff", back_populates="income")
    the_shift = relationship("Shift", back_populates="the_income")

#---------------------------------------    
