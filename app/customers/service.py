from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.customers.models import Product
from app.customers.schemas import ProductCreate, ProductUpdate


class CustomerService:
    no_task:str = "Customer doesn't exits"
    # CREATE
    # ----------------------
    def create_product(self, item_data: ProductCreate, session: SessionDep):
        product_db = Product.model_validate(item_data.model_dump())
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ONE
    # ----------------------
    def get_product(self, item_id: int, session: SessionDep):
        product_db = session.get(Product, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return product_db

    # UPDATE
    # ----------------------
    def update_product(self, item_id: int, item_data: ProductUpdate, session: SessionDep):
        product_db = session.get(Product, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        product_db.sqlmodel_update(item_data_dict)
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ALL PLANS
    # ----------------------
    def get_products(self, session: SessionDep):
        return session.exec(select(Product)).all()

    # DELETE
    # ----------------------
    def delete_product(self, item_id: int, session: SessionDep):
        product_db = session.get(Product, item_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        session.delete(product_db)
        session.commit()
        
        return {"detail": "ok"}
