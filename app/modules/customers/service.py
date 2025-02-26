from fastapi import HTTPException, status
from sqlmodel import select, Session
from .models import Customer
from .schemas import CustomerCreate, CustomerUpdate


class CustomerService:
    no_task:str = "Customer doesn't exits"
    # CREATE
    # ----------------------
    def create_customer(self, item_data: CustomerCreate, session: Session):
        item_db = Customer.model_validate(item_data.model_dump())
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ONE
    # ----------------------
    def get_customer(self, item_id: int, session: Session):
        item_db = session.get(Customer, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return item_db

    # UPDATE
    # ----------------------
    def update_customer(self, item_id: int, item_data: CustomerUpdate, session: Session):
        item_db = session.get(Customer, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        item_db.sqlmodel_update(item_data_dict)
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ALL PLANS
    # ----------------------
    def get_customers(self, session: Session):
        return session.exec(select(Customer)).all()

    # DELETE
    # ----------------------
    def delete_customer(self, item_id: int, session: Session):
        item_db = session.get(Customer, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        session.delete(item_db)
        session.commit()
        
        return {"detail": "ok"}
